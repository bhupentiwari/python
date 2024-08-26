import random
# Create a guess game with the names of colors . At each round pick a random color from
# a list and let the user try to guess it. When he does it , ask if he wants to play again. 
# keep playing unitl the user types "no"

colors = ["red","green","blue","cyan"]

while True: 
    color = colors[random.randint(0, len(colors)-1)]
    guess = input("Please guess color :")

    while True :
        if(color == guess.lower()) :
            break
        else:
            guess = input("Nope Try again : ")
    print("you guesed it i was thinking about : ",color)

    play_again = input("Lets play again type 'no' to quit.")

    if(play_again.lower() == 'no') :
        break
print("Thanks for playing it was fun")






    

