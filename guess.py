#產生一個隨機整數1~100
#讓使用者重複輸入去猜
#猜對的話 印出猜對了
#猜錯的話 要印出比答案小/大

import random
start = int(input('請輸入範圍起始值:'))
end = int(input('請輸入範圍結束值:'))

r = random.randint(start,end)
count = 0
while True:

	count += 1
	num = input('請輸入數字:')
	num = int(num)

	if num == r:
		print('猜對了!')
		print('這是你猜的第 ',count,'次!')
		break

	elif num > r:
		print('比答案大')

	elif num < r:
		print('比答案小')	

	print('這是你猜的第 ',count,'次!')