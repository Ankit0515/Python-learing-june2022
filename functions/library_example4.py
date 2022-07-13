def library_fine(days,cat_b):
    if cat_b=="A":
        if days<10:
           fine=100*days
        else :
            fine= (days*100)*2
        return fine
    elif cat_b=="B":
        if days<10:
            fine=50*days
        else :
            fine= (days*50)*2
        return fine
    elif cat_b=="C":
        if days<10:
            fine=10*days
        else :
            fine= (days*10)*2
        return fine
    
    
if __name__=="__main__":
    days=int(input("enter number days book were not returned"))
    cat_b= input("enter your choice")
    book= library_fine(days,cat_b)
    print(f"the fine is {book}")