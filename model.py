from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings("ignore")
class Model():
    def __init__(self,layers_list=[]):
        self.models = Sequential()
        self.X_train = pd.read_csv("X_train.csv")
        self.y_train = pd.read_csv("y_train.csv")
        self.X_test = pd.read_csv("X_test.csv")
        self.y_test = pd.read_csv("y_test.csv")
        for v in range(len(layers_list)):
            if v==0:
                self.models.add(Dense(units=layers_list[v],activation='relu',input_shape=(self.X_train.shape[1],)))
            else:
                self.models.add(Dense(units=layers_list[v],activation='relu'))
        self.models.add(Dense(1,activation='sigmoid'))
        self.models.compile(loss="binary_crossentropy",metrics=["accuracy"],optimizer='adam')
    def train(self):
        self.models.fit(self.X_train.values,self.y_train.values,epochs=10,verbose=0)
    def evaluate(self):
        pred = self.models.predict_classes(self.X_test.values)
        score = accuracy_score(self.y_test.values,pred)
        return score
        




    

