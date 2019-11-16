# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11.16

# Description:
#   csv（主程序）
# ------------------------(max to 80 columns)-----------------------------------

import csv

filename = 'test_write.csv'
repeat_times = 10

#try to write a row
header_data = ['item','c1', 'c2']
row_data = [1, '第1列数据', '第2列数据'] #data of a row
with open(filename, "w", encoding='utf8',  newline='') as csvfile:
    writer = csv. writer(csvfile)
    writer.writerow(header_data)
    writer.writerow(row_data)

    for cnt in range(repeat_times):
        row_data = [cnt, '第一列数据','第二列数据']
        writer.writerow(row_data)

# Practice 2 - read
with open(filename, "r", encoding='utf8') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        print(line)
