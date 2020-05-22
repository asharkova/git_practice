letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
# Using a list comprehension and zip, create a dictionary called letter_to_points that has the elements of letters as the keys and the elements of points as the values.
letters += [letter.lower() for letter in letters]
points *= 2

letter_to_points = {letters:points for letters, points in zip(letters, points)}

# Our letters list did not take into account blank tiles. Add an element to the letter_to_points dictionary that has a key of " " and a point value of 0.
letter_to_points[""] = 0

# We want to create a function that will take in a word and return how many points that word is worth.
def score_word(word):
  point_total = 0
  for char in word:
    point_total += letter_to_points.get(char, 0)
  return point_total

# Let's test this function!   
brownie_points = score_word("BROWNIE")
print(brownie_points)

# Score a Game
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"],  "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
player_to_points = {}
def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points


### Extra
# A function that would take in a player and a word, and add that word to the list of words they've played
def play_word(player, word):
  player_to_words[player].append(word)
  update_point_totals()
  
play_word("player1", "code")
print(player_to_words)
print(player_to_points)
