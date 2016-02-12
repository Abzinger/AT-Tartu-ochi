__author__ = 'Abdullah'

import gurobipy as gb
from gurobipy import *
import random as rn
import math
import json
import sys


if len(sys.argv) != 3:
    print("Usage: abdullah_color tournamentfilename_wo_txt gridfilename_wo_txt")
    # return 1
    sys.exit()

tournament_filename = sys.argv[1]
grid_filename       = sys.argv[2]


input_tournament_filename = tournament_filename+".txt"
input_grid_filename       = grid_filename+".txt"

# def main_program():
#     if len(sys.argv) != 3:
#         print("Usage: abdullah_color tournamentfilename_wo_txt gridfilename_wo_txt")
#         return 1
#
#     tournament_filename = sys.argv[1]
#     grid_filename       = sys.argv[2]
#
#     print ("You have called the program with the following parameters:\n",)
#     print ("Tournament filename: ",tournament_filename,"\n",)
#     print ("Grid filename: ",grid_filename,"\n")
#
#     input_tournament_filename = tournament_filename+".txt"
#     input_grid_filename       = grid_filename+".txt"


def tournament_coloring(input_tournament_filename, input_grid_filename):
    # reads the grid file
    n, m, nodes, arcs = read_grid(input_grid_filename)
    # reads the tournament from a file
    # n_tournaments = [0,1,1,2,4,12,56,456, 6880, 191556, 9733056]
    fh = open(input_tournament_filename, "r")
#    fh=open("../Data/remaining"+str(k)+"--after_grid22x7.txt","r")
    for the_idx,b in enumerate(fh):
        a = []
        print("grid_IP_color: tournament_coloring(): Read tournament "+ b);
        bs = []
        for r in range(math.floor(8*(8-1)/2)):
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
            a.append(t)
        print("grid_IP_color: tournament_coloring(): Invoking GUROBI stuff...");
        answer = solve_color_IP(n, m, nodes, arcs, a)
        print("grid_IP_color: tournament_coloring(): GUROBI done.  Result is: "+answer);

        b_wo_newline = b[0:-1]
        if len(b_wo_newline) != 8*7/2:
            print("ThErE's A bUg!!")
            exit(7)

        if answer == "colorable":
            f = open("tournaments_remaining_alive.txt", 'a')
            f.write(b)
            f.close()
            print("grid_IP_color: tournament_coloring(): Appended "+b_wo_newline+" to alive list");
        elif answer == "not colorable":
            f = open("tournaments_dead.txt", 'a')
            f.write(b_wo_newline+' cannot color '+grid_filename)
            f.write('\n')
            f.close()
            print("grid_IP_color: tournament_coloring(): Appended "+b_wo_newline+" to dead list");
        elif answer == "maybe colored":
            f = open("tournaments_undecided.txt", 'a')
            f.write(b_wo_newline+' crashed with '+grid_filename)
            f.close()
            print("grid_IP_color: tournament_coloring(): Appended "+b_wo_newline+" to crashed list");
        else:
            print("\n There's a BUG !!!!!!! ( solve_color_IP() returned ",answer,")\n")
            exit(6)


def read_grid(input_grid_filename):
    fhh = open(input_grid_filename, "r")
    c = fhh.readline()
    w = []
    w = c.split()
    n = int(w[0])
    m = int(w[1])
    # grid's node list
    nodes = []
    rows = range(m)
    columns = range(n)
    for i in rows:
        for j in columns:
                nodes.append((i, j))
    # grid's arcs
    arcs = {}
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


def solve_color_IP(n, m, nodes, arcs, a):
    # returns "colorable" or "not colorable"
    model = Model("ffff")
    model.setParam(GRB.Param.Threads, 1)
    # variables

    x_vars = {}
    for v in nodes:
        for j in range(8):
            x_ver = model.addVar(vtype=gb.GRB.BINARY, name="x_(v,j)")
            x_vars[(v, j)] = x_ver

    y_vars = {}
    for i in range(8):
        for j in range(8):
            y = model.addVar(vtype=gb.GRB.BINARY, name="y_(i,j)")
            y_vars[(i, j)] = y

    model.update()

    # constraints
    # assignment constraints
    for v in nodes:
        left = gb.quicksum([x_vars[(v, j)] for j in range(8)])
        model.addConstr(left, gb.GRB.EQUAL, 1)

    model.update()

    # proper coloring constraints
    for l in arcs:
        for j in range(8):
            model.addConstr(1, gb.GRB.GREATER_EQUAL, gb.quicksum([x_vars[(l[0], j)] + x_vars[(l[1], j)]]))

    # 2-path constraints
    for u in nodes:
        for v in nodes:
            if u == v:
                continue
            if not (u, v) in arcs:
                continue
            if not arcs[(u, v)] == +1:
                continue
            for w in nodes:
                if u == w or v == w:
                    continue
                if not (v, w) in arcs:
                    continue
                if not arcs[(v, w)] == +1:
                    continue
                for j in range(8):
                    model.addConstr(gb.quicksum([x_vars[(u, j)], x_vars[(w, j)]]), gb.GRB.LESS_EQUAL, 1)

    model.update()

    # homomorphism constraints
    for l in arcs:
        if arcs[l] == 1:
            for i in range(8):
                for j in range(8):
                    model.addConstr(gb.quicksum([y_vars[(i, j)] + 1]), gb.GRB.GREATER_EQUAL, gb.quicksum([x_vars[(l[0], i)] + x_vars[(l[1], j)]]))
        else:
            for i in range(8):
                for j in range(8):
                    model.addConstr(gb.quicksum([y_vars[(i, j)] + 1]), gb.GRB.GREATER_EQUAL, gb.quicksum([x_vars[(l[1], i)] + x_vars[(l[0], j)]]))

    # fix y-variables to tournament
    for i in range(8):
        for j in range(8):
            left = gb.quicksum([y_vars[(i, j)]])
            right = gb.quicksum([a[i][j]])
            model.addConstr(left, gb.GRB.EQUAL, right)

    model.update()
    # no objective function
    model.modelSense = gb.GRB.MINIMIZE

    model.update()

    model.optimize()
    status = model.status
    if status == gb.GRB.status.OPTIMAL:
        return "colorable"
    elif status == gb.GRB.status.INFEASIBLE:
        # f = open("non_color_grid_k"+str(k)+".txt", 'a')
        # f.write('tournament:')
        # json.dump(a, f)
        # f.write('\n grid:')
        # json.dump(m, f)
        # f.write('x')
        # json.dump(n, f)
        # f.write('arcs=')
        # json.dump(str(arcs), f)
        # f.write('\n')
        # f.close()
        return "not colorable"
    else:
        return "maybe colored"

# main_program()
tournament_coloring(input_tournament_filename, input_grid_filename)
