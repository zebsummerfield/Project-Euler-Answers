
def perimeterSolutions(p: int) -> list:
    solutions = []
    for a in range(int(p/2)):
        for b in range(int(p/2)):
            c = p - a - b
            if a**2 + b**2 == c**2:
                solution = [a, b, c]
                solution.sort()
                solutions.append(solution)
    return set(tuple(sol) for sol in solutions)

max_perimeter = 0
max_solutions = 0
num_max_solutions = 0

for i in range(1000):
    print(i)
    solutions = perimeterSolutions(i)
    if len(solutions) > num_max_solutions:
        max_perimeter = i
        max_solutions = solutions
        num_max_solutions = len(solutions)

print()
print(max_perimeter)
print(max_solutions)
print(num_max_solutions)
