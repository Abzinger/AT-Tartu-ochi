__author__ = 'Abdullah'
import random as rn
import math
import json


def read_grid(o):
    fhh = open("../Data/Grids/"+str(o)+".txt", "r")
    nodes = []
    arcs = {}
    w = []
    c = fhh.readline()
    w = c.split()
    n = int(w[0])
    m = int(w[1])
    rows = range(m)
    columns = range(n)
    for i in rows:
        for j in columns:
            nodes.append((i, j))
    for q, c in enumerate(fhh):
        if q % 2 == 0:
            if c[0] == 'l' or c[0] == 'r':
                for s in range(n):
                    if s > 0:
                        if c[s-1] == 'r':
                            arcs[((q/2, s-1), (q/2, s))] = 1
                        elif c[s-1] == 'l':
                            arcs[((q/2, s-1), (q/2, s))] = -1
            else:
                print("There is a Bug!!!")
                exit(1)
        if q % 2 == 1:
            if c[0] == 'u' or c[0] == 'd':
                for s in range(n+1):
                    if q > 0 and c[s] == 'u':
                        arcs[(((q+1)/2 - 1, s), ((q+1)/2, s))] = 1
                    elif q > 0 and c[s] == 'd':
                        arcs[(((q+1)/2 - 1, s), ((q+1)/2, s))] = -1
            else:
                print("There is a Bug!!!")
                exit(1)
    return n, m, nodes, arcs

def search_pattern(o):
    n, m, nodes, arcs = read_grid(o)
    pat = []
    pat1 = []
    for ver in nodes:
        if ver[1] == n-2 and ver[0] != m-1  and ver[0] != m-2:
            if arcs[ver, (ver[0], ver[1] +1)] == 1 and arcs[ver, (ver[0] + 1, ver[1])] == 1 and arcs[(ver[0] + 1,ver[1]), (ver[0] + 1, ver[1] +1)] == 1 and arcs[(ver[0] + 1, ver[1]), (ver[0] +2, ver[1])] == 1 and arcs[(ver[0] + 2, ver[1]), (ver[0]+2, ver[1] +1)] == -1 and arcs[(ver[0], ver[1] + 1), (ver[0] +1, ver[1]+1)] == -1 and arcs[(ver[0] + 1, ver[1]+1), (ver[0] +2, ver[1]+1)] == 1:
                pat.append( ver)
                pat.append((ver[0], ver[1] +1)) 
                pat.append((ver[0]+ 1, ver[1]))
                pat.append((ver[0]+ 1, ver[1]+1))
                pat.append((ver[0]+ 2, ver[1]))
                pat.append((ver[0]+ 2, ver[1]+1))
    for ver in nodes:
        if ver[1] == 0  and ver[0] != m-1  and ver[0] != m-2:
            if arcs[ver, (ver[0], ver[1] +1)] == -1 and arcs[ver, (ver[0] + 1, ver[1])] == -1 and arcs[(ver[0] + 1,ver[1]), (ver[0] + 1, ver[1] +1)] == -1 and arcs[(ver[0] + 1, ver[1]), (ver[0] +2, ver[1])] == 1 and arcs[(ver[0] + 2, ver[1]), (ver[0]+2, ver[1] +1)] == 1 and arcs[(ver[0], ver[1]+1), (ver[0] +1, ver[1]+1)] == 1 and arcs[(ver[0] + 1, ver[1]+1), (ver[0] +2, ver[1]+1)] == 1:
                pat1.append( ver)
                pat1.append((ver[0]+ 1, ver[1]))
                pat1.append((ver[0]+ 1, ver[1]))
                pat1.append((ver[0]+ 1, ver[1]+1))
                pat1.append((ver[0]+ 2, ver[1]))
                pat1.append((ver[0]+ 2, ver[1]+1))
    return pat1, pat



            
