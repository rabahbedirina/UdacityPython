no_list = [22,22,2,1,11,11,2,2,3,3,3,4,5,5,5,55,55,66]

def unique_list(l):
  #complete the function's body to return the unique list of numbers
    unique=[]    
   
    for l in no_list:
        if l not in unique:
            unique.append(l)
    
    return unique            

print(sorted(unique_list(no_list)))
lista=set(no_list)


print('set', lista)
#........................
text = "this is not a reversed text"

def reverse(x):
    #complete this function so that it takes string x as an input 
    reverse = list(x)
    reverse.reverse()
    
    
    return ''.join(reverse)
    


print("the reversed text is: "+reverse(text))
#.........
no_list = [10,2,9,4,6]

def maximum(no_list):
    #complete the function to return the highest number in the list
    lenght=len(no_list)
    index=0
    nmax=0
    while index < lenght :
        if no_list[index]> nmax :
            nmax=no_list[index]
        else:
            nmax=nmax  
        index +=1
         
    return nmax

print(maximum(no_list))