motorcycle = ['honda','yamaha','suzuki']
print(motorcycle)
#accessing list items using index
#printmotorcyclye
motorcycle[1]= "Bugati" #changing element in a list
print("i love "+ str (motorcycle[1]))
#adding element in a list
motorcycle. append("Bugati") #adding an item to a list
print(motorcycle)
#task print the motorcycle and their plate number 
#deleting an item from a list--del
del motorcycle[2] #deleting an item from a list
print(motorcycle)
popped_motorcycle = motorcycle.pop()
print (motorcycle)
#task print statement
#my name is Mojo jojo and i own a motorcycle plate number
print ("Am JOjo i own a motocycle" + str (motorcycle [1]))
print(f"My name is Jojo and i own {motorcycle[0]} plate number[0]")
# removing an item from a list
motorcycle.remove("Bugati")
print(motorcycle)

school = ['Joy','Hope','Happy']
pupil = ['Peace','Paient','Amani','Charles']
print (f"i am {pupil[0]} and i school at {school[0]}")
print (f"i am{pupil[1]} and i schol at {school[1]}")
print (f"i am{pupil[2]} and i school at{school[2]}")
#p
#rint (f"i am{pupil[3]} and i school at{school[3]}")
#for pupil in pupil:
   #print('hello i am pupil {pupil}')
#p
#rint (pupil[-1])
#print(pupil)
fruits =['mango','banana','orange']
print(fruits)
fruits [2] = 'guava'
print(fruits[12])