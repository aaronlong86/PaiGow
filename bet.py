import random
initMoney = 1000
bet = 0
i = 0

while initMoney>0:
    i = i+1
    if initMoney>=150:
        bet = random.randrange(50,200,50)
        if random.randint(0,1)==1:
            initMoney = initMoney+bet
            print(i,":赢了：",bet,"，还有：",initMoney)
        else:
            initMoney =initMoney-bet
            print(i,":    输了：",bet,"，还有：",initMoney)
    else:
        if initMoney>50:
            bet = random.randrange(50,initMoney)
        else:
            bet = initMoney
        if random.randint(0,1)==1:
            initMoney = initMoney+bet
            print(i,":赢了：",bet,"，还有：",initMoney)
        else:
            initMoney =initMoney-bet
            print(i,":    输了：",bet,"，还有：",initMoney)
        
        
        
