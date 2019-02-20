name = "Yolanda"
print("Hello {}!".format(name))



name = "Yolanda"
name = name.upper()
print("Hello {}!".format(name))



print("What's your name?")
name = input()
print("Hello {}!".format(name))



# function body
def calculate_mean(number1, number2):
  answer = (number1 + number2) / 2
  print("The mean of {} and {} is {}.".format(number1, number2, answer))

# run function for different number pairs
calculate_mean(5, 10)
calculate_mean(1, 11)
calculate_mean(1, 12)



# function body
def welcome_user(name, location):
    print("Hi {} from {}!".format(name, location))

# run function for different names and locations
welcome_user("Yolanda", "London")
welcome_user("Yukey", "Manchester")
welcome_user("Harper", "Sheffield")
