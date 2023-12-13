from itertools import combinations
from itertools import combinations_with_replacement
from itertools import permutations
from itertools import count

names_male = ["Piter", "Bob", "Nick"]
name_female = ["Kate", "Alice"]
names = names_male + name_female

def demo_combination():
    pairs = combinations(names, 2)
    for pair in pairs:
        print(pair)

def demo_combinations_with_replacement():
    pairs = combinations_with_replacement(["appl", "banana", "orange", "mango"], 2)
    for pair in pairs:
        print(pair)

def demo_permutations():
    todos = ["wash", "eat", "dress"]
    result = permutations(todos, 3)
    for res in result:
        print(res)

def demo_count():
    c = count(1)
    for cnt, value in zip(c, range(10, 20, 2)):
        print(cnt, value)


if __name__ == "__main__":
    #demo_combination()
    #demo_combinations_with_replacement()
    #demo_permutations()
    demo_count()