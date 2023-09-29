# #Guess the correct no., give limited guesses , tell how many guesses are left, &  at last tell how many guesses it took
## This is my code ....heee heee

# print("number of guesses are 5")
# print("entered no. should be in between 10 to 20")
# n=15
# a=0
# while(a <= 5):
#     a = a + 1
#     guess_number = int(input("guess a no: \n"))
#
#     if guess_number < 10:
#         print("no. less than 10 is not allowed")
#
#     elif guess_number > 20:
#         print("no. greater than 20 is not allowed")
#
#     elif 10 <= guess_number <= 20 and guess_number != 15:
#         print("u r near ur right value , come on ....Go ahead ! ")
#
#     else:
#         print("Congrats ! ....u won ")
#         print(a ," no. of guesses u took to finish ")
#         break
#     print(5 - a , "no. of guesses left")
#
# if (a == 5 ):
#     print("u r out of guesses")
#     print("try again!")


##1.

# n=18
# number_of_guesses=1
# print("Number of guesses is limited to only 9 times: ")
# while (number_of_guesses<=9):
#     guess_number = int(input("Guess the number :\n"))
#     if guess_number<18:
#         print("you enter less number please input greater number.\n")
#     elif guess_number>18:
#         print("you enter greater number please input smaller number.\n ")
#     else:
#         print("you won\n")
#         print(number_of_guesses,"no.of guesses he took to finish.")
#         break
#     print(9-number_of_guesses,"no. of guesses left")
#     number_of_guesses = number_of_guesses + 1
#
# if(number_of_guesses>9):
#     print("Game Over")


##2.

# number = 54
# number_for_guesses = 1
#
# print("The number of guesses is limited to 9 times only")
#
# while (number_for_guesses <= 9):
#     number_guess = int(input("Enter the number:\n"))
#
#     if number_guess < 54:
#         print("The entered number is smaller")
#     elif number_guess > 54:
#         print("The entered number is greater")
#     else:
#         print("You Won")
#
#         print("The number of guesses you took to finish:", number_for_guesses)
#         break
#     print("The number of guesses left:", 9 - number_for_guesses)
#
#     number_for_guesses = number_for_guesses + 1
#
#     if number_for_guesses > 9:
#         print("Game Over")
# print("Thank You")




##3.  (problem in this code is , not telling if entered no. is greater or samaller)

# n = 18
# # number of guesses should be 9
# # print the number of guesses
# # if number of guesses == 0: print("Game Over.")
# number_of_guesses = 9
# guess = int(input("Enter the number you think is equal to n: "))
# while(number_of_guesses>0):
#     if(guess==n):
#         print("Congrats!You guessed it right.")
#         break
#
#     else:
#         number_of_guesses -= 1
#         if number_of_guesses == 0:
#             print("You've exhausted all your guesses.You Lose!")
#             break
#         print(f"Gusses left: {number_of_guesses}")
#         guess = int(input("Enter the number you think is equal to n: "))




##4.

# numguess = 20
# # it is the number which user needs to guess
#
# print("Press \"P\" to play the game and press \"E\" to exit the game")
# choice = input()
# choice = choice.upper()
#
# guessleft = 6
# while(choice == "P") and (guessleft >= 1):
#     print("\nEnter a number to play a guessing number game.")
#     numbyuser = int(input())
#     if (numbyuser > numguess):
#         guessleft = guessleft-1
#         print("\n\n\nYou need to guess a smaller number\nGuess left by you is:", guessleft)
#     elif (numbyuser < numguess):
#         guessleft = guessleft-1
#         print("\n\n\nYou need to guess a bigger number\nGuess left by you is:", guessleft)
#     elif (numbyuser == numguess):
#         guessleft = 6-guessleft
#         print("\n\n\nCongraulations! You had guessed the number\nYou had taken",1+guessleft, "guesses to complete the game")
#         guessleft = 6
#
# if (choice == "E") or (guessleft == 0):
#     print("\n\nGame Over!")
#     print(5*"\n")
#     print("Press \"P\" to play the game again and press \"E\" to exit the game")
#     choicebyuser = input()
#     choice = choicebyuser.upper()




# n = 56
# m = 8
# print("You have 8 guesses in hand...so don't make mistakes")
# x = int(input("Please input your number:"))
# while n:
#     if x > n:
#         m = m - 1
#         print("You have", m, "guesses left")
#         x = int(input("Guess a smaller number:"))
#         if m == 1:
#             print("Game over!!!")
#             break
#         continue
#     elif x < n:
#         m = m - 1
#         print("You have", m, "guesses left")
#         x = int(input("Guess a larger number:"))
#         continue
#     else:
#         print("You have won!!!")
#         print("You have taken", 9 - m, "guesses to finish the game")
#         break



# import random
# b = random.randint(1,20)
# i  = 0
# while True:
#     print("Enter The Number Here: \n")
#     a  = int(input())
#     while(i<=5):
#         i+=1
#         if a == b:
#             print("You are Right\n")
#             print("You have guessed in: %d " %i)
#             break
#         elif a > b:
#             print("Enter The samller Number: \n")
#             break
#         else:
#             print("Enter The larger Number: \n")
#             break



# n = 30
# no_of_guesses = 0
# while(no_of_guesses < 10):
#     i = int(input("Enter your guess: "))
#     if i == n:
#         print("Your guess is correct!")
#         break
#     elif i > n:
#         print("Your guess is too big, guess something smaller!")
#         no_of_guesses = no_of_guesses + 1
#         print("Guess left: ", 10 - no_of_guesses)
#         continue
#
#     elif i < n:
#         print("Your guess is too small, guess something bigger!")
#         no_of_guesses = no_of_guesses + 1
#         print("Guess left: ", 10 - no_of_guesses)
#         continue
# print("Game Over")



# n = 46
# g = 7
# c=-1
# while(True):
#     print("\nyou have guesses:",g)
#     i=int(input("\nenter a number: "))
#     g=g-1
#     c=c+1
#     if g==0:
#         print("\nGame over!!")
#         break
#     if i ==46:
#         print("\ncongratulations you have successfully guessed the number")
#         print("\nRESULTS: \nguessing number=",n)
#         print("guesses used:",c)
#         break
#     elif i<n:
#         print("increase your number")
#     else:
#         print("decrease your number")
#     continue



# n = 30
# guesses = 1
# print("Your guess is limited to 10 times")
# while(guesses<=10):
#     x = int(input("Enter the Number\n"))
#     guesses = guesses+1
#     if x>30:
#         print("Your number is too high!")
#     elif x<20:
#         print("Your number is too low!")
#     elif x==30:
#         print("You entered Correct number\n")
#         break
#     else:
#         print("Number",10-guesses)
#         print("Game over")
