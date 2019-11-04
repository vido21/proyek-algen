from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
from sklearn.metrics import accuracy_score
class Model():
    def __init__(self,layers_list=[]):
        self.models = Sequential()
        for v in range(len(layers_list)):
            if v==0:
                self.models.add(Dense(units=layers_list[i],activation='relu',input_shape=(8,)))
            else:
                self.models.add(Dense(units=layers_list[i],activation='relu'))
        self.models.add(Dense(1,activation='sigmoid'))
    def train(self):
        X_train = pd.read_csv()
        y_train
        X_test
        y_test


    

