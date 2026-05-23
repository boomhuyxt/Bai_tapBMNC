from string import ascii_uppercase

ALPHABET = list(ascii_uppercase)

class CaesarCipher:  # Viết liền PascalCase
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(self, text: str, shift: int) -> str:
        if not text: return ""
        alphabet_len = len(self.alphabet)
        text = text.upper()
        result = []
        
        for letter in text:
            if letter in self.alphabet:
                letter_index = self.alphabet.index(letter)
                output_index = (letter_index + shift) % alphabet_len
                result.append(self.alphabet[output_index])
            else:
                result.append(letter)
                
        return ''.join(result)

    def decrypt_text(self, text: str, shift: int) -> str:
        # Tận dụng hàm mã hóa với số shift âm để rút gọn code
        return self.encrypt_text(text, -shift)