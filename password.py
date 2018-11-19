#password
#password = a123456
password = 'a123456'
y = 3 #剩餘次數
while True:#當
	key = input('請輸入密碼: ')
	if key == password:
		print('登入成功')
		break #離開迴圈
	else:
		y = y - 1
		print('密碼錯誤! 還有',  y, '次機會')
		if y == 0:
			break
			

