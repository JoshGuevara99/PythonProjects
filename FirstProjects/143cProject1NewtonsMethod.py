from decimal import*
getcontext().prec = 20


   
   
def f(Xvalue):
    xCubed = pow(Xvalue,3)
    TwoxSquared = 2 * (pow(Xvalue,2))
    TenX = 10 * Xvalue
    fx = xCubed + TwoxSquared + (10*(Xvalue))-20
    return fx
        
def fPrime(Xvalue):
    ThreexSquared = 3 * (pow(Xvalue,2))
    FourX = 4 * Xvalue
    primed = ThreexSquared + FourX +10
    return primed


def NewtonsMethod(xSub, counter):
    
    previousXvalueString = str(xSub)
    nextValue = xSub - (f(xSub)/fPrime(xSub))
    
    nextValueString = str(nextValue)
    if previousXvalueString[1:9] == nextValueString[1:9] :
        counterString = str(counter)
        print(nextValue)
        print(counterString + ' ' "iterations completed")
    else: 
        counter = counter + 1
        NewtonsMethod(nextValue, counter)

   
        


testt = NewtonsMethod(1.5, 0)

print(1+(11/30)+(7/3600)+(7/36000)+(11/4320000)+(1/194400000)+(1/1166400000))




