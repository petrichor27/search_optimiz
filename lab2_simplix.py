import numpy as np
import scipy
from scipy.optimize import minimize

class SimplixMethod:
    @staticmethod
    def fun(x):
        return 2*x[0]**2 + 2*x[0]*x[1] + 2*x[1]**2 - 4*x[0] - 6*x[1]

    @staticmethod
    def fun_text():
        return "f(x1,x2) = 2*(x1)^2 + 2*x1*x2\n+ 2*(x2)^2 - 4*x1 - 6*x2\n      x1 + 2*x2 <= 2,\n     x1 >= 0, x2 >= 0"

    @staticmethod
    def main_lim_fun(x):
        return -x[0] - 2*x[1] + 2

    def method(self):
        x = [0.1,0.1]
        bounds = ((0, 2), (0, 1))
        start = np.array([x[0], x[1]])
        result = minimize(SimplixMethod.fun, start, method='SLSQP', constraints={'type': 'ineq', 'fun': SimplixMethod.main_lim_fun}, bounds=bounds)
        x_min = result.x

        result = [x_min[0], x_min[1], SimplixMethod.fun(x_min)]
        result_text = 'Координаты найденной точки\nминимума:\nx = '+str(round(result[0],3))+"\ny = "+str(round(result[1],3))+"\nf(x,y) = "+str(round(result[2],3))
        return result, result_text

    def graph(self):
        x1 = np.linspace(0, 2, 50)
        x2 = np.linspace(0, 1, 50)
        x1,x2 = np.meshgrid(x1, x2)

        for i in range(len(x1)):
            for j in range(len(x1[i])):
                if x1[i][j] + 2*x2[i][j] > 2:
                    x1[i][j] = x1[i][j-1]
                    x2[i][j] = x2[i][j-1]

        f = np.array([SimplixMethod.fun([x1[i],x2[i]]) for i in range(len(x1))])
        return x1,x2,f

# SimplixMethod().graph()
# python lab2_simplix.py