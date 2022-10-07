def TextDelete(line):
    words = line.split(' ')
    fragment = "абв"
    new_words = []
    for word in words:
        if fragment not in word:
            new_words.append(word)
    print(' '.join(new_words))

line = "абв габв абвгд еёжз иклмн"
TextDelete(line)