def square(number):
    if number>=1 and number<=64:
       return 2**(number-1) 
    else:
        raise ValueError("square must be between 1 and 64")
def total():
    s=0
    m=1
    for i in range(1,65,1):
        m=2**(i-1) 
        s+=m
    return s
