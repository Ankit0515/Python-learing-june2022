def simple_interest(p:int,r:int,t:int):  # text after ":" shows the data type ; the return will be float type
    '''
    to calculate simple interest  
    '''
    return(p*r*t)/100

def compound_interest(p,r,t):
    return p*(1+r/100) **t 


if__name__="__main__"

#passing test data
p=int(input("enter the no. "))
r=int (input("enter th rate"))
t=int(input("enter the time"))
si=simple_interest(p,r,t) #declaring variable that calls function
ci=compound_interest(p,r,t)
print(f"simple interest is {si}")
print(f"compound interest is {ci}")
