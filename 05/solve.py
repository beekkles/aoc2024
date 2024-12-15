import re
import bisect
from collections import defaultdict
from queue import deque

with open('input.txt','r') as f:
    lines = f.readlines()
    
    reglas = {}
    listas = []
    brk = False
    for line in lines:
        if line == "\n":
            brk = True
            continue

        if brk == False:
            reg = re.findall(r"\d+",line)
            reg[0],reg[1] = int(reg[0]), int(reg[1])
            if reg[0] in reglas:
                bisect.insort(reglas[reg[0]], reg[1])
            else:
                reglas[reg[0]] = [reg[1]]
            
        else:
            line = line.strip()
            lista = line.split(",")
            nums = [int(n) for n in lista]
            listas.append(nums)

def solve1():
    res = 0
    for lista in listas:
        re = True
        for k in lista:
            for i in lista[:lista.index(k)]:
                if any(i == l for l in reglas.get(k, [])):
                    re = False

        if re == True:
            mid = len(lista)//2
            res += lista[mid]

    return res

def toposort(in_list, reglas):
    gr_in = defaultdict(int)
    grafo = defaultdict(list)

    for u in in_list:
        if u in reglas:
            for v in reglas[u]:
                if v in in_list:
                    grafo[u].append(v)
                    gr_in[v] += 1

    for node in in_list:
        if node not in gr_in:
            gr_in[node] = 0

    queue = deque([w for w in in_list if gr_in[w] == 0])
    list_sortd = []

    while queue:
        w = queue.popleft()
        list_sortd.append(w)

        for vecino in grafo[w]:
            gr_in[vecino] -= 1
            if gr_in[vecino] == 0:
                queue.append(vecino)

    return list_sortd


def ordenado(lista, reglas):
    vistos = set()
    for k in lista:
        for i in lista[:lista.index(k)]:
            if i in reglas.get(k, []):
                return False
        vistos.add(k)
    return True

def solve2():
    res = 0
    for lista in listas:
        if not ordenado(lista, reglas):
            lista_sortd = toposort(lista,reglas)
            if lista_sortd:
                mid = len(lista_sortd) // 2
                res += lista_sortd[mid]
    
    return res