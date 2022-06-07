# !/usr/bin/python

####################
# name:kendi
# Date:6,june,2022
# student details

##################

class student:
    def __init__(self,name,reg_number,subject,grade):
        self.name = name
        self.reg_number = reg_number
        self.subject = subject
        self.grade = grade
    def choose_subject(self):
          print('Hello my name is  ' +  self.name, ' my registration_number is ' +  self.reg_number, ' i do this subject ' +  self.subject, ' i got this grade ' + self.grade)   
student1 =  student('Ivy',str(653),'Biology','B+')
student1.choose_subject()          
