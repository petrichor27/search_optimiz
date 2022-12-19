#-*- coding: utf-8 -*-
import random
import math
import numpy as np
from lab5_pybee import *

class Himmelblaybee(Floatbee):
    count = 2
    
    @staticmethod
    def getstartrange():
        return [6.0] * Himmelblaybee.count
    
    @staticmethod
    def getrangekoeff():
        return [0.9] * Himmelblaybee.count
        
    def __init__(self):
        Floatbee.__init__(self)
        self.minval = [-6.0] * Himmelblaybee.count
        self.maxval = [6.0] * Himmelblaybee.count
        self.position = [random.uniform(self.minval[n], self.maxval[n]) for n in range(Himmelblaybee.count)]
        self.calcfitness()
        
    def calcfitness(self):
        """Расчет целевой функции. Этот метод необходимо перегрузить в производном классе. 
        Функция не возвращает значение целевой функции, а только устанавливает член self.fitness
        Эту функцию необходимо вызывать после каждого изменения координат пчелы"""
        self.fitness = -Himmelblaybee.fun(self.position[0],self.position[1])

    @staticmethod
    def fun(x1,x2):
        return (x1*x1 + x2 - 11)**2 + (x1 + x2*x2 - 7)**2

    @staticmethod
    def graph():
        x1 = np.linspace(-6, 6, 100)
        x2 = np.linspace(-6, 6, 100)
        x1,x2 = np.meshgrid(x1, x2)
        f = np.array([Himmelblaybee.fun(x1[i],x2[i]) for i in range(len(x1))])
        return x1,x2,f



class Rastriginbee(Floatbee):
    count = 2
    
    @staticmethod
    def getstartrange():
        return [5.0] * Rastriginbee.count
        
    @staticmethod
    def getrangekoeff():
        return [0.9] * Rastriginbee.count 
        
    def __init__(self):
        Floatbee.__init__(self)
        self.minval = [-5.0] * Rastriginbee.count
        self.maxval = [5.0] * Rastriginbee.count
        self.position = [random.uniform(self.minval[n], self.maxval[n]) for n in range(Rastriginbee.count)]
        self.calcfitness()
    
    def calcfitness(self):
        """Расчет целевой функции. Этот метод необходимо перегрузить в производном классе. 
        Функция не возвращает значение целевой функции, а только устанавливает член self.fitness
        Эту функцию необходимо вызывать после каждого изменения координат пчелы"""
        self.fitness = -Rastriginbee.fun(self.position[0],self.position[1])

    @staticmethod
    def fun(x1,x2):
        return 20 + x1**2 - 10*np.cos(2*np.pi*x1) + x2**2 - 10*np.cos(2*np.pi*x2)

    @staticmethod
    def graph():
        x1 = np.linspace(-5, 5, 100)
        x2 = np.linspace(-5, 5, 100)
        x1,x2 = np.meshgrid(x1, x2)
        f = np.array([Rastriginbee.fun(x1[i],x2[i]) for i in range(len(x1))])
        return x1,x2,f



class Rosenbrockbee(Floatbee):
    count = 2
    
    @staticmethod
    def getstartrange():
        return [2.0] * Rosenbrockbee.count
        
    @staticmethod
    def getrangekoeff():
        return [0.9] * Rosenbrockbee.count    
        
    def __init__(self):
        Floatbee.__init__(self)
        self.minval = [-2.0] * Rosenbrockbee.count
        self.maxval = [2.0] * Rosenbrockbee.count
        self.position = [random.uniform(self.minval[n], self.maxval[n]) for n in range(Rosenbrockbee.count)]
        self.calcfitness()
        
    def calcfitness(self):
        """Расчет целевой функции. Этот метод необходимо перегрузить в производном классе. 
        Функция не возвращает значение целевой функции, а только устанавливает член self.fitness
        Эту функцию необходимо вызывать после каждого изменения координат пчелы"""
        self.fitness = -Rosenbrockbee.fun(self.position[0],self.position[1])

    @staticmethod
    def fun(x1,x2):
        return (1-x1)**2 + 100*(x2-x1**2)**2

    @staticmethod
    def graph():
        x1 = np.linspace(-2, 2, 100)
        x2 = np.linspace(-2, 2, 100)
        x1,x2 = np.meshgrid(x1, x2)
        f = np.array([Rosenbrockbee.fun(x1[i],x2[i]) for i in range(len(x1))])
        return x1,x2,f
