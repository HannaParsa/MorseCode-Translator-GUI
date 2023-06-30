class MorseCode():
    # I added a translated value to a space,
    # it's equal to a vertical bar "|" (see last k,v in morse dictionary)
    # so morse code words now are separated with a vertical bar between 2 spaces " | "
    morse = {
        # Letters
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        # Numbers
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        # Punctuation
        "&": ".-...",
        "'": ".----.",
        "@": ".--.-.",
        ")": "-.--.-",
        "(": "-.--.",
        ":": "---...",
        ",": "--..--",
        "=": "-...-",
        "!": "-.-.--",
        ".": ".-.-.-",
        "-": "-....-",
        "+": ".-.-.",
        '"': ".-..-.",
        "?": "..--..",
        "/": "-..-.",
        # Space
        " ": "|"
    }
    
    def __init__(self):
        self.result = ""

    def encrypt(self, text):
      encrypted_chars =[ f"{self.morse[char.lower()]} " for char in text if char.lower() in self.morse ]
      return self.result.join(encrypted_chars)
    
    def decrypt(self, text):
      decrypted_text=[]
      morse_words = text.split(" | ")
      for word in morse_words:
        morse_chars = word.split(' ')
        decrypted_word=[ k for char in morse_chars for k,v in self.morse.items() if char==v ]
        decrypted_text.append(f"{''.join(decrypted_word)} ")
      return self.result.join(decrypted_text)