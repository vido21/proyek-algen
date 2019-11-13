#!/usr/bin/python3

import time
import random
from model import Model
from itertools import combinations

random.seed(time.time())

def populationInitiation(maxPopulation,chromLength):
    population=[]

    for _ in range(maxPopulation):
        randomChrom=[random.randint(0, 1 << 8) for i in range(chromLength)]
        population.append({"kromosom":randomChrom,"fitness":0})

    return population

def seleksi(population,pilih):
    matingPool=[]
    while len(matingPool) < pilih:
        a=random.choice(population)
        b=random.choice(population)
        if (a['fitness']>b['fitness']):
            if a not in matingPool:
                matingPool.append(a)
            else :
                continue
        else:
            if b not in matingPool:
                matingPool.append(b)
            else :
                continue
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
    # Ambil n/2 dari nC2 population
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
    # hasilnya akan terdapat sebanyak 2x|population| awal
    return offspring


def mutasi(population,panjangKromosom):

    individu=population.index(random.choice(population))
    gen=random.randint(0,panjangKromosom+1)
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

    #inisiasi population
    population = populationInitiation(5, 8)
    
    #menghitung fitness
    fitness(population)
    print("Inisiasi Populasi")
    for individu in population:
        print(individu)
    print("")

    for i in range(20):

        #seleksi
        population = seleksi(population,3)

        print("seleksi generasi ke "+str(i+1))
        for individu in population:
            print(individu)
        print("")

        #crossover
        population = crossover(population)

        #menghitung fitness
        fitness(population)
        print("crossover generasi ke "+str(i+1))
        for individu in population:
            print(individu)
        print("")

        #mutasi
        mutasi(population,8)
        print("mutasi generasi ke "+str(i+1))
        for individu in population:
            print(individu)
        print("")
