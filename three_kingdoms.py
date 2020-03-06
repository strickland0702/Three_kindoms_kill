'''使用类与对象实现简易三国杀游戏'''
import time
import numpy as np
from random import shuffle
class player():
    def __init__(self, player_name):
        self.life = 3
        self.name = player_name
        self.handcard = []

    def get_card(self, deck):
        self.handcard.append(deck.card_list[0])
        deck.remove_card()

    def play_card(self, card_index):
        self.handcard.pop(card_index)

    def display_handcard(self):
        for card in self.handcard:
            print(card.display_card())

class card():
    def __init__(self, index, color, name):
        self.index = index
        self.color = color
        self.name = name
    
    def display_card(self):
        return '[%s - %s - %s]'%(self.color, self.index, self.name)
    
class deck():
    def __init__(self):
        self.card_list = []

    def append_card(self, card):
        return self.card_list.append(card)

    def remove_card(self):
        return self.card_list.pop(0)

    def display_all_cards(self):
        for card in self.card_list:
            print(card.display_card())

color_list = ['Heart', 'Diamond', 'Club', 'Spade']
num_list = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
card_name_list = ['Kill','Defence','Peach']

game_deck = deck()

for col in color_list:
    for num in num_list:
        new_card = card(num, col, '')
        game_deck.append_card(new_card)
            
shuffle(game_deck.card_list)
for i in range(35):
    game_deck.card_list[i].name = 'Kill'

for i in range(35,45):
    game_deck.card_list[i].name = 'Defence'

for i in range(45,52):
    game_deck.card_list[i].name = 'Peach'

shuffle(game_deck.card_list)
game_deck.display_all_cards()
time.sleep(2)

#初始化玩家
player_list = []
player_name = ['Chris','Susan','Bob']
for pl in player_name:
    new_player = player(pl)
    for i in range(2):
        new_player.get_card(game_deck)
    player_list.append(new_player)

print('Game Starts!')
time.sleep(2)

while (len(player_list) > 1):
    for player in player_list:
        print('-----Round for %s(%s life points) starts-----'%(player.name, player.life))
        time.sleep(2)

        # 摸牌阶段
        for i in range(2):
            player.get_card(game_deck)
        time.sleep(2)

        # 出牌阶段
        while(True):
            player.display_handcard() 
            choice = int(input('Please choose the card you want to play:\n'))
            if choice == -1:
                print('%s ends his playing phase.\n'%(player.name))
                time.sleep(2)
                break
            else:
                if player.handcard[choice].name == 'Kill':
                    choose_player = int(input('Please choose a player to attack:\n'))
                    player.play_card(choice)

                    flag = 0
                    for i in range(len(player_list[choose_player].handcard)):
                        if player_list[choose_player].handcard[i].name == 'Defence':
                            player_list[choose_player].play_card(i)
                            print('%s defences!\n'%(player_list[choose_player].name))
                            flag = 1
                            break

                    if flag == 0:
                        print('%s loses one point life!\n'%(player_list[choose_player].name))
                        player_list[choose_player].life -=1
                        
                        if player_list[choose_player].life == 0:
                            print('%s is dead!'%(player_list[choose_player].name))
                            player_list.pop(choose_player)
                            if (len(player_list) == 1):
                                break
                            time.sleep(2)

                    time.sleep(2)   

                elif player.handcard[choice].name == 'Peach':
                    if player.life >= 3:
                        print('You are full life now!\n')
                    else:
                        player.play_card(choice)
                        player.life +=1
                        print('%s heals for one point!\n'%(player.name))
                    time.sleep(2)
                    
                else:
                    print('Defense is not valid!\n')
                    time.sleep(2)

        # 弃牌阶段
        exceed_card = len(player.handcard) - player.life
        if exceed_card > 0:
            print('You should discard %d handcards'%(exceed_card))
            player.display_handcard()
            for i in range(exceed_card):
                discard = int(input('Please choose the cards you want to discard'))
                player.play_card(discard)

            time.sleep(2)
        
        # 结束阶段
        print('Cards Left For %s:\n'%(player.name))
        player.display_handcard()
        time.sleep(2)
        
        print('-----Round for %s ends-----\n\n'%(player.name))
        time.sleep(3)

# 输出胜利信息
print('%s wins!'%(player_list[0].name))