# _*_ coding: utf-8 _*_

"""
python_visual.py by xianhu
"""

import numpy as np
import matplotlib
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from mpl_toolkits.mplot3d import Axes3D



def simple_plot():
    """
    simple plot
    """
    
    # 生成数据
    x = np.linspace(-np.pi,np.pi,256,endpoint=True)
    y_cos,y_sin = np.cos(x),np.sin(x)

    # 生成画布
    plt.figure(figsize=(12,9),dpi=80)
    plt.title("Easy Plot")
    plt.grid(True)

    # 设置 x 轴
    plt.xlabel('x')
    plt.xlim(*(-4.0,4.0))

    # 设置 y 轴
    plt.ylabel('y')
    plt.ylim(-1.0,1.0)
      # 设置刻度线
    plt.yticks(np.linspace(-1, 1, 9, endpoint=True)) 

    # 画两条曲线
    plt.plot(x,y_cos,"b--",linewidth=2.0,label='cos example') 
    plt.plot(x,y_sin,"b--",linewidth=2.0,label='sin example') 

    # 设置图例位置
    plt.legend(loc="upper left")

    # 展示
    plt.show()
    return 0

#simple_plot()


# and more 

def simple_advanced_plot():
    """
    simple advanced plot
    """
    # 生成测试数据
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    y_cos, y_sin = np.cos(x), np.sin(x)

    # 生成画布, 并设定标题
    plt.figure(figsize=(8, 6), dpi=80)
    plt.title("complex plot")
    plt.grid(True)

    # 画图的另外一种方式
    ax_1 = plt.subplot(111)
    ax_1.plot(x, y_cos, color="blue", linewidth=2.0, linestyle="--", label="左cos")
    ax_1.legend(loc="upper left", shadow=True)

    # 设置Y轴(左边)
    ax_1.set_ylabel("left cos")
    ax_1.set_ylim(-1.0, 1.0)
    ax_1.set_yticks(np.linspace(-1, 1, 9, endpoint=True))

    # 画图的另外一种方式
    ax_2 = ax_1.twinx()
    ax_2.plot(x, y_sin, color="green", linewidth=2.0, linestyle="-", label="右sin")
    ax_2.legend(loc="upper right", shadow=True)

    # 设置Y轴(右边)
    ax_2.set_ylabel('right sin ')
    ax_2.set_ylim(-2.0, 2.0)
    ax_2.set_yticks(np.linspace(-2, 2, 9, endpoint=True))

    # 设置X轴(共同)
    ax_1.set_xlabel("x")
    ax_1.set_xlim(-4.0, 4.0)
    ax_1.set_xticks(np.linspace(-4, 4, 9, endpoint=True))

    # 图形显示
    plt.show()
    return
# simple_advanced_plot()


# 子图的画法

def sub_plot():
    """
    simple subplot
    """

    # 设置 style 
    style_list = ["g+-", "r*-", "b.-", "yo-"]
    plt.figure(figsize=(12,9))
    # 挨个开始画图
    for num in range(4):
        # 测试数据
        x = np.linspace(0.0, 2+num, num=10*(num+1))
        y = np.sin((5-num) * np.pi * x)

        # 开始设置图
        plt.subplot(2,2,num+1)
        plt.title('plot %d'%(num+1))
        plt.plot(x,y,style_list[num])
    plt.show()
    return 0
# sub_plot()


# 随机漫步测试

# 测试一下 yield 关键字
def gen_rand(n):
    """
    n is steps ,default 100
    """ 
    if isinstance(n,int):
        n = abs(n)
    else:
        n = 100 
    for i in np.random.randint(-10,10,size=n):
        yield i 

# matplotlib plot 

def random_walk():
    """
    Easy Random Walk
    """  

    # 生成数据
    num = np.random.randint(-5,5,100)
    x , y = [],[]
    for k,v in enumerate(num):
        x.append(k)
        y.append( num[:k+1].sum() )

    # 开始画图

    plt.figure(figsize=(12,9),dpi=80)
    plt.title('Easy Random Walk')
    plt.grid(True)

    # 设置 x 轴
    plt.xlabel('x')
    plt.xlim(0,100)
    plt.xticks(np.linspace(0,100,1,endpoint=True))

    # 设置 y 轴 
    plt.ylabel('y')
    plt.ylim(-100,100)
    plt.yticks(np.linspace(-100,100,1,endpoint=True))

    # 画曲线
    plt.plot(x,y,'b--',linewidth=2.0)
    plt.legend('upper left')

    plt.show()
    return 0

random_walk()
