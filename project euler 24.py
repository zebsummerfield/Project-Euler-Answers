
def permutation(term_list):
    term_list.reverse()
    permutations = [] if len(term_list) == [] else [term_list[:1]]
    for item in term_list[1:]:
        new_permutations = []
        for i in range(len(permutations[0])+1):
            for perm in permutations:
                new_perm = perm[:i] + [item] + perm[i:]
                new_permutations.append(new_perm)
        permutations = new_permutations
    permutations.sort()
    return permutations
            
print(permutation([0,1,2,3,4,5,6,7,8,9])[999999])
