import re
import requests
import xlwt

def login():
    response=requests.get(url,headers=headers)
    response.encoding="utf-8"
    response=response.text
    fullurl(response)

def fullurl(response):
    paturl=re.findall(r'pyName="(.*?)"',response)
    patName=re.findall(r'quName="(.*?)"',response)
    for name in patName:
        Name.append(name)
    for url in paturl:
        full='http://flash.weather.com.cn/wmaps/xml/'+url+'.xml'
        FULLurl.append(full)
    for i in range(len(FULLurl)-3):
        resp=requests.get(FULLurl[i],headers=headers)
        resp.encoding="utf-8"
        resp=resp.text
        data=re.findall(r' (.*?)="',resp)
        data.pop(0)
        list_all.append(data[:18])

    wb = xlwt.Workbook('utf-8')

    for a in range(len(Name)):
        worksheet=wb.add_sheet(Name[a],cell_overwrite_ok=True)
        worksheet.write_merge(0,0,1,3,FULLurl[a])
        worksheet.write_merge(1, 1, 1, 3, 'get')
        for b in range(len(list_all[0])):
            font = xlwt.Font()
            font.bold = True
            pattern_top = xlwt.Pattern()
            pattern_top.pattern = xlwt.Pattern.SOLID_PATTERN
            pattern_top.pattern_fore_colour = 5
            style = xlwt.XFStyle()
            style.font = font
            style.pattern = pattern_top
            worksheet.write(0, 0, 'url地址',style)
            worksheet.write(1, 0, '请求方式',style)
            worksheet.write(2, 0, '请求的参数',style)
            worksheet.write(2, 1, '类型',style)
            worksheet.write(2, 2, '说明',style)
            worksheet.write(3, 0, paturl[a]+'.xml')
            worksheet.write(4, 0, '返回参数',style)
            worksheet.write(4,1,'类型',style)
            worksheet.write(4,2,'说明',style)
            worksheet.write(b+5,0,list_all[a][b])
            worksheet.write(b+5,1,'字符串')
            wb.save('weather.xlsx')

if __name__ == '__main__':
    url='http://flash.weather.com.cn/wmaps/xml/china.xml'
    FULLurl=[]
    list_all=[]
    Name=[]
    headers={
        'Content-Type':'text/xml',
        'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29'
    }
    login()