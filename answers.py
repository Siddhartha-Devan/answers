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





     

    
            
            
         
            
                
            
        