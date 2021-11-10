import copy
import xlrd
import xlwt

wb = xlrd.open_workbook(r'C:\Users\呆瓜\Desktop\icbc.xlsx')
table1=wb.sheets()[0]
table2=wb.sheets()[1]
def get_data(file_name,index):
    aa = []
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_index(index)
    for i in range(1, sheet.nrows):
        aa.append(list(sheet.row_values(i, 1, sheet.ncols-1)))
    return aa
