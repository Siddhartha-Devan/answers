# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 11:46:26 2022

@author: Siddhartha Devan V
"""

class Node:
    def __init__ (self, value = None, next_node = None):
        self.val = value
        self.next_node = next_node
        
        
class sing():
    def __init__(self):
        self.head = None
        
        
    def add_at_end(self, node):
        if self.head == None:
            self.head = node
            
        else:
            current_node = self.head 
            while current_node.next_node != None:
                current_node = current_node.next_node
            current_node.next_node = node
            
            
    def add_at_ind(self,ind,node):
        current_node = self.head
        prev_node = current_node
        try:
            for _ in range(0, ind-1):
                prev_node = current_node.next_node
                current_node = current_node.next_node
            current_node = current_node.next_node
            prev_node.next_node = node
            node.next_node = current_node
        except AttributeError:
            print("index out of range")
            
            
    def add_at_beg(self, node):
        node.next_node = self.head    
        self.head = node
            
            
    def del_at_end(self):
        if self.head == None:
            print("")
            
        else:
            current_node = self.head
            if current_node.next_node == None:
                self.head = None
            
            else:
                current_node = self.head
                previous_node = current_node
                while current_node.next_node != None:
                    previous_node = current_node
                    current_node = current_node.next_node
                    
                previous_node.next_node = None
                del current_node
        
            
    def del_at_index(self,ind):
        current_node = self.head
        prev_node = current_node
        try:
            for _ in range (0,ind-1):
                prev_node =current_node.next_node
                current_node = current_node.next_node
            current_node = current_node.next_node
            point_node = current_node.next_node
            prev_node.next_node = point_node
            del current_node
        except AttributeError:
            print("cannot delete ... index out of range")
    
    
    # def del_at_beg(self):
    #     current_node = self.head
    #     if self.head == None:
    #         print()
    #     else:
    #         self.head = current_node.next_node
    #         del current_node

        
    def del_at_beg(self):
        if self.head == None:
            print("")
        else:
            current_node = self.head
            current_node = current_node.next_node
            del self.head
            self.head = current_node            
            
            
    def show(self):
        if self.head == None:
            print(None)
        else:
            current_node = self.head
            print(self.head)
            print(current_node.val, current_node.next_node)
            while current_node.next_node != None:
                current_node = current_node.next_node 
                print(current_node.val, current_node.next_node)
                     
            
sll = sing()
sll.add_at_end(Node(10))
sll.add_at_end(Node(20))
sll.add_at_end(Node(30))
sll.add_at_end(Node(40))
sll.add_at_end(Node(50))
sll.add_at_end(Node(60))
sll.add_at_end(Node(70))
sll.add_at_end(Node(80))
sll.del_at_end()
sll.add_at_ind(4, Node(300))
sll.add_at_beg(Node(200))
sll.del_at_beg()
sll.del_at_beg()
sll.del_at_index(5)
sll.show()           
           
             
            
            
            
        




        