# Original problem here https://www.interviewcake.com/question/python3/recursive-string-permutations?course=fc1&section=dynamic-programming-recursion
# Write a recursive function for generating all permutations of an input string. Return them as a set.

def get_permutations(string):
    # Edge case
    if len(string) == 0 :
        return set([''])
    # Base Case
    if len(string) == 1:
        return set(string)
    # Generate all permutations of the input string
    if len(string) >= 2:
        oldPermut = get_permutations(string[0:len(string)-1])
        permuts = set()
        for currentPermut in oldPermut:
            for strIndx in range(0, len(currentPermut)+1):
                permuts.add(currentPermut[:strIndx] + string[-1] + currentPermut[strIndx:])
        print("Permutations for: \"" + currentPermut + string[-1] + "\"")
        print(permuts)
        print()
        return set(permuts)

# Tests
print(get_permutations('abcd'))