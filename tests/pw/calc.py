num=int(input('enter the number'))
num_2=int(input("enter the number"))

def calcsum(num,num_2):
   return num+num_2

 
    
def calcsub(num,num_2):
    return num-num_2

def calcmul(num,num_2):
    return num*num_2

def calcdevi(num,num_2):
    return num/num_2


choise=int(input("choise 1,2,3,4"))
if choise==1:
      add=calcsum(num,num_2)  
      print(add)
elif choise==2:
      minus=calcsub(num,num_2)
      print(minus)
elif choise==3:
        mult=calcmul(num,num_2)    
        print(mult)
elif choise==4:
        dive=calcdevi(num,num_2)    
        print(dive)

    