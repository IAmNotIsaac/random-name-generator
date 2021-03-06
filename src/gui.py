import tkinter as tk
import generator as gen

from tkinter import ttk

class App(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()

		self.create_widgets()
	
	def create_widgets(self):
		self.name_list = tk.Listbox(self, yscrollcommand=set(), width=30)
		self.syl_name_list = tk.Listbox(self, yscrollcommand=set(), width=30)
		consonant_box = tk.Text(self, wrap="word", yscrollcommand=set(), width=30)
		vowel_box = tk.Text(self, wrap="word", yscrollcommand=set(), width=30)
		gen_button = tk.Button(self, text="Generate Name", command=self.generate_name)

		#Create the consonant box
		consonant_box.insert(1.0, str(gen.CONSONANTS)[1:-1])
		consonant_box.insert(2.0, str(gen.CONSONANTS_DIGRAPHS_INITIAL)[1:-1])
		consonant_box.insert(3.0, str(gen.CONSONANTS_DIGRAPHS_FINAL)[1:-1])
		consonant_box.grid(column=0, row=0)

		#Create the vowel list box
		vowel_box.insert(1.0, str(gen.VOWELS)[1:-1], str(gen.VOWEL_DIGRAPHS)[1:-1])
		vowel_box.grid(column=1, row=0)

		#Create the "Generate Name" button
		gen_button.grid(column=0, row=1, columnspan=2)

		#Create the name list box
		self.name_list.grid(column=0, row=2)

		#Create a name list box with syllable spacing
		self.syl_name_list.grid(column=1, row=2)
	
	def generate_name(self):
		names = []
		names_spaced = []
		
		for i in range(10):
			#name = gen.generate_name()
			name, name_spaced = gen.generate_name()
			print(name)
			#print(type(name))
			print(name_spaced)
			#print(type(name_spaced))
			names.append(name)
			names_spaced.append(name_spaced)
		
		self.name_list.delete(0, "end")
		self.syl_name_list.delete(0, "end")

		for name in names:
			self.name_list.insert(0, name)

		for name_spaced in names_spaced:
			self.syl_name_list.insert(0, name_spaced)

def setup():
	root = tk.Tk()

	app = App(root)

	app.master.title("Random Name Generator")
	app.master.maxsize(1280, 720)

	root.mainloop()


setup()
