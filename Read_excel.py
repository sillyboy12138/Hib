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

def write1_data(ret,retu,row):
    workbook=copy.copy(table1)
    worksheet=workbook.get_sheet(0)
    if ret==retu:
        worksheet.write(row,7,'pass')
        workbook.save('icbc.xlsx')
    else:
        worksheet.write(row,7,'false')
        workbook.save('icbc.xlsx')

def write2_data(ret,retu,row):
    workbook = copy.copy(table2)
    worksheet = workbook.get_sheet(1)
    if ret == retu:
        worksheet.write(row, 6, 'pass')
        workbook.save('icbc.xlsx')
    else:
        worksheet.write(row,6,'false')
        workbook.save('icbc.xlsx')
