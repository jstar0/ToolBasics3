import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

width = 0.55
b = width / (2 * np.pi)
theta = 32 * np.pi

R = 16 * width

r_circle = 3.41 - 0.55

length_list = [2.2 - 0.55] * 223
length_list[0] = 3.41 - 0.55

t0 = 0.275

def f(theta):  # 螺线的极坐标方程
    return b * theta

def f1(theta):  # 螺线的笛卡尔坐标方程
    return b * theta * np.cos(theta), b * theta * np.sin(theta)  # x, y

def C(theta):  # 弧长函数
    return (
        b / 2 * (theta * np.sqrt(1 + theta**2) + np.log(theta + np.sqrt(1 + theta**2)))
    )

def calculate_theta(t):  # 求 theta
    return np.sqrt(-2 * (t - 0.275) / b + (32 * np.pi) ** 2)

def slope(theta):  # 斜率
    return (np.sin(theta) + theta * np.cos(theta)) / (
        np.cos(theta) - theta * np.sin(theta)
    )

def get_back_handle(theta, L):  # 计算后把手的 theta
    x, y = f1(theta)

    def d_distance(theta2):
        return (
            (b * theta2 * np.cos(theta2) - x) ** 2
            + (b * theta2 * np.sin(theta2) - y) ** 2
            - L**2
        )

    theta_2 = fsolve(d_distance, theta + 0.1)
    while d_distance(theta_2) > 1e-4 or theta_2 < theta:
        theta_2 += 1e-2

    return theta_2

def draw(t):  # 画底图
    theta = np.linspace(0, 32 * np.pi, 100000)
    x, y = f1(theta)
    plt.plot(x, y, label='Base Spiral')
    
    result = get_result_at_t(t)
    for res in result:
        plt.plot(res['front']['x'], res['front']['y'], 'ro')  # Front handle
        plt.plot(res['back']['x'], res['back']['y'], 'bo')  # Back handle
    
    plt.axis("equal")
    plt.legend()
    plt.title(f"Positions at t={t}s")
    plt.show()

def get_result_at_t(t):
    theta_front = calculate_theta(t)
    v_front = 1.0
    result_list = []
    for k in range(len(length_list)):
        x_front, y_front = f1(theta_front)
        theta_back = get_back_handle(theta_front, length_list[k])[0]
        x_back, y_back = f1(theta_back)
        
        beta = np.arctan2(y_back - y_front, x_back - x_front)  # 该板凳与 x 轴的夹角
        k_front = slope(theta_front)
        alpha_front = np.arctan(k_front)
        k_back = slope(theta_back)
        alpha_back = np.arctan(k_back)
        v_back = v_front * np.cos(beta - alpha_front) / np.cos(beta - alpha_back)

        result_list.append(
            {
                "front": {"x": x_front, "y": y_front, "v": v_front},
                "back": {"x": x_back, "y": y_back, "v": v_back},
            }
        )

        theta_front = theta_back
        v_front = v_back

    return result_list

# Plot the graph at t=66s
draw(266)