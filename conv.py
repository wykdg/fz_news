import json

import xlwt

data = json.load(open('data.json', 'r'))

work_book = xlwt.Workbook()
sheet = work_book.add_sheet('data')

for index, line in enumerate(data):
    # print line['title'][:-1], '\t', line['news_type'][:-1], '\t',line['content']
    sheet.write(index, 0, line['title'])
    sheet.write(index, 1, line['news_type'])
    sheet.write(index, 2, line['content'])
work_book.save('data.xls')
