__author__ = 'Abdullah'
import random as rn
import math
import json
import collections as cll
import numpy as np

def cyc_tourn(o):
    fh = open("../Data/"+str(o), "r")
    for q in enumerate(fh):
        ma = []
        x = []
        y = []
        z = []
        a = []
        r = 0
        b = fh.readline()
        bs = []
        for r in range(28):
            bs.append(int(b[r]))
        s = 0
        for i in range(8):
            t = []
            for j in range(8):
                if i == j:
                    t.append(0)
                if j > i:
                    t.append(bs[s])
                    s = s+1
                if j < i:
                    t.append(1-a[j][i])
                #fhh = open("matrix", "a")
                #fhh.write(t)
                #fhh.close()
            a.append(t)
        ma = np.matrix(a)
        x = ma*ma
        y = x*ma
        z = y*ma
        fhh = open("matrix1", "a")
        fhh.write("the tournament is "+str(b)+'\n')
        fhh.write("This is ma\n "+str(ma)+'\n')
        fhh.write("This is ma2\n "+str(x)+'\n')
        fhh.write("This is ma3\n "+str(y)+'\n')
        fhh.write("This is ma4\n "+str(z)+'\n')
        fhh.close()
        ffhh = open("record", "a")
        ffhh.write("the tournament is "+str(b)+'\n')
        ffhh.close
        r = 0
        for i in range(8):
            if z[i, i] !=0:
                r = r + 1
        ffhh.write("number of vertices on 4 cycles "+str(r)+'\n')
        ffhh.close()
         
def num_of_tourn(b):
    br = 0
    for dig in range(28):
        br += int(int(b[dig])*math.pow(2, 28-dig))
    return br


cyc_tourn('tourn8.txt')
