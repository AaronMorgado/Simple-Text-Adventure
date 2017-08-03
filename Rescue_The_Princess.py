import random

'''
Things to do
   make a map
'''

# displays a message for the user to inform him/her where she/he is


def msg(room):

    if room['name'] == 'Level 1' or room['name'] == 'Level 2' or room['name'] == 'Level 3':
        return "You are now on " + room['name'] + "."
    elif room['msg'] == '':
        return "You have entered the " + room['name'] + '.'
    else:
        return room['msg']

# establishes directions


def dir_choice(room, dir):

    if dir == 'N' or dir == 'n':
        choice = 0
    elif dir == 'E' or dir == 'e':
        choice = 1
    elif dir == 'S' or dir == 's':
        choice = 2
    elif dir == 'W' or dir == 'w':
        choice = 3
    elif dir == 'D' or dir == 'd':
        choice = 4
    elif dir == 'U' or dir == 'u':
        choice = 5
    else:
        return -1

    if room['directions'][choice] == 0:
        return 6
    else:
        return choice


def dmg_multiplier():
    multiplier = random.randrange(1, 3)
    return multiplier

# battle between player and boss


def battle_sequence(traveler):
    in_battle = True

    print('Blackout: Welcome ' + traveler + ', I have been awaiting your arrival.')
    print('Blackout: I hope you are a worthy foe. I have had a plethora of time to master my dueling skills.')
    print('Blackout: I hereby challenge you to a duel!')
    print(traveler + ': I accept the challenge foul beast, today is the day I strike you down!')

    hero_dmg = 2
    boss_dmg = 1.5
    boss_hearts = 12
    hero_hearts = 10

    while in_battle:
        attack = input('Type attack to deal damage to the boss ')

        if attack == 'attack':
            boss_hearts = boss_hearts - (hero_dmg * dmg_multiplier())
            print('Blackout now has ' + str(boss_hearts) + ' hearts left')
            print('Blackout has attacked!')
            hero_hearts = hero_hearts - (boss_dmg * dmg_multiplier())
            print('You now have ' + str(int(hero_hearts)) + ' hearts left')

            if hero_hearts <= 0 and boss_hearts <= 0:
                print('You are both of equal skill, and therefore both of you have suffered fatal wounds.')
                print('Game Over')
                in_battle = False
                return in_battle

            elif boss_hearts <= 0:
                print('Congratulations! You have slain Blackout and saved the princess. Now escort her back outside in order to deliver her back to the village.')
                in_battle = True  # so the if statement in main doesnt evaluate to true and break the loop causing the game to end
                return in_battle

            elif hero_hearts <= 0:
                print('Blackout has bested you in combat.')
                print('Game Over')
                in_battle = False
                return in_battle

        else:
            print('You cannot escape the battle, type attack to continue.')

# main program


def main():

    dirs = [0, 0, 0, 0, 0, 0]

    # defines each room as a dictionary
    outside = {'name': 'Outside', 'directions': dirs, 'msg': ""}
    fort_entrance = {'name': 'Fort Ruins Entrance', 'directions': dirs, 'msg': ''}
    level_1 = {'name': 'Level 1', 'directions': dirs, 'msg': ""}
    north_doorway = {'name': 'Dinning Hall', 'directions': dirs, 'msg': ''}
    level_2 = {'name': 'Level 2', 'directions': dirs, 'msg': ""}
    east_doorway = {'name': 'Sleeping Quarters', 'directions': dirs, 'msg': ''}
    south_doorway = {'name': 'Guest Sleeping Quarters', 'directions': dirs, 'msg': ''}
    level_3 = {'name': 'Level 3', 'directions': dirs, 'msg': ""}
    west_doorway = {'name': 'Storage Room', 'directions': dirs, 'msg': ''}
    north_doorway2 = {'name': 'Armory', 'directions': dirs, 'msg': ''}
    east_doorway2 = {'name': 'Wine Cellar', 'directions': dirs, 'msg': ''}

    # directions to each room and level [N,E,S,W,D,U]
    outside['directions'] = (fort_entrance, 0, 0, 0, 0, 0)
    fort_entrance['directions'] = (0, 0, outside, 0, level_1, 0)
    level_1['directions'] = (north_doorway, 0, level_1, 0, level_2, fort_entrance)
    north_doorway['directions'] = (0, 0, level_1, 0, 0, 0)
    level_2['directions'] = (0, east_doorway, south_doorway, 0, level_3, level_1)
    east_doorway['directions'] = (0, 0, 0, level_2, 0, 0)
    south_doorway['directions'] = (level_2, 0, 0, 0, 0, 0)
    level_3['directions'] = (north_doorway2, east_doorway2, 0, west_doorway, 0, level_2)
    west_doorway['directions'] = (0, level_3, 0, 0, 0, 0)
    north_doorway2['directions'] = (0, 0, level_3, 0, 0, 0)
    east_doorway2['directions'] = (0, 0, 0, level_3, 0, 0)

    rooms = [north_doorway, east_doorway, south_doorway, west_doorway, north_doorway2, east_doorway2]
    room_with_princess = random.choice(rooms)
    princess_found = False
    room = fort_entrance
    traveler = input('Who goes there? ')

    print(
        "You set out on the perilous journey to rescue the princess. Your heart filled with excitement, terror, and courage.")
    print(
        "You approach the entrance of the dungeon in which the princess is being held captive. You wipe the sweat from your forehead")
    print(
        "and draw your sword and shield. You look around and only find one entrance to the fort ruins.")

    # starts the game

    while True:


        if princess_found and room['name'] == 'Outside':
            print('You and the princess walk together all the way back to the kingdom and you relieve her to the king.')
            print('The King gives great thanks to you and says he is going to throw an amazing party and the whole Kingdom is invited.')
            print('Later, the King pulls you aside and says: Oh ' + traveler + ' I can not express my thanks well enough with words.')
            print('The King retrieves a pouch full of gold and hands it over. Take this as an expression of my thanks, he says.')
            print('You confidently respond with thank you and go to your home and prepare for the party.')
            print('Thank you for playing!')

            break

        elif not princess_found and room['name'] == room_with_princess['name']:
            princess_found = True
            print('There is the princess! But something feels strange about this room. You look all around.')
            print('When you look back at the princess you see this mighty creature. He seems to be at least 15 feet tall.')
            print('The creature also has breath that smells utterly foul and it\'s face is repulsive.')
            print('But this does not deter you, you ready your shield and sword and prepare for a great battle')

            if not battle_sequence(traveler):  # battle sequence between player and boss

                break

            room['msg'] = 'This is where you found the princess, you need to bring her back to the kingdom.'

        else:
            print(msg(room))
            if room['name'] == 'Outside':
                room['msg'] = 'You have already been ' + room['name']
            else:
                room['msg'] = 'You have already been in the ' + room['name']

        unmoving = True

        while unmoving:
            dir = input('Which direction do you want to go: N,E,S,W,D,U? ')
            choice = dir_choice(room, dir)

            if choice == -1:
                print('Trying to be smart I see. Looks like I am more intelligent. Enter N,E,S,W,D, or U')

            elif choice == 6:
                print('There seems to be no entry way in this direction, try another.')

            else:
                room = room['directions'][choice]
                unmoving = False

main()
