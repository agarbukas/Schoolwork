#CS1321L Final Fall 2018
#Name: Andy Garbukas
#Student ID Number: 000569062
#Date: 12/7/18
#Lab Instructor: Solomon Walker
#NOTE: Turn this file in with the others in D2L after you are finished with the final



#public static void Search !!!!this is for java???????!!!!




def search(arrayx, numberz):
    if numberz > 9:
        return print("Your number is not here!! -1 -1")


    for x in range(len(arrayx)):
            for y in range(len(arrayx)):
                if arrayx[x][y] == numberz:
                    return print("The first indices is at: ", x, y)











#test the Search method with these two lists that correspond to Sample runs 1 and 2


arr1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
number = int(input("Enter the number to search for"))
print("\nYour number was: ", number)
print("\nYour array to search was: ", arr1)

search(arr1, number)


#test your Search method here