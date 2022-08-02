row = int(input("Enter the number of rows: "))
colm = int(input("Enter the number of columns: "))
count = 1
matrix = [[] for x in range(row)]

for i in range(row):
  for j in range(colm):
    matrix[i].append(0)

def valid(i, j):
    if (i < 0 or i >= row or j >= colm or j < 0):
        return False
    return True


for k in range(0, row):
      matrix[k][0] = count
      count += 1
      i = k - 1
      j = 1
      while (valid(i, j)):
          matrix[i][j] = count
          count += 1
          i -= 1
          j += 1 

for k in range(1, colm):
        matrix[row-1][k] = count
        count += 1
        i = row - 2
        j = k + 1
        while (valid(i, j)):
            matrix[i][j] = count
            count += 1
            i -= 1
            j += 1

for i in range(row):
  for j in range(colm):
    print(matrix[i][j], end=" ")
  print()
