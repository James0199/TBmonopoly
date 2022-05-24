# monopoly
from random import randint
from time import sleep


class stats:
    def __init__(self, location, balance, jail, jailFree, doubles):
        self.location = location
        self.balance = balance
        self.jailFree = jailFree
        self.jail = jail
        self.doubles = doubles


player = {}
for count in range(1, 7):
    player.update({count: stats(0, 1500, False, False, 0)})
# select number of players
players = int(input("Number of players:"))
if players > 8:
    players = 8
if players < 2:
    players = 1
current = 1

# community chest
comChest = {"go": "Advance to Go\n(Collect $200)",
            "bank": "Bank error in your favor\nCollect $200",
            "services": "Receive\nfor services $25",
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
properties = {0: "Go",
              1: "Mediterranean Avenue",
              2: "Community Chest",
              3: "Baltic Avenue",
              4: "Income Tax",
              5: "Reading Railroad",
              6: "Oriental Avenue",
              7: "Chance",
              8: "Vermont Avenue",
              9: "Connecticut Avenue",
              10: "Just Visiting",
              11: "St. Charles Place",
              12: "Electric Company",
              13: "States Avenue",
              14: "Virginia Avenue",
              15: "Pennsylvania Railroad",
              16: "St. James Place",
              17: "Community Chest",
              18: "Tennessee Avenue",
              19: "New York Avenue",
              20: "Free Parking",
              21: "Kentucky Avenue",
              22: "Chance",
              23: "Indiana Avenue",
              24: "Illinois Avenue",
              25: "B. & O. Railroad",
              26: "Atlantic Avenue",
              27: "Ventnor Avenue",
              28: "Water Works",
              29: "Marvin Gardens",
              30: "Go To Jail",
              31: "Pacific Avenue",
              32: "North Carolina Avenue",
              33: "Community Chest",
              34: "Pennsylvania Avenue",
              35: "Short Line",
              36: "Chance",
              37: "Park Place",
              38: "Luxury Tax",
              39: "Boardwalk"}

while True:
    sleep(2)
    # player stats
    print("\n\nplayer", current, "turn")
    print("location:", player[current].location, "-", properties[player[current].location],
          "\nbalance:", player[current].balance)
    sleep(1)

    if not player[current].jail:
        # roll dice
        roll1 = randint(1, 6)
        roll2 = randint(1, 6)
        player[current].location += + roll1 + roll2
        print("\ndice roll:", roll1, roll2, "=", roll1 + roll2)
        sleep(1)
        # doubles count, 3 doubles in a row, go to jail
        if roll1 == roll2:
            player[current].doubles += 1
        else:
            player[current].doubles = 0

        # passes go, collects $200
        if player[current].location >= 40:
            player[current].location -= 40
            player[current].balance += 200
            print("\nlocation:", player[current].location)
            print("passes go, collects $200")

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
        print("\nCommunity Chest:\n", comChest[comChestCard[comChestDraw]])
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
            pass
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
        print("\nChance:\n", chance[chanceCard[chanceDraw]])
        sleep(1)
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
            pass
        elif chanceCard[chanceDraw] == "utility":
            pass
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
            pass
        elif chanceCard[chanceDraw] == "jail":
            player[current].jail = True
        elif chanceCard[chanceDraw] == "jailFree":
            player[current].jailFree = True

    # Use "Get out of jail free" card
    if player[current].jailFree:
        player[current].jailFree = False
        player[current].jail = False
        print("\nYou have used your \"Get out of jail free\" card")
        sleep(1)
    # go to jail from "go to jail" space or 3 doubles in a row
    if player[current].location == 30 or player[current].doubles == 3 or player[current].jail:
        player[current].location = 10
        player[current].doubles = 0
        player[current].jail = True
        print("\nplayer", current, "is in jail")
    # bail choice
    if player[current].jail:
        bail = input("roll doubles(d) or pay(p) to bail? (d/p/n):")
        # roll doubles
        if bail == "d":
            roll1 = randint(1, 6)
            roll2 = randint(1, 6)
            print("dice roll:", roll1, roll2, "=", roll1 + roll2)
            if roll1 == roll2:
                player[current].jail = False
                player[current].doubles = 0
                print("\nplayer", current, "bailed")
        # pay $50 bail
        if bail == "p":
            player[current].balance -= 50
            player[current].jail = False
            print("\nplayer", current, "bailed")

    # advance to next turn
    current += 1
    if current > players:
        current = 1
