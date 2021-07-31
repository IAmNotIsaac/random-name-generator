import random as rand

# The English language has 6 syllable types: 
# Open, Closed, R-controlled, Vowel Team, Silent-e, and C-le.
SYLLABLE_TYPES = [
	"V",	# open
	"VC",	# closed
	"VV",	# vowel team
	"VR",	# r controlled
	"VCE",	# silent e
	"CL",	# consonant plus le (end of word only)
]

CONSONANTS = [
	"b", "c", "d",
	"f", "g", "h",
	"j", "k", "l", 
	"m", "n", "p",
	"q", "r", "s", 
	"t", "v", "w",
	"x", "z",
]

CONSONANTS_DIGRAPHS_INITIAL = [
	"ch", "kn", "ph", "sh",
	"th", "wh", "wr", "sc",
	"fr", "y", "bl", "br", "cl",
	"cr", "dr", "fl", "fr", "gl", "gr",
	"pl", "pr", "sc", "sl", "sm", "sp", "st", "tr",
	"spl", "spr", "str"
]

CONSONANTS_DIGRAPHS_FINAL = [
	"ch", "ck", "sh",
	"ss", "tch", "bl", "br", "cl",
	"cr", "dr", "fl", "fr", "gl", "gr",
	"pl", "pr", "sc", "sl", "sm", "sp", "st", "tr",
	"spl", "spr", "str"
]

VOWELS = [
	"a", "e", "i", "o", "u", "y",
]
VOWEL_TRIPH = [
	"eau", "eou", "iou"
]

VOWEL_DIGRAPHS = [
	"aa", "ai", "ay", "ae",
	"ee", "ea", "ei",
	"ia", "ie",
	"oo", "oa", "oe",
	"uu", "ue", "ui",
]

SYLLABLE_RANGE = {
	"min": 1,
	"max": 4,
}

# Inputs:
#	int num: defining number of vowels to return
#	boolean inc_y: include y or not
def get_vowels(num, inc_y):
	vowel = ""
	if num == 3:
		new_vowel = VOWEL_TRIPH[rand.randint(0, len(VOWEL_TRIPH)-1)]
	elif num == 2:
		new_vowel = VOWEL_DIGRAPHS[rand.randint(0, len(VOWEL_DIGRAPHS)-1)]
	else:
		new_vowel = VOWELS[rand.randint(0, len(VOWELS) - 2 + inc_y)]
	return new_vowel

# Inputs:	
#	boolean pos: Whether the consonant is in initial or final position
#			0: initial
#			1: final
def get_cons(pos):
	consonant = ""
	if pos:
		table = [CONSONANTS, CONSONANTS_DIGRAPHS_INITIAL][rand.randint(0, 1)]
	else:
		table = [CONSONANTS, CONSONANTS_DIGRAPHS_FINAL][rand.randint(0, 1)]
	new_char = table[rand.randint(0, len(table) - 1)]
	consonant += new_char
	return consonant

# An open syllable has only one vowel.
# The vowel is the last letter of the syllable.
# Open syllables have no more than one consonant between the open syllable and the next vowel.
# V, CV, 
def gen_open(pos, word):
	syl = ""
	vowel_select = get_vowels(1, 1)
	if rand.randint(0, 1):
		syl += get_cons(True)
	syl += vowel_select
	return syl

# A closed syllable has only one vowel.
# If the word is only 2 letters, it must end with a consonant.
# If the word is 3+ letters, a closed syllable has 1 consonant before and 1 (or more) consonants after the vowel.
# If a word has 2 closed syllables next to each other, there will be two consonants between the vowels.
# I think there can be a silent e at the end as well
def gen_closed(pos, word):
	syl = ""
	vowel_select = get_vowels(1, 1)
	if len(word) == 1:
		syl += vowel_select
		syl += get_cons(False)
	else:
		syl += get_cons(True)
		syl += vowel_select
		syl += get_cons(False)
# I think there can be a silent e at the end as well
	return syl

# A group of 2 to 4 letters, usually vowels, which make a single vowel sound.
# VV, CVV, VVC, CVVC
def vowel_team(pos, word):
	syl = ""
	vowel_select = get_vowels(2,1)
	format = rand.randint(0, 3)
	if format:
		if format % 2 == 1:	# Has an initial consonant
			c_sel_a = get_cons(True)
			syl += c_sel_a
		syl += vowel_select
		if format > 1: # Has a final consonant
			c_sel_b = get_cons(False)
			syl += c_sel_b
	else:
		syl += vowel_select
	return syl

# A vowel, diphthong, or triphthong that has an "r" or a "re" ("r" with a silent "e") after it.
# CVr or Vr
def r_controlled(pos, word):
	syl = ""
	if rand.randint(0, 1):
		syl += get_cons(False)
		syl += get_vowels(rand.randint(1, 3), 1)
	else:
		syl += get_vowels(rand.randint(1, 3), 0)
	syl += "r"
	if rand.randint(0, 1):
		syl += "e"
	return syl

# The silent-e syllable is also called VCe, which stands for Vowel-Consonant-e.
# It consists of a vowel, followed by a consonant, followed by an "e" that is silent.
# VCe
def gen_sil_e(pos, word):
	syl = ""
	syl += get_vowels(1, 0)
	syl += get_cons(False)
	syl += "e"
	return syl

# The C-le syllable is also called the Consonant-le.
# It consists of a consonant followed by an "le."
# It's usually the last syllable in a root word.
# Does the word end with 'ckle'?
# Divide right before the 'le.'
# Does the word end with 'le' (not 'ckle')?
# Is the letter before the 'le' a consonant?
# Divide 1 letter before the 'le.'
# Is the letter before the 'le' a vowel?
# Do nothing.
# C le
def c_le(pos, word):
	syl = "le"
	return syl

syl_types = {	0 : gen_open,
           		1 : gen_closed,           		
           		2 : vowel_team,
           		3 : r_controlled,
				4 : gen_sil_e,
           		5 : c_le,
}

# Should capitalise if it's the first syllable
# First syllable if n = 0
def generate_name():
#def generate_name() -> str:
	name = ""
	name_spaced = ""
	name_new = ""

	# syllable pattern
	syl_patterns = []
	# syllable pattern with numerated definitions
	syl_numerate = []

	# Choose number of syllables
	r = rand.randrange(SYLLABLE_RANGE["min"], SYLLABLE_RANGE["max"])
	print("=========================")	
	print("Number of syllables: ", r)
	
	for i in range(r):
		if i < r-1:	# This is because "Cle" and silent e can only come at the of a word 
			c = rand.randint(0, len(SYLLABLE_TYPES) - 3)
		else:
			c = rand.randint(0, len(SYLLABLE_TYPES) - 1)
		if r == 1 and c == 5: # Only one syllable and it's "le"
			c = rand.randint(0, len(SYLLABLE_TYPES) - 2)
		syllable = SYLLABLE_TYPES[c]
		syl_patterns.append(syllable)
		syl_numerate.append(c)
		print("\t--------\n\ti: ", i, " ", c, "\t", syl_types[c].__name__)

	print("Pattern: ", syl_numerate)

	# match syl pattern and push to name
	last_char = ""

	for n, s in enumerate(syl_numerate):
		syl = syl_types[s](s, syl_numerate)
		print("213 syl:", syl)
		if n == 0:
			syl = syl.capitalize()
		name_new += syl
		name_spaced += syl
	# Need something to divide off le properly
		if not n is r-1:
			name_spaced += "."
		else:
			# Do some stuff in here to break the syllables given the rules
			# In the comment above c_le
			temp = 0
	print(name_new)
	print(type(name_new))
	

	"""
	for n, pattern in enumerate(syl_patterns):
		i = 0
		print("Pattern:\t", pattern)
		for char_type in pattern:
			# determine which consonant to use
			if char_type == "C":
				if not i:		#Is the first character in the syllable
					#print("if not i:\t", i)
					while True:
						#Choose a random item from the consonant table
						table = [CONSONANTS, CONSONANTS_DIGRAPHS_INITIAL][rand.randint(0, 1)]
						print("Table:\t", table)
						print(type(table))
						new_char = table[rand.randrange(0, len(table) - 1)]
						print("New char:\t", new_char)

						if new_char[0] != last_char:
							last_char = new_char[-1]
							name += new_char
							name_spaced += new_char
							break
				
				else:	#Not the first character in the syllable
					#print("Else:\t", i)
					while True:
						#Choose a random item from the consonant table
						table = [CONSONANTS, CONSONANTS_DIGRAPHS_FINAL][rand.randint(0, 1)]
						#print("Table:\t", table)
						new_char = table[rand.randrange(0, len(table) - 1)]
						#print("New char:\t", new_char)

						if new_char[0] != last_char:
							last_char = new_char[-1]
							name += new_char
							name_spaced += new_char
							break
			
			# determine which vowel to use
			if char_type == "V":
				vowel_select = get_vowel(1, 1)
				name += vowel_select
		
			if char_type == "E":
				name += "e"

			i += 1
		print("N and R:\t", n, "\t", r)

		#Spaces between syllables
		if not n is r-1:
			name_spaced += "."
	"""
	
	#print(name)
	#print(type(name))
	#print(name_spaced)
	#print(type(name_spaced)

	return name_new, name_spaced
