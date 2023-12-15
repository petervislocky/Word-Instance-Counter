import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from components.instanceCounter import pdfExtract

#TODO make this whole class. lol

class GUI:

    def __init__(self, master, default_pdfs) -> None:
        self.master = master
        master.title = 'PDF Scanner'

        # GUI components
        self.pdf_combobox = ttk.Combobox(master, values=default_pdfs, state='readonly')
        self.word_entry = tk.Entry(master)
        self.result_text = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.word_count_label = tk.Label(master, text='Word Count:')
        self.show_more_button = tk.Button(master, text='Show More') # add show more command
        self.search_button = tk.Button(master, text='Search') # add search command
        self.clear_button = tk.Button(master, text='Clear') # add clear field command
        
        # Layout
        self.pdf_combobox.pack()
        self.search_button.pack()
        self.word_entry.pack()
        self.result_text.pack()
        self.show_more_button.pack()
        self.word_count_label.pack()
        self.clear_button.pack()

