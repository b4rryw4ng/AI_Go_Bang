import colors
class node:
	def __init__(self, dir1, dir1_cnt, dir2, dir2_cnt, dir3, dir3_cnt):
		self.dir1= dir1
		self.dir1_cnt= dir1_cnt
		self.dir2= dir2
		self.dir2_cnt= dir2_cnt
		self.dir3= dir3
		self.dir3_cnt= dir3_cnt
	def print_p(self):
		print(self.dir1, self.dir1_cnt, self.dir2, self.dir2_cnt, self.dir3, self.dir3_cnt)





h = 9
flag = 1
flag1 = 0
for i in range(217):
	if flag == 1 and flag1 != 1:
		print ( h * '  ', end= '')
		flag = 0
	if flag1 == 1 and flag == 1:
		print ( h * '  ', end= '')
		flag = 0

	if i < 10 :
		print ('  ', end= '')
	elif i < 100:
		print (' ', end = '')

	if i >= 60 and i<= 63:
		print ('', colors.red(str(i)), end ='')
	elif i >= 74 and i<= 78:
		print ('', colors.red(str(i)), end ='')
	elif i >= 89 and i<= 94:
		print ('', colors.red(str(i)), end ='')
	elif i >= 105 and i<= 111:
		print ('', colors.red(str(i)), end ='')
	elif i >= 122 and i<= 127:
		print ('', colors.red(str(i)), end ='')
	elif i >= 138 and i<= 142:
		print ('', colors.red(str(i)), end ='')
	elif i >= 153 and i<= 156:
		print ('', colors.red(str(i)), end ='')

	else :
		print ('', colors.white(str(i)), end= '')

	if i == 8 or i == 18 or i == 29 or i == 41 or i == 54 or i == 68 or i == 83 or i == 99 or i == 116 or i == 132 or i == 147 or i == 161 or i == 174 or i == 186 or i == 197 or i == 207 or i == 216:
		print ('\n')
		flag = 1;

		if h>0 and flag1 == 0:
			h -=1
		elif flag1 == 1:
			h+=1

		if h==0:
			flag1 = 1
			h+=2
nodes=[]
nodes.append(node(True,1,True,6,False,3))

nodes[0].print_p()	
