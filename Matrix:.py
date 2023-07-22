class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.data])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition.")
        result_data = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result_data)

    def __mul__(self, other):
        if isinstance(other, int):
            result_data = [[self.data[i][j] * other for j in range(self.cols)] for i in range(self.rows)]
            return Matrix(result_data)
        elif isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix for matrix multiplication.")
            result_data = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in range(self.rows)]
            return Matrix(result_data)
        else:
            raise TypeError(
                f"Unsupported operand type(s) for *: 'Matrix' and '{type(other).name}'"
            )

    def __matmul__(self, other):
        return self.mul(other)

    def transpose(self):
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(transposed_data)
    
if __name__ == "__main__":
    m = Matrix([[1, 2, 3], [4, 5, 6]])
    n = Matrix([[3, 4,], [5, 6]])

    result = m.transpose()
    print("Transpose:")
    print(result)
    print()
    print(m*n)
    print()
    print(n*m)