import numpy as np
import random
import datetime
import matplotlib.pyplot as plt

class Bacterium:
    def __init__(self):
        self.max = None
        self.min = None
        self.position = None
        self.fitness = 0
        self.old_fitness = 0
        self.health = 0
        self.my_imm_cell = None
        self.radius = None
        self.velocity = self.make_new_velocity()
        self.step = self.make_new_step()

    def make_start_position(self):
        return [random.uniform(self.min,self.max), random.uniform(self.min,self.max)]

    def make_new_velocity(self):
        return [random.uniform(-1,1),random.uniform(-1,1)]

    def make_new_step(self):
        return random.uniform(0,0.3)

    def calc_fitness(self):
        pass

    def checkposition(self):
        for n in range(len(self.position)):
            if self.position[n] < self.min:
                self.position[n] = self.min
                
            elif self.position[n] > self.max:
                self.position[n] = self.max


class BacteriaAlgoritm:
    def __init__(self,bacterium,count,e_d_count,probability,count_error,start_population):
        self.count_error = count_error
        self.error = 0
        self.res = []
        self.min_time = []
        self.elimination_and_dispersal_probability = probability
        self.elimination_and_dispersal_count = e_d_count
        self.bacterium = bacterium
        self.population = self.make_start_population2(start_population)
        self.best_bacterium = None
        self.old_best_bacterium = None
        self.find_best_bacterium()

    def make_start_population(self,count):
        population = []
        for i in range(count):
            population.append(self.bacterium())
        return population

    def make_start_population2(self,p):
        population = []
        for i in p:
            a = self.bacterium()
            a.position[0] = i[0]
            a.position[1] = i[1]
            a.calc_fitness()
            population.append(a)

        return population
    
    def find_best_bacterium(self): 
        self.old_best_bacterium = self.best_bacterium
        self.best_bacterium = min(self.population, key=lambda x: x.fitness)
        if self.old_best_bacterium != None:
            if self.best_bacterium.fitness > self.old_best_bacterium.fitness:
                self.error += 1
            else: self.error = 0
    
    def get_positions(self):
        return [i.position + [i.fitness] for i in self.population]

    def norm(self,vector):
        res = 0
        for i in vector:
            res += i**2
        return np.sqrt(res)

    def chemotaxis(self):
        for i in range(len(self.population)):
            #кувырок:
            if self.population[i].old_fitness < self.population[i].fitness:
                self.population[i].velocity = self.population[i].make_new_velocity()
            
            self.population[i].position[0] += self.population[i].step * (self.population[i].velocity[0]/self.norm(self.population[i].velocity))
            self.population[i].position[1] += self.population[i].step * (self.population[i].velocity[1]/self.norm(self.population[i].velocity))
            self.population[i].checkposition()
            self.population[i].calc_fitness()
            self.population[i].step = self.population[i].make_new_step()

    def reproduction(self):
        self.population.sort(key=lambda x: x.health, reverse=False)
        self.population = self.population[:len(self.population)//2]
        self.population += self.population.copy()
        for i in range(len(self.population)//2,len(self.population)):
            self.population[i].velocity = self.population[i].make_new_velocity()
            self.population[i].calc_fitness()

    def elimination_and_dispersal(self):
        j = 1
        indexes_of_eliminated_bacteria = []
        while j < self.elimination_and_dispersal_count:
            bacterium = random.randint(0,len(self.population)-1)
            
            while indexes_of_eliminated_bacteria.count(bacterium) > 0:
                bacterium = random.randint(0,len(self.population)-1)

            probability = random.uniform(0,1)
            if probability < self.elimination_and_dispersal_probability:
                self.population[bacterium].position = self.population[bacterium].make_start_position()
                self.population[bacterium].velocity = self.population[bacterium].make_new_velocity()
                self.population[bacterium].calc_fitness()
                self.population[bacterium].old_fitness = 20000
                self.population[bacterium].step = self.population[bacterium].make_new_step()
                indexes_of_eliminated_bacteria.append(bacterium)
                j += 1

    def next_iteration(self):
        self.chemotaxis()
        self.find_best_bacterium()

        if self.error > self.count_error:
            self.reproduction()
            self.elimination_and_dispersal()
            self.find_best_bacterium()

        now = datetime.datetime.now().second*1000000+datetime.datetime.now().microsecond
        self.res.append(self.best_bacterium.fitness)
        self.min_time.append(now)
        print(self.min_time)

    
class HypersphereBacterium(Bacterium):
    def __init__(self):
        Bacterium.__init__(self)
        self.max = 100
        self.min = -100
        self.position = self.make_start_position()
        self.calc_fitness()

    def calc_fitness(self):
        self.old_fitness = self.fitness
        self.fitness = HypersphereBacterium.fun(self.position[0],self.position[1])
        self.health += self.fitness

    @staticmethod
    def fun(x1,x2):
        return (x1**2 + x2**2)

    @staticmethod
    def graph():
        x1 = np.linspace(-100, 100, 100)
        x2 = np.linspace(-100, 100, 100)
        x1,x2 = np.meshgrid(x1, x2)
        f = np.array([HypersphereBacterium.fun(x1[i],x2[i]) for i in range(len(x1))])
        return x1,x2,f

class HimmelblauBacterium2(Bacterium):
    def __init__(self):
        Bacterium.__init__(self)
        self.max = 5
        self.min = -5
        self.position = self.make_start_position()
        self.calc_fitness()

    def calc_fitness(self):
        self.old_fitness = self.fitness
        self.fitness = HimmelblauBacterium2.fun(self.position[0],self.position[1])
        self.health += self.fitness

    @staticmethod
    def fun(x1,x2):
        return (x1*x1 + x2 - 11)**2 + (x1 + x2*x2 - 7)**2

    @staticmethod
    def graph():
        x1 = np.linspace(-5, 5, 100)
        x2 = np.linspace(-5, 5, 100)
        x1,x2 = np.meshgrid(x1, x2)
        f = np.array([HimmelblauBacterium2.fun(x1[i],x2[i]) for i in range(len(x1))])
        return x1,x2,f

# tempIter = 1
# start_population = [[4.962839362865536, 3.9820617276003656], [2.5844671883527104, 1.9135660997888237], [-0.39768018724216336, -2.4576265565897604], [-3.0247691574893656, -3.4144729250174164], [-3.645195175090267, 0.16510613437367816], [-3.1779974437756464, -0.09853680039819679], [0.33084262463772607, 3.954619077172296], [3.126519754778217, 1.4734491253034374], [0.6448946280206354, -4.164979232329863], [2.302720916881908, -2.441509209494732], [-1.6825225884857273, -1.0225122745687152], [0.5208415499374475, -4.113637880496026], [4.542666066418233, 2.35431544136374], [4.079375722655458, 0.41296101002868735], [-1.62010146557382, -3.885668244593062], [2.0273135268393014, -1.7732093437130092], [0.31220596662483047, 0.9055262318169097], [-4.336180958149312, 1.8628851194625398], [-1.420779135612892, -0.053358024795514325], [-0.41371576627855866, -4.63412799667962], [-4.959299805595208, 0.7914535039464639], [4.969732857388788, 4.269780844544734], [1.8869816253497067, 3.32658674697427], [2.553217493733606, 2.077944933025239], [-2.2735902824958663, 3.9668388533354033], [2.085993433723628, -2.6087264906042664], [0.4653576610170571, 4.442105661231752], [2.9175169215996384, 2.880036343721647], [-1.7978726661375988, -3.9580265521963796], [-3.9321836551229303, 1.8740783292423906], [2.8183026834129423, 3.473196802788358], [-3.417995298685698, 2.3915344265714076], [-2.909287465591226, 3.005382155715882], [-0.166833226843897, -3.6008163322134856], [3.9097111621227185, 3.202664866160548], [2.963408010839311, -3.580602562898656], [-2.05155120171571, 2.1986492092147643], [-2.9090950202241226, -1.179098497852963], [-3.1947757238399808, -1.6036180870184724], [3.4121687681937445, -4.720174194654342], [2.6719930096949804, 4.5978998317435344], [0.4504872098040451, -4.117648385570666], [-4.3156279627387395, 3.164153178075786], [-1.871726722563627, -0.49334193777984225], [4.576508289760181, 2.721797262529238], [-0.9666001245847884, -1.5202557963276297], [-1.6366837665700573, 2.391448107941704], [1.9837199327733623, -0.4235797417746312], [-1.0285984019233831, -3.225062427172103], [0.3292893955026308, -2.6053475721581343], [1.2525396474334158, 2.468539071209089], [-0.8317894256482354, 2.224609139865528], [-4.592520282132422, -4.9776277387311545], [2.5768488168312427, 0.977686032939312], [0.1727795199247497, 3.7684957628327425], [1.188944553980516, -0.7623311783390267], [-4.475155618687791, 2.6282915739378856], [-2.0994955761017655, -4.467021824461761], [-3.0898443855752378, -1.756870508173515], [-1.744250675522939, -2.582506234609041], [3.410466703214846, -2.2925891453291647], [3.671136131521717, 2.5769460146951753], [4.522360522133356, -0.5542422295622078], [4.323195551169581, -1.4079791523880258], [2.6680702416291355, 2.785467094510386], [-0.718703951172218, 1.176548777578553], [-3.949148691563713, -3.6188035672073604], [-0.9640938523567755, -1.991566599511394], [4.159452174422224, 4.296404678482823], [-4.585305360995392, 2.6223172306152804]]
# bact = BacteriaAlgoritm(HypersphereBacterium,70,20,0.3,5,start_population)
# t=[]
# t2=[0]
# while 50 >= tempIter:
#     bact.next_iteration()
#     t.append(tempIter)
#     tempIter += 1

# for i in range(1,len(bact.min_time)):
#     t2.append(bact.min_time[i]-bact.min_time[0])

# # print(t)
# # print()
# # print(bact.res)
# plt.plot(t, bact.res)
# plt.show()

# plt.plot(t2, bact.res)
# plt.show()