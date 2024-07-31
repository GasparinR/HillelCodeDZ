def popular_words(text, words):
    text_lower = text.lower()
    text_words = text_lower.split()

    word_count = {word: 0 for word in words}

    for word in text_words:
        if word in word_count:
            word_count[word] += 1

    print(word_count)

    return word_count


popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
              ['i', 'was', 'had', 'when'])
