def makegreaterzero(function):
	def _mydecorator(*args, **kw):
		# виконати дії перед викликом реальної ункції
		res = function(*args, **kw)
		# виконати дії після виклику функції
		if res<0:
			res = -res
		elif res==0:
			res = 1

		return res
	# повренути підфункцію
	return _mydecorator


@makegreaterzero
def f(x):
	return 2*x - 1

@makegreaterzero
def f1(x,y):
	return -1



def ininterval(a,b):
	def _mydecorator(function):
		def __mydecorator(*args, **kw):
			# виконати дії перед викликом реальної ункції
			res = function(*args, **kw)
			# виконати дії після виклику функції
			if res<a or res>b:
				res = (a+b)/2

			return res
		# повренути підфункцію
		return __mydecorator
	return _mydecorator


@makegreaterzero
def f(x):
	return 2*x - 1

@makegreaterzero
def f1(x,y):
	return -1



@ininterval(0,1)
def f3(x):
	return 2*x - 1

@ininterval(0,2)
def f4(x,y):
	return -1


class ExceptNonEqual(Exception):

	def __init__(self):
		super()

	def __str__(self):
		return "Non Equal sizes!!!"




def key_value_equal_sizes(fun):

	def _key_value_equal_sizes(*args,**kwargs):

		if len(args) != len(kwargs):
			raise ExceptNonEqual
		res = fun(*args, **kwargs)
		return res
	return _key_value_equal_sizes


@key_value_equal_sizes
def func1(*args, **kwargs):
	p = 1
	for x,y in zip(args,kwargs.values()):
		if y==0:
			continue
		p *= (x + 1/ y)

	return p


if __name__ == '__main__':
	print("{}".format(f(2)))
	print("{}".format(f(-3)))
	print("{}".format(f1(1,4)))

	print("{}".format(f3(1)))
	print("{}".format(f3(-3)))
	print("{}".format(f4(1,4)))


	a1 = func1(1,2,3,y1=1,y2=2,y3=3)
	print("a=",a1)

	try:
		a1 = func1(1,2,3,y1=1,y2=2)
		print("a=",a1)
	except ExceptNonEqual as e:
		print("Caught exception: ", e)