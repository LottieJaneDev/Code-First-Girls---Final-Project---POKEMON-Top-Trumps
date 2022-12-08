import random
import requests
import sys
import time

my_pokemon = ''
your_stats = ''
my_score = 0
computer_score = 0
your_stat_score = ''
computer_stat_score = ''
round_no = ''


def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'experience': pokemon['base_experience']

    }


def choose_pokemon():
    global my_pokemon
    global your_stats
    random_pokemon_1 = random_pokemon()
    random_pokemon_2 = random_pokemon()
    random_pokemon_3 = random_pokemon()

    print('\n----- ROUND {} -----\n'.format(round_no+1))
    print('Your pokemon choices are: {}, {}, {} '.format(random_pokemon_1['name'].upper(),
                                                         random_pokemon_2['name'].upper(),
                                                         random_pokemon_3['name'].upper()))
    pokemon_choice = input('Which pokemon do you want to duel with?! \n')

    if pokemon_choice == random_pokemon_1['name']:
        my_pokemon = random_pokemon_1
    elif pokemon_choice == random_pokemon_2['name']:
        my_pokemon = random_pokemon_2
    elif pokemon_choice == random_pokemon_3['name']:
        my_pokemon = random_pokemon_3
    else:
        print('Hmm.. it seems you have input an incorrect value, try that again\n')
        choose_pokemon()

    print('\nYou have chosen {}\n'.format(my_pokemon['name'].upper()))
    time.sleep(2)
    your_stats = (
        '{}\'S stats are: Height: {}ft, Weight: {}lbs, Experience: {} Points \n'.format(my_pokemon['name'].upper(),
                                                                                        my_pokemon['height'],
                                                                                        my_pokemon['weight'],
                                                                                        my_pokemon['experience']))
    print(your_stats)
    time.sleep(3)
    play_game()


def heads_tails():
    answer = input("To make it fair, we will toss a coin to decide who chooses which stat to do battle with! "
                   "Decide your fate: \n * Heads? \n * Tails? \n")
    return answer


def coin_toss():
    return random.choice(['heads', 'tails'])


def computer_stat():
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        return 'height'
    if computer_choice == 1:
        return 'weight'
    if computer_choice == 2:
        return 'experience'


def finish_game():
    play_again = input('Would you like to play again? \nYes or No \n')

    if play_again == 'y' or play_again == 'yes' or play_again == 'Yes':
        print('\n')
        time.sleep(3)
        run()
    else:
        print('\nOkay! Thanks for playing! See you again soon!\n')
        time.sleep(2)
        print('\n  *** Game created by LottieJane1312 @ Github ***')
        return


def round_results():
    global your_stat_score
    global computer_stat_score
    global my_score
    global computer_score

    if your_stat_score > computer_stat_score:
        my_score += 1
        print('Yes! You won this round! The current score is {} ~ {} to you!\n'.format(my_score, computer_score))
        time.sleep(4)
    if your_stat_score < computer_stat_score:
        computer_score += 1
        print('Sorry, you lost this round! The current score is {} ~ {} to the computer\n'.format(my_score,
                                                                                                  computer_score))
        time.sleep(4)
    if your_stat_score == computer_stat_score:
        computer_score += 1
        my_score += 1
        print('It\'s a tie! The current score is {} ~ {}!\n'.format(my_score, computer_score))
        time.sleep(4)

    return my_score, computer_score


def play_game():
    global your_stat_score
    global computer_stat_score
    global my_score
    global computer_score

    computer_pokemon = random_pokemon()
    print('The computer has chosen {} for this Pokemon battle!\n'.format(computer_pokemon['name'].upper()))
    time.sleep(2)
    choose_heads_tails = heads_tails()
    toss_result = coin_toss()
    print('\nYou have chosen {}!'.format(choose_heads_tails.upper()))
    time.sleep(2)
    print('The result of the coin toss is... {}!'.format(toss_result.upper()))
    time.sleep(3)

    if toss_result == choose_heads_tails:
        print('Congratulations! You have won the coin toss! \nNow, which stat would you like to play??'
              ' Here\'s a reminder of your stats:\n')
        time.sleep(2)
        print(your_stats)
        time.sleep(2)

        stat_choice = input('You can choose between: '
                            '\n * Experience - the Base Experience points you will gain for defeating this Pokemon '
                            '\n * Height - the height of your Pokemon (tallest wins!) '
                            '\n * Weight - the weight of your Pokemon (heaviest wins!)\n')

        your_stat_score = my_pokemon[stat_choice]
        computer_stat_score = computer_pokemon[stat_choice]
        print('\nYou have chosen the {} stat:\n'.format(stat_choice))
        time.sleep(2)
        print('\nYour Pokemon = {} : {}\'s {} is {} \n'
              'Computer Pokemon = {} : {}\'s {} is {} \n'.format(my_pokemon['name'].upper(), my_pokemon['name'].upper(),
                                                                 stat_choice, your_stat_score, computer_pokemon['name'].upper(),
                                                                 computer_pokemon['name'].upper(),
                                                                 stat_choice, computer_stat_score))
        time.sleep(4)
        round_results()

    else:
        print('\nBad luck! You lost the coin toss :(\nThe computer will now choose which stat to play with...')
        time.sleep(4)
        print('\nFirst, here\'s a reminder of your stats:\n')
        time.sleep(3)
        print(your_stats)
        time.sleep(3)
        print(' * Experience - the Base Experience points you will gain for defeating this Pokemon '
              '\n * Height - the height of your Pokemon (tallest wins!) '
              '\n * Weight - the weight of your Pokemon (heaviest wins!)\n')
        time.sleep(5)
        computer_stat_choice = computer_stat()
        print('The computer has chosen {}!\n'.format(computer_stat_choice.upper()))
        time.sleep(4)
        your_stat_score = my_pokemon[computer_stat_choice]
        computer_stat_score = computer_pokemon[computer_stat_choice]
        print('Your Pokemon = {} : {}\'s {} is {} \n'
              'Computer Pokemon = {} : {}\'s {} is {} \n'.format(my_pokemon['name'].upper(), my_pokemon['name'].upper(),
                                                                 computer_stat_choice, your_stat_score, computer_pokemon['name'].upper(),
                                                                 computer_pokemon['name'].upper(),
                                                                 computer_stat_choice, computer_stat_score))
        time.sleep(4)
        round_results()


def run():
    global round_no
    choice = input('WELCOME! Are you ready to play Pokemon Top Trumps?! (Yes / No)\n')
    if choice == 'yes' or choice == 'y' or choice == 'Yes':
        print('Great! Lets go! \nThere will be 4 ROUNDS - Good Luck!')
        time.sleep(3)

        for number in range(4):
            if number < 4:
                round_no = number
                choose_pokemon()

        print('That\'s the end of the game! The final score is:\n')
        time.sleep(3)
        print('*\n'
              '*\n'
              '*\n'
              '*\n'
              '\n   You  {} ~ {}  Computer\n'.format(my_score, computer_score))
        time.sleep(3)
        if computer_score > my_score:
            print('Bad luck! The computer beat you this time :(')
        if computer_score == my_score:
            print('It was a draw! Well played :)')
        if my_score > computer_score:
            print('CONGRATULATIONS! YOU WON THE GAME!!! :D')
        time.sleep(3)
        finish_game()

    if choice == 'no' or choice == 'n' or choice == 'No':
        print('Okay! Maybe we\'ll see you again soon! Goodbye!')
        sys.exit(0)
    if choice != 'yes' and choice != 'y' and choice != 'Yes' and choice != 'no' and choice != 'n' and choice != 'No':
        print('I\'m sorry, I don\'t understand your response')
        run()

run()
