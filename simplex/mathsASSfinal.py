
import numpy as np
import warnings

def simplex(type, A, B, C, D, M):

    (m, n)= A.shape                                     # m = no of restrictions, n = no of variables
    basic_vars = []
    count = n
    R = np.eye(m)                                       # matrix with new variables
    P = B                                               # values of the new variables
    artificial= []                                      # artificial variables position indicator

    for i in range(m):
        if D[i] == 1:
            C = np.vstack((C, [[0]]))                   # add the slack variable to objective function
            count = count + 1
            basic_vars = basic_vars + [count-1]         # regist the slack variable as basic variable
            artificial = [artificial, 0]
        elif D[i] == 0:
            if type == 'min':                           # add the artificial variable to objective function with the big M value
                C = np.vstack((C, [[M]]))
            else:
                C = np.vstack((C, [[-M]]))
            count = count + 1
            basic_vars = basic_vars + [count-1]
            artificial = [artificial, 1]
        elif D[i] == -1:
            if type == 'min':
                C = np.vstack((C, [[0], [M]]))        # add the surplus and artificial variables to objective function
            else:
                C = np.vstack((C, [[0], [-M]]))
            R = repeatColumnNegative(R, count + 1 - n)
            P = insertZeroToCol(P, count + 1 - n)
            count = count + 2
            basic_vars = basic_vars + [count-1]
            artificial = [artificial, 0, 1]
        else:
            print("invalid case")
    
    X = np.vstack((np.zeros((n, 1)), P))              # current vertex
    A = np.hstack((A, R))                             # add new variables to matrix A
    st = np.vstack((np.hstack((-np.transpose(C), np.array([[0]]))), np.hstack((A, B))))            # simplex tableau
    (rows, cols) = st.shape
    # basic_vars = ((n + 1):n+m)'
    print('\nsimplex tableau\n')
    print(st)
    print('\ncurrent basic variables\n')
    print(basic_vars)
    print('\noptimal point\n')
    print(X)
    z_optimal = np.matmul(np.transpose(C), X)
    print('\ncurrent Z\n\n', z_optimal)

    if z_optimal != 0:                                # check if z != 0 (when there are artificial variables)
        for i in range(m):
            if D[i] == 0 or D[i] == -1:
                if type == 'min':
                    st[0,:]= st[0,:] + M * st[1+i,:]
                else:
                    st[0,:]= st[0,:] - M * st[1+i,:]
        print('\ncorrected simplex tableau\n')
        print(st)

    iteration = 0
    while True:
    # for zz in range(2):
        if type == 'min':                             # select the more positive value
            w = np.amax(st[0, 0:cols-1])
            iw = np.argmax(st[0, 0:cols-1])
        else:                                         # select the more negative value
            w = np.amin(st[0, 0:cols-1])
            iw = np.argmin(st[0, 0:cols-1])
        if w <= 0 and type == 'min':
            print('\nGlobal optimum point\n')
            break
        elif w >= 0 and type == 'max':
            print('\nGlobal optimum point\n')
            break
        else:
            iteration = iteration + 1
            print('\n----------------- Iteration {} -------------------\n'.format(iteration))
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                T = st[1:rows, cols-1] / st[1: rows, iw]
            R = np.logical_and(T != np.inf, T > 0)
            (k, ik) = minWithMask(T, R)
            cz = st[[0],:]                            # current z row
            pivot = st[ik+1, iw]                      # pivot element
            prow = st[ik+1,:] / pivot
            st = st - st[:, [iw]] * prow
            st[ik+1,:]= prow                          # pivot row is a special case
            basic_vars[ik] = iw                       # new basic variable
            print('\ncurrent basic variables\n')
            print(basic_vars)
            basic = st[:, cols-1]                     # new vertex
            X = np.zeros((count, 1))
            t = np.size(basic_vars)
            for k in range(t):
                X[basic_vars[k]] = basic[k+1]
            print('\ncurrent optimal point\n')
            print(X)
            C = -np.transpose(cz[[0], 0:count])       # new z value
            z_optimal = cz[0, cols-1] + np.matmul(np.transpose(C), X)
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            st[0, cols-1] = z_optimal
            print('\nsimplex tableau\n\n')
            print(st)
            print('\ncurrent Z\n\n')
            print(z_optimal)
    
    # tv = np.size(artificial)                        ## check if some artificial variable is positive (infeasible solution)
    # for i in range(tv):
    #     if artificial[i] == 1:
    #         if X[n + i] > 0:
    #             print('\ninfeasible solution\n')
    #             break

    return (z_optimal[0, 0], X)

def minWithMask(x, mask):
    min = 0
    imin = 0
    n = np.size(x)
    for i in range(n):
        if mask[i] == 1:
            if min == 0:
                min = x[i]
                imin = i
            else:
                if min > x[i]:
                    min = x[i]
                    imin = i
    return (min, imin)


def repeatColumnNegative(Mat, h):
    (r, c) = Mat.shape
    Mat = np.hstack((Mat[:, 0:h-1], -Mat[:, [h-1]], Mat[:, h-1:c]))
    return Mat

def insertZeroToCol(col, h):
    k = np.size(col)
    col = np.vstack((col[0:h-1, [0]], np.array([[0]]), col[h-1:k, [0]]))
    return col

type = input("Enter the type of optimization ('max' or 'min'): ")
n = int(input("Enter the number of constraints: "))
m = int(input("Enter the number of decision variables: "))

A = np.zeros((n, m))
B = np.zeros((n, 1))
C = np.zeros((m, 1))
D = np.zeros((n, 1))

print("Enter coffecient of constraints (one row at a time):")
for i in range(n):
    A[i] = input("A{} (space-separated values): ".format(i)).split()

print("constraints equates to (one value at a time):")
for i in range(n):
    B[i] = float(input("B{}: ".format(i)))

print("coefficient of objective function (one value at a time):")
for i in range(m):
    C[i] = float(input("C{}: ".format(i)))

print("Enter 1 for <=, 0 for =, -1 for >=:")
for i in range(n):
    D[i] = int(input("D{}: ".format(i)))

# M = float(input("Enter the value for M: "))
M=10000

(z,x) = simplex(type , A,B,C,D,M)