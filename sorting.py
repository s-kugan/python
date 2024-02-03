# Define the list of numbers
dupnums = [1,5,2,9,4,3,100,6,56,89,12,5000]

def sortlist(arg):
  for i in range(len(arg)):
        
    for j in range(i+1,len(arg)):
            
      if(arg[i] >= arg[j]):
        temp = arg[i]
        arg[i] = arg[j]
        arg[j] = temp
        
  return arg
      
print(sortlist(dupnums))