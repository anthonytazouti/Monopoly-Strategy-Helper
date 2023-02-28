userinput = input("Enter the name of the SPOT YOU Landed on.").upper()


brown1 = ("MEDITERRANEAN")
brown2 = ("BALTIC")

lightBlue1 = ("ORIENTAL AVENUE")
lightBlue2 = ("VERMONT AVENUE")
lightBlue3 = ("CONNECTICUT AVENUE")

pink1 = ("ST. CHARLES")
pink2 = ("STATES AVENUE")
pink3 = ("VIRGINIA AVENUE")

orange1 = ("ST. JAMES PLACE")
orange2 = ("TENNESSEE AVENUE")
orange3 = ("NEW YORK AVENUE")

red1 = ("KENTUCKY AVENUE")
red2 = ("INDIANA AVENUE")
red3 = ("ILLINOIS AVENUE")

yellow1 = ("ATLANTIC AVENUE")
yellow2 = ("VENTNOR AVENUE")
yellow3 = ("MARVIN GARDENS")

green1 = ("PACIFIC AVENUE")
green2 = ("NORTH CAROLINA")
green3 = ("PENNSYLVANIA AVENUE")

blue1 = ("PARK PLACE")
blue2 = ("BOARDWALK")

trains = ("READING RAILROAD", "PENNSYLVANIA RAILROAD", "B&0 RAILROAD", "SHORT LINE")
utility = ("ELECTRIC COMPANY", "WATER WORKS",)
tax = ("LUXURY TAX", "INCOME TAX")


chest = ("Pick a card.")
incomeTax = ("Pay the tax.")
chance = ("Pick a card.")
jail = ("Go to jain and you also loose a turn :/")
freeParking = ("Take the money in the pot!")
onGo = ("Collect $200.")





if userinput == brown1 or brown2:
    print ("Price: $60")
    print ("-"*25)
    print ("Price to put up a house: $50")
    print ("-"*25)
    print("Is it a good buy?: Not overall, though this board position is cheap it has a terrible position. No chance card is worth it")
elif userinput == lightBlue1 or lightBlue2:
    print ("Price: $100")
    print ("-"*25)
    print ("Price to put up a house: $50")
    print ("-"*25)
    print("Is it a good buy?: This position is 50/50, it's not bad and it is not amazing, take a chance if you feel lucky.")
elif userinput == lightBlue3:
    print ("Price: $120")
    print ("-"*25)
    print ("Price to put up a house: $50")
    print ("-"*25)
    print("Is it a good buy?: Unlike any of the other light blue colors, this is little more worth the investment, You will receive a higher ROI.")
elif userinput == pink1 or pink2:
    print ("Price: $140")
    print ("-"*25)
    print ("Price to put up a house: $100")
    print ("-"*25)
    print("Is it a good buy?: Yes, buy. Very profitable, and has a good position on the board.")
elif userinput == pink3:
    print ("Price: $160")
    print ("-"*25)
    print ("Price to put up a house: $100")
    print ("-"*25)
    print("Is it a good buy?: Yes, buy. Very profitable, and has a good position on the board.")
elif userinput == orange1 or orange2:
    print ("Price: $180")
    print ("-"*25)
    print ("Price to put up a house: $100")
    print ("-"*25)
    print("Is it a good buy?: Yes, Orange is easily the best property in the game, great board position and very profitable.")
elif userinput == orange3:
    print ("Price: $200")
    print ("-"*25)
    print ("Price to put up a house: $100")
    print ("-"*25)
    print("Is it a good buy?: Is it a good buy?: Yes, Orange is easily the best property in the game, great board position and very profitable.")
elif userinput == red1 or red2:
    print ("Price: $220")
    print ("-"*25)
    print ("Price to put up a house: $150")
    print ("-"*25)
    print("Is it a good buy?: Really great board position, invest in these properties.")
elif userinput == red3:
    print ("Price: $240")
    print ("-"*25)
    print ("Price to put up a house: $150")
    print ("-"*25)
    print("Is it a good buy?: Is it a good buy?: Really great board position, invest in these properties.")
elif userinput == yellow1 or yellow2:
    print ("Price: $260")
    print ("-"*25)
    print ("Price to put up a house: $150")
    print ("-"*25)
    print("Is it a good buy?: Pretty average, the board position is just a little out of the way from being decent, very average.")
elif userinput == yellow3:
    print ("Price: $280")
    print ("-"*25)
    print ("Price to put up a house: $150")
    print ("-"*25)
    print("Is it a good buy?: Pretty average, the board position is just a little out of the way from being decent, very average.")
elif userinput == green1 or green2:
    print ("Price: $300")
    print ("-"*25)
    print ("Price to put up a house: $200")
    print ("-"*25)
    print("Is it a good buy?: Bad position, no chance this card benefits. Don't even bother investing.")
elif userinput == green3:
    print ("Price: $320")
    print ("-"*25)
    print ("Price to put up a house: $200")
    print ("-"*25)
    print("Is it a good buy?: Bad position, no chance this card benefits. Don't even bother investing.")
elif userinput == blue1:
    print ("Price: $350")
    print ("-"*25)
    print ("Price to put up a house: $200")
    print ("-"*25)
    print("Is it a good buy?: This is a risky buy, if you invest in this property you have a 50/50 chance of making a lot of money.")
elif userinput == blue2:
    print ("Price: $400")
    print ("-"*25)
    print ("Price to put up a house: $200")
    print ("-"*25)
    print("Is it a good buy?: Is it a good buy?: This is a risky buy, if you invest in this property you have a 50/50 chance of making a lot of money.")
else:
    print("You entered in an invalid Monopoly square name! Try again.")
