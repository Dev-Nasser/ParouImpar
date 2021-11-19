par = 0
impar = 0
answer = "S"
total = 0
while answer == "S":
    number = int(input("Enter a number for a verification"))
    if number % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1
    total = total + number
    answer = str(input ("Press S to continue \n or any other key to end the program")).upper()



print ("The odd number is {}, the even number is {}, the sum of all values {}".format(impar, par, total))
