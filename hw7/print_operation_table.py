def print_operation_table(operation, num_rows=6, num_columns=6):
    rjust_index = len(str(operation(num_rows, num_columns)))
    for i in range(num_columns):
        for j in range(num_rows):
            print(str(operation(i+1, j+1)).rjust(rjust_index), end=" ")
        print('\n')



print_operation_table(lambda x,y: x**y,4,4)
print_operation_table(lambda x,y: x*y)