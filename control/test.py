'''
 # @ Author: Peter Bowman
 # @ Create Time: 2022-11-19 08:01:56
 # @ Modified by: Peter Bowman
 # @ Modified time: 2022-11-19 15:06:13
 # @ Description:
 '''


from direction import directionVector

e = directionVector(90, 0)
b = e()

print(b)
print(b.__str__())