x = '2'
y = '-8'

def reader(x,y):
	os_x = None
	os_y = None
	if x.startswith('-') == True:
		os_x = 'LEFT'
	else:
		os_x = 'RIGHT'

	if x.startswith('-') == True:
		os_x = 'LEFT'
	else:
		os_x = 'RIGHT'

	if y.startswith('-') == True:
		os_y = 'BOTTOM'
	else:
		os_y = 'TOP'

	return os_x, os_y

def final(func):
	os_x = func[0]
	os_y = func[1]
	num = 0
	if os_x == 'LEFT' and os_y == 'BOTTOM':
		num = '3'
	elif os_x == 'LEFT' and os_y == 'TOP':
		num = '2'
	elif os_x == 'RIGHT' and os_y == 'TOP':
		num = '1'
	elif os_x == 'RIGHT' and os_y == 'BOTTOM':
		num = '4'
	print(num)

final(reader(x, y))
