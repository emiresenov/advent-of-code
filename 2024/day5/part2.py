from part1 import correctOrder

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

def updateBroken(rules, arr):
    arr2=arr.copy()
    i=0
    for a in arr:
        j=i+1
        for b in arr[1:]:
            if brokenRule(rules, (a,b)):
                arr2[i],arr2[j] = arr2[j],arr2[i]
                return arr2
            j+=1
        arr = arr[1:]
        i+=1
    return arr2


def fixOrder(rules, arr):
    while updateBroken(rules, arr) != arr:
        arr = updateBroken(rules, arr)
    return arr

print(fixOrder(rules, [97,13,75,29,47]))


#Solution
with open("input.txt", "r") as file:
    input = file.read()
    first, second = input.strip().split("\n\n")

    rules = [tuple(map(int, line.split("|"))) for line in first.splitlines()]
    updates = [list(map(int, line.split(","))) for line in second.splitlines()]

    sum=0
    for update in updates:
        if not correctOrder(rules, update):
            update = fixOrder(rules, update)
            sum+=update[int((len(update) - 1)/2)]

    print(sum)