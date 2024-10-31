"""
    RSA 加密算法密钥制作：
    1、选取两个质数p，q
    2、质数相乘 N = p * q
    3、欧拉函数 T = (p - 1) * (q - 1)
    4、选取公钥 E 满足：质数；1<公钥<T；不是T的因子
    5、计算私钥 D 满足：(D * E) % T = 1
"""
import random

# 初始化数据
# Num为学号，Reverse_Num为反转学号，List_Prime为不大于Sqrt(Num)的所有素数
Num = '57123514'
Reverse_Num = int(Num[::-1])
Num = int(Num)
print(f"学号：{Num},学号反序：{Reverse_Num}")

# 找出不大于n最大的两个素数，使用平凡除法
def GetMaxPrime(n):
    # 1.1、找出不大于sqrt(n)的素数
    List_Prime = []
    Result = []
    sqrt_n = int(n**0.5)
    for i in range(2, sqrt_n):
        Status = True
        for j in range(2, i):
            if i % j == 0 :
                Status = False
                break
        if Status == True :
            List_Prime.append(i)

    # 1.2、平凡除法
    for i in range(n, 2, -1):
        Status = True
        for j in List_Prime:
            if i % j == 0:
                Status = False
                break
        if Status == True and len(Result) < 2:
            Result.append(i)
        if len(Result) >= 2:
            break

    for elem in Result: # 打印结果
        print(f"找到最大的两个素数结果：{elem}")
    return Result[0], Result[1]

# 求n模m的逆元，使用广义欧几里得除法
def GetInverseElement(n, m):
    if gcd(n, m) != 1: # 不互质，无逆元
        return

    if n > m:
        a = n
        b = m
    else:
        a = m
        b = n

    r = 1
    # 列表法
    list = {'s': [], 't': [], 'q': [], 'r': []}
    list['r'].extend([a, b])
    list['q'].extend([0, 0])
    list['s'].extend([0, 1, 0])
    list['t'].extend([0, 0, 1])
    # a 是被除数，b 是除数，r 是余数
    while a % b != 0:
        r = a % b
        list['r'].append(r)
        list['q'].append(a // b)
        a = b
        b = r
    list['r'].append(0)
    list['q'].append(a // b)
    # 计算s和t
    for i in range(3, len(list['r'])):
        list['s'].append(list['s'][i - 2] - list['s'][i - 1] * list['q'][i - 1])
        list['t'].append(list['t'][i - 2] - list['t'][i - 1] * list['q'][i - 1])
    result = list['s'][-1] if n > m else list['t'][-1]
    # 负数调整到正数
    while(result < 0):
        result += m
    return result

# 辗转相除法求最大公因数
def gcd(n, m):
    if n > m:
        a = n
        b = m
    else:
        a = m
        b = n
    r = 1
    # a 是被除数，b 是除数，r 是余数
    while a % b != 0:
        r = a % b
        a = b
        b = r
    return b

# RSA加密运算 参考教材例子3.2.7
def RSA(p, q):
    print(f"1、两个质数：{p}，{q}")
    # 计算模数
    n = p * q
    print(f"2、质数相乘：N = {n}")
    # 计算欧拉函数
    euler = (p - 1) * (q - 1)   # p，q 都是素数
    print(f"3、欧拉函数：T = {euler}") # 打印欧拉函数

    e = 0
    # 随机找到 1 < e < euler 的一个素数，且与 euler 互质
    while True :
        e = random.randint(2, euler - 1)
        Status = True
        for j in range(2, e):   # 判断e是否为素数
            if e % j == 0:
                Status = False
                break
        if Status == True and gcd(e, euler) == 1:  # e 为素数 且 与euler互质
            break
    print(f"4、选取公钥：E = {e}")

    # 求e模euler的逆元
    d = GetInverseElement(e, euler)
    print(f"5、计算私钥：D = {d}")
    print(f"总结：公钥是K_e = ({e},{n})  私钥是K_d = ({d},{n})")

    # 对学号Num进行加密
    print(f"--- 对数据{Num}进行加密 ---")
    Data = Num
    C = []
    M = []
    for i in range(0, 3):
        C.append((Data % 1000) ** e % n)
        Data //= 1000
    print(f"加密后：{C}")
    for i in range(2, -1, -1):
        M.append(C[i] ** d % n)
    print(f"解密后：{M}")

if __name__ == '__main__':
    p, q = GetMaxPrime(Reverse_Num)
    RSA(23, 29)