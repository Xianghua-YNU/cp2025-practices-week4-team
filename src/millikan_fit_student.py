"""
最小二乘拟合和光电效应实验
"""

import numpy as np
import matplotlib.pyplot as plt

def load_data(filename):
    """
    加载数据文件
    
    参数:
        filename: 数据文件路径
        
    返回:
        x: 频率数据数组
        y: 电压数据数组
    """
    try:
        data = []
        f = open(filename)
        lines = f.readlines()
        for each in lines:
          items = each.split(' ')
          data += [[float(i) for i in items]]
        np.array(data,dtype = int)
        f.close()
        #读取列向量
        x = [row[0] for row in data]
        y = [row[1] for row in data]
        x = np.array(x)
        y = np.array(y)
    except Exception as e:
        raise FileNotFoundError(f"无法加载文件: {filename}") from e    
    return x,y
    

def calculate_parameters(x, y):
    """
    计算最小二乘拟合参数
    
    参数:
        x: x坐标数组
        y: y坐标数组
        
    返回:
        m: 斜率
        c: 截距
        Ex: x的平均值
        Ey: y的平均值
        Exx: x^2的平均值
        Exy: xy的平均值
    """
    # 在此处编写代码，计算Ex, Ey, Exx, Exy, m和c
    if len(x) == 0 or len(y) == 0:
        raise ValueError("输入数据不能为空")
    if len(x) != len(y):
        raise ValueError("x和y数组长度必须相同")
    

    
    N = len(x)#获取数组中数据个数
    sum_x = x.sum()
    sum_y = y.sum()
    sum_xx = np.dot(x,x)
    sum_xy = np.dot(x,y)
    Ex = sum_x/N
    Ey = sum_y/N
    Exx =  sum_xx/N
    Exy = sum_xy/N
    D = (Exx - Ex**2)
    if D == 0:
        raise ValueError("无法计算参数，分母为零")
    
    m = (Exy - Ex*Ey)/(Exx - Ex**2)
    c = (Exx*Ey - Ex*Exy)/(Exx - Ex**2)
    
    return m, c, Ex, Ey, Exx, Exy
    

def plot_data_and_fit(x, y, m, c):
    """
    绘制数据点和拟合直线
    
    参数:
        x: x坐标数组
        y: y坐标数组
        m: 斜率
        c: 截距
    
    返回:
        fig: matplotlib图像对象
    """
    # 在此处编写代码，绘制数据点和拟合直线
    if np.isnan(m) or np.isnan(c):
        raise ValueError("斜率和截距不能为NaN")
    fig, ax = plt.subplots()#开一个fig和一个子图
    ax.scatter(x, y, label='experimental_data')
    m = np.array([m])
    y_fit = np.multiply(m,x) + np.array([c])
    ax.plot(x, y_fit, 'r', label='fitting')
    ax.set_xlabel('ν(Hz)')
    ax.set_ylabel('V(V)')
    ax.legend()
    return fig #绘制两个图像，添加图例
    
    
    

def calculate_planck_constant(m):
    """
    计算普朗克常量
    
    参数:
        m: 斜率
        
    返回:
        h: 计算得到的普朗克常量值
        relative_error: 与实际值的相对误差(%)
    """
    # 电子电荷
    if m <= 0:
        raise ValueError("斜率必须为正数")
    e = 1.602e-19  # C
    
    # 在此处编写代码，计算普朗克常量和相对误差
    # 提示: 实际的普朗克常量值为 6.626e-34 J·s
    h =  e*m
    r_e = (abs(h- 6.626e-34))/(6.626e-34)#计算误差
    return h,r_e

    
def main():
    """主函数"""
    # 数据文件路径
    filename = r"E:\计算物理\cp2025-practices-week4-team-main\data\millikan.txt"
    
    # 加载数据
    x, y = load_data(filename)
    
    # 计算拟合参数
    m, c, Ex, Ey, Exx, Exy = calculate_parameters(x, y)
    
    # 打印结果
    print(f"Ex = {Ex:.6e}")
    print(f"Ey = {Ey:.6e}")
    print(f"Exx = {Exx:.6e}")
    print(f"Exy = {Exy:.6e}")
    print(f"斜率 m = {m:.6e}")
    print(f"截距 c = {c:.6e}")
    
    # 绘制数据和拟合直线
    fig = plot_data_and_fit(x, y, m, c)
    
    # 计算普朗克常量
    h, relative_error = calculate_planck_constant(m)
    print(f"计算得到的普朗克常量 h = {h:.6e} J·s")
    print(f"与实际值的相对误差: {relative_error:.2f}%")
    
    # 保存图像
    fig.savefig("millikan_fit.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    main()
