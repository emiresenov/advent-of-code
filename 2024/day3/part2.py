import re

#Example
str = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

regex = r"(do\(\)|don't\(\))|mul\((\d+),(\d+)\)"

def regMult(input_string):
    sum=0
    state = 'do()'
    for i in re.findall(regex, input_string):
        if i[0] in ["do()", "don't()"]:
            state = i[0]
        else:
            if state == 'do()':
                sum += int(i[1])*int(i[2])
    return sum
            
print(regMult(str))

#Solution
with open("input.txt", "r") as file:
    str = file.read()
    print(regMult(str))