import random as rand


SYLLABLE_TYPES = [
	"CV",	# open
	"VC",	# closed
	"CVC"	# sandwich
]

CONSONANTS = [
	"b", "c", "d",
	"f", "g", "h",
	"j", "k", "l", 
	"m", "n", "p",
	"qu", "r", "s", # 'q' has 'u' attached because like theres 2 words in english where it doesnt
	"t", "v", "w",
	"x", "y", "z",
]

CONSONANTS_DIGRAPHS_INITIAL = [
	"ch", "kn", "ph", "sh",
	"th", "wh", "wr",
]

CONSONANTS_DIGRAPHS_FINAL = [
	"ch", "ck", "sh",
	"ss", "tch", # "cc" ;)
]

VOWELS = [
	"a", "e", "i", "o", "u"
]

VOWELS_DIGRAPHS = [
	"aa", "ai", "ay", "ae", "aa",
	"ee", "ea", "ei",
	"ie",
	"oo", "oa", "oe",
	"uu", "ue", "ui",
]

SYLLABLE_RANGE = {
	"min": 2,
	"max": 5,
}


def generate_name() -> str:
	name = ""

	# syllable pattern
	syl_patterns = []

	r = rand.randrange(SYLLABLE_RANGE["min"], SYLLABLE_RANGE["max"])
	
	for i in range(r):
		syl_patterns.append(SYLLABLE_TYPES[rand.randrange(0, len(SYLLABLE_TYPES) - 1)])
	
	# match syl pattern and push to name
	last_char = ""

	for pattern in syl_patterns:
		i = 0
		for char_type in pattern:
			# determine which consonent to use
			if char_type == "C":
				if not i:
					while True:
						table = [CONSONANTS, CONSONANTS_DIGRAPHS_INITIAL][rand.randrange(0, 1)]
						new_char = table[rand.randrange(0, len(table) - 1)]

						if new_char[0] != last_char:
							last_char = new_char[-1]
							name += new_char

							break
				
				else:
					while True:
						table = [CONSONANTS, CONSONANTS_DIGRAPHS_FINAL][rand.randrange(0, 1)]
						new_char = table[rand.randrange(0, len(table) - 1)]

						if new_char[0] != last_char:
							last_char = new_char[-1]
							name += new_char

							break
			
			# determine which vowel to use
			if char_type == "V":
				table = [VOWELS, VOWELS_DIGRAPHS][rand.randrange(0, 1)]
				name += table[rand.randrange(0, len(table) - 1)]
		
			i += 1
	
	return name