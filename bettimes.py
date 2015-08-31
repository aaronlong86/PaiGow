import random

earn = 0
startMoney = 5000
for m in range(365):
    i = 0
    initMoney = startMoney
    playtime = random.randrange(60,200)
    while initMoney>0 and playtime>0:
        i = i+1
        minute = random.randrange(5,10)
        playtime = playtime-minute
        if initMoney>=150:
            bet = random.randrange(50,200,50)
            if random.randint(0,1)==1:
                initMoney = initMoney+bet
            else:
                initMoney =initMoney-bet
        else:
            if initMoney>50:
                bet = random.randrange(50,initMoney)
            else:
                bet = initMoney
            if random.randint(0,1)==1:
                initMoney = initMoney+bet
            else:
                initMoney =initMoney-bet
    else:
        earn = initMoney-startMoney+earn
        print("第",m,"天,赌博",i,"次，还有：",initMoney,"回家。赢：",earn)
