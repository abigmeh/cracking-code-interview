'''

Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold the additional characters,
and that you are given the "true" length of the string.
'''

def urlify(s):
    word = str(s.rstrip()).split(' ')
    result = ''
    for i in range(len(word) - 1):
        result += str(word[i]) + '%20'
    return result+word[-1]
print(urlify("mr john musih     "))
