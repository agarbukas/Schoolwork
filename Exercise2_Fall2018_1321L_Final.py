#CS1321L Final Fall 2018
#Name: Andy Garbukas
#Student ID Number:000569062
#Date: 12/7/18
#Lab Instructor:Solomon Walker
#NOTE: Turn this file in with the others in D2L after you are finished with the final

#Here you will define your public ZombieDog class
#Delete the pass keyword when you start.


class ZombieDog:
    def __init__(self, barkSound, idnum, fur,):
        self.barkSound = barkSound
        self.fur = fur
        self.idnum = idnum


    #SetID() method
    def SetID(self):
        self.idnum = input("Enter the Id number for your zombie-dog -1 or 1")

    #DogBark() method
    def DogBark(self):
        print("Identifier: ", self.fur, " Bark: ", self.barkSound, " CDC: ", self.idnum)




d1 = ZombieDog("woooofffwoooffff", -1, "brown")
d2 = ZombieDog("yipyip", -1, "orange")

d1.SetID()

d1.DogBark()

d2.DogBark()





"""
#Example instantiation and test of a ZombieDog instance that will output Sample run 1
ZombieDog d1 = ZombieDog("grrr")
d1.DogBark()
ZombieDog d2 = ZombieDog("yip")
d2.SetID(17)
d2.DogBark()
"""