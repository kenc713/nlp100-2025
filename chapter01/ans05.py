import re

def get_char_n_gram(sentence: str, n: int, separator_set: set[str] = {",", "."}) -> list[str]:
    if n <= 0: return []
    if len(sentence) < 0: return []
    
    no_space_sentence = "".join(list(sentence.split()))
    no_separated_sentence = re.sub(f"[{''.join(separator_set)}]", "", no_space_sentence)

    return [no_separated_sentence[i:i + n] for i in range(len(no_separated_sentence) - n + 1)]

def get_word_n_gram(sentence: str, n: int, separator_set: set[str] = {",", "."}) -> list[list[str]]:
    if n <= 0: return []
    if len(sentence) < 0: return []

    words = sentence.split()
    no_separated_words = list(map(lambda w: re.sub(f"[{''.join(separator_set)}]", "", w), words))

    return [no_separated_words[i:i + n] for i in range(len(no_separated_words) - n + 1)]

if __name__ == "__main__":
    given_string = "I am an NLPer"
    print(get_char_n_gram(given_string, 3))
    print(get_word_n_gram(given_string, 2))