# temperature conversion: C / F
def temperatureConver():
    unit = input('In this temperature in Celsius or Fahrenheit (C/F):')
    temp = float(input('Enter the temperature:')) # float() 允許有小數點的數

    if (unit == 'c'):
        # (c*9/5)+32=f
        Temp = round((temp*9)/5+32, 1)   # round(number, 1) 取小數點到第一位
        print(f'{temp} C° = {Temp} F°')  # 符號°: Windows, alt+0176  
    elif(unit == 'f'):
        Temp = round((temp -32)*5/9, 1)
        print(f'{temp} F° = {Temp} C°')
    else:
        print(f'{unit} is invaild unit of measurement')

# 台幣轉換: 泰銖/ 日幣/ 美金(就是新台幣 1元是 ?泰銖/ 日幣/ 美金) class 與 callback function

# 建立一個台幣換算美金和日幣的callback fun (function A pass a argument to function B)
def dollars(money, cb):
    return cb(money)
def toUSA(m):
    return m*0.031
def toJan(m):
    return m*4.75
m_unit = input("新台幣換算美金(按'a')或日圓(按'j'): ")
money = int(input("輸入兌換金額(單位:台幣): "))
if m_unit == 'a':
    ans = dollars(100, toUSA)
    print(ans)
elif m_unit == 'j':
    ans = dollars(money, toJan)
    print(ans)
else:
    print(f'{m_unit} is invaild unit of measurement')


# 建立一個台幣換算美金和日幣的class fun
class Dollars:
    def __init__(self, money):
        self.m = money
        # self.unit = unit
    def toUSA(self):
        return self.m*0.031
    def toJan(self):
        return self.m*4.75
m_unit = input("新台幣換算美金(按'a')或日圓(按'j'): ")
m = int(input("輸入兌換金額(單位:台幣): "))
if m_unit == 'a':
    ans = Dollars(m).toUSA()
    print(ans)
elif m_unit == 'j':
    ans = Dollars(m).toJan()
    print(ans)
else:
    print(f'{m_unit} is invaild unit of measurement')