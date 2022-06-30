print('Welcome to My Computer Quiz!')

playing =input('Do you want to play? ')

if playing.lower()!= 'yes':
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What is a female elephant called? ")
if answer.lower() == 'cow':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("The Beaver Is The National Emblem Of Which Country? ")
if answer.lower() == 'canada':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("How Many Hearts Does An Octopus Have? ")
if answer.lower() == 'three' or answer == '3':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("Which Two Countries Share The Longest International Border? ")
if answer == 'canada and USA':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("In A Website Browser Address Bar, What Does “Www” Stand For? ")
if answer == 'World Wide Web' or answer == 'world wide web':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What Is The Only Fruit That Has Its Seeds On The Outside? ")
if answer.lower() == 'stawberry':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print('You got ' + str(score) + ' questions correct')
print('You got ' + str((score / 6) * 100) + '%')

