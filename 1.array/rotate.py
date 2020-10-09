'''
Given an image represented by an NxN matrix,
where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees.
'''

def rotate(matrix):
    new_matrix = []
    for i in range(len(matrix)):
         temp = []
         for j in range(len(matrix[i])):
             temp.append(matrix[j][len(matrix)-i-1])
         new_matrix.append(temp)
    return new_matrix
print(rotate([[1, 4, 5], [-5, 8, 9], [3, 4, 5]]))
