import numpy as np
from itertools import permutations

with open('input.txt','r') as f:
    lines = f.readlines()

matrix = [list(line.strip()) for line in lines]

n = len(matrix)
m = len(matrix[0])

dirs = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]

def xmas(i,j,di,dj):
    for k in range(4):
        ni = i+k*di
        nj = j+k*dj
        if not (0<=ni<n and 0<=nj<m):
            return False
        if matrix[ni][nj] != "XMAS"[k]:
            return False
    return True

def solve1():
    res = 0
    for i in range(n):
        for j in range(m):
            for di,dj in dirs:
                if xmas(i,j,di,dj):
                    res+=1
    return res

dirs2 = [(-1,-1),(-1,1),(1,-1),(1,1)]

permuts = [['M','M','S','S'],['S','S','M','M'],['M','S','M','S'],['S','M','S','M']]

def crossmas(i,j):
    mat = []

    mat = []
    for (di,dj) in dirs2:
        ni = i+di
        nj = j+dj
        if 0 <= ni < n and 0 <= nj < m:
            mat.append(matrix[ni][nj])

    if len(mat) != 4:
        return False
    for p in permuts:
        if mat == p:
            return True
    return False

def solve2():
    res = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'A' and crossmas(i,j):
                res+=1
    return res