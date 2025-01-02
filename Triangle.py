


def equilateral(sides):
    a,b,c = sorted(sides)
    if a > 0 and b >0 and c > 0:
        if a==b and b==c and c==a:
            return True
        else :
            return False
    else:
        return False
    
   
        
    
  
    
    


def isosceles(sides):
    a,b,c = sorted(sides)
    
    if a + b >= c and b + c >= a and c + a >=b:
        if a>0 and b > 0 and c > 0:
            if a == b or b == c or c == a:
                
                return True
            else :
                return False
        else : 
            return False
    
    else :
        return False
        
    


def scalene(sides):
    a,b,c = sorted(sides)
    
    if a + b >= c and b + c >= a and c + a >=b:
        if a>0 and b > 0 and c > 0:
            if a != b and b != c and c != a:
                
                return True
            else :
                return False
        else : 
            return False
    
    else :
        return False
    
