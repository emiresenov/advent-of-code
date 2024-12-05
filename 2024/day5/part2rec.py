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
        if (rule[1], rule[0]) == pair:
            return True

def fixBroken(rules, arr, index=0):
    if index >= len(arr) - 1:
        return arr
    
    for j in range(index + 1, len(arr)):
        if brokenRule(rules, (arr[index], arr[j])):
            arr[index], arr[j] = arr[j], arr[index]
            return fixBroken(rules, arr, 0) 
    return fixBroken(rules, arr, index + 1)

print(fixBroken(rules, [97, 13, 75, 29, 47]))