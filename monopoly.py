from random import randint
from time import sleep


class stats:
    def __init__(self, location, balance, jail, jailFree, doubles, ownedRR, ownedUT):
        self.location = location
        self.balance = balance
        self.jailFree = jailFree
        self.jail = jail
        self.doubles = doubles
        self.ownedRR = ownedRR
        self.ownedUT = ownedUT


# set up players
player = {}
for count in range(0, 7):
    if count == 0:
        player.update({count: stats(0, 0, False, False, 0, [], [])})
    else:
        player.update({count: stats(0, 1500, False, False, 0, [], [])})
# select number of players
players = int(input("Number of players: "))
if players > 8:
    players = 8
if players < 2:
    players = 1
current = 0
flag = False

# community chest
comChest = {"go": "Advance to Go\n(Collect $200)",
            "bank": "Bank error in your favor\nCollect $200",
            "services": "Receive $25\nfor services",
            "opera": "Grand Opera Opening\nCollect $50 from every player\nfor opening night seats",
            "school": "Pay school tax\nof $150",
            "insurance": "Life insurance matures\nCollect $100",
            "stock": "From sale of stock\nYou get $50",
            "inherit": "You inherit $100",
            "doctor": "Doctor's fees\nPay $50",
            "repairs": "You are assessed for street repairs\n$40 per house\n$115 per hotel",
            "contest": "You have won second prize \nin a beauty contest\nCollect $10",
            "income": "Income tax refund\nCollect $20",
            "xmas": "Xmas fund matures\nCollect $100",
            "hospital": "Pay hospital $100",
            "jail": "Go to jail\nDO NOT PASS GO\nDO NOT COLLECT $200",
            "jailFree": "Get out of jail free\nThis card may be kept until needed, or sold"}
# community chest selection
comChestCard = ["go", "bank", "services", "opera", "school", "insurance", "stock", "inherit", "doctor", "repairs",
                "contest", "income", "xmas", "hospital", "jail", "jailFree"]
# chance
chance = {"go": "Advance to Go\n(Collect $200)",
          "broadwalk": "Take a walk on the Broadwalk"
                       "\nAdvance token to Broadwalk",
          "illinois": "Advance to Illinois Ave.",
          "charles": "Advance to St. Charles Place\n"
                     "If you pass Go, collect $200",
          "reading": "Take a ride on the Reading\n"
                     "If you pass Go, collect $200",
          "railroad": "Advance token to nearest railroad\n"
                      "and pay the owner Twice the rental\n"
                      "to which he/she is otherwise entitled\n"
                      "If Railroad is UNOWNED, you may buy it from the Bank.",
          "utility": "Advance token to nearest Utility\n"
                     "If UNOWNED you may buy it from the bank.\n"
                     "If OWNED, throw dice and pay owner\n"
                     "a total ten times the amount thrown",
          "back3": "Go back 3 spaces",
          "bank": "Bank pays you dividend of $50",
          "mature": "Your building and loan matures\nCollect $150",
          "poor": "Pay poor tax of $15",
          "chairman": "You have been elected chairman of the board\n"
                      "Pay each player $50",
          "repairs": "Make general repairs on all your property\n"
                     "For each house pay $25\n"
                     "For each hotel $100",
          "jail": "Go directly to jail\nDo not pass Go, do not collect $200",
          "jailFree": "Get out of jail free\nThis card may be kept until needed, or sold"}
# chance selection
chanceCard = ["go", "broadwalk", "illinois", "charles", "reading", "railroad", "utility", "back3", "bank", "mature",
              "poor", "chairman", "repairs", "jail", "jailFree"]
# properties
properties = {0: {"name": "Go", "price": 0, "rent": 0, "color": "none", "type": "corner", "owner": "none", "houses": 0, "hotels": 0},
              1: {"name": "Mediterranean Avenue", "price": 60, "hPrice": 50, "rent": 2, "color": "brown", "type": "property", "owner": "none", "houses": 0, "hotels": 0},
              2: {"name": "Community Chest", "price": 0, "rent": 0, "color": "none", "type": "community", "owner": "none", "houses": 0, "hotels": 0},
              3: {"name": "Baltic Avenue", "price": 60, "hPrice": 50, "rent": 4, "color": "brown", "type": "property", "owner": "none", "houses": 0, "hotels": 0},
              4: {"name": "Income Tax", "price": 0, "rent": 0, "color": "none", "type": "tax", "owner": "none", "houses": 0, "hotels": 0},
              5: {"name": "Reading Railroad", "price": 200, "rent": 25, "color": "none", "type": "railroad", "owner": "none", "houses": 0, "hotels": 0},
              6: {"name": "Oriental Avenue", "price": 100, "rent": 6, "color": "light blue", "type": "property", "owner": "none", "houses": 0, "hotels": 0},
              7: {"name": "Chance", "price": 0, "rent": 0, "color": "none", "type": "chance", "owner": "none", "houses": 0, "hotels": 0},
              8: {"name": "Vermont Avenue", "price": 100, "hPrice": 50, "rent": 6, "color": "light blue", "type": "property", "owner": "none", "houses": 0, "hotels": 0},
              9: {"name": "Connecticut Avenue", "price": 120, "hPrice": 50, "rent": 8, "color": "light blue", "type": "property", "owner": "none", "houses": 0, "hotels": 0},
              10: {"name": "Just Visiting/Jail", "price": 0, "rent": 0, "color": "none", "type": "corner", "owner": "none", "houses": 0, "hotels": 0},
              11: {"name": "St. Charles Place", "price": 140, "hPrice": 100, "rent": 10, "color": "pink", "type": "property", "owner": "none", "houses": 0, "hotels": 0},
              12: {"name": "Electric Company", "price": 150, "rent": 0, "color": "none", "type": "utility", "owner": "none", "houses": 0, "hotels": 0},
              13: {"name": "States Avenue", "price": 140, "hPrice": 100, "rent": 10, "color": "pink", "type": "property", "owner": "none", "houses": 0, "hotels": 0},
              14: {"name": "Virginia Avenue", "price": 160, "hPrice": 100, "rent": 12, "color": "pink", "type": "property", "owner": "none", "houses": 0, "hotels": 0},
              15: {"name": "Pennsylvania Railroad", "price": 200, "rent": 25, "color": "none", "type": "railroad", "owner": "none", "houses": 0, "hotels": 0},
              16: {"name": "St. James Place", "price": 180, "hPrice": 100, "rent": 14, "color": "orange", "type": "property", "owner": "none", "houses": 0, "hotels": 0},
              17: {"name": "Community Chest", "price": 0, "rent": 0, "color": "none", "type": "community", "owner": "none", "houses": 0, "hotels": 0},
              18: {"name": "Tennessee Avenue", "price": 180, "hPrice": 100, "rent": 14, "color": "orange", "type": "property", "owner": "none", "houses": 0, "hotels": 0},
              19: {"name": "New York Avenue", "price": 200, "hPrice": 100, "rent": 16, "color": "orange", "type": "property", "owner": "none", "houses": 0, "hotels": 0},
              20: {"name": "Free Parking", "price": 0, "rent": 0, "color": "none", "type": "corner", "owner": "none", "houses": 0, "hotels": 0},
              21: {"name": "Kentucky Avenue", "price": 220, "hPrice": 150, "rent": 18, "color": "red", "type": "property", "owner": "none", "houses": 0, "hotels": 0},
              22: {"name": "Chance", "price": 0, "rent": 0, "color": "none", "type": "chance", "owner": "none", "houses": 0, "hotels": 0},
              23: {"name": "Indiana Avenue", "price": 220, "hPrice": 150, "rent": 18, "color": "red", "type": "property", "owner": "none", "houses": 0, "hotels": 0},
              24: {"name": "Illinois Avenue", "price": 240, "hPrice": 150, "rent": 20, "color": "red", "type": "property", "owner": "none", "houses": 0, "hotels": 0},
              25: {"name": "B. & O. Railroad", "price": 200, "rent": 25, "color": "none", "type": "railroad", "owner": "none", "houses": 0, "hotels": 0},
              26: {"name": "Atlantic Avenue", "price": 260, "hPrice": 150, "rent": 22, "color": "yellow", "type": "property", "owner": "none", "houses": 0, "hotels": 0},
              27: {"name": "Ventnor Avenue", "price": 260, "hPrice": 150, "rent": 22, "color": "yellow", "type": "property", "owner": "none", "houses": 0, "hotels": 0},
              28: {"name": "Water Works", "price": 150, "rent": 0, "color": "none", "type": "utility", "owner": "none", "houses": 0, "hotels": 0},
              29: {"name": "Marvin Gardens", "price": 280, "hPrice": 150, "rent": 24, "color": "yellow", "type": "property", "owner": "none", "houses": 0, "hotels": 0},
              30: {"name": "Go To Jail", "price": 0, "rent": 0, "color": "none", "type": "corner", "owner": "none", "houses": 0, "hotels": 0},
              31: {"name": "Pacific Avenue", "price": 300, "hPrice": 200, "rent": 26, "color": "green", "type": "property", "owner": "none", "houses": 0, "hotels": 0},
              32: {"name": "North Carolina Avenue", "price": 300, "hPrice": 200, "rent": 26, "color": "green", "type": "property", "owner": "none", "houses": 0, "hotels": 0},
              33: {"name": "Community Chest", "price": 0, "hPrice": 200, "rent": 0, "color": "none", "type": "community", "owner": "none", "houses": 0, "hotels": 0},
              34: {"name": "Pennsylvania Avenue", "price": 320, "hPrice": 200, "rent": 28, "color": "green", "type": "property", "owner": "none", "houses": 0, "hotels": 0},
              35: {"name": "Short Line", "price": 200, "rent": 25, "color": "none", "type": "railroad", "owner": "none", "houses": 0, "hotels": 0},
              36: {"name": "Chance", "price": 0, "rent": 0, "color": "none", "type": "chance", "owner": "none", "houses": 0, "hotels": 0},
              37: {"name": "Park Place", "price": 350, "hPrice": 200, "rent": 35, "color": "dark blue", "type": "property", "owner": "none", "houses": 0, "hotels": 0},
              38: {"name": "Luxury Tax", "price": 0, "rent": 0, "color": "none", "type": "tax", "owner": "none", "houses": 0, "hotels": 0},
              39: {"name": "Boardwalk", "price": 400, "hPrice": 200, "rent": 50, "color": "dark blue", "type": "property", "owner": "none", "houses": 0, "hotels": 0}}

colors = {"brown": (1, 3),
          "light blue": (6, 8, 9),
          "pink": (11, 13, 14),
          "orange": (16, 18, 19),
          "red": (21, 23, 24),
          "yellow": (26, 27, 28),
          "green": (31, 32, 34),
          "dark blue": (37, 39)}

titleDeeds = {"Mediterranean Avenue": {0: 2, 1: 10, 2: 30, 3: 90, 4: 160, 5: 250},
              "Baltic Avenue": {0: 4, 1: 20, 2: 60, 3: 180, 4: 320, 5: 450},
              "Oriental Avenue": {0: 6, 1: 30, 2: 90, 3: 270, 4: 400, 5: 550},
              "Vermont Avenue": {0: 6, 1: 30, 2: 90, 3: 270, 4: 400, 5: 550},
              "Connecticut Avenue": {8: 4, 1: 40, 2: 100, 3: 300, 4: 450, 5: 600},
              "St. Charles Place": {0: 10, 1: 50, 2: 150, 3: 450, 4: 625, 5: 750},
              "States Avenue": {0: 4, 1: 50, 2: 150, 3: 450, 4: 625, 5: 750},
              "Virginia Avenue": {0: 4, 1: 60, 2: 180, 3: 500, 4: 700, 5: 900},
              "St. James Place": {0: 4, 1: 70, 2: 200, 3: 550, 4: 750, 5: 950},
              "Tennessee Avenue": {0: 4, 1: 70, 2: 200, 3: 550, 4: 750, 5: 950},
              "New York Avenue": {0: 4, 1: 80, 2: 220, 3: 600, 4: 800, 5: 1000},
              "Kentucky Avenue": {0: 4, 1: 90, 2: 250, 3: 700, 4: 875, 5: 1050},
              "Indiana Avenue": {0: 4, 1: 90, 2: 250, 3: 700, 4: 875, 5: 1050},
              "Illinois Avenue": {0: 4, 1: 100, 2: 300, 3: 750, 4: 925, 5: 1100},
              "Atlantic Avenue": {0: 4, 1: 110, 2: 330, 3: 800, 4: 975, 5: 1150},
              "Ventnor Avenue": {0: 4, 1: 120, 2: 360, 3: 850, 4: 1025, 5: 1200},
              "Marvin Gardens": {0: 4, 1: 130, 2: 390, 3: 900, 4: 1100, 5: 1275},
              "Pacific Avenue": {0: 4, 1: 140, 2: 450, 3: 1000, 4: 1200, 5: 1400},
              "North Carolina Avenue": {0: 4, 1: 150, 2: 450, 3: 1000, 4: 1200, 5: 1400},
              "Pennsylvania Avenue": {0: 4, 1: 160, 2: 480, 3: 1100, 4: 1300, 5: 1500},
              "Park Place": {0: 4, 1: 170, 2: 500, 3: 1200, 4: 1400, 5: 1700},
              "Boardwalk": {0: 4, 1: 200, 2: 600, 3: 1400, 4: 1700, 5: 2000}}

while True:
    if current == 0:
        current += 1
        continue
    elif player[current].balance <= 0:
        current += 1
        continue
    else:
        # player stats
        print("\n\nplayer", current, "turn")
        print("location:", player[current].location, "-", properties[player[current].location]["name"],
              "\nbalance:", player[current].balance)
        sleep(2)

    if not player[current].jail:
        # dice roll
        roll1 = randint(1, 6)
        roll2 = randint(1, 6)
        player[current].location += + roll1 + roll2
        if player[current].location >= 40:
            player[current].location -= 40
            player[current].balance += 200
            print("\ndice roll:", roll1, roll2, "=", roll1 + roll2, "\nlocation:", player[current].location, "-", properties[player[current].location]["name"])
            print("\nplayer", current, "passed go, collected $200")
        else:
            print("\ndice roll:", roll1, roll2, "=", roll1 + roll2, "\nlocation:", player[current].location, "-", properties[player[current].location]["name"])
        sleep(1)
        # doubles count, 3 doubles in a row, go to jail
        if roll1 == roll2:
            player[current].doubles += 1
        else:
            player[current].doubles = 0
        if player[current].doubles == 3:
            player[current].jail = True

        # properties
        # if player is on an Unowned property, choose to buy or not
        if properties[player[current].location]["type"] == "property":
            if properties[player[current].location]["owner"] == "none":
                print("\nUnowned property")
                buy = input("buy for " + str(properties[player[current].location]["price"]) + "? " + "[y/(n)]: ")
                if buy == "y":
                    player[current].balance -= properties[player[current].location]["price"]
                    properties[player[current].location]["owner"] = current
                    print("\nplayer", current, "bought", properties[player[current].location]["name"])
                    print("balance:", player[current].balance)
                    sleep(1)

            # if player is on an owned property, pay rent
            elif properties[player[current].location]["owner"] != current:
                print("\nowned property of player", current)
                print("pay rent of", properties[player[current].location]["rent"])
                player[current].balance -= properties[player[current].location]["rent"]
                player[properties[player[current].location]["owner"]].balance += properties[player[current].location]["rent"]
                print("\nplayer", current, "paid rent to player", properties[player[current].location]["owner"])
                print("balance:", player[current].balance)
                sleep(1)

            # if player is on a property owned by themself,
            # buy houses or hotel if properties of the same color are owned by the player
            elif properties[player[current].location]["owner"] == current:
                print("\nowned property of player", current)
                # check if player owns all properties of the same color
                for loc in colors[properties[player[current].location]["color"]]:
                    if properties[loc]["owner"] == current:
                        flag = True
                    else:
                        flag = False
                        break
                if flag == True:
                    properties[player[current].location]["rent"] *= 2
                    # buy houses
                    if properties[player[current].location]["houses"] < 4:
                        house = input("buy house for " + str(properties[player[current].location]["price"]) + "? " + "[y/(n)]: ")
                        if house == "y":
                            player[current].balance -= properties[player[current].location]["hPrice"]
                            properties[player[current].location]["houses"] += 1
                            print("\nplayer", current, "bought house")
                            print("balance:", player[current].balance)
                            sleep(1)
                    # buy hotel
                    elif properties[player[current].location]["hotels"] < 1:
                        house = input("buy hotel for " + str(properties[player[current].location]["hPrice"]) + "? " + "[y/(n)]: ")
                        if house == "y":
                            player[current].balance -= properties[player[current].location]["hPrice"]
                            properties[player[current].location]["houses"] += 1
                            properties[player[current].location]["hotels"] += 1
                            print("\nplayer", current, "bought hotel")
                            print("balance:", player[current].balance)
                            sleep(1)
                # set rent
                properties[player[current].location]["rent"] = titleDeeds[properties[player[current].location]["name"]][properties[player[current].location]["houses"]]

        # railroads
        # if player is on an Unowned railroad, choose to buy or not
        elif properties[player[current].location]["type"] == "railroad":
            if properties[player[current].location]["owner"] == "none":
                print("\nUnowned railroad")
                buy = input("buy for " + str(properties[player[current].location]["price"]) + "? " + "[y/(n)]: ")
                if buy == "y":
                    player[current].balance -= properties[player[current].location]["price"]
                    properties[player[current].location]["owner"] = current
                    player[current].ownedRR.append(player[current].location)
                    properties[player[current].location]["rent"] = 25 * len(player[current].ownedRR)
                    print("\nplayer", current, "bought", properties[player[current].location]["name"])
                    print("balance:", player[current].balance)
                    sleep(1)

            # if player is on an owned railroad, pay rent
            elif properties[player[current].location]["owner"] != current:
                print("\nOwned railroad")
                print("pay rent of", properties[player[current].location]["rent"])
                player[current].balance -= properties[player[current].location]["rent"]
                player[properties[player[current].location]["owner"]].balance += properties[player[current].location]["rent"]
                print("\nplayer", current, "paid rent to player", properties[player[current].location]["owner"])
                print("balance:", player[current].balance)
                sleep(1)

        # utilities
        # if player is on an Unowned utility, choose to buy or not
        elif properties[player[current].location]["type"] == "utility":
            if properties[player[current].location]["owner"] == "none":
                print("\nUnowned utility")
                buy = input("buy for " + str(properties[player[current].location]["price"]) + "? " + "[y/(n)]: ")
                if buy == "y":
                    player[current].balance -= properties[player[current].location]["price"]
                    properties[player[current].location]["owner"] = current
                    player[current].ownedUT.append(player[current].location)
                    print("\nplayer", current, "bought", properties[player[current].location]["name"])
                    print("balance:", player[current].balance)

            # if player is on an owned utility, pay rent
            elif properties[player[current].location]["owner"] != current:
                print("\nowned utility")
                # if one utility is owned, rent is 4 times dice roll
                if len(player[properties[player[current].location]["owner"]].ownedUT) == 1:
                    utRent = (roll1 + roll2) * 4
                    print("pay rent of", utRent)
                    player[current].balance -= utRent
                    player[properties[player[current].location]["owner"]].balance += utRent
                # if both utilities are owned, rent is 10 times dice roll
                elif len(player[properties[player[current].location]["owner"]].ownedUT) == 2:
                    utRent = (roll1 + roll2) * 10
                    print("pay rent of", utRent)
                    player[current].balance -= utRent
                    player[properties[player[current].location]["owner"]].balance += utRent
                print("\nplayer", current, "paid rent to player", properties[player[current].location]["owner"])
                print("balance:", player[current].balance)

        # taxes
    if player[current].location == 4:
        print("Income tax (pay $200)")
        player[current].balance -= 200
    if player[current].location == 38:
        print("Luxury tax (pay $100)")
        player[current].balance -= 100

    # community chest
    if player[current].location == 2 or player[current].location == 17 or player[current].location == 33:
        comChestDraw = randint(0, 15)
        print("\nCommunity Chest:\n" + str(comChest[comChestCard[comChestDraw]]))
        sleep(1)
        if comChestCard[comChestDraw] == "go":
            player[current].balance += 200
        elif comChestCard[comChestDraw] == "bank":
            player[current].balance += 200
        elif comChestCard[comChestDraw] == "services":
            player[current].balance += 25
        elif comChestCard[comChestDraw] == "opera":
            for count in range(1, players + 1):
                player[count].balance += 50
        elif comChestCard[comChestDraw] == "school":
            player[current].balance -= 150
        elif comChestCard[comChestDraw] == "insurance":
            player[current].balance += 100
        elif comChestCard[comChestDraw] == "stock":
            player[current].balance += 50
        elif comChestCard[comChestDraw] == "inherit":
            player[current].balance += 100
        elif comChestCard[comChestDraw] == "doctor":
            player[current].balance -= 50
        elif comChestCard[comChestDraw] == "repairs":
            for prop in range(0, 40):
                if properties[prop]["owner"] == current:
                    player[current].balance -= 40 * properties[prop]["houses"] - 115 * properties[prop]["hotels"]
        elif comChestCard[comChestDraw] == "contest":
            player[current].balance += 10
        elif comChestCard[comChestDraw] == "income":
            player[current].balance += 20
        elif comChestCard[comChestDraw] == "xmas":
            player[current].balance += 100
        elif comChestCard[comChestDraw] == "hospital":
            player[current].balance -= 100
        elif comChestCard[comChestDraw] == "jail":
            player[current].jail = True

    # chance
    if player[current].location == 7 or player[current].location == 22 or player[current].location == 36:
        chanceDraw = randint(0, 14)
        print("\nChance:\n" + str(chance[chanceCard[chanceDraw]]))
        if chanceCard[chanceDraw] == "go":
            player[current].balance += 200
        elif chanceCard[chanceDraw] == "broadwalk":
            player[current].location = 39
        elif chanceCard[chanceDraw] == "illinois":
            player[current].location = 24
        elif chanceCard[chanceDraw] == "charles":
            if player[current].location > 11:
                player[current].balance += 200
            player[current].location = 11
        elif chanceCard[chanceDraw] == "reading":
            if player[current].location > 5:
                player[current].balance += 200
            player[current].location = 5
        elif chanceCard[chanceDraw] == "railroad":
            if player[current].location > 5:
                player[current].location = 15
            elif player[current].location > 15:
                player[current].location = 25
            elif player[current].location > 25:
                player[current].location = 35
            elif player[current].location > 35:
                player[current].location = 5
            if properties[player[current].location]["owner"] == "none":
                print("\nUnowned railroad")
                buy = input("buy for " + str(properties[player[current].location]["price"]) + "? " + "[y/(n)]: ")
                if buy == "y":
                    player[current].balance -= properties[player[current].location]["price"]
                    properties[player[current].location]["owner"] = current
                    player[current].ownedRR.append(player[current].location)
                    print("\nplayer", current, "bought", properties[player[current].location]["name"])
                    print("balance:", player[current].balance)
            elif properties[player[current].location]["owner"] != current:
                player[current].balance -= properties[player[current].location]["rent"] * 2
                player[properties[player[current].location]["owner"]].balance += properties[player[current].location]["rent"] * 2
            sleep(1)
        elif chanceCard[chanceDraw] == "utility":
            if player[current].location > 12:
                player[current].location = 28
            elif player[current].location > 28:
                player[current].location = 12
            if properties[player[current].location]["owner"] == "none":
                print("\nUnowned utility")
                buy = input("buy for " + str(properties[player[current].location]["price"]) + "? " + "[y/(n)]: ")
                if buy == "y":
                    player[current].balance -= properties[player[current].location]["price"]
                    properties[player[current].location]["owner"] = current
                    player[current].ownedUT.append(player[current].location)
                    print("\nplayer", current, "bought", properties[player[current].location]["name"])
                    print("balance:", player[current].balance)
            elif properties[player[current].location]["owner"] != current:
                roll1 = randint(1, 6)
                roll2 = randint(1, 6)
                player[current].balance -= (roll1 + roll2) * 10
                player[properties[player[current].location]["owner"]].balance += (roll1 + roll2) * 10
                print("\ndice roll:", roll1, roll2)
                print("\nplayer", current, "paid rent to player", properties[player[current].location]["owner"])
        elif chanceCard[chanceDraw] == "back3":
            player[current].location -= 3
        elif chanceCard[chanceDraw] == "bank":
            player[current].balance += 50
        elif chanceCard[chanceDraw] == "mature":
            player[current].balance += 150
        elif chanceCard[chanceDraw] == "poor":
            player[current].balance -= 15
        elif chanceCard[chanceDraw] == "chairman":
            for count in range(1, players + 1):
                player[count].balance += 50
        elif chanceCard[chanceDraw] == "repairs":
            for prop in range(0, 40):
                if properties[prop]["owner"] == current:
                    player[current].balance -= (25 * properties[prop]["houses"] + 100 * properties[prop]["hotels"])
        elif chanceCard[chanceDraw] == "jail":
            player[current].jail = True
        elif chanceCard[chanceDraw] == "jailFree":
            player[current].jailFree = True

    # go to jail from "go to jail" space or 3 doubles in a row
    if player[current].location == 30 or player[current].doubles == 3 or player[current].jail:
        player[current].location = 10
        player[current].doubles = 0
        player[current].jail = True
        print("\nplayer", current, "is in jail")

    # bail choice
    if player[current].jail:
        bail = input("roll doubles(d) or pay(p) or use \"get out of jail free\" to bail? [d/p/f/(n)]: ")
        # roll doubles
        if bail == "d":
            roll1 = randint(1, 6)
            roll2 = randint(1, 6)
            print("dice roll:", roll1, roll2, "=", roll1 + roll2)
            if roll1 == roll2:
                player[current].jail = False
                player[current].doubles = 0
                print("\nplayer", current, "bailed\nbalance: ", player[current].balance)
        # pay $50 bail
        if bail == "p":
            player[current].balance -= 50
            player[current].jail = False
            print("\nplayer", current, "bailed")
        if bail == "f":
            if player[current].jailFree:
                player[current].jail = False
                print("\nplayer", current, "bailed")
            else:
                print("\nplayer", current, "does not have \"get out of jail free\"")

    # next turn
    if current > 0:
        input("\nnext turn...")
    current += 1
    if current > players:
        current = 1
