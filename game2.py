##### THIS IS THE QUIZGAME ########################


##### QUESTION ZONE ###############################################

##### here are all variables of the questions.
## if you add more or delete some, just update the list "questions"

question1 = ("What\'s 12+6? ")
question2 = ("What\'s the name of the USA president? ")
question3 = ("What\'s the height of the Eiffel tower? ")
question4 = ("In which year the Impossible Project team produced the first film for sale? ")
question5 = ("How many people lives in Amsterdam? ")
question6 = ("In what red-blooded body organ are the vitamins A, D, E and K stored? ")
question7 = ("Who is the author behind the vampire book series Twilight? ")
question8 = ("Who is the author behind the Harry Potter books? ")
    
##### this is the list   questions

questions = [question1, question2, question3, question4, question5, question6, question7, question8]


##### ANSWER ZONE ################################################
## if you make changes in the question zone, don't forget to syncronise this zone (the variable and the list)!!!! 

##### here are all variables of the answers. 

answer1 = ("18")
answer2 = ("Barack Obama")
answer3 = ("324")
answer4 = ("2010")
answer5 = ("820000")
answer6 = ("liver")
answer7 = ("Stephenie Meyer")
answer8 = ("J.K. Rowling")
    
##### this is the list   answers

answers = [answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8]


##### GLOBAL GAME SETTINGS ###############################################


points = 0
name = None
yes = ['Yes', 'yes', 'YES']
no = ['No', 'no', 'NO']


##### RESET ZONE #########################################################


def game_reset():
    '''
    Reset all variables of the whole game for a new play
    '''

    global points
    global name

    points = 0
    name = None
#end-function#
    

##### GAME INTRO ZONE ####################################################


def game_intro():
    '''
    Welcome the player and ask him for his name as long as he thinks is correct.
    '''

    print("\n       ------ !! Welcome to the QuizGame !! ------\n")
    
    global name

    while name == None:
        name = input("What's your name? ")
        print("Your name is", name)
        correct = input("Is that correct? ")
        if yes.count(correct) == True: ##"Yes" or ok == "yes" or ok == "YES":
            print("Good, let's go on!\n")
        else:
            print("Mh? Try again and confirm with Yes!")
            name = None
#end-function#
            

##### GAME PLAY ZONE #####################################################


def print_play_status(x):
    '''
    just print out the current score and the current challenge number.
    '''

    global points
    print("At the moment your total points are", points)
    print("Challenge", x+1, "\n")
#end-function#
    

def play_quest(x):
    '''int -> int
    this functions asks the player question X, checks if player's answer is right and eventually changes the variable points.
    no examples needed
    '''
    
    global points
    answerPlayer = input(questions[x])
    if answerPlayer == answers[x]:
        print("Well done,", name + ", 10 points gained! Let's move to the next question.\n")
        points +=10
    else:
        print("Wrong! 0 points gained, the correct answer was:", answers[x], ". Next question...\n")
#end-function#
        

def game_play():
    '''
    first : tell the player his current score and the current challenge number
    second: tell the play_quest-function how many and which questions it must asks the player.
    '''
    
    for x in range(len(questions)):
        print_play_status(x)
        play_quest(x)
#end-function#


##### GAME END ZONE ########################################################


def game_end():
    '''
    first : tell the player his finish score.
    second: ask the player if wants to play again and fullfil his wish.
    '''

    print("\nYou finished the game with a total of", points, "points! \n")

    again = None
    
    while again == None:
        again = input("Once again? ")
        if yes.count(again) == True:
            print("\nEnjoy :)\n")
            game_control()
        elif no.count(again) == True:
            print("For fresh ideas, new feautures, new questions/answers, graphics, please post or edit yourself at")
            print("  https://github.com/eliosfederico/Python-trivia-game")
            print("  https://class.coursera.org/programming1-2012-001/forum/thread?thread_id=1969")
            print("                                                                              ")
            print("                             Thanks for playing!")
            print("                           ------ !! bye !! ------")
        else:
            print("oh, just yes or no!")
            again = None
#end-function#
        
    
##### GAME CONTROL ZONE ####################################################


def game_control():
    '''
    Control the whole game with the single steps.
    '''
    game_reset()
    game_intro()
    game_play()
    game_end()
#end-function#


##### FIRST GAME START ZONE ################################################


game_control()


