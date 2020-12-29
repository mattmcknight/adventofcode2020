import itertools

operators = ['+','-','*','/']

def operate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    else:
        return a / b


def solve(inputs, target):
    permutations = list(itertools.permutations(inputs))
    operator_combinations = list(itertools.combinations_with_replacement(operators, len(inputs)-1))
    operator_permutations = set([])
    for operator_combination in operator_combinations:
        operator_permutations.update(itertools.permutations(operator_combination))
    for permutation in permutations:
        for operator_permutation in operator_permutations:
            total = permutation[0]
            expression = str(permutation[0])
            for i in range(1, len(inputs)):
                total = operate(total, permutation[i], operator_permutation[i-1])
                expression += operator_permutation[i-1] + str(permutation[i])
            if total == target:
                print("{}={}".format(expression, total))



if __name__ ==  '__main__':
    solve([25,50,75,100,3,6], 952)
    solve([11, 12, -3, 5], 24)