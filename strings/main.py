# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# Players that scored
Ruud_Gullit_32 = 'Ruud Gullit'
Marco_van_Basten_54 = "Marco van Basten"

# Minute each goal was made
goal_0 = 32
goal_1 = 54
scorers = Ruud_Gullit_32 + ' ' + str(goal_0) + ", " + Marco_van_Basten_54 + ' ' + str(goal_1)

# Fstring with variables
report = f"{Ruud_Gullit_32} scored in the {goal_0}nd minute\n{Marco_van_Basten_54} scored in the {goal_1}th minute"

# Part 2
player = "Frank Rijkaard"
# slicing a[start:stop:step]
# a[::-1]  << this is reverse slicing

first_name = player[:player.find(' ')]
last_name = player[player.find(' ')+1:]

first_name_len = len(first_name)
last_name_len = len(last_name)

name_short = player[0] + '. ' + last_name

# to remove whitespace right side with rstrip(), left side with lstrip() and both sides with strip()

chant = (first_name + "! ") * first_name_len
chant = f"{chant.rstrip()}"


good_chant = chant != str("Frank! Frank! Frank! Frank! Frank! ")