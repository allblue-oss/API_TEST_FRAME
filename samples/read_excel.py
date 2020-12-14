#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/14 10:58
# @Author : 杜云慧
# @Site : 
# @File : read_excel.py
# @Software: PyCharm

import os
import xlrd

excel_path = os.path.join(os.path.dirname(__file__), 'data\\test_data.xlsx')

wb = xlrd.open_workbook(excel_path)  # 创建工作簿对象
sheet = wb.sheet_by_name("Sheet1")  # 创建表格对象
# sheet = wb.sheet_by_index(0)
cell_value = sheet.cell_value(0, 0)  # 直接取值，行列下标从0开始

merged = sheet.merged_cells

# 逻辑： 凡是在Merged_cell属性内的单元格 ，它的值都等于左上角首个单元格的值

row_index = 3
col_index = 0

for (rlow, rhigh, clow, chigh) in merged:  # 遍历表格中所有合并单元格位置信息
    if (row_index >= rlow and row_index < rhigh):  # 判断行坐标
        if (col_index >= clow and col_index < chigh):  # 判断列坐标
            # 如果满足条件，就把合并单元格第一个位置的值赋给其他单元格
            cell_value = sheet.cell_value(rlow, clow)


def get_merged_cell_value(row_index, col_index):
    '''技能获取普通单元格的数据，又能获取合并单元格的数据'''
    cell_value = None
    for (rlow, rhigh, clow, chigh) in merged:  # 遍历表格中所有合并单元格位置信息
        if (row_index >= rlow and row_index < rhigh):  # 判断行坐标
            if (col_index >= clow and col_index < chigh):  # 判断列坐标
                # 如果满足条件，就把合并单元格第一个位置的值赋给其他单元格
                cell_value = sheet.cell_value(rlow, clow)
                break  # 防止循环判断，出现值覆盖的情况
            else:
                cell_value = sheet.cell_value(row_index, col_index)
        else:
            cell_value = sheet.cell_value(row_index, col_index)
    return cell_value


# print(get_merged_cell_value(4, 0))

for i in range(1, 9):
    print(get_merged_cell_value(i, 0))
