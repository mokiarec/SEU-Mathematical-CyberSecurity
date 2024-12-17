# Num为学号
from sympy.codegen import While

Num = '57123514'

r1 = int(Num[-3])
r2 = int(Num[-2])
r3 = int(Num[-1])
print(f"r1的值为{r1}，r2的值为{r2}，r3的值为{r3}")

G = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
G1 = {
    'A': '10',
    '2': 'Q',
    '3': 'A',
    '4': '5',
    '5': '2',
    '6': '6',
    '7': 'K',
    '8': '3',
    '9': '8',
    '10': '9',
    'J': '7',
    'Q': 'J',
    'K': '4'
}
G2 = {
    'A': '3',
    '2': '6',
    '3': '7',
    '4': 'A',
    '5': '10',
    '6': 'K',
    '7': '4',
    '8': '2',
    '9': 'J',
    '10': 'Q',
    'J': '9',
    'Q': '5',
    'K': '8'
}
G3 = {
    'A': '4',
    '2': 'A',
    '3': '3',
    '4': 'K',
    '5': 'J',
    '6': '10',
    '7': '6',
    '8': 'Q',
    '9': '8',
    '10': '9',
    'J': '5',
    'Q': '7',
    'K': '2'
}

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

# 求最小公倍数
def lcm(n, m):
    return n * m / gcd(n, m)

# 洗牌
def Shuffle(Card, Sequence, Times):
    """
    :param Card: 牌数组
    :param Sequence: 洗牌规则
    :param Times: 洗牌次数
    :return:
    """
    Card_temp = Card.copy()
    for i in range(Times):  # 进行Times次洗牌
        for j in range(len(G)): # 遍历字典G，将对应的 Key 映射到 Value
            Card_temp[j] = Sequence[Card_temp[j]]
    return Card_temp

# 将置换分解为轮换
def Alternate_decompose(Group):
    """
    :param Group: 洗牌顺序
    :return:
    """
    SubGroup = []
    InnerGroup = Group.copy()
    # 对 洗牌顺序（交换群）的每个相进行分析
    for i in Group:
        Group_temp = {}
        index = i
        while index in InnerGroup:  # 若当前项没有被分析过
            Group_temp[index] = InnerGroup[index]   # 将当前项加入到轮换群
            next_index = InnerGroup[index]  # 标记下一个可能的项
            del InnerGroup[index]   # 将当前项删除（已分析过）
            index = next_index
        if Group_temp:  # 若这次轮换构成了轮换群
            SubGroup.append(Group_temp)     # 记录
    return SubGroup

# 求牌从初始值经过洗牌后复原的最小次数
def Min_Recover(Group):
    """
    :param Group: 洗牌顺序
    :return:
    """
    decompose = Alternate_decompose(Group) # 将交换群分解成多个轮换群
    times = 1
    # 求所有轮换群的最小公倍数，即所有的轮换群都重置的最小次数
    for i in decompose:
        times = lcm(times, len(i))
    return int(times)

if __name__ == '__main__':
    print(f"按照群置换G1洗r1次：{Shuffle(G, G1, r1)}")
    print(f"按照群置换G2洗r2次：{Shuffle(G, G2, r2)}")
    print(f"按照群置换G3洗r3次：{Shuffle(G, G3, r3)}")

    print(Alternate_decompose(G1))
    print(Alternate_decompose(G2))
    print(Alternate_decompose(G3))

    print(f"G群最少通过G1循环{Min_Recover(G1)}次后重新回到G")
    print(f"G群最少通过G2循环{Min_Recover(G2)}次后重新回到G")
    print(f"G群最少通过G3循环{Min_Recover(G3)}次后重新回到G")

    print(f"G按G1洗了{r1}次后，再洗{Min_Recover(G1) - r1 % Min_Recover(G1)}次后重新回到G")
    print(f"G按G2洗了{r2}次后，再洗{Min_Recover(G2) - r2 % Min_Recover(G2)}次后重新回到G")
    print(f"G按G3洗了{r3}次后，再洗{Min_Recover(G3) - r3 % Min_Recover(G3)}次后重新回到G")