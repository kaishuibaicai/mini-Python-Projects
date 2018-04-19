import openpyxl
import os

filepath = 'H:\标注管理\\images\动漫角色爬取\第一周角色标注任务.xlsx'
basepath = 'H:\标注管理\\images\动漫角色爬取\第一周角色标注任务'
l = []
i = 1
def readExcel(path):
	wb = openpyxl.load_workbook(path)
	sheet = wb.get_sheet_by_name('第一周标注任务（动漫）')

	for row in sheet.rows:
		i = 1
		for cell in row:
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
					curpath = os.path.abspath(curpath)

			i +=1
			print(cell.value)
		print ()
            

if __name__ == '__main__':
    readExcel(filepath)