import random;
r = random.randint(1,100);
while True:
	num = input("请输入一个1-100的数字：");
	num = int(num);
	if num < r:
		print("比答案小！继续猜");
	elif num > r:
		print("比答案大！继续猜");
	else:
		print("猜对了！");
		break;