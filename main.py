from model import Model
import random
from itertools import combinations

def inisiasi_populasi(maxPopulasi,panjangKromosom):
    populasi=[]

    for _ in range(maxPopulasi):
        randomKromosom=[random.randint(0, 1 << 8) for i in range(panjangKromosom)]
        populasi.append({"kromosom":randomKromosom,"fitness":0})
    return populasi

def seleksi(populasi,pilih):
    matingPool=[]
    for _ in range(pilih):
        a=random.choice(populasi)
        b=random.choice(populasi)
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

def crossover(populasi):
    offspring = []
    tmp = combinations(populasi, 2)
    x = []
    for _ in tmp:
        x.append(_)
    random.shuffle(x)
    # Ambil n/2 dari nC2 populasi
    x = x[:len(populasi)//2]
    for p1, p2 in x:
        tx = []
        ty = []
        for index in range(len(p1['kromosom'])):
            result = one_point_crossover(p1['kromosom'][index], p2['kromosom'][index])
            tx.append(result[0])
            ty.append(result[1])
        offspring.append({'kromosom':tx, 'fitness':0})
        offspring.append({'kromosom':ty, 'fitness':0})
    offspring.extend(populasi)
    # hasilnya akan terdapat sebanyak 2x|populasi| awal
    return offspring

def mutasi(populasi):
    panjangKromosom=8
    individu=populasi.index(findchoose.random(populasi))
    gen=random.randint(0,panjangKromosom+1)
    populasi[individu]['kromosom'][gen]=random.randint(1,255)
    m=Model(populasi[individu]['kromosom'])
    m.train()
    populasi[individu]['fitness']=m.evaluate()
    del m

def fitness(populasi):
    for individu in range(len(populasi)):
        if (populasi[individu]['fitness'] != 0) : continue
        m=Model(populasi[individu]['kromosom'])
        m.train()
        populasi[individu]['fitness']=m.evaluate()
        del m

if __name__ == "__main__":
    #inisiasi Populasi
    populasi = inisiasi_populasi(5, 8)

    for i in range(5):
        #menghitung fitness
        fitness(populasi)
        
        #seleksi
        populasi = seleksi(populasi,3)
        print(populasi)

        #crossover
        populasi = crossover(populasi)
        fitness(populasi)

        #mutasi
        mutasi(populasi)

    
    print(populasi)
    
    # totalPopulasi=[]
    # matingPool=seleksi(inisiasiPopulasi,3)
    # while len(totalPopulasi)<50:
