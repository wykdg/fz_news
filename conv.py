import json

import xlwt

# data = json.load(open('data.jl', 'r'))

work_book = xlwt.Workbook()
sheet = work_book.add_sheet('data')
index = 0
for line in open('scraped_data.jl').readlines():
    try:
        line = json.loads(line)
    except:
        break
    # for index, line in enumerate(data):
    # print line['title'][:-1], '\t', line['news_type'][:-1], '\t',line['content']
    sheet.write(index, 0, line['title'])
    sheet.write(index, 1, line['news_type'])
    sheet.write(index, 2, line['content'].strip())
    index += 1
work_book.save('data.xls')
