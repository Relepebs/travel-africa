def traveled(x):
  return x+500
#while traveled("0Km","1000Km","2500Km"):
  BNG =input ("1. Look at map  \n2. Start Journey \n3. Buy supplies  \n4.END")
GAME = True
SPU = 0
GA = 2
TRV = 500
AP = 0
countrylist = ["start", "Cairo,Egypt","Al Fashir,Sudan", "Juba,South Sudan", "Addis Abba,Ethiopia", "Nairobi,Kenya", "Mbeya,Tanzania", "Beira,Mozambique", "Maputo,Swaziland", "Destination-Johanesburg,South Africa"]
location = 0
while GAME:
  print("Welcome to the Africa Tour. \nYou will be traveling from Cairo,Egypt to Johannesburg,South Africa" )
  print("You should not run out of supplies before you reach your destination or you lose")
  BNG =input ("1. Look at map  \n2. Start Journey \n3. Buy supplies  \n4. END \n5. Check supplies\n")
  if BNG == ("4"):
    GAME = False 
  if BNG == ("1"):
    print("\nCountries: \nEgypt \nSudan \nSouth Sudan \nEthiopia \nKenya \nTanzania \nMozambique \nSwaziland \nDestination-South Africa\n")
  if BNG == ("2"):
    location += 1
    SPU += TRV
    GA -=1
    print("\nYou have arrived to:", countrylist[location]) 
    print("Traveled:", SPU,"Km\n")
  if BNG == ("3"): 
    AP = int(input("How many supplies would you like to buy? \nMax is 3"))
    print("\nYou have bought supplies\n")
    if AP < 4:
     GA += AP
  if GA < 1:
    print("lose")
    GAME = False 
  if BNG == ("4"):
    print("This is the END of your African Journey")
  if BNG == ("5"):
    print("\nYou have", GA, "amount of supplies\n")
  if location == 8:
    print("Congradulations you have arrived to Johannesburg!")
    GAME = False
