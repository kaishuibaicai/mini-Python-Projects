#-*- coding: utf-8 -*-

import sys
import time
from collections import deque

fancy_loading = deque('>--------------------')

while 1:
	print '\r%s' % ''.join(fancy_loading)
	fancy_loading.rotate(1)
	#sys.stdout.flush()
	time.sleep(0.08)