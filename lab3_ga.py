import numpy as np
import random

class GA:
    @staticmethod
    def fun(x,y):
        return (1-x)**2 + 100*(y-x**2)**2

    @staticmethod
    def fun_text():
        return 'f(x,y) = (1-x)^2 + 100*(y-x^2)^2'

    def make_start_population(self,N):
        population = []
        for i in range(N//4):
            group = []
            for j in range(0,3):
                group.append([random.uniform(-2,2),random.uniform(-1,3)])
            population.append(group)
        return population

    def selection(self,population): # Метод ранжирования
        selected = []
        for i in population:
            fitnes_res = []
            for j in i:
                fitnes_res.append((j,self.fun(j[0],j[1])))
            fitnes_res = sorted(fitnes_res, key=lambda f: f[1])
            group = []
            for j in fitnes_res[:3]:
                group.append(j[0])
            selected.append(group)
        return selected

    def mutation(self,gen):
        m = 20
        
        a = random.choices([0,1], weights=[1-1/m,1/m], k=m)
        delta = sum([a[i]*2**(-i) for i in range(m)])

        interval_izmenenia = 2
        alpha = 0.5 * interval_izmenenia

        sign = random.choices(['+','-'], weights=[0.5,0.5], k=1)
        if sign == '+':
            return gen + alpha*delta
        else:
            return gen - alpha*delta

    def recombination(self,population): # Дискретная рекомбинация
        new_population = []
        for i in population:
            new_generation_for_group = []
            new_generation_for_group.append([self.mutation(i[1][0]),i[0][1]])
            new_generation_for_group.append([self.mutation(i[2][0]),i[0][1]])
            new_generation_for_group.append([i[0][0],self.mutation(i[1][1])])
            new_generation_for_group.append([i[0][0],self.mutation(i[2][1])])
            new_population.append(new_generation_for_group)
        return new_population

    def method(self,population):
        # селекция
        selected = self.selection(population)
        # Размножение + Мутации
        population = self.recombination(selected)
        return population

    def graph(self):
        x1 = np.linspace(-2, 2, 100)
        x2 = np.linspace(-2, 4, 100)
        x1,x2 = np.meshgrid(x1, x2)
        f = np.array([GA.fun(x1[i],x2[i]) for i in range(len(x1))])
        return x1,x2,f




