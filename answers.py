# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 21:36:24 2022

@author: Siddhartha Devan V
# """

# # 1

class engine_no():
    def engine(self, plate_num):
        num_string = ""
        for i in plate_num:
            if i.isnumeric():
                num_string += i
        
        eng_num = 0
        for i in num_string:
            eng_num += int(i)
        
        return eng_num
    
plate_number = input("enter plate number  :")

numb = engine_no()
print("The engine number =",numb.engine(plate_number))    


# # 5

class valid_parentheses:
    def is_valid(self,string):
        for i in range(0,len(string),2):
            
            if len(string)%2 != 0:
                return False 
            if string[i] == "(" and string[i+1] != ")":
                return False
            if string[i] == "[" and string[i+1] != "]":
                return False
            if string[i] == "{" and string[i+1] !="}":
                return False
            
        return True
    
    
string = "(){}["
check = valid_parentheses()
print(check.is_valid(string))


# 7

class unique:
    def display(self,lis):
        unique_ = []
        for i in range(len(lis)):
            for j in lis[i].values():
                if j not in unique_:
                    unique_.append(j)
        print(unique_)
          
ob = unique()
ob.display([{"a":1, "b": 2, "c": 2, "d":3},{"h":5, "j": 3}])


# bubble sort 
a = [5,3,57,30,21]
n = len(a)
for i in range(n):
    for j in range(n-1-i):
        if a[j] > a[j+1]:
            n1 = a[j]
            n2 = a[j+1]
            a[j] = n2
            a[j+1] = n1
        
        print(a)
        
        
# selection sort

a = [5,3,57,30,21]
sort = []
for i in range(len(a)):
    min = a[0]
    for j in range(len(a)):
        if a[j] < min:
            min = a[j]
            
    a.pop(a.index(min))
    sort.append(min)
    print(sort)
    
    

#insertion sort
a = [5,3,57,30,21]
sort = []
sort.append(a[0])

for i in range(1,len(a)):
    sort.append(a[i])
    for j in range(len(sort)-1,0,-1):
        if sort[j] < sort[j-1]:
            n1 = sort[j]
            n2 = sort[j-1]
            sort[j] = n2
            sort[j-1] = n1
print(sort)


#stack
class stack():
    def __init__(self):
        self.a = []
        
    def push(self,n):
        self.a.append(n)
        for i in self.a[::-1]:
            print(i)
            print("--")
        print("successfully pushed ", n)
            
    def popp(self):
        popped_element = self.a.pop()
        for i in self.a[::-1]:
            print(i)
            print("--")
        print("successfully popped ",popped_element)
            
s = stack()
m = int(input("enter the number of elements you want to push:"))
for _ in range(m):
    n= eval(input("enter an element:"))
    s.push(n)
    
o = int(input("enter the number of elements you want to pop:"))
if o > len(s.a):
    print("enter a valid number: ")
    o = int(input("enter the number of elements you want to pop:"))
for _ in range(o):
    s.popp()

#queue
class queue():
    def __init__(self):
        self.a = []
        
    def enqueue(self,element_to_enqueue):
        self.a.append(element_to_enqueue)
        for elements in self.a:
            print(elements)
            print("--")
        print("successfully enqueued ", element_to_enqueue)
        
    def dequeue(self):
        dequeued_element = self.a.pop(0)
        for elements in self.a:
            print(elements)
            print("--")
        print("successfully dequeued ", dequeued_element)
        
        
        
q = queue() 
m = int(input("enter the number of elements you want to enqueue:"))
for _ in range(m):
    n= eval(input("enter an element:"))
    q.enqueue(n)
     
o = int(input("enter the number of elements you want to dequeue:"))
if o > len(q.a):
    print("enter a valid number: ")
    o = int(input("enter the number of elements you want to dequeue:"))
for _ in range(o):
    q.dequeue()      
    



     

    
            
            
         
            
                
            
        
