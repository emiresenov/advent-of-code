l1 = []
l2 = []

with open("input.txt", "r") as file:
    for line in file:
        vals=line.split()
        l1.append(int(vals[0]))
        l2.append(int(vals[1]))

l1.sort()
l2.sort()

diff = 0
for i in range(len(l1)):
    diff += abs(l1[i] - l2[i])

print(diff)

