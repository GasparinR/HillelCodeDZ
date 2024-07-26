def correct_sentence(text):
    sentences = text.split('. ')
    corrected_sentences = []

    for sentence in sentences:
        if sentence:
            corrected_sentence = sentence[0].upper() + sentence[1:]
            corrected_sentences.append(corrected_sentence)

    corrected_text = '. '.join(corrected_sentences)
    if not corrected_text.endswith('.'):
        corrected_text += '.'

    print(corrected_text)
    return corrected_text


assert correct_sentence("greetings, friends")  # == "Greetings, friends.", 'Test1'
assert correct_sentence("hello")  # == "Hello.", 'Test2'
assert correct_sentence("greetings. Friends")  # == "Greetings. Friends.", 'Test3'
assert correct_sentence("greetings, friends.")  # == "Greetings, friends.", 'Test4'
assert correct_sentence("greeting, all.")  # == "Greetings, friends.", 'Test5'
assert correct_sentence("hello world")

print('ОК')
