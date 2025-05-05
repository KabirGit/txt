def remind_name():
    print("please , remind me your name ")
    name = input()
    print("what a great name you have ")

def guess_age():
    print("let me guess your age.")
    print("enter remainders of dividing you age by 3 , 5 and 7 respectively. ")
    rem3 = int(input("remainder when divided by 3 "))
    rem5 = int(input("remainder when divided by 5"))
    rem7 = int(input("remainder when divided by 7"))

    for age in range(105):
        if(age %3 == rem3 and age % 5 == rem5 and age % 7 == rem7 ):
            print("your age is {0};".format(age))
            return
    print("could not determine you age . please ensure remainders are correct. ")

def count():
    print("now i will prove to you that i can count to any number you want ")
    num = int(input("enter a number: "))
    counter = 0
    while(counter <= num):
        print("{0}".format(counter))
        counter += 1


def test():
    print("let's test your programming knowledge.")
    print("why do we use methods ?")
    print("1. to repeat a statment multiple times.")
    print("2. to decompose a program into several small subroutines ")
    print("3. To demonstrate the execution of a program.")
    print("4. To interrupt the execution of a program.")
    answer = 2
    guess  = int(input())
    while (guess != answer):
        print("please try again")
        guess = int(input())
    print("completed , have a nice day !")

def end():
    print("congratulations! have a nice day")


remind_name()
guess_age()
count()
test()
end()