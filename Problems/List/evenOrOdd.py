# Even or odd

def even_odd(list):
    evenCount = 0
    oddCount = 0
    for i in list:
        if(i%2==0):
            evenCount += 1
            print(f"Even number: {evenCount}")  
        else:
            oddCount += 1
            print(f"Odd number: {oddCount}")
    return evenCount,oddCount
            
    

list = [2,3,4,5,6,7,8]
print(even_odd(list))
    
