# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 14:41:16 2022

@author: Siddhartha Devan V
"""

class Node:
    def __init__(self, value = None, next_node = None, prev_node = None):
        self.val = value
        self.next_node = next_node
        self.prev_node = prev_node
    
    
class double:
    def __init__(self):
        self.head = None
        
    
    def add_at_end(self,node):
        if self.head == None:
            self.head = node
          
        else:
            current_node = self.head
            
            if current_node.next_node == None:
                current_node.next_node = node
                node.prev_node = current_node
                
            else:
                while current_node.next_node != None:
                    current_node = current_node.next_node
                current_node.next_node = node
                node.prev_node = current_node
                
                
    def add_at_ind(self, node, ind):
         current_node = self.head
         for _ in range(0, ind):
             current_node = current_node.next_node
         before_node = current_node.prev_node
         current_node.prev_node = node 
         before_node.next_node = node
         node.next_node = current_node
         node.prev_node = before_node
   

    def add_at_beg(self, node):
        if self.head == None:
            self.head = node
        else:    
            current_node = self.head
            self.head = node
            node.next_node = current_node
            current_node.prev_node = node
        

    def del_at_end(self):
        if self.head == None:
            print("deleted")
            
        else:
            current_node = self.head
            if current_node.next_node == None:
                self.head = None
            else:
                while current_node.next_node != None:
                    before_node = current_node
                    current_node = current_node.next_node
                del current_node
                before_node.next_node = None
     
            
    def del_at_index(self, ind):
        current_node = self.head
        try:
            for _ in range(0,ind):
                current_node = current_node.next_node
            before_node = current_node.prev_node
            after_node = current_node.next_node
            before_node.next_node = after_node
            after_node.prev_node = before_node
            del current_node
        except AttributeError:
            print("cannot delete... list index out of range")


    def del_at_beg(self):
        if self.head == None:
            print("deleted")
        else:
            current_node = self.head
            self.head = current_node.next_node
            self.head.prev_node = None
            del current_node
            # print("current.prev =  ",current_node.prev_node)
        
            
    def show(self):
        if self.head == None:
            print()
        else:
            current_node = self.head
            print(f"head oda prev address {self.head.prev_node}")
            print(current_node.next_node)
            while current_node.next_node != None:
                current_node = current_node.next_node
                print(current_node.prev_node,current_node.val,current_node.next_node)
            
            
dll = double()
dll.add_at_end(Node(10))
dll.add_at_end(Node(20))
dll.add_at_end(Node(30))
dll.add_at_end(Node(40))
dll.add_at_end(Node(50))
dll.add_at_end(Node(60))
dll.add_at_end(Node(70))
dll.add_at_end(Node(80))
dll.del_at_end()
dll.del_at_end()
dll.del_at_index(4)
dll.add_at_ind(Node(100), 2)
dll.add_at_beg(Node(11))
dll.del_at_beg()
dll.show()

            
            
            
            
            
            