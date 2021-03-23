# REVIEWING LOOPS



#-----> GENERAL STUCTURE OF FOR LOOPS USING A COLLECTION:

    # for <temporary variable> in <collection>:
    #       <action>

    # A for keyword indicates the start of a for loop.
    # A <temporary variable> that is used to represent the value of the element in the collection the loop is currently on.
    # An in keyword separates the temporary variable from the collection used for iteration.
    # A <collection> to loop over. In our examples, we will be using a list.
    # An <action> to do anything on each iteration of the loop.



# Write a for loop that prints each sport and game in the lists:

board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
  print(game)

for sport in sport_games:
  print(sport)


# Add students from list A to list B:

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  students_period_B.append(student)
  print(student)
  
print(students_period_B)



#------> GENERAL STRUCTURE OF FOR LOOPS USING A RANGE FUNCTION

    # for <temporary variable> in <list of length 6>:
    #   print("Learning Loops!")

    # Notice temp variable is not used in the function body but we can use temp + 1 to see how many iterations.

    # We use range directly in our for loops as the collection to perform a number of given steps.



# Print out the provided promise five times:

promise = "I will finish the python loops module!"

for sentence in range(5):
  print(promise)



#-----> GENERAL STRUCTURE FOR A WHILE LOOP:

    # while <conditional statement>:
    #   <action>

    # count = 0
    # while count <= 3:
    # # Loop Body
    # print(count)
    # count += 1


    # Similar to for loops, Python allows us to write elegant one-line while loops. Here is our previous example in a single line:

    # count = 0
    # while count <= 3: print(count); count += 1

    # Note: Here we separate each statement with a ; to denote a separate line of code.



# Complete a countdown and Liftoff sequence

countdown = 10

while countdown >= 0:
  print(countdown)
  countdown -= 1
print("We have liftoff!")



# -----> GENERAL STURCTURE OF WHILE LOOPS WITH LISTS

    # We can use while loops to iterate through a list
    # We can then use this length in addition to another variable to construct the while loop:
    
    # length = len(ingredients)
    # index = 0
 
    # while index < length:
    # print(ingredients[index])
    # index += 1



# Iterate over the list and print out topics

python_topics = ["variables", "control flow", "loops", "modules", "classes"]
# NOTE: It's like javascript forloop and while loop takes a takes a start and stop, but the iteration part is added manually later in the code, after the action is taken.
#Your code below: 

length = len(python_topics)
index = 0

while index < length:
  print(f"I am learning about {python_topics[index]}")
  index +=1



    #-----> GENERAL STUCTURE FOR LOOP CONTROL: BREAK

    # When the program hits a break statement it immediately terminates a loop.
    # It’s often the case that we want to search a list to check if a specific value exists. But once it's found we don't want to waste resources checking the rest of the items in the list.

    # items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]
    # for item in items_on_sale:
    #   if item == "knit dress":
    # print("Found it")

# Search for the dog bread you want, then use break to stop the loop:

dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]

dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    
    break


 #-----> GENERAL STUCTURE FOR LOOP CONTROL: CONTINUE
    
    # Used to skip the current iteration/index in the loop. The following skips iterations less than 1 and outputs positive numbers.

    #Continue is usually paired with a conditional (if/else/elif)

    # big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
    # for num in big_number_list:
    #   if num <= 0:
    #     continue
    #   print(num)

# If an entry is less than 21 skip it and move on to the next entry, otherwise print age.


ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for i in ages:
  if i < 21:
    continue
  print(i)



#-----> NESTED LOOPS

    # We may want to access data inside a nested loop
    # We must iterate over the outer loop, then the inner loop

    # project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]
    # # Loop through each sublist
    # for team in project_teams:
    #     # Loop elements in each sublist
    #     for student in team:
    #         print(student)


# Iterate over the nested loop and caluclate the total scoop sales.

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  for sale in location:
    scoops_sold += sale
  print(location)
print(scoops_sold)


#-----> GENERAL STRUCTURE FOR LIST COMPREHENSION

    # new_list = [<expression> for <element> in <collection>]

    # numbers = [2, -1, 79, 33, -45]
    # doubled = [num * 2 for num in numbers]
    # print(doubled)

# Scale grades based on highest score:

grades = [90, 88, 62, 76, 74, 89, 48, 57]

scaled_grades = [grade + 10 for grade in grades]

print(scaled_grades)

#-----> GENERAL STRUCTURE FOR LIST COMPREHENSION WITH CONDITIONALS:

    # numbers = [2, -1, 79, 33, -45]
    # negative_doubled = [num * 2 for num in numbers if num < 0]
    # print(negative_doubled)


    # If there is more than one condition, such as an else, it all comes before the for loop. 

    # numbers = [2, -1, 79, 33, -45]
    # doubled = [num * 2 if num < 0 else num * 3 for num in numbers ]
    # print(doubled)


#If a rider is taller than 161 centimeters thy can ride the ride. Print a list for those that can ride:

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]

print(can_ride_coaster)



# -----> FINAL REVIEW <---------


# Create a list that consists of numbers 0 to 9
single_digits = range(0, 10)

# Loop through single_digits
for digit in single_digits:
  print(digit)

# square each digit in the list and return list
squares = []
for digit in single_digits:
  print(digit)
  squares.append(digit ** 2)
print(squares)

# List comprehension to the third power
cubes = [digit ** 3 for digit in single_digits]
print(cubes)