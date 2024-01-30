import luigi
from luigi import Task

class Mathematical_Operations(Task):
    
    intNum_1 = luigi.Parameter()
    intNum_2 = luigi.Parameter()
    
    def Add(self,intNum_1,intNum_2):
        return intNum_1 + intNum_2

    def Double(self,intNum):
        return 2*intNum
    
    def run(self):
        
        Sum = self.Add(self.intNum_1,self.intNum_2)
                
        Doubled_Sum = self.Double(Sum)

        print(Doubled_Sum)
    
luigi.build([Mathematical_Operations(intNum_1=5,intNum_2=10)],local_scheduler=True)


