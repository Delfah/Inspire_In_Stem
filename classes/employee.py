# !/usr/bin/python

####################
# name:kendi
# Date:2,june,2022
# assignment

##################
#create name and the employee salary

class employee:
    def __init__(self, _name, _salary, _ID ):
        self.name = _name
        self.salary = _salary
        self.ID = _ID
        
    def company(self):
        print("Hello,my name is" +self.name, "my salary is"  +self.salary,'in kenya shillings' "my ID number is" +self.ID)
employee1 = employee("Mary", str(700000), str(7900))
employee1.company()
