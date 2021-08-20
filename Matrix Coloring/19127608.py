import numpy as np
import itertools
import time
from pysat.solvers import Glucose3

def readMat(path):
	f = open(path, 'rt')
	h, w = [int(x) for x in f.readline().strip().split(' ')]
	assert h > 0 and w > 0
	mat = - np.ones((h, w), dtype=np.int32)
	for ih in range(h):
		iw = 0
		for it in f.readline().strip().split(' '):
			if it != '.':
				mat[ih][iw] = int(it)
			iw += 1
	f.close()
	return mat

def toCNF(mat, lvars):
	CNF = []
	for i in range(mat.shape[0]):
		for j in range(mat.shape[1]):
			get_clauses = getClauses(mat, lvars, i,j)
			for temp in get_clauses:
				if temp != []:
					CNF.append(temp)
	return CNF

def getClauses(mat, lvars, ih, iw):
	clauses = []
	adjacents = getAllAdj(mat, lvars, ih, iw)
	for it in itertools.combinations(adjacents, mat[ih, iw] + 1):
		tmp = []
		for v in it:
			tmp.append(-v)
		clauses.append(tmp)
	
	for it in itertools.combinations(adjacents, len(adjacents) - mat[ih, iw] + 1):
		tmp = []
		for v in it:
			tmp.append(v)
		clauses.append(tmp)
	return clauses

def getAllAdj(mat, lvars, ih, iw):
	res = []
	for i in [-1, 0, 1]:
		for j in [-1, 0, 1]:
			ii = i + ih
			jj = j + iw
			if validCell(ii, jj, mat.shape) and lvars[ii][jj] not in res:
				res.append(lvars[ii][jj])
	return res

def validCell(i, j, shape):
	return 0 <= i and i < shape[0] and 0 <= j and j < shape[1]

def initVars(mat):
	hh, ww = mat.shape
	lvars = [[i*ww+j+1 for j in range(ww)] for i in range(hh)]
	return lvars, hh*ww

def solveCNF(clauses):
	g = Glucose3()
	for it in clauses:
		g.add_clause(it)
	sol = g.solve()
	if sol:
		return True, g.get_model()
	return False, None
	pass

def process(infile, outfile):
	t2 = time.time()
	mat = readMat(infile)
	
	lvars, num = initVars(mat)
	clauses = toCNF(mat, lvars)

	sol, res = solveCNF(clauses)
	t1 = time.time()
	print('Running time:', round(t1 - t2, 8), 'seconds')
	if not sol:
		print('Unsolved ' + infile + '\n')
		return

	with open(outfile, 'wt') as f:
		for ih in range(mat.shape[0]):
			for iw in range(mat.shape[1]):
				if lvars[ih][iw] in res:
					f.write('1')
				else:
					f.write('0')
				f.write(' ')
			f.write('\n')
	print('Solved to ' + outfile + '\n')

if __name__ == '__main__':
	process('input1.txt', 'output1.txt')
	process('input2.txt', 'output2.txt')
	process('input3.txt', 'output3.txt')
	process('input4.txt', 'output4.txt')
	process('input5.txt', 'output5.txt')
	process('input6.txt', 'output6.txt')
	process('input7.txt', 'output7.txt')