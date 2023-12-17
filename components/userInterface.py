from tkinter import scrolledtext
from tkinter import ttk
from instanceCounter import pdfExtract
import tkinter as tk

#TODO finish this class

DEFAULT_PDFS = {
    'AA Big Book': r'C:\Users\lilv4\OneDrive\Documents\AA-BigBook-4th-Edition.pdf',
    'KJV Bible': r'C:\Users\lilv4\OneDrive\Documents\kjvBible.pdf'
}

class GUI:

    def __init__(self, master) -> None:
        self.master = master
        master.title = 'PDF Scanner'

        self.default_pdfs = DEFAULT_PDFS

        # GUI components
        self.word_entry = tk.Entry(master)
        self.result_text = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.word_count_label = tk.Label(master, text='Word Count:')
        self.show_more_button = tk.Button(master, text='Show More') # add show more command
        self.search_button = tk.Button(master, text='Search') # add search command
        self.clear_button = tk.Button(master, text='Clear') # add clear field command
        
        # Dropdown bar
        self.default_var = tk.StringVar()
        self.default_var.set('AA Big Book')
        self.pdf_dropdown = tk.OptionMenu(master, self.default_var, *self.default_pdfs.keys())

        # Layout
        self.pdf_combobox.pack()
        self.search_button.pack()
        self.word_entry.pack()
        self.result_text.pack()
        self.show_more_button.pack()
        self.word_count_label.pack()
        self.clear_button.pack()

