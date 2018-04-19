# -*- coding: UTF-8 -*-
import openpyxl
import os

filepath = 'H:\标注管理\\images\动漫角色爬取\第一周角色标注任务.xlsx'
basepath = 'H:\标注管理\\images\动漫角色爬取\第一周角色标注任务'
l = []
i = 1
def readExcel(path):
	wb = openpyxl.load_workbook(path)
	sheet = wb.get_sheet_by_name('第一周标注任务（动漫）')
	curpath = ''
	for row in sheet.rows:
		l = []
		
		for cell in row:
			l.append(cell.value)

		#print (l)
		if l[1] and l[2]:
			curpath = os.path.join(basepath, l[1].strip(), l[2].strip())
			print (curpath)
			if not os.path.exists(curpath):
				os.makedirs(curpath)
				with open(os.path.join(curpath, 'keywords.txt'), 'w', encoding='utf-8') as f:
						f.write(l[3] + '\n')
		elif l[1] is None and l[2] is None:
			print (curpath)
			with open(os.path.join(curpath, 'keywords.txt'), 'a+', encoding='utf-8') as f:
				
				if l[3]:
					f.write(l[3] + '\n')

		elif l[1] is None and l[2]:
			curpath = os.path.join(os.path.dirname(curpath), l[2].strip())
			print (curpath)
			if not os.path.exists(curpath):
				os.makedirs(curpath)
				output_file = open(os.path.join(curpath, 'keywords.txt'), 'w', encoding='utf-8')
				output_file.write(l[3] + '\n')
				output_file.close()
				# with open(os.path.join(curpath, 'keywords.txt'), 'w', encoding='utf-8') as f:
						# f.write(l[3] + '\n')


		'''for cell in row:
			if i == 2:
				if cell.value :
					curpath = os.path.join(basepath, cell.value.strip())
					if not os.path.exists(curpath):
						os.mkdir(curpath)
			elif i ==3:
				if cell.value :
					curpath = os.path.join(basepath, cell.value.strip())
					if not os.path.exists(curpath):
						os.mkdir(curpath)
			elif i ==4:
				if cell.value :
					with open(os.path.join(curpath, 'keywors.txt'), 'w') as f:
						f.write(cell.value.strip(), '\n')
					curpath = os.path.abspath(os.path.join(curpath, ".."))'''

			
            

if __name__ == '__main__':
    readExcel(filepath)