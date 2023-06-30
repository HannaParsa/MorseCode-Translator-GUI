
from morse_converter_class import MorseCode
from tkinter import *
#import pyperclip
#### ------------ Morse Converter ------------ ####
morse_converter = MorseCode()
def to_morse():
    alph_text = alph_text_entry.get("1.0",END)
    morse_code = morse_converter.encrypt(alph_text)
    morse_code_entry.delete('1.0', END)
    morse_code_entry.insert('1.0', morse_code)
    morse_code_entry.focus()
    pyperclip.copy(morse_code)
def to_alph():
    morse_code = morse_code_entry.get("1.0",END)
    alph_text = morse_converter.decrypt(morse_code)
    alph_text_entry.delete("1.0", END)
    alph_text_entry.insert('1.0', alph_text)
    alph_text_entry.focus()
    pyperclip.copy(alph_text)
#### ------------ UI Setup ------------ ####
window=Tk()
window.title('Morse Code Translator')
window.config(padx=10, pady=20)
# ------ Labels ------ #
alph_text_label = Label(text='Alphabetic Text')
alph_text_label.grid(column=0, row=0)
morse_code_label = Label(text='Morse Code')
morse_code_label.grid(column=1, row=0)
# ------ Entries ------ #
alph_text_entry= Text(width=50, height=10)
alph_text_entry.grid(column=0, row=1)
alph_text_entry.focus()
morse_code_entry= Text(width=50, height=10)
morse_code_entry.grid(column=1, row=1)
# ------ Buttons ------ #
alph_btn = Button(text='translate to morse', command=to_morse)
alph_btn.grid(column=0,row=2)
morse_btn = Button(text='translate to alphabetic', command=to_alph)
morse_btn.grid(column=1,row=2)
window.mainloop()