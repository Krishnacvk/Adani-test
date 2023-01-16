import random

def create_2d_list(numberOfRows, numberOfColumns):
    two_d_list = []
    for i in range(numberOfRows):
        row = []
        for j in range(numberOfColumns):
            row.append(random.randint(0, 100))
        two_d_list.append(row)
    return two_d_list
def sort_2d_list(two_d_list, columnIndex):
    return sorted(two_d_list, key=lambda x: x[columnIndex])
    

two_d_list = create_2d_list(2, 4)
print(two_d_list)
sorted_two_d_list = sort_2d_list(two_d_list, 2)
print(sorted_two_d_list)