# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.


def counter(count=10):
    for i in range(count):
        print(i)
        
def counter2(otherCount, count=5):
    for i in range(count):
        print("new loop")
        for f in range(otherCount):
            print(f)
            
counter2(10,5)
"""
"""
g=5

def set_to_ten():
    global g
    g=10
    
print(g)
set_to_ten()
print(g)
"""
"""
def change_list(lis):
    lis[0]=20
    print(lis)
    
l=[5,9,3,12]
change_list(l)
print(l)
"""
"""
#tuple with mutable object
first_names=["sally","ted", "john"]
last_names=["alastair","mcdonald","reynolds"]
t=(first_names,last_names)
print(t)
first_names.append("kelly")
print(t)
"""
"""
#change id
a=5
print(a)
print(id(a))
a=10
print(a)
print(id(a))

#same id
l=[5,9,1]
print(l)
print(id(l))
#l=[20]
l.append(20)
print(l)
print(id(l))
#imutable objects gets new id numbers when changed, mutable objects use same id
"""
"""
class Bed:
    #softness_values=["soft","med", "hard"]#will change all instances
    def __init__(self): #constructor
        self.is_made=True
        self.softness_values=["soft","med", "hard"]
    def MakeBed(self):
        self.is_made=True
    def SleepInBed(self):
        self.is_made=False
        
myBed=Bed()
print(myBed.is_made)
myBed.softness_values.append("very hard")
print(myBed.softness_values)

yourBed=Bed()
myBed.SleepInBed()
print(yourBed.softness_values)
"""

