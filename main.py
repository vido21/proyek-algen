from model import Model
import random

def inisiasiPopulasi(max):
    populasi=[]
    for i in range(max):
        randomKromosom=[random.randint(0,255),
                        random.randint(0,255),
                        random.randint(0,255),
                        random.randint(0,255),
                        random.randint(0,255),
                        ]
        populasi.append({"kromosom":[],"fitness":0})
    return populasi
# def seleksi(populasi):

# def crossOver(populasi):

# def mutasi()

if __name__=="__main__":
    mm = Model([5,2])
    print(type(mm))
    # totalPopulasi=[]
    # matingPool=seleksi(inisiasiPopulasi,3)
    # while len(totalPopulasi)<50:



    
