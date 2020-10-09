'''
Given two strings, write a method to decide if one is a permutation of the other.
'''

def is_permutation(s1, s2):
    return sorted(s1) == sorted(s2)

def is_per_counting(s1, s2):
    check = {}
    for s in s1:
        if s in check:
            check[s] += 1
        else:
            check[s] = 1
    for s in s2:
        if s in check.keys() and check[s]>0:
            check[s] -=1
        else:
            return False
    return True
print(is_per_counting('sinwpo','inWpso ' ))