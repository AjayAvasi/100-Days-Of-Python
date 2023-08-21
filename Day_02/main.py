print("Welcome to the tip calculator!")
total = float(input("What was the total bill? ").replace("$",""))
tip = int(input("How much tip would you like to give? 10, 12, or 15? ").replace("%",""))
people = int(input("How many people to split the bill? "))

print(f"Each person must pay ${round(total*(1+tip/100)/people,2)}")