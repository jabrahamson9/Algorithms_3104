import xlwt 
from xlwt import Workbook

def sort(filename):
	count=0
	temp1=[]
	try:
		file=open(filename,"r")
	except IOError:
		return None
	for line in file:
		temp=[]
		line=line.strip("\n")
		temp=line.split()
		temp1.append(temp[0])
	return temp1




def f(x):
	alpha_index = {'X': 24, 'F': 6, 'A': 1, 'Q': 17, 'D': 4, 'S': 19, 'U': 21, 'M': 13, 'L': 12, 'H': 8, 'Z': 26, 'E': 5, 'N': 14, 'V': 22, 'P': 16, 'R': 18, 'G': 7, 'C': 3, 'I': 9, 'B': 2, 'K': 11, 'O': 15, 'T': 20, 'J': 10, 'Y': 25, 'W': 23}
	if x in alpha_index:
		return alpha_index[x]
	

def h(temp1, bucket_size, filename2):
	wb =xlwt.Workbook()
	counter=0
	countname=1
	countvalue=1
	# try:
	# 	file1=open(filename2,"a")
	# except IOError:
	# 	return None
	file1 = wb.add_sheet(filename2)
	for name in temp1:
		if counter<60000:
			sum_character = 0
			name = name.upper()
			for character in name:
				sum_character = sum_character + f(character)
				sum_character = sum_character % bucket_size
			
			file1.write(countname, 0, name)
			file1.write(countvalue, 1, sum_character)
			countname=countname+1
			countvalue=countvalue+1
			counter=counter+1
	wb.save('hashoutput.xls')
	return None

if __name__ == '__main__':
	array=[]
	array=sort("census.txt")
	h(array, 175, "output.csv")
