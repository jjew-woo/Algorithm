from itertools import product

def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    dic = []
    for i in range(1,6):
        dic += [''.join(word) for word in product(vowels, repeat=i)]
    
    return sorted(dic).index(word)+1