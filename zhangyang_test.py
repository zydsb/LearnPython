# date : 2020-02-29
# author : zhangyang

# 测试类型
a = 1 
if isinstance(a,list):
    print('yes')
else:
    print('no')


# fractions 分数
from fractions import Fraction
print(Fraction(16,10))
print(Fraction('0.33'))

# complex 复数
print(complex(1,2))

# list , set , dict 为不可 hash 类型

# 数字常量
int_num = 0x9ff
print(type(int_num))
print(int_num)

n = 2559
print('整数 %d 的二进制表示是：%s' %(n,bin(n)))


# 无穷大
if 2**100 < float('inf'):
    print('true')

# yield 迭代器，好处在于节省时间空间上的开销

# lambda
# 简单定义一个求 开根号 * 10 的函数
import  math 
func = lambda x: 10 * math.sqrt(x)
print(func(36))


# Decimal 
from decimal import Decimal

print(Decimal('0.01') + Decimal('0.02'))


# Set 基本知识
# 添加删除，和其他 Set 的操作，不保证有序
s = set([i for i in range(10)])
t = set([j for j in range(5,15)])
print(S ,"\n",T )

# frozenset(set) ： 把 set 变成不可变对象 

# 字符转义
s = 's\nt\no\np'
print(s)

# Raw 字符串 , 会抑制转义

s_raw = r's\nt\no\np'
print(s_raw)

# 字符串连接
print('a'+'b')
print('.'.join(['a','b']))

# 每个单词首字母大写

str0 = 'zhangyang and lipeikun'
print(str0.title())

# 字符串格式化
# 还有很多东西，不过这个可以先基本了解下即可
"""
%s : 字符串
%d : 整数
"""

# 系统信息
import sys


# 常用列表操作
# ord() : ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值

def gen():
    for i in range(10):
        yield i**2
L = []
gen_l = gen()
for i in range(5):
    print(gen_l)
    L.extend(gen_l)
print(L)


# end at line 249 , 2029-02-29 16:36



# start 2020-02-29 18:57

# 常用字典操作
D = {'name':'zhangyang','address':'beijing'}
print(D['name'])

D1 = dict(name='tom',age=12)
print(D1)

# 字典解析

D2 = {k:v for (k,v) in zip(['name','yang'],['sex','male'])}
print(D2)


# 元组是不可变对象，列表是可变对象

# 使用小括号可以创建所需结果的生成器generator object
# 和 yield 类似


# 函数注释

def gen(n):
    """
    function test.
    """
    return 1 

print(gen.__doc__)


# map()

def squre(n):
    """
    返回 n 的平方
    """
    if isinstance(n,int):
        return n**2
    else:
        return 1 
a = list(map(squre,[i for i in range(5)]))
print(a)


def maker(N):
    def action(X):
        return X ** N
    return action

f = maker(2)
f(3) 

# 函数可变参数匹配

#-- 可变参数匹配: * 和 **
    def f(*args): print(args)          # 在元组中收集不匹配的位置参数
    f(1, 2, 3)                         # 输出(1, 2, 3)
    def f(**args): print(args)         # 在字典中收集不匹配的关键字参数
    f(a = 1, b = 2)                    # 输出{'a':1, 'b':2}
    def f(a, *b, **c): print(a, b, c)  # 两者混合使用
    f(1, 2, 3, x=4, y=5)               # 输出1, (2, 3), {'x':4, 'y':5}

# 调用函数时解包
# * 解元组，** 解字典

# lambda 和 map() 等函数的组合


res0 = map( lambda x:x**2+1,[i for i in range(10)])
res1 = map( lambda x:x**2+1,[i for i in range(10) if i%2 == 1 ])



# 生成器表达式:小括号进行列表解析
# 生成器不保留生产的结果 

G = (x**2 for x in range(10))


# 定义函数时，参数的默认值是不可变的

class person():
    address = 'beijing'
    def __init__(self,name):
         self.name = name
    def __del__(self):
        print('goodbye ',self.name)

class son(person):
    pass

# 类相关的知识，后面还需要细看

# 给类动态绑定属性或者方法

class Student(object):
    pass
s = Student()
s.name = 'zhangyang'
s.school = 'bashu'
def set_age(self,age):
    self.age = age 
from types import MethodType
s.set_age = MethodType(set_age,s)  # 只给该实例绑定了该方法
s.set_age(25)
print(s.age)


# 继承

class fooParent(object):
    def __init__(self,a):
        self.parent = 'I\'m the Parent'
        print('Parent:a=' + str(a))
    def bar(self,message):
        print(message +' from Parent')

class fooChild(fooParent):
    def __init__(self,a):
        fooParent.__init__(self,a)
        print('Child:a=' + str(a))
    def bar(self,message):
        fooParent.bar(self,message)
        print(message + ' from Child')
child = fooChild('yang') 


#-- #实例方法 / 静态方法 / 类方法
class Methods(object):
    def imeth(self, x): print(self, x)      # 实例方法：传入的是实例和数据，操作的是实例的属性
    def smeth(x): print(x)                  # 静态方法：只传入数据 不传入实例，操作的是类的属性而不是实例的属性
    def cmeth(cls, x): print(cls, x)        # 类方法：传入的是类对象和数据
    smeth = staticmethod(smeth)            # 调用内置函数，也可以使用@staticmethod
    cmeth = staticmethod(cmeth)             # 调用内置函数，也可以使用@classmethod



# property 没看懂

# 重写类的方法

class Fib(object):
    def __init__(self,n):
        """
        2**n is stop condition,default value is 2**20 
        """
        self.a , self.b = 0,1
        if isinstance(n,int):
            self.stopCondtion = pow(2,abs(n)) 
        else:
            self.stopCondtion = pow(2,20)
    def __iter__(self):
        return(self)
    def next(self):
        self.a , self.b = self.b , self.a + self.b
        if self.a > self.stopCondtion:
            raise StopIteration
        else:
            return self.a


# (4)__getattr__方法: 定制类的属性操作
class Student(object):
    def __getattr__(self, attr):          # 定义当获取类的属性时的返回值
        if attr=='age':
            return 25                     # 当获取age属性时返回25
    raise AttributeError('object has no attribute: %s' % attr)



### 异常相关

#-- #捕获异常: 
        try:
        except:                               # 捕获所有的异常 等同于except Exception:
        except name:                          # 捕获指定的异常
        except name, value:                   # 捕获指定的异常和额外的数据(实例)
        except (name1, name2):
        except (name1, name2), value:
        except name4 as X:
        else:                                 # 如果没有发生异常
        finally:                              # 总会执行的部分
    # 引发异常: raise子句(raise IndexError)
        raise <instance>                      # raise instance of a class, raise IndexError()
        raise <class>                         # make and raise instance of a class, raise IndexError
        raise                                 # reraise the most recent exception


# coding = utf-8 


