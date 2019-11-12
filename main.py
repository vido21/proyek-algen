from model import Model
import random
from itertools import combinations

def populationInitiation(maxPopulation,chromLength):
    population=[]

    for _ in range(maxPopulation):
        randomChrom=[random.randint(0, 1 << 8) for i in range(chromLength)]
        population.append({"kromosom":randomChrom,"fitness":0})

    return population

def seleksi(population,pilih):
    matingPool=[]
    for _ in range(pilih):
        a=random.choice(population)
        b=random.choice(population)
        if (a['fitness']>b['fitness']):
            matingPool.append(a)
        else:
            matingPool.append(b)
    return matingPool

def one_point_crossover(x, y):
    # crossover on position 4
    x = "{0:b}".format(x).zfill(9)
    y = "{0:b}".format(y).zfill(9)
    cx = int(x[:4] + y[4:], 2)
    cy = int(y[:4] + x[4:], 2)
    return (cx, cy)

def crossover(population):
    offspring = []
    tmp = combinations(population, 2)
    x = []
    for _ in tmp:
        x.append(_)
    random.shuffle(x)
    # Ambil n/2 dari nC2 populasi
    x = x[:len(population)//2]
    for p1, p2 in x:
        tx = []
        ty = []
        for index in range(len(p1['kromosom'])):
            result = one_point_crossover(p1['kromosom'][index], p2['kromosom'][index])
            tx.append(result[0])
            ty.append(result[1])
        offspring.append({'kromosom':tx, 'fitness':0})
        offspring.append({'kromosom':ty, 'fitness':0})
    offspring.extend(population)
    # hasilnya akan terdapat sebanyak 2x|populasi| awal
    return offspring

def mutasi(population):
    chromLength=8
    individu=population.index(findchoose.random(population))
    gen=random.randint(0,chromLength+1)
    population[individu]['kromosom'][gen]=random.randint(1,255)
    m=Model(population[individu]['kromosom'])
    m.train()
    population[individu]['fitness']=m.evaluate()
    del m

def fitness(population):
    for individu in range(len(population)):
        if (population[individu]['fitness'] != 0) : continue
        m=Model(population[individu]['kromosom'])
        m.train()
        population[individu]['fitness']=m.evaluate()
        del m

if __name__ == "__main__":
    #inisiasi Populasi
    population = populationInitiation(5, 8)

    # for i in range(5):
    #     #menghitung fitness
    #     fitness(population)
        
    #     #seleksi
    #     population = seleksi(population,3)
    #     print(population)

    #     #crossover
    #     population = crossover(population)
    #     fitness(population)

    #     #mutasi
    #     mutasi(population)

    
    print(population)
    
    # totalPopulasi=[]
    # matingPool=seleksi(inisiasiPopulasi,3)
    # while len(totalPopulasi)<50:
