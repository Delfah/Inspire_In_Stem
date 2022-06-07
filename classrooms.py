# !/usr/bin/python

####################
# name:kendi
# Date:6,june,2022
# classroom details

##################

class classroom:
    def __init__(self,capacity,type):
        self.capacity = capacity
        self.type = type
    def sayhi(self):
        print('The classroom has a capacity of ' + self.capacity, ' it is '+ self.type)
classroom1 = classroom(str(200),'red')    
classroom1.sayhi()         