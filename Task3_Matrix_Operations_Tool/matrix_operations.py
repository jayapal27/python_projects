import numpy as np

def input_matrix(name):
    rows = int(input(f"Enter number of rows for Matrix {name}: "))
    cols = int(input(f"Enter number of columns for Matrix {name}: "))
    print(f"Enter elements of Matrix {name} row-wise:")

    matrix = []
    for i in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)

    return np.array(matrix)

# Step 1: Input matrices
A = input_matrix("A")
B = input_matrix("B")

print("\nMatrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Step 2 & 3: Menu-driven operations with continue option
while True:
    print("\nChoose Matrix Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        if A.shape == B.shape:
            print("\nResult (A + B):")
            print(A + B)
        else:
            print("Addition not possible. Matrices must have same dimensions.")

    elif choice == 2:
        if A.shape == B.shape:
            print("\nResult (A - B):")
            print(A - B)
        else:
            print("Subtraction not possible. Matrices must have same dimensions.")

    elif choice == 3:
        if A.shape[1] == B.shape[0]:
            print("\nResult (A x B):")
            print(np.dot(A, B))
        else:
            print("Multiplication not possible. Columns of A must equal rows of B.")

    elif choice == 4:
        print("\nTranspose of Matrix A:")
        print(A.T)
        print("\nTranspose of Matrix B:")
        print(B.T)

    elif choice == 5:
        if A.shape[0] == A.shape[1]:
            print("\nDeterminant of Matrix A:")
            print(np.linalg.det(A))
        else:
            print("Determinant not possible. Matrix A must be square.")

    else:
        print("Invalid choice!")

    # Continue option
    cont = input("\nDo you want to continue? (yes/no): ").lower()
    if cont != "yes":
        print("\nThank you for using the Matrix Operations Tool.")
        break
