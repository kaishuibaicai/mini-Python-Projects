done = ['01.rmvb	cartoon_characterdetectionai_Origin_Video_20180122_00000001_00',
'02.rmvb	cartoon_characterdetectionai_Origin_Video_20180122_00000002_00',
'03.rmvb	cartoon_characterdetectionai_Origin_Video_20180122_00000003_00',
'04.rmvb	cartoon_characterdetectionai_Origin_Video_20180122_00000004_00',
'05.rmvb	cartoon_characterdetectionai_Origin_Video_20180122_00000005_00',
'06.rmvb	cartoon_characterdetectionai_Origin_Video_20180122_00000006_00',
'07.rmvb	cartoon_characterdetectionai_Origin_Video_20180122_00000007_00',
'08.rmvb	cartoon_characterdetectionai_Origin_Video_20180122_00000008_00',
'09.rmvb	cartoon_characterdetectionai_Origin_Video_20180122_00000009_00',
'10.rmvb	cartoon_characterdetectionai_Origin_Video_20180122_00000010_00',
'13.rmvb	cartoon_characterdetectionai_Origin_Video_20180122_00000011_00',
'14.rmvb	cartoon_characterdetectionai_Origin_Video_20180122_00000012_00',
'15.rmvb	cartoon_characterdetectionai_Origin_Video_20180122_00000013_00',
'18.rmvb	cartoon_characterdetectionai_Origin_Video_20180122_00000014_00',
'23.rmvb	cartoon_characterdetectionai_Origin_Video_20180122_00000015_00',
'28.rmvb	cartoon_characterdetectionai_Origin_Video_20180122_00000016_00',
'33.rmvb	cartoon_characterdetectionai_Origin_Video_20180122_00000017_00',
'12.rmvb	cartoon_characterdetectionai_Origin_Video_20180122_00000018_00',
'20.rmvb	cartoon_characterdetectionai_Origin_Video_20180122_00000019_00',
'27.rmvb	cartoon_characterdetectionai_Origin_Video_20180122_00000020_00',
'58.mp4	cartoon_characterdetectionai_Origin_Video_20180122_00000022_00',
'36.rmvb	cartoon_characterdetectionai_Origin_Video_20180122_00000018_00',
'36.rmvb	cartoon_characterdetectionai_Origin_Video_20180122_00000023_00',
'47.mp4	cartoon_characterdetectionai_Origin_Video_20180122_00000024_00',
'49.mp4	cartoon_characterdetectionai_Origin_Video_20180122_00000025_00']

el = []
whole = []
n = 0
for i in range(64):
	n = n + 1
	a = '%02d' % n
	whole.append(a)
	
for i in done:
	if i[0:2] in whole:
		whole.remove(i[0:2])

print (whole)