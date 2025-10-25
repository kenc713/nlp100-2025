def _is_english_lowercase(char: str) -> bool:
    return (len(char) == 1 and char.islower() and char.isalpha())

def cipher(english_text: str):
    ret = ""
    for char in english_text:
        if _is_english_lowercase(char):
            ret += chr(219 - ord(char))
        else:
            ret += char
    return ret

if __name__ == "__main__":
    given_string = "I am an NLPer"
    print(cipher(given_string))
    print(cipher(cipher(given_string)))