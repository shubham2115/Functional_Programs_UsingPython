class Matrix:

    @staticmethod
    def inputMatrix(Rows, Col):

        matrix = []
        print("Enter the entries in row wise:")

        for M in range(Rows):
            array = []
            for N in range(Col):
                array.append(int(input()))  # for input in array
            matrix.append(array)

        print("The 2D array is given below:")

        for M in range(Rows):
            for N in range(Col):
                print(matrix[M][N], end=" ")  # printing array
            print()


Rows = int(input("Enter the number of rows:"))
Col = int(input("Enter the number of columns:"))
Matrix.inputMatrix(Rows, Col)
