def prime(n):
    return all(n%i for i in range(2,int(n**.5)+1)) 
