
# find min max numbers in the list

mynumbers = [1,5,2,7,8,0,3,4,99,1000,1000.5]

def findminmax(args):
    min = args[0]
    max = args[0]
    
    for i in range(len(args)):
        
        if args[i]>max :
            max = args[i]
        
        
        elif args[i]<min:
            min = args[i]
            
    return min,max
        
    
    
print(findminmax(mynumbers))

