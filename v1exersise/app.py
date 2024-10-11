# x = input('x: ')
# print(x)
# y = int(x) + 1

# print(f"x: {x}, y: {y}")
# print(float(2))

# conditional statements
# temperature = 15
# if temperature > 30:
#     print("Its' warm")
#     print("Drink' water")
# elif temperature > 20:
#     print("It's nice")
# else:
#     print("It's cold")
# print("Done")

# Ternary Operation
# if age >= 17:
#     message = ('Eligible')
# else:
#     message = ('Not Eligible')

# age = 20
# message = "Eligible" if age >= 18 else 'Not eligible'

# print(message)

# high_income = False
# good_credit = True
# student = False

# if not student:
#     print('Eligible')
# else:
#     print('NotEligible')

# successful = False
# for number in range(3):
#     print('Hello world')
#     if successful:
#         print('Successful')
#         break
# else:
#     print('Attempted 3 times')

# number = input('add any number: ')
# for x in range(int(number + '')):
#     pattern = ''
#     for i in range(x):
#         pattern += '*'
#         print(pattern)

# nested loops
# for x in range(5):
#     for y in range(3):
#         print(f"{x}, {y}")

# Iterable
# for name in 'Product cart':
#     print(name)

# for number in [1, 2, 3, 4]:
#     print(number)

# While loop
# number = 100
# while number > 0:
#     print(number)
#     # number = number // 2
#     number //= 2

# command = ''
# while command.lower() != 'quit':
#     command = input('>')
#     print('ECHO', command)

# count = 0
# for even in range(1, 10):
#     if even % 2 == 0:
#         count += 1
#         print(even)
# print(f"we have {even} number")

# Project 1
name = input('Hey, type your name: ')
print(f"Hello {name}, welcome to my game!")

# Ask if they want to play
should_we_play = input("Do you want to play? (y/n): ").lower()
play = should_we_play == 'yes' or should_we_play == 'y'

if play:
    print('Great! We are going to play!')

    # First decision: left or right
    direction = input('Do you want to go left or right? (l/r): ').lower()

    # Map input to full direction words
    if direction == 'left' or direction == 'l':
        direction = 'left'
        print(f'You went {direction}.')
    elif direction == 'right' or direction == 'r':
        direction = 'right'
        print(f'You went {direction}.')
    else:
        print('Invalid choice, game over!')
        exit()

    # Second stage after choosing direction
    encounter = input(f'While going {
                      direction}, you found a cave. Do you want to enter or keep walking? (enter/walk): ').lower()

    if encounter == 'enter':
        print(f'You bravely enter the cave and find a treasure chest!')
        action = input(
            'Do you want to open it or leave it? (open/leave): ').lower()

        if action == 'open':
            print(f'Congratulations, {
                  name}! You found a bag of gold coins. You win the game!')
        elif action == 'leave':
            print(f'You decide to leave the chest untouched. You exit the cave safely.')
        else:
            print('Invalid choice, a trap was triggered. Game over!')

    elif encounter == 'walk':
        print(f'You keep walking along the {
              direction} path, but it leads to a dead end. Game over!')

    else:
        print('Invalid choice, game over!')

else:
    print('We are not going to play. Goodbye!')
