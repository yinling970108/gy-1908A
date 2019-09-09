a = 1
if(a==0):
    print('我有女朋友我就笑')
else:
    print('没有女朋友我就哭')



# 90分为优秀，60-90分为良好 ，60分为不及格  小燕考了89分
h =89

if(h >= 90):
    print('小燕很优秀')
elif(h > 60):
    print('小燕良好')
else:
    print('小燕不及格')

if(h >= 90):
    print('小燕很优秀')
if(h < 90 and h >=60 ):
    print('小燕良好')
if(h < 60):
    print('小燕不及格')
