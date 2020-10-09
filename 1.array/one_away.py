'''
There are three types of edits that can be performed on strings:
insert a character,
remove a character,
or replace a character.

Given two strings, write a function to check if they are one edit (or zero edits) away.

'''

def one_away(a, b):
    if abs(len(a) - len(b)) > 1:
        return False
    else:
        max_length = max(len(a), len(b))
        for i in range(max_length):
            if a[i] != b[i]:
                if len(a) == len(b):
                    return a[i+1:] == b[i+1:]
                if len(a) > len(b):
                    return a[i+1:] == b[i:]
                if len(a) < len(b):
                    return a[i:] == b[i+1:]
print(one_away('bale', 'ale'))
