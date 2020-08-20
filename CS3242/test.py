import random

import numpy as np
import math

f = open('newskull.obj', 'r')

all = f.readlines()

f.close()
vs = []
ts = []

for i in all:
    j = i.split(' ')
    if j[0] == 'v':
        vs.append(np.array([[float(j[1])], [float(j[2])], [float(j[3])]]))
    else:
        ts.append([int(j[1]), int(j[2]), int(j[3])])


A = np.array([[math.cos(-math.pi * 0.5), -math.sin(-math.pi* 0.5), 0], [math.sin(-math.pi* 0.5), math.cos(-math.pi* 0.5), 0], [0, 0, 1]])
B = np.array([[1, 0, 0], [0, math.cos(math.pi* 0.5), -math.sin(math.pi* 0.5)], [0, math.sin(math.pi* 0.5), math.cos(math.pi* 0.5)]])

C = np.matmul(A, B)
for i in range(len(vs)):
    vs[i] = np.matmul(C, np.matmul(C, vs[i]))
    vs[i][0] -= 3
    vs[i][1] += 2
    vs[i][2] -= 5

f = open('skullsrc.obj', 'w')

for i in range(len(vs)):
    f.write('v %.3f %.3f %.3f\n' % (vs[i][0][0], vs[i][1][0], vs[i][2][0]))

f.write('\n')

for i in range(len(ts)):
    f.write('f {} {} {}\n'.format(ts[i][0], ts[i][1], ts[i][2]))

f.close()