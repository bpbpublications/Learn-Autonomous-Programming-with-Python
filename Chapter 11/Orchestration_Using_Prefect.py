
from prefect import task, Flow

@task
def Add(intNum_1,intNum_2):
    return intNum_1 + intNum_2

@task
def Double(intNum):
    return 2*intNum

@task
def Print_Value(strValue):
    print(strValue)


with Flow('Mathematical-Operations') as flow:
    
    intNum_1 = 5

    intNum_2 = 10
    
    Sum = Add(intNum_1,intNum_2)
        
    Doubled_Sum = Double(Sum)

    Print_Value(Doubled_Sum)
    
flow.run()

flow.visualize(filename="Mathematical Operations")
    
































































   
    