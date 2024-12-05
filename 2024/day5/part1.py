#Example
input = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

first, second = input.strip().split("\n\n")

rules = [tuple(map(int, line.split("|"))) for line in first.splitlines()]
updates = [list(map(int, line.split(","))) for line in second.splitlines()]


def brokenRule(rules, pair):
    for rule in rules:
        if (rule[1],rule[0]) == pair:
            return True

def correctOrder(rules, arr):
    for i in arr:
        for j in arr[1:]:
            if brokenRule(rules, (i,j)):
                #print(f'broken: {(i,j)}')
                #break
                return False
        arr = arr[1:]
    return True

sum=0
for update in updates:
    if correctOrder(rules, update):
        sum+=update[int((len(update) - 1)/2)]

print(sum)

#Solution
with open("input.txt", "r") as file:
    input = file.read()
    first, second = input.strip().split("\n\n")

    rules = [tuple(map(int, line.split("|"))) for line in first.splitlines()]
    updates = [list(map(int, line.split(","))) for line in second.splitlines()]

    sum=0
    for update in updates:
        if correctOrder(rules, update):
            sum+=update[int((len(update) - 1)/2)]

    print(sum)