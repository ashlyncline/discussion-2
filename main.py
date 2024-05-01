# this program walks you through a day after school. You are asked if you have homework, decide what to eat based on your likes and dislikes, make decisions about the weather as you go on a walk, and buy donuts.

print("You get home from school.")

# this section asks for user input to define the variable homework. It tells you to work on your homework if you have it.

homework = input("Do you have any homework? (yes/no): ")

if homework == "yes":
    print("Okay. You can work on it tonight.")
else:
    print("Nice!")
    
print("Now you're hungry. Let's decide what to eat.")

# This section chooses a food based on what you like to eat. It uses the "and" operator to decide if you want a ham and cheese sandwich. If you don't want one,  it will ask if you are allergic to peanut butter. 

ham = input("Do you like ham and cheese sandwiches? (yes/no): ")
mustard = input("Do you like mustard? (yes/no): ")

if ham == "yes" and mustard == "yes":
    print("You eat a ham and cheese sandwich with mustard.")
elif ham == "yes" and mustard == "no":
    print("You eat a ham and cheese sandwich without mustard.")
else: 
    pb = input("Are you allergic to peanut butter? (yes/no): ")
    if pb == "yes":
        print("You eat some cereal.")
    else:
        print("You eat a PB&J.")
    
print("After you eat, you decide to take a walk outside.")

weather = input("What is the weather like outside? (sunny/cloudy/rainy): ")

# This block of code tells you what to bring on your walk based on the weather. If one of the three options is not inputted by the user, the program will print "Invalid input."

if weather == "sunny":
    print("You put sunscreen on before you leave.")
elif weather == "cloudy":
    print("You bring a jacket.")
elif weather == "rainy":
    print("You bring an umbrella.")
else:
    print("Invalid input.")

print("While you're walking, you see a small donut stand and want to buy some donuts for $2 each.")

# This section determines how many $2 donuts you can buy based on the money that you have. It uses integer division so you can only purchase whole donuts. There is also a limit on how mnay donuts you can buy.

money = float(input("How much money do you have? "))

donutTotal = money//2

if donutTotal < 1:
    print("You don't have enough money to buy a donut. ")
elif donutTotal > 150:
    print("You have enough money to buy " + str(donutTotal) + " donuts, but the stand does not have that many, so you buy 150.")
else:
    print("You buy " + str(donutTotal) + " donuts.")

# This block of code refers back to the homework variable. If homework == "yes" then it will ask you when it is due. Otherwise, it wishes you a good night.

print("You walk back to your house.")
if homework == "yes":
    due = input("Is your homework due tonight? (yes/no): ")
    if due == "yes":
        print("You should start working on it!")
    else: 
        print("You don't have to do it tonight, but it is always a good idea to get ahead! Enjoy your evening!")
else: 
    print("Enjoy your evening!")
    
    
    
