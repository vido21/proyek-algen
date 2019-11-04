from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
from sklearn.metrics import accuracy_score
class Model():
    def __init__(self,layers_list=[]):
        self.models = Sequential()
        self.X_train = pd.read_csv()
        self.y_train = pd.read_csv()
        self.X_test = pd.read_csv()
        self.y_test = pd.read_csv()
        for v in range(len(layers_list)):
            if v==0:
                self.models.add(Dense(units=layers_list[i],activation='relu',input_shape=(8,)))
            else:
                self.models.add(Dense(units=layers_list[i],activation='relu'))
        self.models.add(Dense(1,activation='sigmoid'))
    def train(self):
        self.models.fit(self.X_train,self.y_train,epochs=10,verbose=0)
    def evaluate(self):
        pred = self.models.predict(X_test)
        score = accuracy_score(y_test,pred)
        return score



    

