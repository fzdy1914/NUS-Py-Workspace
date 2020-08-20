f = open("trisrc2.obj", "w")

map = dict()
index = 1

for i in range(6):
    for j in range(6):
        for k in range(6):
            if i == 0 and j + k <= 5 or j == 0 and i + k <= 5 or k == 0 and i + j <= 5 or i + k + j == 5:
                f.write("v {:.3f} {:.3f} {:.3f} \n".format(i * 4, j * 4, k * 4))
                map[(i, j, k)] = index
                index += 1

for i in range(5):
    for j in range(5):
        if map.get((i, j, 0)) and map.get((i + 1, j, 0)) and map.get((i, j + 1, 0)):
            f.write("f {} {} {} \n".format(map[(i, j, 0)], map[(i, j + 1, 0)], map[(i + 1, j, 0)]))
        if map.get((i, j, 0)) and map.get((i + 1, j, 0)) and map.get((i, j + 1, 0)) and map.get((i + 1, j + 1, 0)):
            f.write("f {} {} {} \n".format(map[(i + 1, j, 0)], map[(i, j + 1, 0)], map[(i + 1, j + 1, 0)]))

for i in range(5):
    for k in range(5):
        if map.get((i, 0, k)) and map.get((i + 1, 0, k)) and map.get((i, 0, k + 1)):
            f.write("f {} {} {} \n".format(map[(i, 0, k)], map[(i, 0, k+1)], map[(i+1, 0, k)]))
        if map.get((i, 0, k)) and map.get((i + 1, 0, k)) and map.get((i, 0, k + 1)) and map.get((i + 1, 0, k + 1)):
            f.write("f {} {} {} \n".format(map[(i+1, 0, k)], map[(i, 0, k+1)], map[(i+1, 0, k+1)]))

for j in range(5):
    for k in range(5):
        if map.get((0, j, k)) and map.get((0, j + 1, k)) and map.get((0, j, k + 1)):
            f.write("f {} {} {} \n".format(map[(0, j, k)], map[(0, j, k + 1)], map[(0, j + 1, k)]))
        if map.get((0, j, k)) and map.get((0, j + 1, k)) and map.get((0, j, k + 1)) and map.get((0, j + 1, k + 1)):
            f.write("f {} {} {} \n".format(map[(0, j + 1, k)], map[(0, j + 1, k + 1)], map[(0, j, k+1)]))

f.write("f {} {} {} \n".format(map[(0, 5, 0)], map[(0, 0, 5)], map[(5, 0, 0)]))
