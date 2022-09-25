import numpy as np

t_matrix= 0

while t_matrix != 22:
    matrix= np.random.randint(0,2, size=(8,8))
    # print(sum(matrix))
    t_matrix = sum(sum(matrix))
    # print(t_matrix)

print(matrix)

while t_matrix > 0:
    if matrix[int(input()),int(input())] == 1:
        print("ACERTOU")  
        t_matrix-=1
    else:
        print("AGUA")