#Example
l1 = [3,4,2,1,3,3]
l2 = [4,3,5,3,9,3]

def sim(l1, l2):
    sim=0
    for i in range(len(l1)):
        count=0
        for j in range(len(l2)):
            if l2[j] == l1[i]:
                count+=1
        sim+=l1[i]*count
    return sim

print(sim(l1,l2))

#Solution
l1 = []
l2 = []
with open("input.txt", "r") as file:
    for line in file:
        vals=line.split()
        l1.append(int(vals[0]))
        l2.append(int(vals[1]))

print(sim(l1,l2))