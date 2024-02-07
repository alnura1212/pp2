from itertools import permutations
string=str(input())
def per(string):
    for char in permutations(string):
        print("".join(char))
        
per(string)
