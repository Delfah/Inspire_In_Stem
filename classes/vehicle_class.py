#! usr/bin/python

#################
# name:kendi
# date:3,june,2022
# vehicle class write any variables

#################

class vehicle :
    def __init__(vehicle, _mileage, _max_speed):
        vehicle.mileage = _mileage
        vehicle.max_speed = _max_speed
    def yes(vehicle):
        print("Yes, this cars mileage is " + vehicle.mileage, "MPG " " it has a max_speed of " + vehicle.max_speed,"km/hr"  )
vehicle1 = vehicle(str(55000),str(180))
vehicle1.yes()

class vehile :
    def __init__(self,max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
Toyota = vehicle(4000,60000)
print(Toyota.max_speed,Toyota.mileage)       



