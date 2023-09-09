#Implement a recursive function to calculate the factorialist a given number.
def fact_rec(n):
  if n==1 or n==0:
    return 1
  else:
    return n*fact_rec(n-1)

number=int(input("ENTER THE VALUE:"))  
res= fact_rec(number)
print("THE FACTORIAL OF {} IS {}.".format(number,res))




