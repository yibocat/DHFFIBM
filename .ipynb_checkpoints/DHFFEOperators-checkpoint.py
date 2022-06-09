import math
from math import *

# 代数 t-范数 加性元
def algebraic_tau(x):
    return -math.log2(x)
def in_algebraic_tau(x):
    return 1/math.pow(2,x)
def algebraic_s(x):
    return algebraic_tau(1-x)
def in_algebraic_s(x):
    return 1-in_algebraic_tau(x)

# 代数 t-范数
def algebraic_T(x,y):
    return in_algebraic_tau(algebraic_tau(x)+algebraic_tau(y))
def algebraic_S(x,y):
    return in_algebraic_s(algebraic_s(x)+algebraic_s(y))

def pithy_algebraic_T(x,y):
    return x*y
def pithy_algebraic_S(x,y):
    return x+y-x*y

# 直觉模糊 Interaction 运算
def IFIO_MD_Power(mu,nu,l):
    # 隶属度幂运算
    # mu 表示隶属度，nu 表示非隶属度，l 表示幂次方
    m=l*algebraic_s(mu+nu)
    n=l*algebraic_s(nu)
    return in_algebraic_s(m)-in_algebraic_s(n)

def IFIO_NMD_Power(mu,nu,l):
    # 非隶属度幂运算
    # mu 表示隶属度，nu 表示非隶属度，l 表示幂次方
    return in_algebraic_s(l*algebraic_s(nu))

def IFIO_MD_Times(mu,nu,l):
    # 隶属度倍运算
    return in_algebraic_s(l*algebraic_s(mu))

def IFIO_NMD_Times(mu,nu,l):
    # 非隶属度倍运算
    m=l*algebraic_s(mu+nu)
    n=l*algebraic_s(mu)
    return in_algebraic_s(m)-in_algebraic_s(n)

def IFIO_MD_Multiply(mu1,nu1,mu2,nu2):
    # 隶属度乘法
    return pithy_algebraic_S(mu1+nu1,mu2+nu2)-pithy_algebraic_S(nu1,nu2)

def IFIO_NMD_Multiply(mu1,nu1,mu2,nu2):
    # 非隶属度乘法
    return pithy_algebraic_S(nu1,nu2)

def IFIO_MD_Plus(mu1,nu1,mu2,nu2):
    # 隶属度加法
    return pithy_algebraic_S(mu1,mu2)

def IFIO_NMD_Plus(mu1,nu1,mu2,nu2):
    # 非隶属度加法
    return pithy_algebraic_S(mu1+nu1,mu2+nu2)-pithy_algebraic_S(mu1,mu2)














# 费马模糊 Interaction 运算
def FFIO_MD_Power(mu,nu,l):
    # 隶属度幂运算
    # mu 表示隶属度，nu 表示非隶属度，l 表示幂次方
    m = math.pow(mu,3)
    n = math.pow(nu,3)
    return math.pow(IFIO_MD_Power(m,n,l),1/3)

def FFIO_NMD_Power(mu,nu,l):
    # 非隶属度幂运算
    m = math.pow(mu,3)
    n = math.pow(nu,3)
    return math.pow(IFIO_NMD_Power(m,n,l),1/3)

def FFIO_MD_Times(mu,nu,l):
    # 隶属度倍运算
    m = math.pow(mu,3)
    n = math.pow(nu,3)
    return math.pow(IFIO_MD_Times(m,n,l),1/3)

def FFIO_NMD_Times(mu,nu,l):
    # 非隶属度倍运算
    m = math.pow(mu,3)
    n = math.pow(nu,3)
    return math.pow(IFIO_NMD_Times(m,n,l),1/3)

def FFIO_MD_Multiply(mu1,nu1,mu2,nu2):
    # 隶属度乘法
    m1 = math.pow(mu1,3)
    n1 = math.pow(nu1,3)
    m2 = math.pow(mu2,3)
    n2 = math.pow(nu2,3)
    return math.pow(IFIO_MD_Multiply(m1,n1,m2,n2),1/3)

def FFIO_NMD_Multiply(mu1,nu1,mu2,nu2):
    # 非隶属度乘法
    m1 = math.pow(mu1,3)
    n1 = math.pow(nu1,3)
    m2 = math.pow(mu2,3)
    n2 = math.pow(nu2,3)
    return math.pow(IFIO_NMD_Multiply(m1,n1,m2,n2),1/3)

def FFIO_MD_Plus(mu1,nu1,mu2,nu2):
    # 隶属度加法
    m1 = math.pow(mu1,3)
    n1 = math.pow(nu1,3)
    m2 = math.pow(mu2,3)
    n2 = math.pow(nu2,3)
    return math.pow(IFIO_MD_Plus(m1,n1,m2,n2),1/3)

def FFIO_NMD_Plus(mu1,nu1,mu2,nu2):
    m1 = math.pow(mu1,3)
    n1 = math.pow(nu1,3)
    m2 = math.pow(mu2,3)
    n2 = math.pow(nu2,3)
    return math.pow(IFIO_NMD_Plus(m1,n1,m2,n2),1/3)

### 对偶犹豫模糊集的结构
### 其实就是对偶犹豫模糊元素
# s = {'MD':{0.5,0.7,0.9},'NMD':{0.2,0.3,0.5,0.6}}
## 有时间再创建对偶犹豫模糊集类

# 对偶犹豫费马模糊 Interaction 基本运算
# dhffe 表示对偶犹豫费马模糊元素
def DHFF_Power(dhffe,l):
    # 幂运算
    new_dhffe = {'MD':set(),'NMD':set()}
    for i in dhffe['MD']:
        for j in dhffe['NMD']:
            new_dhffe['MD'].add(FFIO_MD_Power(i,j,l))
            new_dhffe['NMD'].add(FFIO_NMD_Power(i,j,l))
    return new_dhffe

def DHFF_Times(dhffe,l):
    # 倍运算
    new_dhffe = {'MD':set(),'NMD':set()}
    for i in dhffe['MD']:
        for j in dhffe['NMD']:
            new_dhffe['MD'].add(FFIO_MD_Times(i,j,l))
            new_dhffe['NMD'].add(FFIO_NMD_Times(i,j,l))
    return new_dhffe

def DHFF_Multiply(dhffe1,dhffe2):
    # 乘法法则
    new_dhffe = {'MD':set(),'NMD':set()}
    for i1 in dhffe1['MD']:
        for j1 in dhffe1['NMD']:
            for i2 in dhffe2['MD']:
                for j2 in dhffe2['NMD']:
                    new_dhffe['MD'].add(FFIO_MD_Multiply(i1,j1,i2,j2))
                    new_dhffe['NMD'].add(FFIO_NMD_Multiply(i1,j1,i2,j2))
                    
#     for i1 in dhffe1['MD']:
#         for i2 in dhffe2['MD']:
#             new_dhffe['MD'].add(FFIO_MD_Multiply(i1,j1,i2,j2))
#     for j1 in dhffe1['NMD']:
#         for j2 in dhffe2['NMD']:
#             new_dhffe['NMD'].add(FFIO_NMD_Multiply(i1,j1,i2,j2))
                    
    return new_dhffe

def DHFF_Plus(dhffe1,dhffe2):
    # 加法法则
    new_dhffe = {'MD':set(),'NMD':set()}
    for i1 in dhffe1['MD']:
        for j1 in dhffe1['NMD']:
            for i2 in dhffe2['MD']:
                for j2 in dhffe2['NMD']:
                    new_dhffe['MD'].add(FFIO_MD_Plus(i1,j1,i2,j2))
                    new_dhffe['NMD'].add(FFIO_NMD_Plus(i1,j1,i2,j2))
    
    
    # for i1 in dhffe1['MD']:
    #     for i2 in dhffe2['MD']:
    #         new_dhffe['MD'].add(FFIO_MD_Plus(i1,j1,i2,j2))
    # for j1 in dhffe1['NMD']:
    #     for j2 in dhffe2['NMD']:
    #         new_dhffe['NMD'].add(FFIO_NMD_Plus(i1,j1,i2,j2))              
            
    return new_dhffe

# 检验
# def x(m,n):
#     幂运算
#     return pow(pow(1-pow(n,3),2)-pow(1-pow(m,3)-pow(n,3),2),1/3)





