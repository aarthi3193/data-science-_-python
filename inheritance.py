
# coding: utf-8

# In[79]:


import math
class Shape(object):
    def __init__(self,base,side):
        self.base = base
        self.side = side
        #self.height = height
    def area(self):pass
    def perimeter(self):pass   
    
        
class Rectangle(Shape):  
    def __init__(self,base,side):
        super(Rectangle, self).__init__(base,side)
        
    def area(self):
        return(self.base*self.side)
    def perimeter(self):
        return(2*self.base+2*self.side)
        
class Square(Shape):
    def __init__(self,side):
        super(Square, self).__init__(side,side)
  
    def perimeter(self):
        return(4*self.side)
    
class Rhombus(Shape):
    def __init__(self,side):
        super(Rhombus, self).__init__(side,side)
   
    def perimeter(self):
        return(4*self.side)
    
class Parallelogram(Shape):
    def __init__(self,base,side):
        super(Parallelogram, self).__init__(base,side)
    
    def perimeter(self):
        return(2*self.base+2*self.side)
        
rect = Rectangle(5,5)
rect.area()
rect.perimeter()
        
sq = Square(6)
sq.area()
sq.perimeter() 

rh = Rhombus(8)
rh.perimeter() 

pg = Parallelogram(10,20)
pg.perimeter() 


        
        




# In[80]:


rect.area()


# In[81]:


rh.perimeter() 


# In[82]:


pg.perimeter()


# In[83]:


rect.perimeter()

