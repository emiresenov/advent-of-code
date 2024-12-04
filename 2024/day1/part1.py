#Example
l1 = [3,4,2,1,3,3]
l2 = [4,3,5,3,9,3]

l1.sort()
l2.sort()

def diff(l1, l2):
    diff = 0
    for i in range(len(l1)):
        diff += abs(l1[i] - l2[i])
    return diff

print(diff(l1,l2))

#Solution
l1 = []
l2 = []
with open("input.txt", "r") as file:
    for line in file:
        vals=line.split()
        l1.append(int(vals[0]))
        l2.append(int(vals[1]))

l1.sort()
l2.sort()

print(diff(l1,l2))