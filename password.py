#password
#password = a123456
password = 'a123456'
y = 3 #剩餘次數
while y > 0:#當剩餘次數大於0次執行迴圈
	y = y - 1#當失敗的時候剩餘次數遞減
	key = input('請輸入密碼: ')
	if key == password:
		print('登入成功')
		break #離開迴圈
	else:
		print('登入失敗')#當剩餘次數=0時值行
		print('帳號已鎖定')
		if y > 0:#當剩餘次數>0時值行
			print('密碼錯誤! 還有',  y, '次機會')
		else:
			print('請重新驗證')


