def si_calc():
    p=float(input("enter the principle :"))
    r=float(input("enter the rate of interest:"))
    t=float(input("enter the time :"))
    si=p*(r*t)/100
    print(f'simple insterest is{si}')

# si_calc()  #calling function 
    
def ci_calc():   # define compound interest function
    p=float(input("enter the principle :"))
    r=float(input("enter the rate of interest:"))
    t=float(input("enter the time :"))
    ci=p*(1+r/100)**t
    print(f'compound interest is{ci}')

# ci_calc()

