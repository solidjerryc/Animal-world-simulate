# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 23:22:25 2018

@author: JerryC
"""
INIT_STARS=3 #星星的个数

import random
import collections

class player:
    def __init__(self,no=0):
        self.__no=no
        self.__cards=['s','r','p']*4 #初始牌 s:剪刀  r:石头  p:布
        self.__stars=INIT_STARS
        random.shuffle(self.__cards)
        
    def isDead(self):
        if self.__stars==0 or (0 < self.__stars < INIT_STARS and len(self.__cards)==0):
            return True
        else:
            return False
        
    def isWin(self):
        if self.__stars>=INIT_STARS and len(self.__cards)==0:
            return True
        else:
            return False
        
    def isAvailable(self):
        if self.isWin() or self.isDead():
            return False
        else:
            return True
        
    def countCards(self):
        num=dict(collections.Counter(self.__cards))
        try:
            s=num['s']
        except:
            s=0
            num['s']=0
        try:
            p=num['p']
        except:
            p=0
            num['p']=0
        try:
            r=num['r']
        except:
            r=0
            num['r']=0
        num['all']=s+p+r
        return num
    
    def getStars(self):
        return self.__stars
    
    def getNo(self):
        return self.__no
    
    def win(self):
        self.__stars=self.__stars+1

    def lose(self):
        self.__stars=self.__stars-1
        
    # 出牌
    def check(self):
        if len(self.__cards)==0:
            raise Exception("No cards")
            return 0
        else:
            return self.__cards.pop()
        random.shuffle(self.__cards)

def play(player1,player2):
    card1=player1.check()
    card2=player2.check()
    if card1=='s':
        if card2=='r':
            player1.lose()
            player2.win()
        elif card2=='s':
            pass
        elif card2=='p':
            player1.win()
            player2.lose()
    elif card1=='r':
        if card2=='r':
            pass
        elif card2=='s':
            player1.win()
            player2.lose()
        elif card2=='p':
            player1.lose()
            player2.win()
    elif card1=='p':
        if card2=='r':
            player1.win()
            player2.lose()
        elif card2=='s':
            player1.lose()
            player2.win()
        elif card2=='p':
            pass
#    print(player1.getNo(),card1,player1.getStars(),'\t',player2.getNo(),card2,player2.getStars())
        
