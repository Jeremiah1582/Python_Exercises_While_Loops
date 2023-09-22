# Note: there are many ways to solve this challenge

# ......................code here.................
# get user input
temp_input = input("Enter the current room temperature") #returns input as string 
temp = int(temp_input) # change string to integer (**casting**)

if temp>20 and temp<25:
        print("GOOOODD !!! Temperature is within comfort range.", temp )
else:
    while temp<20: # While loop for continuous temp monitoring
        # Check and adjust temperature
        if temp < 20:
            temp +=1
            print("Heating up to 20 degrees for comfort.", temp)

    while temp>25:
        if temp>25:
            temp-=1 
            print("Cooling down to 25 degrees for comfort.", temp)
        
        
# .....................code here ...................
# remember: 
# 1) be aware of where you place your conditions, placing a condition in the wrong place can prevent the computer from ever reading it
# 2) while loops must eventually meet a false condition to prevent the infinite loop