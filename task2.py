def alphabet_position(text):
    a = ['abcdefghijklmnopqrstuvwxyz'.index(text[i].lower()) + 1 for i in range(len(text)) if text[i].isalpha()]
    return " ".join(str(x) for x in a)