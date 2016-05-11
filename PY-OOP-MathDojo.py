
class MathDojo(object):
	"""docstring for MathDojo"""
	def __init__(self):
		self.result = 0

	def add(self, *num, **other):
		for something in num:
			if type(something) is list:
				self.add(*something)
			elif type(something) is dict:
				self.add(**something)
			else:	
				self.result += something
		for someother in other:
				self.result += other[someother]
		return self

	def subtract(self, *num, **other):
		for something in num:
			if type(something) is list:
				self.subtract(*something)
			elif type(something) is dict:
				self.subtract(**something)
			else:
				self.result -= something
		for someother in other:
				self.result -= other[someother]
		return self

myDic = {'three': 3, 'four': 4, 'seven': 7}
print MathDojo().add(2).add(2,5).subtract(3,2).result

print MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, myDic, [1.1, 2.3]).result