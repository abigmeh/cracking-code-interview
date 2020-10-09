'''
Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2blc5a3.
If the "compressed" string would not become smaller than the original string,
your method should return the original string.
You can assume the string has only uppercase and lowercase letters (a - z).

'''
def string_compress(string):
    result = []
    c = 0
    for i in range(len(string)):
        if i != 0 and string[i] != string[i-1]:
            result.append(string[i-1] +str(c))
            c = 0
        c += 1
    result.append(string[-1] + str(c))
    return min(string,''.join(result), key = len)

print(string_compress('abcc'))