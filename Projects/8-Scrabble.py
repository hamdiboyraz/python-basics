letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters +=[i.lower() for i in letters]
print(letters)
points *=2
print(points)

letter_to_points = {i:k for i,k in zip(letters,points)}
print(letter_to_points)
letter_to_points[" "] = 0
def score_word(word):
    point_total = 0
    for i in word:
        point_total += letter_to_points.get(i,0)
    return point_total
brownie_points = score_word("BROWNIE")
print(brownie_points)
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"],
                   "wordNerd": ["EARTH", "EYES", "MACHINE"],
                   "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
                   "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
print(player_to_words)
player_to_points = {}

for k,v in player_to_words.items():
    print(k,v)
    player_points = 0
    for word in v:
        player_points += score_word(word)
        player_to_points[k] = player_points
    print(player_points)
print(player_to_points)

def play_word(player, word):
    player_to_words[player].append(word)
    for k, v in player_to_words.items():
        print(k, v)
        player_points = 0
        for word in v:
            player_points += score_word(word)
            player_to_points[k] = player_points
        print(player_points)
    print(player_to_points)

play_word("player1","CODE")

############################################ BAŞKA ALTERNATİF KOD #####################################################
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters +=[i.lower() for i in letters]
print(letters)
points *=2
print(points)

letter_to_points = {i:k for i,k in zip(letters,points)}
print(letter_to_points)

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"],
                   "wordNerd": ["EARTH", "EYES", "MACHINE"],
                   "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
                   "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
print(player_to_words)

letter_to_points[" "] = 0
def score_word(word):
    point_total = 0
    for i in word:
        point_total += letter_to_points.get(i,0)
    return point_total

player_to_points = {}
def play_word(player, word):
  if player in player_to_words.keys():
    player_to_words[player].append(word)
    for k, v in player_to_words.items():
      player_points = 0
      for word in v:
        player_points += score_word(word)
        player_to_points[k] = player_points


  else:
    player_to_words[player] = word
    for k, v in player_to_words.items():
      player_points = 0
      for word in v:
        player_points += score_word(word)
        player_to_points[k] = player_points

  return player_to_words,player_to_points

print(play_word("ahmet","selaaam"))


