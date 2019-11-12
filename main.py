from model import Model
import random
from itertools import combinations

def inisiasiPopulasi(maxPopulasi,panjangKromosom):
    populasi=[]
    for i in range(maxPopulasi):
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

def crossOver(populasi):
    offspring=[]
    tmp=combinations(populasi,2)
    # masih belum jadi

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
    populasi=inisiasiPopulasi(3,2)

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

    
    print(populasi)
    
    # totalPopulasi=[]
    # matingPool=seleksi(inisiasiPopulasi,3)
    # while len(totalPopulasi)<50:



    
