import sys
import time
from volz_servo import ServoResource
from collections import namedtuple


for i in range(0,40):
	print ("Angles",i)
	self.scale.set(i)
	time.sleep(2)
	
self.scale.set(0)


for i in range(0,-40):
	print ("Angles",i)
	self.scale.set(i)
	time.sleep(2)
	
self.scale.set(0)
