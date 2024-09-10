def count_chars(text):
    # If there is nothing in the text it returns 0
    if not text:
        return 0
     # For every character in text it adds to the total
    total = 0
    for _ in text:
        total += 1
    # Returns total number of charecters in text
    return total

def count_words(text):
    # If there is nothing in the text it returns 0
    if not text:
        return 0
    total = 0
    # For every word in text it splits it by a space and adds the number of words to the total 
    for _ in text.split(" "):
        total += 1
    return total

def count_sentences(text):
    # Starts at 0 
    total = 0
    # For every punctuation mark, it counts as a sentence and adds to the total
    for char in text:
        if char == "." or char == "?" or char == "!":
            total += 1
    # Returns total number of sentences in text
    return total