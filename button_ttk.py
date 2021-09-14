f = open('demo_file.txt', 'w')


for i in range(1, 1001):
    for j in range(0, 1001):
        f.write(f"elif a == {i} and b == {j}:\n")
        a = i + j

        f.write(f"\tprint(\"{i} + {j} = {a}\")\n")


f.close()
