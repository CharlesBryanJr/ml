'''sparse_matrix_multiplication'''
# pylint: disable=C0114
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=W0621
# pylint: disable=W191
# pylint: disable=E101

print(" ")

'''

Type of Question:
- 

Clarifying Questions / Insights:
- both matrices will be sparse
- sparse == most of their elements will be zero
- given sparse matrices, reduce the number of computations.

Question:
Write a function that takes in 
two integers matrices 
and
multiples them together.
-

Input:
- Intuitive
- Primitive Types
    - Numbers
			- Zero (0)
			- NULL or nil
			- Negative Numbers
			- Floats or Doubles (clarifies if Ints only?)
			- Min/Max Int
		- Arrays
			- Empty array
			- Nested or not nested
	
- If I knew / had this....
	- Dictionary of Keys

Output: matrix
- [[]]
'''


# iterate through the rows of A
#   iterate through the columns of A or rows of B
# iterate through the columns of B

# Time: O() | # Space: O()
def sparse_matrix_multiplication_1(matrix_a, matrix_b):
    # Pre-calculate the dimensions

    # Verify if columns of A == rows of B

    # create dictionary of nonzero elements

    # create matrix c and initalize with zeros

    # perform matrix multiplication and update matrix c

    return 0


def sparse_matrix_multiplication_2(matrix_a, matrix_b):
    # Pre-calculate the dimensions

    # Verify if columns of A == rows of B

    # create dictionary of nonzero elements

    # create matrix c and initalize with zeros

    # perform matrix multiplication and update matrix c

    return 0


def sparse_matrix_multiplication(matrix_a, matrix_b):
    # Pre-calculate the dimensions
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])

    # Verify if columns of A == rows of B
    if cols_a != rows_b:
        return [[]]

    # create dictionary of nonzero elements
    sparse_a = get_dict_of_nonzero_elements(matrix_a)
    sparse_b = get_dict_of_nonzero_elements(matrix_b)

    # create matrix c and initalize with zeros
    matrix_c = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    # perform matrix multiplication and update matrix c
    for i, k in sparse_a.keys():
        for j in range(len(matrix_b[0])):
            if (k, j) in sparse_b.keys():
                matrix_c[i][j] += sparse_a[(i, k)] * sparse_b[(k, j)]

    return matrix_c

def get_dict_of_nonzero_elements(matrix):
    nonzero_elements_dict = {}
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] != 0:
                nonzero_elements_dict[(row, col)] = matrix[row][col]
    return nonzero_elements_dict


matrix_a = [
    [0, 2, 0],
    [0, -3, 5]
]
matrix_b = [
    [0, 10, 0],
    [0, 0, 0],
    [0, 0, 4]
]
print("matrix_a:", matrix_a)
print("matrix_b:", matrix_b)
print("sparse_matrix_multiplication_1:", sparse_matrix_multiplication_1(matrix_a, matrix_b))
print("sparse_matrix_multiplication_2:", sparse_matrix_multiplication_2(matrix_a, matrix_b))
print("sparse_matrix_multiplication:", sparse_matrix_multiplication(matrix_a, matrix_b))
match1 = sparse_matrix_multiplication_1(matrix_a, matrix_b) == sparse_matrix_multiplication_2(matrix_a, matrix_b)
match2 = sparse_matrix_multiplication_2(matrix_a, matrix_b) == sparse_matrix_multiplication(matrix_a, matrix_b)
all_match = match1 == match2
print("all_match:", all_match)
print(" ")

matrix_a = [
    [0],
    [0],
    [0],
    [0],
    [0],
    [3],
    [0],
    [0]
]
matrix_b = [
    [0, 0, 0, 0, 0, 2, 0, 0]
]
print("matrix_a:", matrix_a)
print("matrix_b:", matrix_b)
print("sparse_matrix_multiplication_1:", sparse_matrix_multiplication_1(matrix_a, matrix_b))
print("sparse_matrix_multiplication_2:", sparse_matrix_multiplication_2(matrix_a, matrix_b))
print("sparse_matrix_multiplication:", sparse_matrix_multiplication(matrix_a, matrix_b))
all_match = match1 == match2
print("all_match:", all_match)
print(" ")

matrix_a = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [-5, -9, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 5, -4, -3, 0],
    [0, 0, 0, 0, 0, 0, 0, -2, 0, 0, 0, 0],
    [0, 0, -8, 0, 0, 0, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 0, 9, 0, 3, 4, 0, 0, 0, 0]
]
matrix_b = [
    [3, 0],
    [0, 0],
    [8, 0],
    [7, 0],
    [-8, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 8],
    [0, 0],
    [0, 0],
    [0, 0]
]
print("matrix_a:", matrix_a)
print("matrix_b:", matrix_b)
print("sparse_matrix_multiplication_1:", sparse_matrix_multiplication_1(matrix_a, matrix_b))
print("sparse_matrix_multiplication_2:", sparse_matrix_multiplication_2(matrix_a, matrix_b))
print("sparse_matrix_multiplication:", sparse_matrix_multiplication(matrix_a, matrix_b))
all_match = match1 == match2
print("all_match:", all_match)
print(" ")