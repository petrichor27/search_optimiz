import numpy as np

class GradientMethod:
    @staticmethod
    def fun(x):
        return 2 * x[0] * x[0] + x[0] * x[1] + x[1] * x[1]
    
    def dx1(self,x):
        return 4 * x[0] + x[1]

    def dx2(self,x):
        return x[0] + 2 * x[1]

    @staticmethod
    def fun_text():
        return "f(x1,x2) = 2*(x1)^2 + x1*x2\n+ (x2)^2"

    def delta_f(self,x):
        return [self.dx1(x),self.dx2(x)]

    def norm(self,vector):
        res = 0
        for i in vector:
            res += i**2
        return np.sqrt(res)

    def method(self):
        e = 0.01
        e1 = 0.1
        e2 = 0.15
        m = 100
        k = 0
        x2 = [0.5,1]
        x1 = x2
        res = []
        
        while True:
            if self.norm(self.delta_f(x2)) >= e1:
                if k<m:
                    tk = 0.1
                    x1 = list(x2)
                    while True:
                        x2 = np.array(x1) - np.array([i*tk for i in self.delta_f(x1)])
                        if GradientMethod.fun(x2)-GradientMethod.fun(x1)<0:
                            break
                        else:
                            tk /= 2
                    if self.norm(x2-x1)<e2 and self.norm([GradientMethod.fun(x2)-GradientMethod.fun(x1)])<e2:
                        res = list(x2)
                        break
                    else: k+=1
                else: 
                    res = x2
                    break
            else: 
                res = x2
                break
        res.append(GradientMethod.fun(res))
        text_result = "Координаты найденной точки\nминимума:\nx = "+str(round(res[0],3))+"\ny = "+str(round(res[1],3))+"\nf(x,y) = "+str(round(res[2],3))+"\nКоличество итераций = "+str(k)
        return res,text_result

    def graph(self):
        x1 = np.linspace(-10, 10, 100)
        x2 = np.linspace(-10, 10, 100)
        x1,x2 = np.meshgrid(x1, x2)
        f = np.array([GradientMethod.fun([x1[i],x2[i]]) for i in range(len(x1))])
        return x1,x2,f



# GradientMethod().method()