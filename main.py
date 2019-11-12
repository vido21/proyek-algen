from model import Model
import random
from itertools import combinations

def inisiasiPopulasi(maxPopulasi,panjangKromosom):
    populasi=[]
    for i in range(max):
        randomKromosom=[random.randint(1,6) for i in range(panjangKromosom)]
        populasi.append({"kromosom":randomKromosom,"fitness":0})
    return populasi

def seleksi(populasi,pilih):
    matingPool=[]
    for i in range(pilih):
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
        for index in range(len(p1)):
            result = one_point_crossover(p1[index], p2[index])
            tx.append(result[0])
            ty.append(result[1])
        offspring.extend((tx, ty))
    offspring.extend(populasi)
    # hasilnya akan terdapat sebanyak 2x|populasi| awal
    return offspring

def mutasi(populasi):
    panjangKromosom=9
    individu=populasi.index(findchoose.random(populasi))
    gen=random.randint(0,panjangKromosom+1)
    populasi[individu]['kromosom'][gen]=random.randint(1,255)
    m=Model(populasi[individu]['kromosom'])
    m.train()
    populasi[individu]['fitness']=m.evaluate()
    del m

def fitness(populasi):
    for individu in range(len(populasi)):
        m=Model(populasi[individu]['kromosom'])
        m.train()
        populasi[individu]['fitness']=m.evaluate()
        del m

if __name__=="__main__":
    #inisiasi Populasi
    populasi=inisiasiPopulasi(5)

    for i in range(5):
        #menghitung fitness
        fitness(populasi)
        
        #seleksi
        populasi=seleksi(populasi,3)
        print(populasi)

        #crossover
        crossOver(populasi)
        fitness(populasi)

        #mutasi
        mutasi(populasi)

    
    print populasi
        

    
    
    # totalPopulasi=[]
    # matingPool=seleksi(inisiasiPopulasi,3)
    # while len(totalPopulasi)<50:



    
