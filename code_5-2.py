#розмір масиву.
n = 7

#створення і заповнення масиву.
array = [[7 - (i - j) if i >= j else 0 for j in range(n)] for i in range(n)]

#виведення масиву на екран.
for row in array:
    print(*row)
