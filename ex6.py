name = input("What is your name? ")
age = int(input("How old are you? "))
height = int(input("How tall are you in inches? "))
weight = int(input("How heavy are you in pounds? "))
eyecolour = input("What colour are your eyes? ")
haircolour = input("What colour is your hair? ")

weight = weight * 0.454 # convert to kilos
height = height * 0.0254 # convert to metres

print("How's it going? You are", name + ", you've been around for", age, "years.")
print("Your BMI is", weight/height**2 + ", 30 and above is obese.")
