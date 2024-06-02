def main():
    # Request text input
    text = input("Text: ")
    size = len(text)

    # Discover the number of letters, words and phrases.
    L = letter(text, size)
    W = word(text, size)
    S = sentence(text, size)

    # Perform the final calculation
    L = float(L) / float(W) * 100
    S = float(S) / float(W) * 100
    index = 0.0588 * float(L) - 0.296 * float(S) - 15.8

    # Call a decision tree
    tree(index)


def letter(text, size):
    l = 0
    for i in range(size):
        if text[i].isalpha() == True:
            l = l + 1

    return l


def word(text, size):
    w1 = 0
    for i in range(size):
        if text[i] == ' ':
            w1 = w1 + 1

    w1 = w1 + 1
    return w1


def sentence(text, size):
    s = 0
    for i in range(size):
        if text[i] in {'?', '.', '!'}:
            s = s + 1

    return s


def tree(index):
    if (index <= 1):
        print("Before Grade 1")
    if index < 2.5:
        print("Grade 2")
    if index < 3.5:
        print("Grade 3")
    if index < 4.5:
        print("Grade 4")
    if index < 5.5:
        print("Grade 5")
    if index < 6.5:
        print("Grade 6")
    if index < 7.5:
        print("Grade 7")
    if index < 8.5:
        print("Grade 8")
    if index < 9.5:
        print("Grade 9")
    if index < 10.5:
        print("Grade 10")
    else:
        print("Grade 16+")


main()
