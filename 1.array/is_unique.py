'''
Is Unique: Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
'''

def is_unique(s):
    if len(s) > 128:
        return False
    check_list = []
    for c in s:
        if check_list.count(str(c))>0:
            return False
        else:
            check_list.append(str(c))
    return True
print(is_unique('hahaha'))

print(is_unique('sinwpo'))