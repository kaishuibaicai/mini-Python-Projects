lax_coordinates = (33.9425, -118.408056)
city, year, pip, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
	print ('%s/%s' % passport)
'''sort 与 sorted 区别：
sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，
而不是在原来的基础上进行的操作。'''

for country, _ in traveler_ids:
	print (country)
