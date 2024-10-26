# Num为学号，Reverse_Num为反转学号，List_Prime为不大于Sqrt(Num)的所有素数
Num = '57123514'
Reverse_Num = int(Num[::-1])
print(f"两个数：{Num},{Reverse_Num}")
Num = int(Num)
sqrt_Num = int(Reverse_Num**0.5)
List_Prime = []

# 1、找出不大于Num最大的两个素数，使用平凡除法
# 1.1、找出不大于sqrt(Num)的素数
for i in range(2, sqrt_Num):
    Status = True
    for j in range(2, i):
        if i % j == 0 :
            Status = False
            break
    if Status == True :
        List_Prime.append(i)

# 1.2、平凡除法
Count = 0
for i in range(Reverse_Num, 2, -1):
    Status = True
    for j in List_Prime:
        if i % j == 0:
            Status = False
            break
    if Status == True and Count < 2:
        Count += 1
        print(f"素数结果：{i}") # 打印结果
    if Count >= 2:
        break

# 2、求出Num和Reverse_Num的最大公约数和最小公倍数
# 2.1、辗转相除法求最大公约数
if Num > Reverse_Num:
    a = Num
    b = Reverse_Num
else:
    a = Reverse_Num
    b = Num
r = 1
while a % b != 0:
    r = a % b
    a = b
    b = r
    print(f"({a},{b})")
print(f"最大公约数结果：{b}")
print(f"最小公倍数结果：{int(Num * Reverse_Num / b)}")