import math
import random


class Antibody:
    def __init__(self, x_value, y_value):
        self.x = x_value
        self.y = y_value

class Antigen:
    def __init__(self, x_value, y_value):
        self.x = x_value
        self.y = y_value


class Population:
    def __init__(self):
        self.individuals = None

    def create_population_of_antibodies(self, population_size, a, b):
        self.individuals = [Antibody(random.uniform(a, b), random.uniform(a, b)) for _ in range(population_size)]

    def create_population_of_antigens(self, population_size, a, b):
        self.individuals = [Antigen(random.uniform(a, b), random.uniform(a, b)) for _ in range(population_size)]

    def create_population_of_antibodies2(self, population):
        self.individuals = [Antibody(i[0], i[1]) for i in population]

    def create_population_of_antigens2(self, population):
        self.individuals = [Antigen(i[0], i[1]) for i in population]

    def reduce_population(self, min_affinity, f):
        flag = True
        population_size = len(self.individuals)
        while flag:
            flag = False
            for i in range(population_size):
                for j in range(i + 1, population_size):
                    if self.individuals[i] is not None and self.individuals[j] is not None:
                        if affinity(self.individuals[i], self.individuals[j]) < min_affinity:
                            flag = True
                            if f(self.individuals[i].x, self.individuals[i].y) < f(self.individuals[j].x, self.individuals[j].y):
                                self.individuals[j] = None
                            else:
                                self.individuals[i] = None
        self.individuals = list(filter(lambda a: a is not None, self.individuals))

    def to_list(self):
        list_individuals_of_population = []
        for i in self.individuals:
            list_individuals_of_population.append([i.x, i.y])
        return list_individuals_of_population


# nb - количество антител, которые будут подвергнуты мутации
# nc - число клонов клонируемого антитела
# nd - число оставляемых клонов
# bb - пороговый коэффициент гибели
# br - коэффициент клонального сжатия
# iterations - количество итераций алгоритма
class ImmuneNetworkAlgorithm:
    def __init__(self, f, nb, nd, nc, bb, br):
        self.f = f
        self.nb = nb
        self.nd = nd
        self.nc = nc
        self.bb = bb
        self.br = br

    def create_memory_cells(self, population_of_antibodies, population_of_antigens):
        for antigen in population_of_antigens.individuals:
            best_antibodies = self.get_best_antibodies(population_of_antibodies, antigen, self.nb)
            population_memory_cells = self.clone_and_mutate(best_antibodies, self.nc, self.nd, antigen, self.bb, self.br)
            for memory_cells in population_memory_cells.individuals:
                population_of_antibodies.individuals.append(memory_cells)
            population_of_antibodies.reduce_population(self.br, self.f)
        return population_of_antibodies

    @staticmethod
    def get_best_antibodies(population_of_antibodies, antigen, nb):
        population_of_best_antibodies = Population()
        population_of_best_antibodies.individuals = []

        population_of_antibodies.individuals.sort(key=lambda x: affinity(x, antigen), reverse=False)

        for i in population_of_antibodies.individuals[:nb]:
            population_of_best_antibodies.individuals.append(i)
        return population_of_best_antibodies


    def clone_and_mutate(self, population_of_antibodies, nc, nd, antigen, bb, br):
        clone_population = Population()
        clone_population.individuals = []
        for antibody in population_of_antibodies.individuals:
            clone_population.individuals = []
            alpha = math.exp(-0.1 * affinity(antibody, antigen))
            for c in range(nc):
                clone_population.individuals.append(Antibody(antibody.x + alpha * random.uniform(-1, 1), antibody.y + alpha * random.uniform(-1, 1)))

        clone_population.individuals.sort(key=lambda a: affinity(a, antigen), reverse=False)

        population_memory_cells = Population()
        population_memory_cells.individuals = clone_population.individuals[:nd]

        for i in range(nd):
            if affinity(population_memory_cells.individuals[i], antigen) < bb:
                population_memory_cells.individuals = population_memory_cells.individuals[:i]
                break

        population_memory_cells.reduce_population(br, self.f)
        return population_memory_cells

    def immune_network_algorithm_init(self, a, b, size_population_of_antibodies, size_population_of_antigens):
        population_of_antibodies = Population()
        population_of_antibodies.create_population_of_antibodies(size_population_of_antibodies, a, b)
        population_of_antigens = Population()
        population_of_antigens.create_population_of_antigens(size_population_of_antigens, a, b)
        
        return population_of_antibodies, population_of_antigens

    def immune_network_algorithm_init2(self, antibodies, antigens):
        population_of_antibodies = Population()
        population_of_antibodies.create_population_of_antibodies2(antibodies)
        population_of_antigens = Population()
        population_of_antigens.create_population_of_antigens2(antigens)
        
        return population_of_antibodies, population_of_antigens

def affinity(individual1, individual2):
    return (individual1.x - individual2.x)**2 + (individual1.y - individual2.y)**2
