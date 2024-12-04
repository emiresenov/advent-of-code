#Example
row1 = [7, 6, 4, 2, 1]
row2 = [1, 2, 7, 8, 9]
row3 = [9, 7, 6, 2, 1]
row4 = [1, 3, 2, 4, 5]
row5 = [8, 6, 4, 4, 1]
row6 = [1, 3, 6, 7, 9]

sign = lambda x: (True, False)[x<0]

def safety(arr):
    val_prev=arr[0]
    sign_prev=sign(arr[0]-arr[1])
    for i in range(1,len(arr)):
        val=arr[i]
        diff = val_prev-val
        if(abs(diff) not in range(1,4) or sign(diff)!=sign_prev):
            return False
        val_prev = val
        sign_prev=sign(diff)
    return True

'''print(safety(row1))
print(safety(row2))
print(safety(row3))
print(safety(row4))
print(safety(row5))
print(safety(row6))'''

#Solution
count=0
with open("input.txt", "r") as file:
    for line in file:
        if (safety(list(map(int, line.split())))):
            count+=1

print(count)



