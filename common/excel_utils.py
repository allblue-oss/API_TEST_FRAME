#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/14 14:13
# @Author : 杜云慧
# @Site : 
# @File : excel_utils.py
# @Software: PyCharm

'''封装excel操作'''

import os
import xlrd  # 内置模块，第三方模块，自定义模块


class ExcelUtils():
    def __init__(self, file_path, sheet_name):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.sheet = self.get_sheet()  # 整个表格对象

    '''获取表格'''

    def get_sheet(self):
        wb = xlrd.open_workbook(self.file_path)
        sheet = wb.sheet_by_name(self.sheet_name)
        return sheet

    '''获取总行数'''

    def get_row_count(self):
        row_count = self.sheet.nrows
        return row_count

    '''获取总列数'''

    def get_col_count(self):
        col_count = self.sheet.ncols
        return col_count

    '''获取单元格的值'''

    def __get_cell_value(self,row_index,col_index):
        cell_value = self.sheet.cell_value(row_index,col_index)
        return cell_value

    '''获取合并单元格位置'''

    def get_merged_info(self):
        merged_info = self.sheet.merged_cells
        return merged_info

    def get_merged_cell_value(self, row_index, col_index):
        '''既能获取普通单元格的数据，又能获取合并单元格的数据,通过位置'''
        cell_value = None
        for (rlow, rhigh, clow, chigh) in self.get_merged_info():  # 遍历表格中所有合并单元格位置信息
            if (row_index >= rlow and row_index < rhigh):  # 判断行坐标
                if (col_index >= clow and col_index < chigh):  # 判断列坐标
                    # 如果满足条件，就把合并单元格第一个位置的值赋给其他单元格
                    cell_value = self.__get_cell_value(rlow, clow)
                    break  # 防止循环判断，出现值覆盖的情况
                else:
                    cell_value = self.__get_cell_value(row_index, col_index)
            else:
                cell_value = self.__get_cell_value(row_index, col_index)
        return cell_value


    def get_sheet_data_by_dict(self):
        '''通过字典遍历表格数据'''
        all_data_list = []
        first_row = self.sheet.row(0)  # 获取首行数据
        for row in range(1, self.get_row_count()):
            row_dict = {}
            for col in range(0, self.get_col_count()):
                row_dict[first_row[col].value] = self.get_merged_cell_value(row, col)
            all_data_list.append(row_dict)
        return all_data_list

if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    excel_path = os.path.join(current_path, '..', 'samples/data/test_case.xlsx')
    excelUtils = ExcelUtils(excel_path, 'Sheet1')
    for row in excelUtils.get_sheet_data_by_dict():
      print(row)
