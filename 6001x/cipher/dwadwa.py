class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
        another letter (string). 
        '''
##        alphabet = {'A': 'A', 'C': 'C', 'B': 'B', 'E': 'E', 'D': 'D', 'G': 'G', 'F': 'F', 'I': 'I', 'H': 'H', 'K': 'K', 'J': 'J', 'M': 'M', 'L': 'L', 'O': 'O', 'N': 'N', 'Q': 'Q', 'P': 'P', 'S': 'S', 'R': 'R', 'U': 'U', 'T': 'T', 'W': 'W', 'V': 'V', 'Y': 'Y', 'X': 'X', 'Z': 'Z', 'a': 'a', 'c': 'c', 'b': 'b', 'e': 'e', 'd': 'd', 'g': 'g', 'f': 'f', 'i': 'i', 'h': 'h', 'k': 'k', 'j': 'j', 'm': 'm', 'l': 'l', 'o': 'o', 'n': 'n', 'q': 'q', 'p': 'p', 's': 's', 'r': 'r', 'u': 'u', 't': 't', 'w': 'w', 'v': 'v', 'y': 'y', 'x': 'x', 'z': 'z'}
##        dic={}  
##        for i in range(0,len(alphabet)):  
##            dic[alphabet[i]]=alphabet[(i+shift)%len(alphabet)]
##        return dic
        if shift == 0:
            dic = {'A': 'A', 'C': 'C', 'B': 'B', 'E': 'E', 'D': 'D', 'G': 'G', 'F': 'F', 'I': 'I', 'H': 'H', 'K': 'K', 'J': 'J', 'M': 'M', 'L': 'L', 'O': 'O', 'N': 'N', 'Q': 'Q', 'P': 'P', 'S': 'S', 'R': 'R', 'U': 'U', 'T': 'T', 'W': 'W', 'V': 'V', 'Y': 'Y', 'X': 'X', 'Z': 'Z', 'a': 'a', 'c': 'c', 'b': 'b', 'e': 'e', 'd': 'd', 'g': 'g', 'f': 'f', 'i': 'i', 'h': 'h', 'k': 'k', 'j': 'j', 'm': 'm', 'l': 'l', 'o': 'o', 'n': 'n', 'q': 'q', 'p': 'p', 's': 's', 'r': 'r', 'u': 'u', 't': 't', 'w': 'w', 'v': 'v', 'y': 'y', 'x': 'x', 'z': 'z'}
            dix = dic.copy()
            return dix
  

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        #Convert each letter of plaintext to the corrsponding  
        #encrypted letter in our dictionary creating the cryptext
        dic=[]
        ciphertext=""  
        for l in plaintext.lower():  
            if l in dic:  
                l=dic[l]  
            ciphertext+=l  
  
        return ciphertext
