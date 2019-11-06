import random
class Yolov3(object):

	def __init__(self):
		self.num=0
		self.input_size=[8,16,32]
	def __iter__(self):
		return self
	def __next__(self):
		a = random.choice(self.input_size)
		self.num=self.num+1
		if self.num<3:
			return a
		else:
			raise StopIteration
yolo=Yolov3()
for data in yolo:
	print(data)
