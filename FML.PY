import random
import requests
import sys

my_pokemon = ''
your_stats = ''
my_score = 0
computer_score = 0


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

    print('Your pokemon choices are: {}, {}, {} '.format(random_pokemon_1['name'].upper(),
                                                         random_pokemon_2['name'].upper(),
                                                         random_pokemon_3['name'].upper()))
    pokemon_choice = input('Which pokemon do you want to use? ')

    if pokemon_choice == random_pokemon_1['name']:
        my_pokemon = random_pokemon_1
    elif pokemon_choice == random_pokemon_2['name']:
        my_pokemon = random_pokemon_2
    elif pokemon_choice == random_pokemon_3['name']:
        my_pokemon = random_pokemon_3
    else:
        print('Hmmm.. it seems you have input an incorrect value, try that again')
        choose_pokemon()

    print('You have chosen {}'.format(my_pokemon['name'].upper()))

    your_stats = (
        '{}\'S stats are: Height: {}ft, Weight: {}lbs, Experience: {} Points '.format(my_pokemon['name'].upper(),
                                                                                      my_pokemon['height'],
                                                                                      my_pokemon['weight'],
                                                                                      my_pokemon['experience']))
    print(your_stats)
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


# def finish_game():
#     end_choice = input('Would you like to play another round? \n Yes or No \n')
#
#     if end_choice == 'y' or end_choice == 'yes':
#         print('\n')
#         choose_pokemon()
#
#     else:
#         return


def play_game():

    global my_score
    global computer_score

    computer_pokemon = random_pokemon()
    print('The computer has chosen {} for this Pokemon battle!'.format(computer_pokemon['name'].upper()))

    choose_heads_tails = heads_tails()
    toss_result = coin_toss()

    print('You have chosen {}!'.format(choose_heads_tails.upper()))
    print('The result of the coin toss is (DRUM ROLL PLEASE)... {}!'.format(toss_result.upper()))

    if toss_result == choose_heads_tails:
        print('Congratulations! You have won the coin toss! \n Now, which stat would you like to play? \n'
              'Here\'s a reminder of your stats:\n')

        print(your_stats)

        stat_choice = input('You can choose between: '
                            '\n Experience - the Base Experience points you will gain for defeating this Pokemon '
                            '\n Height - the height of your Pokemon (tallest wins!) '
                            '\n Weight - the weight of your Pokemon (heaviest wins!)\n')

        your_stat_score = my_pokemon[stat_choice]
        computer_stat_score = computer_pokemon[stat_choice]

        print('You have chosen the {} stat. \n'
              'Your Pokemon = {} - {}\'s {} is {} \n'
              'Computer Pokemon = {} - {}\'s {} is {} \n'.format(stat_choice, my_pokemon['name'], my_pokemon['name'],
                                                                 stat_choice, your_stat_score, computer_pokemon['name'],
                                                                 computer_pokemon['name'],
                                                                 stat_choice, computer_stat_score))

        if your_stat_score > computer_stat_score:
            my_score += 1
            print('Yes! You won this round! The score was {} - {} to you!'.format(my_score, computer_score))
        if your_stat_score < computer_stat_score:
            computer_score += 1
            print('Sorry, you lost this round! The score was {} - {} to the computer'.format(my_score, computer_score))
        if your_stat_score == computer_stat_score:
            computer_score += 1
            my_score += 1
            print('It\'s a tie! The score is {} - {}!'.format(my_score, computer_score))

        return my_score, computer_score
        # finish_game()

    else:
        print('Bad luck! You lost the coin toss :( \n The computer will now choose which stat to play with...')
        print('First, here\'s a reminder of your stats:\n')
        print(your_stats)
        print('\n Experience - the Base Experience points you will gain for defeating this Pokemon '
              '\n Height - the height of your Pokemon (tallest wins!) '
              '\n Weight - the weight of your Pokemon (heaviest wins!)\n')

        computer_stat_choice = computer_stat()

        print('\n The computer has chosen {}!\n'.format(computer_stat_choice.upper()))

        your_stat_score = my_pokemon[computer_stat_choice]
        computer_stat_score = computer_pokemon[computer_stat_choice]

        print('Your Pokemon = {} - {}\'s {} is {} \n'
              'Computer Pokemon = {} - {}\'s {} is {} \n'.format(my_pokemon['name'], my_pokemon['name'],
                                                                 computer_stat_choice, your_stat_score,
                                                                 computer_pokemon['name'],
                                                                 computer_pokemon['name'],
                                                                 computer_stat_choice, computer_stat_score))

        if your_stat_score > computer_stat_score:
            my_score += 1
            print('Yes! You won this round! The score was {} - {} to you!'.format(my_score, computer_score))
        if your_stat_score < computer_stat_score:
            computer_score += 1
            print('Sorry, you lost this round! The score was {} - {} to the computer'.format(my_score, computer_score))
        if your_stat_score == computer_stat_score:
            computer_score += 1
            my_score += 1
            print('It\'s a tie! The score is {} - {}!'.format(my_score, computer_score))

            return my_score, computer_score

        # finish_game()


def run():
    global my_score
    choice = input('WELCOME! Are you ready to play Pokemon Top Trumps?! (Yes / No)\n')
    if choice == 'yes' or choice == 'y' or choice == 'Yes':
        print('Great! Lets go!')

        for number in range(3):
            if number < 4:
                choose_pokemon()



        # def loop_program(x):
        #     choose_pokemon()
        #     return x + 1
        #
        # i = (1, 2, 3)
        # print(map(loop_program, i))

        # for x in range(3):
        #     x = choose_pokemon()
        #     return my_score
        #     return computer_score

        # choose_pokemon()
    if choice == 'no' or choice == 'n' or choice == 'No':
        print('Okay! Maybe we\'ll see you again soon! Goodbye!')
        sys.exit(0)
    if choice != 'yes' and choice != 'y' and choice != 'Yes' and choice != 'no' and choice != 'n' and choice != 'No':
        print('I\'m sorry, I don\'t understand your response')
        run()


run()
