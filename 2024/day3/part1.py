import re

#Example
str = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

pattern = r"mul\((\d+),(\d+)\)"

print(sum([int(a) * int(b) for a, b in re.findall(pattern, str)]))

#Solution
with open("input.txt", "r") as file:
    print(sum([int(a) * int(b) for a, b in re.findall(pattern, file.read())]))