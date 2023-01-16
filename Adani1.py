import random

class two_d_list(object):

    def __init__(self, numberOfRows, numberOfColoumns):

        self.numberOfRows = numberOfRows

        self.numberOfColoumns = numberOfColoumns

 

    def create_2d_list(self):

       

        List1 = []

        List2 = []

       

        for j in range(0, self.numberOfColoumns):

            List2.append(random.randrange(0,100))

        

        for i in range(0, self.numberOfRows):

            List1.append(random.randrange(0,100))

        return List1

 

 

column_size = int(input("Enter size of column: "))

row_size = int(input("Enter size of row: "))

 

 

list_object = two_d_list(row_size, column_size )

print(list_object.create_2d_list())