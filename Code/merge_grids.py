__author__ = 'Abdullah'
import random as rn
import math
import json


def merge_side_grids(o, l):
    gh = open("../Data/Grids/"+str(o)+".txt", "r")
    ghh = open("../Data/Grids/"+str(l)+".txt", "r")
    w = []
    v = []
    c = gh.readline()
    d = ghh.readline()
    w = c.split()
    v = d.split()
    n = int(w[0]) + int(v[0])
    m = max(int(w[1]), int(v[1]))
    lam1 = int(w[0]) -1
    lam2 = int(v[0]) -1
    r = 2*m - 1
    dd = n +1
    f = open(o+"_"+l+".txt", 'a')
    f.write(str(n)+' '+str(m))
    f.write('\n')
    f.close()
    print(r)
    # merging grids' arcs
    lines1 = gh.readlines()
    lines2 = ghh.readlines()
    for i in range(0, r):
        f = open(o+"_"+l+".txt", 'a')
        if i <= 2*min(int(w[1]), int(v[1])) - 2: 
            if i % 2 == 0 and i % 2 == 0:
                if lines1[i][0] == 'l' or lines1[i][0] == 'r' and lines2[i][0] == 'l' or lines2[i][0] == 'r':
                    x = []
                    y = []
                    x = lines1[i]
                    for j in range(lam1):
                        f.write(x[j])
                    f.close()
                    y = lines2[i]
                    s = rn.randint(0,1)
                    if s == 0:
                        z = 'l'
                    else:
                        z = 'r'
                    f = open(o+"_"+l+".txt", 'a')
                    f.write(str(z))
                    f.close()
                    f = open(o+"_"+l+".txt", 'a')
                    for j in range(lam2):
                        f.write(y[j])
                   # f.write(str(z[0])+str(z[1])+str(z[2]))
                    f.write('\n')
                    f.close()
                else:
                    print("There is a Bug!!!")
                    exit(1)
            if i % 2 == 1 and i % 2 == 1:
                if lines1[i][0] == 'u' or lines1[i][0] == 'd' and lines2[i][0] == 'u' or lines2[i][0] == 'd':
                    x1 = []
                    y1 = []
                    x1 = lines1[i]
                    y1 = lines2[i]
                    f = open(o+"_"+l+".txt", 'a')
                    for j in range(int(w[0])):
                        f.write(x1[j])
                    f.close()
                    f = open(o+"_"+l+".txt", 'a')
                    for j in range(int(v[0])):
                        f.write(y1[j])
                    f.write('\n')
                    f.close()
                else:
                    print("There is a Bug!!!")
                    exit(1)
        else:
            if int(v[1]) > int(w[1]):
                if i % 2 == 0 and i % 2 == 0:
                    if lines2[i][0] == 'l' or lines2[i][0] == 'r':
                        x2 = []
                        x2 = lines2[i]
                        for j in range(lam2):
                            f.write(x2[j])
                        f.close()
                        s = rn.randint(0,1)
                        if s == 0:
                            z = 'l'
                        else:
                            z = 'r'
                        f = open(o+"_"+l+".txt", 'a')
                        f.write(str(z))
                        f.close()
                        f = open(o+"_"+l+".txt", 'a')
                        for j in range(lam2):
                            f.write(x2[j])
                        # f.write(str(z[0])+str(z[1])+str(z[2]))
                        f.write('\n')
                        f.close()
                    else:
                        print("There is a Bug!!!")
                        exit(1)
                if i % 2 == 1 and i % 2 == 1:
                    if lines2[i][0] == 'u' or lines2[i][0] == 'd':
                        x3 = []
                        x3 = lines2[i]
                        for j in range(int(v[0])):
                            f.write(x3[j])
                        f.close()
                        f = open(o+"_"+l+".txt", 'a')
                        for j in range(int(v[0])):
                            f.write(x3[j])
                            # f.write(str(z[0])+str(z[1])+str(z[2]))
                        f.write('\n')
                        f.close()
                    else:
                        print("There is a Bug!!!")
                        exit(1)
            elif int(w[1]) > int(v[1]):
                if i % 2 == 0 and i % 2 == 0:
                    if lines1[i][0] == 'l' or lines1[i][0] == 'r':
                        x4 = []
                        x4 = lines1[i]
                        for j in range(lam1):
                            f.write(x4[j])
                        f.close()
                        s = rn.randint(0,1)
                        if s == 0:
                            z = 'l'
                        else:
                            z = 'r'
                        f = open(o+"_"+l+".txt", 'a')
                        f.write(str(z))
                        f.close()
                        f = open(o+"_"+l+".txt", 'a')
                        for j in range(lam1):
                            f.write(x4[j])
                        # f.write(str(z[0])+str(z[1])+str(z[2]))
                        f.write('\n')
                        f.close()
                    else:
                        print("There is a Bug!!!")
                        exit(1)
                if i % 2 == 1 and i % 2 == 1:
                    if lines1[i][0] == 'u' or lines1[i][0] == 'd':
                        x5 = []
                        x5 = lines1[i]
                        for j in range(int(w[0])):
                            f.write(x5[j])
                        f.close()
                        f = open(o+"_"+l+".txt", 'a')
                        for j in range(int(w[0])):
                            f.write(x5[j])
                        # f.write(str(z[0])+str(z[1])+str(z[2]))
                        f.write('\n')
                        f.close()
                    else:
                        print("There is a Bug!!!")
                        exit(1)


merge_side_grids('grid6a', 'grid6b')
