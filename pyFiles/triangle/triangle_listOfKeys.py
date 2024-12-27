#from ..dataExploreFile import dataExplore
#from ..triangle.triangleCalcFile import triangleCalc

#class method(dataExplore):
class method():
    def __init__(self):
        super().__init__()
        self.draws = {
            ('an', 'an', 'an'): self.calc1,
            ('an', 'an', 'si'): self.noMethod,
            ('an', 'an', 've'): self.noMethod,
            ('an', 'si', 'si'): self.noMethod,
            ('an', 've', 'si'): self.noMethod,
            ('an', 've', 've'): self.noMethod,
            ('si', 'si', 'si'): self.noMethod,
            ('ve', 'si', 'si'): self.noMethod,
            ('ve', 've', 'si'): self.noMethod,
            ('ve', 've', 've'): self.noMethod
        }

    def noMethod(self):
         print('This method has not been implemented yet!')
