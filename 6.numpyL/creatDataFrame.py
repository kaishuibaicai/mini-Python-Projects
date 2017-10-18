import pandas as pd
s1 = pd.Series([1, 2])
print s1
s2 = pd.Series(['Boris', 'Mikhail'])
print s2

print pd.DataFrame([s1, s2])

new = pd.DataFrame(
	[
		[1, 2],
		['Boris', 'Mikhail']
	],
	columns=['columns1', 'columns2'],
	index=['row1', 'row2']
	)
print new