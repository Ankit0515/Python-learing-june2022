def simple_interest(p:int,r:int,t:int):  # text after ":" shows the data type ; the return will be float type
    '''
    to calculate simple interest  
    '''
    return(p*r*t)/100

def compound_interest(p,r,t):
    return p*(1+r/100) **t 


if __name__=="__main__":
    #passing test data
    p=10000
    r=5
    t=3
    si=simple_interest(p,r,t) #declaring variable that calls function
    ci=compound_interest(p,r,t)
    print(f"simple interest is {si}")
    print(f"compound interest is {ci}")

    #sample 2
    p=float(input("enter the principle amt"))
    r=float(input("enter the rate"))
    t=float(input("enter the duration"))
    si=simple_interest(p,r,t) #declaring variable that calls function
    ci=compound_interest(p,r,t)
    print(f"simple interest is {si}")
    print(f"compound interest is {ci}")
