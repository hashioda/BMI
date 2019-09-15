#bmi=kg/(cm/100*cm/100)
weight = input('請輸入體重(kg): ')
height = input('請輸入身高(cm): ')
w = int(weight)
h = int(height)/100
bmi = w / (h * h)
bmi = int(bmi)
if bmi < 18.5:
    print('你的BMI值是', bmi, '你的體重過輕了')
elif bmi >= 18.5 and bmi < 24:
    print('你的BMI值是', bmi, '恭喜你, 你的體重是正常範圍')
elif bmi >= 24 and bmi < 27:
    print('你的BMI值是', bmi, '你有點過重了')
elif bmi >= 27 and bmi < 30:
    print('你的BMI值是', bmi, '你屬於輕度肥胖')
elif bmi >= 30 and bmi < 35:
	print('你的BMI值是', bmi, '請注意了，你是中度肥胖')
else:
    print('你的BMI值是', bmi, '你是重度肥胖喔，一定要減肥啦')