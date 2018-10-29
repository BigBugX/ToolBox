import numpy as np
from scipy import misc
from PIL import Image
import cv2

dim1 = 800
dim2 = 600
acc_sum = 0
count_90 = 0
count_80 = 0
count_70 = 0
count_60 = 0
count_50 = 0
count_40 = 0

for img_count in range(0, 274):
	org = cv2.imread('.\\ann%d.png'%img_count, 0)
	pre = cv2.imread('.\\pre%d.png'%img_count, 0)

	org = org / 255
	pre = pre / 255

	count_and = 0
	count_or = 0

	for row in range (0, dim1):
		for col in range (0, dim2):
			if ((org[row][col]==1) and (pre[row][col]==1)):
				count_and = count_and + 1
			if ((org[row][col]==1) or (pre[row][col]==1)):
				count_or = count_or	+ 1

	print(count_and/count_or)
	if((count_and/count_or) >= 0.9):
		count_90 = count_90 + 1
	elif((count_and/count_or) >= 0.8):
		count_80 = count_80 + 1
	elif((count_and/count_or) >= 0.7):
		count_70 = count_70 + 1
	elif((count_and/count_or) >= 0.6):
		count_60 = count_60 + 1
	elif((count_and/count_or) >= 0.5):
		count_50 = count_50 + 1
	elif((count_and/count_or) >= 0.4):
		count_40 = count_40 + 1
	acc_sum = acc_sum + count_and/count_or

print("total acc_sum: ", acc_sum/274)
print("90%: ", count_90)
print("80%: ", count_80)
print("70%: ", count_70)
print("60%: ", count_60)
print("50%: ", count_50)
print("40%: ", count_40)


"""
org = cv2.imread('.\\ann1.png', 0)
pre = cv2.imread('.\\pre1.png', 0)

#orgarr = np.array(org)
#prearr = np.array(pre)
org = org / 255
pre = pre / 255

dim1, dim2 = org.shape[0], org.shape[1]

count_and = 0
count_or = 0

for row in range (0, dim1):
	for col in range (0, dim2):
		if ((org[row][col]==1) and (pre[row][col]==1)):
			count_and = count_and + 1
		if ((org[row][col]==1) or (pre[row][col]==1)):
			count_or = count_or	+ 1

print(count_and/count_or)
"""
