# today we are going to talk about if
# what is if?
# if is condition that you can write
# how write it?
# we write "if" and after that we have to give a variable for example:
# if number == 2:
    #print(you win)
# what is elif?
# "elif" is another condition that it always write after "if"
# and what is else?
# you write else when that you want to say if all the up condition was false print this
# lets see an example
age = int(input(" its simple game...please enter a number between 1 to 100======>"))

if age == 37:
    print("you win")
elif age < 37:
    print("unfotunately you lose,because you had to say higher ")
elif age  == 50:
    print("unfotunately you lose,because you had to say lower")
else :
    print("you lose")