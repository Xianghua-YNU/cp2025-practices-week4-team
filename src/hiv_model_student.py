import numpy as np
import matplotlib.pyplot as plt

class HIVModel:
    def __init__(self, A, alpha, B, beta):
        # TODO: 初始化模型参数
        self.A = A
        self.alpha = alpha
        self.B = B
        self.beta = beta
        pass

    def viral_load(self, time):
        # TODO: 计算病毒载量
        return self.A * np.exp(-self.alpha * time) + self.B * np.exp(-self.beta * time)
        return np.zeros_like(time)

    def plot_model(self, time):
        # TODO: 绘制模型曲线
        viral_load = self.viral_load(time)
        plt.plot(time, viral_load)
        plt.xlabel('Time (days)')
        plt.ylabel('Viral Load')
        plt.title('HIV Viral Load Model')
        plt.show()
        pass

def load_hiv_data(filepath):
    # TODO: 加载HIV数据
    try:
        data = np.load(filepath)
        return data['time_in_days'], data['viral_load']
    except:
        return np.loadtxt(filepath, delimiter=',', unpack=True)
    return np.array([]), np.array([])

def main():
    # TODO: 主函数，用于测试模型
    model = HIVModel(A=1000, alpha=0.5, B=500, beta=0.1)
    
    # 生成时间序列
    time = np.linspace(0, 10, 100)
    
    # 计算并绘制模型曲线
    model.plot_model(time)
    
    # 加载实验数据
    time_data, load_data = load_hiv_data('/home/qqq/桌面/py/ynu-computational-physics-2025-cp2025-practices-week4-cp2025-practice-week4-main/data/HIVseries.csv')
    
    # 绘制实验数据
    plt.scatter(time_data, load_data, label='Experimental Data')
    plt.legend()
    plt.show()

    pass

if __name__ == "__main__":
    main()
