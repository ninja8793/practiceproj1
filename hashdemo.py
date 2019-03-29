from xlwt import Workbook
SetofBook = set()
class Book:
    def __init__(self,bname,authorname,publications):

        self.bname=bname
        self.authorname=authorname
        self.publications=publications

    def __str__(self):  # object represenation -- whenever you are going to print object.. instead of class name and memory address, contents shud be printed..
        return '\n Book Name : {}, Author: {},Publications:{}'.format(self.bname,self.authorname,self.publications)

    def __repr__(self): # if someone tries to print collection of emp object..s
        return str(self)

    def __eq__(self, other):
        return self.authorname==other.authorname

    def __hash__(self):
        return self.authorname.__hash__()
a=0
NoOfRec = int(input('How many records you want to Insert:'))
filename = "D:\\Python\\practice\\python_excel_test.xls"
excel_file = Workbook()
sheet = excel_file.add_sheet('BookInfo')
sheet.write(0, 0, 'Book Name')
sheet.write(0, 1, 'Author name')
sheet.write(0, 2, 'Publications')

while (a<=NoOfRec):
    bname = input('Enter book name:')
    authorname = input('Enter author name:')
    publications = input('Enter Publications:')

    row = 1
    sheet.write(row, 0, bname)
    sheet.write(row, 1, authorname)
    sheet.write(row, 2, publications)
    row = row + 1
    excel_file.save(filename)
    filename.close()

    print('Data Saved into ExcelSheet...!')
    a+=1

    if a==NoOfRec:
        break

'''
    _continue = int(input('Do you want to enter more if yes enter pos no :'))
    if _continue <= 0:
            break
'''



