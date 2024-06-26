#-*- coding: utf-8 -*-
"""
Реализация алгоритма роя пчел
"""

import random
import math

class Floatbee:
    """Класс пчел, где в качестве координат используется список дробных чисел"""    
    def __init__(self):
        # Положение пчелы (искомые величины)
        self.position = None
        
        # Интервалы изменений искомых величин (координат)
        self.minval = None
        self.maxval = None
        
        # Значение целевой функции
        self.fitness = 0.0
        
    def calcfitness(self):
        """Расчет целевой функции. Этот метод необходимо перегрузить в производном классе. 
        Функция не возвращает значение целевой функции, а только устанавливает член self.fitness
        Эту функцию необходимо вызывать после каждого изменения координат пчелы"""
        pass
        
    def sort(self, otherbee):
        """Функция для сортировки пчел по их целевой функции (здоровью) в порядке убывания."""
        if self.fitness < otherbee.fitness:
            return -1
        elif self.fitness > otherbee.fitness:
            return 1
        else:
            return 0
            
    def otherpatch(self, bee_list, range_list):
        """Проверить находится ли пчела на том же участке, что и одна из пчел в bee_list. 
        range_list - интервал изменения каждой из координат"""
        if len(bee_list) == 0:
            return True
        
        for curr_bee in bee_list:
            position = curr_bee.getposition()
            
            for n in range(len(self.position)):
                if abs(self.position[n] - position[n]) > range_list[n]:
                    return True
        
        return False
    
    def getposition(self):
        """Вернуть копию (!) своих координат"""
        return [val for val in self.position]
        
    def goto(self, otherpos, range_list):
        """Перелет в окрестность места, которое нашла другая пчела. Не в то же самое место! """

        # К каждой из координат добавляем случайное значение
        self.position = [otherpos[n] + random.uniform(-range_list[n], range_list[n]) for n in range(len(otherpos))]
        
        # Проверим, чтобы не выйти за заданные пределы
        self.checkposition()
        
        # Расчитаем и сохраним целевую функцию
        self.calcfitness()
        
    def gotorandom(self):
        # Заполним координаты случайными значениями
        self.position = [random.uniform(self.minval[n], self.maxval[n]) for n in range(len(self.position))]
        self.checkposition()
        self.calcfitness()  
        
        
    def checkposition(self):
        """Скорректировать координаты пчелы, если они выходят за установленные пределы"""
        for n in range(len(self.position)):
            if self.position[n] < self.minval[n]:
                self.position[n] = self.minval[n]
                
            elif self.position[n] > self.maxval[n]:
                self.position[n] = self.maxval[n]
    
class Hive:
    """Улей. Управляет пчелами"""
    def __init__(self, scoutbeecount, selectedbeecount, bestbeecount, selsitescount, bestsitescount, range_list, beetype):
        """scoutbeecount - Количество пчел-разведчиков
        selectedbeecount - количество пчел, посылаемое на один из лучших участков
        selectedbeecount - количество пчел, посылаемое на остальные выбранные участки
        
        selsitescount - количество выбранных участков
        bestsitescount - количество лучших участков среди выбранных
        beetype - класс пчелы, производный от bee
        
        range_list - список диапазонов координат для одного участка"""
        
        self.scoutbeecount = scoutbeecount
        self.selectedbeecount = selectedbeecount
        self.bestbeecount = bestbeecount        
        
        self.selsitescount = selsitescount
        self.bestsitescount = bestsitescount
        
        self.beetype = beetype
        
        self.range = range_list
        
        # Лучшая на данный момент позиция
        self.bestposition = None
        
        # Лучшее на данный момент здоровье пчелы (чем больше, тем лучше)
        self.bestfitness = -1.0e9
        
        # Начальное заполнение роя пчелами со случайными координатами
        beecount = scoutbeecount + selectedbeecount * selsitescount + bestbeecount * bestsitescount
        self.swarm = [beetype() for n in range(beecount)]
        
        # Лучшие и выбранные места
        self.bestsites = []
        self.selsites = []
        
        self.swarm.sort (key = lambda bee: bee.fitness, reverse = True)     
        self.bestposition = self.swarm[0].getposition()
        self.bestfitness = self.swarm[0].fitness
    
    def positions(self):
        return [i.getposition()+[i.fitness] for i in self.swarm]

    def sendbees(self, position, index, count):
        """ Послать пчел на позицию. Возвращает номер следующей пчелы для вылета """
        for n in range(count):
            # Чтобы не выйти за пределы улея
            if index == len(self.swarm):
                break
            
            curr_bee = self.swarm[index]
            
            if curr_bee not in self.bestsites and curr_bee not in self.selsites:
                # Пчела не на лучших или выбранных позициях
                curr_bee.goto(position, self.range)
            
            index += 1
        
        return index
    
    def nextstep(self):
        """Новая итерация"""        
        # Выбираем самые лучшие места и сохраняем ссылки на тех, кто их нашел
        self.bestsites = [self.swarm[0]]
        
        curr_index = 1
        for currbee in self.swarm [curr_index:-1]:
            # Если пчела находится в пределах уже отмеченного лучшего участка, то ее положение не считаем 
            if currbee.otherpatch(self.bestsites, self.range):
                self.bestsites.append(currbee)
                        
                if len(self.bestsites) == self.bestsitescount:
                    break
                
            curr_index += 1
        
        self.selsites = []
        
        for currbee in self.swarm [curr_index:-1]:
            if currbee.otherpatch(self.bestsites, self.range) and currbee.otherpatch(self.selsites, self.range):
                self.selsites.append(currbee)
                    
                if len(self.selsites) == self.selsitescount:
                    break
                    
        # Отправляем пчел на задание :)
        # Отправляем сначала на лучшие места
        
        # Номер очередной отправляемой пчелы. 0-ую пчелу никуда не отправляем
        bee_index = 1
        
        for best_bee in self.bestsites:
            bee_index = self.sendbees(best_bee.getposition(), bee_index, self.bestbeecount)
            
        for sel_bee in self.selsites:
            bee_index = self.sendbees(sel_bee.getposition(), bee_index, self.selectedbeecount) 

        # Оставшихся пчел пошлем куда попадет
        for curr_bee in self.swarm[bee_index:-1]:
            curr_bee.gotorandom()
    
        self.swarm.sort(key = lambda bee: bee.fitness, reverse = True)     
        self.bestposition = self.swarm[0].getposition()
        self.bestfitness = self.swarm[0].fitness
