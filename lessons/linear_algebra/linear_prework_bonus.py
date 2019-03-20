# Do not change these variables
import numpy as np
A = np.array([[1,2,3],[2,7,4]])
B = np.array([[1,-1],[0,1]])
C = np.array([[5,-1],[9,1],[6,0]])
D = np.array([[3,-2,-1],[1,2,3]])

u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])

# Q1: record the dimensions of A, B, C, D, u, v respectively in the dict below. 
#     Do not type the answers, make python do the work

dimensions = {
    'A': A.shape,
    'B': B.shape,
    'C': C.shape,
    'D': D.shape,
    'u': u.shape,
    'v': v.shape
}

# Q2: vector operations
#     assign `None` if the operation is not defined
#     do not type the answers, make python do the work
alpha = 6

try:
    u_plus_v = np.add(u,v)
except ValueError:
    u_plus_v = 'None'
u_minus_v = np.subtract(u,v)# u-v
alpha_times_u = alpha*u       # alpha * u, alpha = 6
u_dot_v = np.dot(u,v)             # u . v
norm_u = np.linalg.norm(u)              # ||u|| 


# Q3: compute the following and assign to variables below:
#     assign `None` if the operation is not defined
#     do not type the answers, make python do the work
try:
    A_plus_C = np.add(A,C)
    print(A_plus_C)# A + C
except ValueError:
    A_plus_C = 'None'
A_minus_Ctranspose = np.subtract(A,C.transpose())   # A - C.T
Ctranspose_plus_3D = np.add(C.transpose(),3*D)   # C.T + 3*D
try:
    B_times_A = np.matmul(B,A)
except ValueError:
    B_times_A = 'None'  # B*A
try:
    B_times_Atranspose = np.matmul(B,A.transpose())   # B*A.T
except ValueError:
    B_times_Atranspose = 'None'
# Q4: (bonus)

try:
    B_times_C = np.matmul(B,C)            # B*C
except ValueError:
    B_times_C = 'None'
try:
    C_times_B = np.matmul(C,B)            # C*B
except ValueError:
    C_times_B = 'None'
    
B_exp_4 = np.linalg.matrix_power(B,4)              # B^4
A_times_Atranspose = np.matmul(A,A.transpose())   # A*A.T
Dtranspose_times_D = np.matmul(D.transpose(),D)   # D.T*D

print('A + C')
print(A_plus_C)

print('A-C^t')
print(A_minus_Ctranspose)

print('C^t + 3D')
print(Ctranspose_plus_3D)
print('B * A')
print(B_times_A)
print('B * A^t')
print(B_times_Atranspose)

print('B * C')
print(B_times_C)
print('C*B')
print(C_times_B)
print('B^4')
print(B_exp_4)
print('A*A^t')
print(A_times_Atranspose)
print('D^t * D')
print(Dtranspose_times_D)