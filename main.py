#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the Tip calculator")
total =  float(input("What was the total bill? $"))
tip = int(input("How much percentage tip would you like to give 10, 12, or 15? "))
pesp = int(input("How many people will split the bill? "))
b_w_t = tip / 100 * total + total
b_w_t /= pesp
spbill = round(b_w_t, 2)
spbill = "{:.2f}".format(b_w_t)
print(f"Each person should pay: ${spbill}")