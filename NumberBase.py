from string import ascii_uppercase as al #import dictionary AZ
import re

dic = {x:i for i, x in enumerate(al, 10)} # A-10...F-15...etc.
for i in range(0,10):
    
    dic[str(i)] = i


def checkio(str_number, radix):
    result = [] 
    str_number = str_number[::-1] #Reverse string
    
    if  (radix > 10 and (str_number.isalpha() or (bool(re.match('[0-9]', str_number)) and bool(re.match('[A-Z]', str_number))))):
        
        str_number = list(str_number) #convert the string to a list
        print (str_number)
        
        for n in range(len(str_number)):
            str_number[n] = dic[str_number[n]] #replace string el. with a dictionary el.
        print (str_number)         
        if any(i>radix-1 for i in str_number):
            print (-1)
            return -1
        else:    
            
            for i in range(len(str_number)):
                result.append(str_number[i]*radix**i)
            print (sum(result))  
            return (sum(result))    
    
    elif not str_number.isalpha():
        
        str_number = list(str_number) #convert the string to a list
        print (str_number)
        for n in range(len(str_number)):
            str_number[n] = dic[str_number[n]] #replace string el. with a dictionary el.
        print (str_number)         
        if any(i>radix-1 for i in str_number):
            print (-1)
            return -1
        else:    
            
            for i in range(len(str_number)):
                result.append(str_number[i]*radix**i)
            print (sum(result))  
            return (sum(result)) 
        
    else:
        print (-1)
        return  (-1)
        
checkio("909", 9)
    


'''

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"
'''
