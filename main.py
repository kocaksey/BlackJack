import random
import dic as df

total = 0
d = {}
cas = {}
bud = {}
for i in range(338):
    x = random.choice(df.deck)
    df.deck.remove(x)
half_deck = df.deck
number_of_player = int(input("Number of Player: "))

for y in range(number_of_player):
    budget=int(input(f"Player{y + 1} budget:"))
    bud["Player{0}".format(y + 1)] = budget
w=1
flag1 = True
while flag1:

    for u in range(number_of_player):
        cash = int(input(f"Player{u + 1} bet:"))
        cas["Player{0}".format(u + 1)] = cash
    dealers_first = random.choice(half_deck)
    half_deck.remove(dealers_first)
    print(f"///////////////////////// Game {w} /////////////////////////\nDealer's Cards:\n{dealers_first}\n-Closed Card-")
    w+=1
    for j in range(number_of_player):
        print(f"\nPlayer{j + 1}:")
        for i in range(2):
            random_card = random.choice(half_deck)
            half_deck.remove(random_card)
            value = df.deck_values[random_card]
            total += value
            if total == 22:
                total = 12
            print(random_card)

        d["Player{0}".format(j + 1)] = total
        total = 0

    flag = True
    for i in range(number_of_player):
        while flag:
            if d[f"Player{i + 1}"] == 21:
                print(f"Player{i + 1} Won x1,5!")
                cas[f"Player{i + 1}"] = cas[f"Player{i + 1}"] * 1.5
                break
            print(f"\n{d}")
            b = input(f"\nPlayer{i + 1}\n1-Hit\n2-Stand\n")

            if b == "1":
                c = d[f"Player{i + 1}"]
                v = random.choice(half_deck)
                half_deck.remove(v)
                value = df.deck_values[v]
                if c > 10 and v[-1] == "1":
                    value = 1
                c = c + value
                d[f"Player{i + 1}"] = c
                print(f"Player{i+1}'s new card: ///// {v} /////")
                if d[f"Player{i + 1}"] > 21:
                    print(f"Player{i + 1} Lost!")
                    break
                elif d[f"Player{i + 1}"] == 21:
                    print(f"Player{i + 1} Win!")
                    break
            if b == "2":
                break
    print("///////////////////////////////////\nDealer's cards:")
    print(dealers_first)
    z = random.choice(half_deck)

    half_deck.remove(z)
    print(z)
    s = df.deck_values[z]
    f = df.deck_values[dealers_first] + s
    if f == 22:
        f = 12
    while f < 17:
        h = random.choice(half_deck)
        half_deck.remove(h)
        r = df.deck_values[h]
        print(h)
        if h[-1] == "1" and f + r > 21:
            r = 1

        f = f + r

    print(f"{f}\n///////////////////////////////////")

    for l in range(number_of_player):

        if f > 21:
            f = 0
        if d[f"Player{l + 1}"] > 21:
            d[f"Player{l + 1}"] = 0
        if f == d[f"Player{l + 1}"]:
            print(f"Player{l + 1} Draw!")
        if f > d[f"Player{l + 1}"]:
            print(f"Player{l + 1} Lost $" + str(cas[f"Player{l + 1}"]) + " !")
            bud[f"Player{l + 1}"] -= cas[f"Player{l + 1}"] * 1
        elif f < d[f"Player{l + 1}"]:
            print(f"Player{l + 1} Won $" + str(cas[f"Player{l + 1}"]) + " !")
            bud[f"Player{l + 1}"] += cas[f"Player{l + 1}"] * 1


    print(f"Balance: " + str(bud))

    n = input("\n1-Continue\n2-End Game\n")

    if n == "2":
        break
