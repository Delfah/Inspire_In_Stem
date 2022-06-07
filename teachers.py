# !/usr/bin/python

####################
# name:kendi
# Date:6,june,2022
# teachers details

##################







class Teachers():
    def __init__(self, name, tsc_no, subject, salary):
        self.name = name
        self.tsc_no = tsc_no
        self.subject = subject
        self.salary = salary
    def sayhi(self):
        print('Am teacher ' +  self.name, ' my tsc_no is ' +  self.tsc_no, ' i teach ' + self.subject, ' i get this salary '+ self.salary)
teacher1 = Teachers('Jane',str(643),'English',str(452000)) 
teacher1.sayhi()       

    


