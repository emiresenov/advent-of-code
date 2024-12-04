from part1 import safety

#Solution
count=0
with open("input.txt", "r") as file:
    for line in file:
        arr = list(map(int, line.split()))
        for i in range(len(arr)):
            popped=arr.copy()
            popped.pop(i)
            if safety(popped):
                count+=1
                break
            
print(count)