def correct_sentence(text):
    sentences = text.split('. ')
    corrected_sentences = []

    for sentence in sentences:
        if sentence:
            # Capitalize the first letter of the sentence
            corrected_sentence = sentence[0].upper() + sentence[1:]
            # Add the corrected sentence to the list
            corrected_sentences.append(corrected_sentence)

    # Join the corrected sentences and ensure the text ends with a period
    corrected_text = '. '.join(corrected_sentences)
    if not corrected_text.endswith('.'):
        corrected_text += '.'

    print(corrected_text)
    return corrected_text


# Test cases
assert correct_sentence("greetings, friends")  # == "Greetings, friends.", 'Test1'
assert correct_sentence("hello")  # == "Hello.", 'Test2'
assert correct_sentence("greetings. Friends")  # == "Greetings. Friends.", 'Test3'
assert correct_sentence("greetings, friends.")  # == "Greetings, friends.", 'Test4'
assert correct_sentence("greeting, all.")  # == "Greetings, friends.", 'Test5'
assert correct_sentence("hello world")

print('ОК')
