#CI Oscar Mateo 

def sum_c(x):
    sum=0
    for i in x:
        if i.isdecimal():
            sum+= int(i)
            print(sum)
  
    return sum
            
sum_c("1726082983")
