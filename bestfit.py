import numpy as np

class SimpleLinearRegression:
    def __init__(self):
        pass
       
    def fit(self, x, y):
        self.independent = x
        self.dependent = y
        
        self.Mx = np.mean(x)
        self.My = np.mean(y)

        self.SS = sum((x-self.Mx)**2)
        self.SP = sum((x-self.Mx)*(y-self.My))

        self.a = self.SP/self.SS
        self.b = self.My - (a*self.Mx)
       
    def predict(self, x, dplaces=3):
        return round(a*x+b, dplaces)