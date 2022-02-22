# here we create game - guess the number

n=5 #we have to find 5 in limit of guesses

no_of_guess=1 #start with 1
print("Number of guess is 5")

# while we use
while(no_of_guess<=5):
    guess_no=int(input("Guess the number :"))
    if guess_no<5: #condition1
        print("its lower number")
    elif guess_no>5:#condition2
        print("its higher number")
    else:
        print("you won") #condition3
        print((no_of_guess,"no og guess you took"))
        break
    print(5-no_of_guess,"number of guess left")
    no_of_guess+=1 #here we count number of guess

if no_of_guess>5:
    print("game over")    
 

