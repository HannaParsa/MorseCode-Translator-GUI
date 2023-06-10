from tkinter import *
from tkinter import messagebox

#creat a GUI windpw
root = TK()

Variable1 = StringVar(root)
variable2 = stringvar(root)

Variable1.set("lang-code")
Variable2.set("lang-code")

#making a dictionary to creat th emorse code
MORSE_CODE_DIC = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

#function that cleans both text and code areas from
def clearAll():
    language1_field.delete(1.0, END)
    language2_field.delete(1.0, END)

#converting language to another
def convert():


if __name__ == "__main__":
    root.configure(background = 'light green') 
    root.geometry("400x350") 
    root.title("Translator")
# Create Welcome to Morse Code Translator label 
    headlabel = Label(root, text = 'Welcome to Morse Code Translator', 
                            fg = 'black', bg = "red") 
# Create a "One Language " label 
    label1 = Label(root, text = "One Language ",
                fg = 'black', bg = 'dark green')
    
# Create a "From Language " label 
    label2 = Label(root, text = "From Language", 
                fg = 'black', bg = 'dark green') 
    
# Create a "To Language " label 
    label3 = Label(root, text = "To Language ", 
                fg = 'black', bg = 'dark green')

# Create a "Converted Language " label 
    label4 = Label(root, text = "Converted Language ", 
                fg = 'black', bg = 'dark green')

# grid method is used for placing 
# the widgets at respective positions 
# in table like structure .  
    headlabel.grid(row = 0, column = 1) 
    label1.grid(row = 1, column = 0) 
    label2.grid(row = 2, column = 0)
    label3.grid(row = 3, column = 0)
    label4.grid(row = 5, column = 0)
# Create a text area box 
# for filling or typing the information. 
    language1_field = Text(root, height = 5, width = 25,
                                     font = "lucida 13")
    language2_field = Text(root, height = 5, width = 25,
                                     font = "lucida 13")
# padx keyword argument used to set padding along x-axis . 
    language1_field.grid(row = 1, column = 1, padx = 10) 
    language2_field.grid(row = 5, column = 1, padx = 10)
   
# list of language codes
    languageCode_list = ["Eng", "Morse"]

# create a drop down menu using OptionMenu function
# which takes window name, variable and choices as
# an argument. use * before the name of the list,
# to unpack the values
    FromLanguage_option = OptionMenu(root, variable1, *languageCode_list)
    ToLanguage_option = OptionMenu(root, variable2, *languageCode_list)
       
    FromLanguage_option.grid(row = 2, column = 1, ipadx = 10)
    ToLanguage_option.grid(row = 3, column = 1, ipadx = 10)
       
# Create a Convert Button and attached 
# with convert function 
    button1 = Button(root, text = "Convert", bg = "red", fg = "black",
                                command = convert)
       
    button1.grid(row = 4, column = 1)

# Create a Clear Button and attached 
# with clearAll function 
    button2 = Button(root, text = "Clear", bg = "red", 
                     fg = "black", command = clearAll)
     
    button2.grid(row = 6, column = 1)
    
# Start the GUI 
    root.mainloop() 