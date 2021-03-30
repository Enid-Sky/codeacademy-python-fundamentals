# SCRABBLE GAME

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# TALLY THE SCORE OF EACH SCRABBLE WORD

# create a dictionary using the lists letters and points.
letters_to_points = dict(zip(letters, points))


# Add an element to the dictionary with and empty key and value of 0:
letters_to_points[" "] = 0
print(letters_to_points)

#create a function that will take in a word and return how many points that word is worth. If the word does not exist add 0 to the point total. 

def score_word(word):
  point_total = 0

  for letter in word:
    letter_in_dict = letters_to_points.get(letter, 0)
    if letter_in_dict == 0:
      point_total += 0
    else:
      point_total += letters_to_points[letter]
  return point_total

brownie_points = score_word("BROWNIE")
print(f"The total for the word is: {brownie_points}")


# Create a dictionary from scrated with given players and their scrabble words:
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

# Create an empty dictionary for player points

player_to_points = {}
# loop over players and their list of words
for player, words in player_to_words.items():
  player_points = 0
  #Now loop over each word in each players' word list
  for word in words: 
    player_points += score_word(word)
    player_to_points[player] = player_points
print(f"The total for each player is: {player_to_points}")






