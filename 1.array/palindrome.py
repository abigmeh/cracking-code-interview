'''
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.

EXAMPLE Input: Tact Coa Output: True (permutations: "taco cat", "atco eta", etc.)

'''

def palindrome(word):
    new_word = word.replace(' ', '').lower()
    check_list = []
    for w in new_word:
        if w in check_list:
            check_list.remove(w)
        else:
            check_list.append(w)
    print(check_list)
    if len(check_list) > 1:
        return False
    else:
        return True
print(palindrome('Tbact Coab CVCV'))