# importing modules
import sys
import pyinputplus as pyip


'''
POTENTIAL TODOS

'OPTIONAL TODO: alternative name for the animal: 
proconamals/ proconimals

'''


'''NOTES
- There are several aspects of this script that can be adjusted to 
change the game dynamics and therefore the strategy the player has to 
make use of. You can find the most important ones when you look for 
"ADJUSTABLE" in the script.

(((- When the inhabitants need e.g. 1 animal per person for 1 year it is
calculated backwards and still makes sense. The extra food already
during the pregnancy is considered. So if the growth factor determines
that after 1 year it is 100 people,  they will have needed 1
animal for each person (even babies) for this year in the past. So if
the user's decisions did not make this possible, the village will have
starved.)))

'''


while True:  # everything that is necessary before the main game loop
    '''These are the values of the main variables at the beginning, 
    which can change each round.'''
    people_amount = 50     # ADJUSTABLE: 50 is the starting value, which 
    # I sometime adjust for testing purposes.
    
    # ADJUSTABLE: 950 is the starting value, which I sometime adjust for
    # testing purposes.
    animal_amount = 950
    round_number = 0

    '''The follwoing 2 variables are for the Welcome-text and the 
    message for the user when the game is won.'''
    people_amount_start = people_amount
    animal_amount_start = animal_amount

    '''These are the fixed values of the variables that do not change 
    throughout the game'''
    round_number_max = 5  # ADJUSTABLE: The amount of maximum rounds 
    # until the game definitely ends.

    # The welcome text is displayed.
    print('''
    ---P R O C O N I M A L S---
    HUNT THEM WITHOUT MAKING THE ECOSYSTEM COLLAPSE

    In this alien civilization there is a village of currently''', people_amount_start, 'people. '
          '''Their main food supply is an animal species called proconimal. '''
          '''If there are too many or too little proconimals
    the ecosystem which the people and the animals depend on collapses and the village does not survive. '''

          '''Each year the village people know how many of these animals
    currently (at the moment''', animal_amount_start, ''') exist and have to decide how many they will hunt.
    The number they decide on influences the number of people and
    the number of proconimals in the coming year.

    You (the player) do not know how exactly the decision influences these numbers
    so pay attention to how your decisions influence the populations.

    Your goal is to make the village survive''', round_number_max, '''years.

    Let's start with the game!
    ''')

    '''
    ------------------------------------------------------
    OPTIONAL TODOs
    - I might reuse the old sentence which was "If there are too many 
    proconimals, the village does not survive because they get 
    attacked.
    
    If there are not enough proconimals, the village does not 
    survive because they starve to death. 

    maybe add something like the following to the welcome-message:
    You (the Player) do not know how exactly the decision influences 
    these numbers but each round you get a tip on how the numbers are 
    calculated._TODO)))
    ------------------------------------------------------
    '''

    '''These are the variables that are used for calculating the amount 
    of food that can be eaten within the next year (leftovers remain 
    because they are frozen as reserve each new round).'''
    # ADJUSTABLE: You might want to have a bigger starting food supply below.
    food_supply = people_amount_start + 0

    '''These are the variables that are used for calculating the amount 
    of people and animals each new round.'''
    hunting_amount = 0
    # ADJUSTABLE: 1.5 a possible value, which I sometime adjust for 
    # testing purposes.
    animal_growth_factor = 1.5
    # ADJUSTABLE: 1.25 is a possible value, which I sometime adjust for
    # testing purposes.
    people_growth_factor = 1.25

    while True:  # Main game loop
        '''The game is over if people cannot procreate, people have too 
        little food supply to survive or if there are too many animals 
        '''
        if people_amount <= 1 or food_supply < people_amount or \
            animal_amount >= 20 * people_amount:
            print(
                "--- GAME OVER: The village people did unfortunately",
                "not survive.\n"
                "You probably need to adjust your strategy the next",
                "time. ---")
            # ToDo: adjust the uppper print-statement so that it is nice 
            # to read but not 1 line in the script.
            '''(((OPTIONAL TODO: I might add something like 
            "or animal_amount < people_growth_factor * people_amount" 
            (because the people should be able to survive a 6th round)
            but this makes the game dynamics even more complicated which
            is why I will currently not implement it. 2.5.22)))'''
            break

        # condition for winning the game
        round_number += 1
        if round_number >= round_number_max:
            print(
                "CONGRATULATIONS: You finished the game! Having started with",
                people_amount_start,
                "people and",
                animal_amount_start,
                "proconimals, now after",
                round_number_max,
                "years there are",
                int(people_amount),
                "people and",
                int(animal_amount),
                "proconimals.")
            break

        print("Of those", int(animal_amount), "proconimals that exist:")
        hunting_amount = pyip.inputInt(
            max=animal_amount,
            min=0,
            prompt='Please decide how many should be hunted in the following year: >>> ')

        # Calculating the main-variables
        food_supply = food_supply - people_amount
        food_supply = food_supply + hunting_amount

        '''ADJUSTABLE: The people_growth_factor varies, because the 
        people procreate more when they know there is more than enough 
        food.'''
        if food_supply >= 2 * people_amount:
            people_growth_factor = people_growth_factor * 2

        animal_amount = animal_amount - hunting_amount
        animal_amount = animal_amount * animal_growth_factor
        people_amount = people_amount * people_growth_factor

        print("1 year has past: Now the village has", int(people_amount),
              "inhabitants and", int(animal_amount), "proconimals exist.")

    '''TODO_Get rid of the follwing  break-statement as soon as Game is 
    finished. If I get rid of it before the game will often exit because 
    of an eternal loop which raises the exit-condition at some point'''
    # break

    # User can make another calculation or quit the game
    print("Do you want to play again or quit the game?")

    proceed_how = pyip.inputMenu(
        ['AGAIN', 'QUIT'], lettered=True, numbered=False)
    print(proceed_how)

    if proceed_how == 'AGAIN':
        continue

    if proceed_how == 'QUIT':
        print("Thanks for playing!")
        sys.exit()

    '''(((OPTIONAL-TODO: Tips: Give player the option to receive 1 out 
    of X tips. Perhaps make a dictionary with X tips and give multiple 
    options for input (with pyIpPlus-Module) and link them to the 
    dictionary like I did in CountryComparisonProgram))).
    '''
