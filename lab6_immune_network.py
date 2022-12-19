import numpy as np
import random

class Cell:
    def __init__(self):
        self.max = None
        self.min = None
        self.position = None
        self.fitness = 0

    def make_start_position(self):
        return [random.uniform(self.min,self.max), random.uniform(self.min,self.max)]

    def calc_fitness(self):
        pass

    def checkposition(self):
        for n in range(len(self.position)):
            if self.position[n] < self.min:
                self.position[n] = self.min
                
            elif self.position[n] > self.max:
                self.position[n] = self.max


class ImmuneNetwork:
    def __init__(self,cell_class,count_sb,count_sg,nb,nc,bs,bb,br,bn):
        self.cell = cell_class
        self.antibody = self.make_start_population(count_sb) #Sb
        self.antigen = self.make_start_population(count_sg) #Sg

        self.memory_cells = [] #Sm - клетки памяти
        self.nb = nb #nb - колво лучших антител
        self.nc = nc #nc - колво клонов на 1 антитело
        self.bs = bs #bs - степень селекции (<1)
        self.bb = bb #bb - порог гибели
        self.br = br #br - порог сжатия
        self.bn = bn #bn - коэф обновления

        self.best_cell = None

    def make_start_population(self,count_cells):
        population = []
        for i in range(count_cells):
            population.append(self.cell())
        return population
    
    def affinity(self,x,y): #аффинность больше если расст меньше
        return (x[0]-y[0])**2+(x[1]-y[1])**2

    def compression(self, population):
        for i in range(len(population)):
            for j in range(i+1,len(population)):
                if population[i] != None and population[j] != None:
                    if self.affinity(population[i].position,population[j].position) >= self.br:
                        if population[i].fitness < population[j].fitness:
                            population[j] = None
                        else:
                            population[i] = None
        return list(filter(lambda x: x != None, population))

    def mutation(self,cell,koeff):
        cell.position[0] += koeff*random.uniform(-0.5,0.5)
        cell.position[1] += koeff*random.uniform(-0.5,0.5)
        cell.checkposition()
        cell.calc_fitness()
        return cell

    def find_best_cell(self): 
        self.best_cell = min(self.antibody, key=lambda x: x.fitness)

    def get_antibody_positions(self):
        return [i.position + [i.fitness] for i in self.antibody]

    def get_antigen_positions(self):
        return [i.position + [i.fitness] for i in self.antigen]

    def next_iteration(self):
        for i in self.antigen:
            self.antibody.sort(key=lambda x: self.affinity(x.position,i.position), reverse=False)
            max_bg_affinity = self.antibody[:self.nb]

            clones = []
            for j in max_bg_affinity:
                clones += [j]*self.nc

            clones.sort(key=lambda x: x.fitness, reverse=False)
            for j in range(len(clones)):
                clones[j] = self.mutation(clones[j],(j+1)/len(clones))

            clones.sort(key=lambda x: self.affinity(x.position,i.position), reverse=False)
            self.memory_cells = clones[:int(self.bs*self.nb*self.nc)]

            self.memory_cells = list(filter(lambda x: self.affinity(x.position,i.position) < self.bb, self.memory_cells))

            self.memory_cells = self.compression(self.memory_cells)

            self.antibody += self.memory_cells
            self.antibody = self.compression(self.antibody)

            self.antibody.sort(key=lambda x: x.fitness, reverse=True)
            for j in range(int(len(self.antibody)*self.bn)):
                self.antibody[j] = self.cell()

            self.find_best_cell()


class ImmRosenbrock(Cell):
    def __init__(self):
        Cell.__init__(self)
        self.max = 2
        self.min = -2
        self.position = self.make_start_position()
        self.calc_fitness()

    def calc_fitness(self):
        self.fitness = ImmRosenbrock.fun(self.position[0],self.position[1])

    @staticmethod
    def fun(x1,x2):
        return (1-x1)**2 + 100*(x2-x1**2)**2

    @staticmethod
    def graph():
        x1 = np.linspace(-2, 2, 100)
        x2 = np.linspace(-2, 2, 100)
        x1,x2 = np.meshgrid(x1, x2)
        f = np.array([ImmRosenbrock.fun(x1[i],x2[i]) for i in range(len(x1))])
        return x1,x2,f
