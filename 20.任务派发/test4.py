import re 


txt='pose_20180330_1200194.fffff'



rg = re.compile('(pose_\\d+_\\d+)',re.IGNORECASE|re.DOTALL)
m = rg.search(txt)
if m:

    print (m.group())
