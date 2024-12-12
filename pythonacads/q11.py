# def triangular_pattern(a):
#   n=len(a)
#   row =0
#   while (row*row+1)//2 <n:
#     row+=1
#   row-=1
#   start=0
#   result=[]
#   for r in range(1,row+1):
#     end= start + r
#     if r%2==0:
#       result.extend(a[start:end][::-1])
#     else:
#       result.extend(a[start:end])
#     start = end
#   if start<n:
#     result.extend(a[start:])
#   return ' '.join(map(str, result))
# a = list(map(int,input().split(',')))
# b = triangular_pattern(a)
# print(b)

# 11
# 12 15
# 13 16 18
# 14 17 19 20
def triangular_pattern_column_wise(a):
    n = len(a)
    row = 0
    
    # Determine the number of rows for the triangular pattern
    while (row * (row + 1)) // 2 < n:
        row += 1
    row -= 1
    
    # Build the triangle structure
    triangle = []
    start = 0
    for r in range(1, row + 1):
        end = start + r
        if end <= n:
            if r % 2 == 0:
                triangle.append(a[start:end][::-1])  # Reverse for even rows
            else:
                triangle.append(a[start:end])  # Normal order for odd rows
        start = end
    
    # Collect elements in column-wise order
    result = []
    for col in range(len(triangle[-1])):  # Max columns equal to the last row size
        for row in range(len(triangle)):
            if col < len(triangle[row]):
                result.append(triangle[row][col])
    
    # Print the result
    print(' '.join(map(str, result)))

# Input
a = list(map(int, input("Enter numbers separated by commas: ").split(',')))
triangular_pattern_column_wise(a)

