def check(mat: list[list[float | int]]) -> None:
    for row in mat:
        if not isinstance(row,list):
            raise TypeError('Все строки матрицы должны быть списками')
    if mat:
        lenrow=len(mat[0])
        for row in mat:
            if len(row) != lenrow:
                raise ValueError('Матрица должна быть прямоугольной')
    
    
def transpose(mat: list[list[float | int]]) -> list[list]:
    check(mat)
    if not mat:
        return []
    res=[]
    for i in range(len(mat[0])):
        nrow=[]
        for row in mat:
            nrow.append(row[i])
        res.append(nrow)
    return res

def row_sums(mat: list[list[float | int]]) -> list[float]:
    check(mat)
    return [sum(row) for row in mat]

def col_sums(mat: list[list[float | int]]) -> list[float]:
    check(mat)
    return(row_sums(transpose(mat)))

def result(function, cases) -> None:
    for value in cases:
        try:
            result = function(value)
        except (ValueError, TypeError) as error:
            result = error

        print(f"{value} -> {result}")
        
if __name__ == "__main__":
    print("transpose:")
    result(transpose, [[[1, 2, 3]], [[1], [2], [3]], [[1, 2], [3, 4]], [], [[1, 2], [3]]])

    print("\nrow_sums:")
    result(row_sums, [[[1, 2, 3], [4, 5, 6]], [[-1, 1], [10, -10]], [[0, 0], [0, 0]], [[1, 2], [3]]])

    print("\ncol_sums:")
    result(col_sums, [[[1, 2, 3], [4, 5, 6]], [[-1, 1], [10, -10]], [[0, 0], [0, 0]], [[1, 2], [3]]])
