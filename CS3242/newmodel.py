f = open("test.obj", "w")

map = dict()
index = 1
for i in range(6):
    for j in range(6):
        for k in range(6):
            if i == 0 or i == 5 or j == 0 or j == 5 or k == 0 or k == 5:
                f.write("v {:.3f} {:.3f} {:.3f} \n".format(i * 2, j * 2, k * 2))
                map[(i, j, k)] = index
                index += 1

for i in range(5):
    for j in range(5):
        f.write("f {} {} {} \n".format(map[(i, j, 0)], map[(i + 1, j + 1, 0)], map[(i + 1, j, 0)]))
        f.write("f {} {} {} \n".format(map[(i, j, 0)], map[(i, j + 1, 0)], map[(i + 1, j + 1, 0)]))

        f.write("f {} {} {} \n".format(map[(i, j, 5)], map[(i + 1, j, 5)], map[(i + 1, j + 1, 5)]))
        f.write("f {} {} {} \n".format(map[(i, j, 5)], map[(i + 1, j + 1, 5)], map[(i, j + 1, 5)]))

for i in range(5):
    for k in range(5):
        f.write("f {} {} {} \n".format(map[(i, 0, k)], map[(i + 1, 0, k)], map[(i + 1, 0, k + 1)]))
        f.write("f {} {} {} \n".format(map[(i, 0, k)], map[(i + 1, 0, k + 1)], map[(i, 0, k + 1)]))

        f.write("f {} {} {} \n".format(map[(i, 5, k)], map[(i + 1, 5, k + 1)], map[(i + 1, 5, k)]))
        f.write("f {} {} {} \n".format(map[(i, 5, k)], map[(i, 5, k + 1)], map[(i + 1, 5, k + 1)]))

for j in range(5):
    for k in range(5):
        f.write("f {} {} {} \n".format(map[(0, j, k)], map[(0, j + 1, k)], map[(0, j + 1, k + 1)]))
        f.write("f {} {} {} \n".format(map[(0, j, k)], map[(0, j + 1, k + 1)], map[(0, j, k + 1)]))

        f.write("f {} {} {} \n".format(map[(5, j, k)], map[(5, j + 1, k + 1)], map[(5, j + 1, k)]))
        f.write("f {} {} {} \n".format(map[(5, j, k)], map[(5, j, k + 1)], map[(5, j + 1, k + 1)]))
