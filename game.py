# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 23:23:43 2018

@author: JerryC
"""
PLAYER_NO=100 # 玩家数量
ROUND_NO=1000 # 循环次数

import player
import random
from tqdm import tqdm
import matplotlib.pyplot as plt

#while a.isAvailable() and b.isAvailable():
#    print(a.countCards(),a.getStars(),b.countCards(),b.getStars())
#    player.play(a,b)
#    
#print(a.countCards(),a.getStars(),b.countCards(),b.getStars())

w=0
l=0

all_player=set()

for j in tqdm(range(ROUND_NO)):
    players=[]
    winner=set()
    loser=set()
    
    for i in range(PLAYER_NO):
        players.append(player.player(i))
        
    #while not len(winner)+len(loser)>=PLAYER_NO-1:
    while not len(players)<=1:
        a,b=random.sample(players,2)
        players.remove(a)
        players.remove(b)
        if a.isAvailable() and b.isAvailable():
            player.play(a,b)
        if a.isWin():
            winner.add(a.getNo())
            all_player.add(a)
        elif a.isDead():
            loser.add(a.getNo())
            all_player.add(a)
        else:
            pass
            players.append(a)
        if b.isWin():
            winner.add(b.getNo())
            all_player.add(b)
        elif b.isDead():
            loser.add(b.getNo())
            all_player.add(b)
        else:
            pass
            players.append(b)
    # 如果最后还剩一个玩家，那么这个玩家死了
    if len(players)==1:
        loser.add(players[0].getNo())
        all_player.add(players[0])
    w=w+len(winner)
    l=l+len(loser)


print(w/(ROUND_NO*PLAYER_NO),l/(ROUND_NO*PLAYER_NO))
    
score=[]
for i in all_player:
    score.append(i.getStars())
    
plt.hist(score,bins=30)
plt.plot()
