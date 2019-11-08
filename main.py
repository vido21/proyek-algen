from model import Model
import random

def inisiasiPopulasi(max):
    populasi=[]
    for i in range(max):
        randomKromosom=[random.randint(1,6),
                        random.randint(1,10),
                        ]
        populasi.append({"kromosom":randomKromosom,"fitness":0})
    return populasi
def seleksi(populasi):
    matingPool=[]
    for i in range(3):
        a=random.choice(populasi)
        b=random.choice(populasi)
        if (a['fitness']>b['fitness']):
            matingPool.append(a)
        else:
            matingPool.append(b)

# def crossOver(populasi):

# def mutasi()

def fitness(populasi):
    for individu in range(len(populasi)):
        m=Model(populasi[individu]['kromosom'])
        m.train()
        populasi[individu]['fitness']=m.evaluate()

if __name__=="__main__":
    populasi=inisiasiPopulasi(5)
    print(populasi)
    fitness(populasi)
    seleksi()

    # generation=0
    # while generation<5:
    
    
    # totalPopulasi=[]
    # matingPool=seleksi(inisiasiPopulasi,3)
    # while len(totalPopulasi)<50:



    
