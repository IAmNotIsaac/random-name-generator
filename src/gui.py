import tkinter as tk
import generator as gen

from tkinter import ttk


class App(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()

		self.create_widgets()
	

	def create_widgets(self):
		self.name_list = tk.Listbox(self)
		consonant_listbox = tk.Listbox(self)
		vowel_listbox = tk.Listbox(self)
		gen_button = tk.Button(self, text="Generate Name", command=self.generate_name)
		
		consonant_listbox.insert(0, str(gen.CONSONANTS)[1:-1], str(gen.CONSONANTS_DIGRAPHS_INITIAL)[1:-1], str(gen.CONSONANTS_DIGRAPHS_FINAL)[1:-1])
		vowel_listbox.insert(0, str(gen.VOWELS)[1:-1], str(gen.VOWELS_DIGRAPHS)[1:-1])
		
		consonant_listbox.grid(column=0, row=0)
		vowel_listbox.grid(column=1, row=0)
		gen_button.grid(column=0, row=1, columnspan=2)
		self.name_list.grid(column=0, row=2, columnspan=2)
	

	def generate_name(self):
		names = []
		
		for i in range(10):
			name = gen.generate_name()
			name = name.capitalize()[0] + name[1:]
			names.append(name)
		
		self.name_list.delete(0, "end")

		for name in names:
			self.name_list.insert(0, name)



WINDOW_SIZE = (1280, 720)


def setup():
	root = tk.Tk()

	root.geometry(f"{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}")

	app = App(root)

	root.mainloop()


setup()