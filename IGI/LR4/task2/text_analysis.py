import re

def analyze_text(text):
    # Количество предложений в тексте
    sentences = re.split(r'[.!?]', text)
    num_sentences = len(sentences)

    # Количество предложений каждого вида отдельно
    normal_sentences = len(re.findall(r'[^.!?]+[.]', text))
    exclamation_sentences = len(re.findall(r'[^.!?]+[!]', text))
    question_sentences = len(re.findall(r'[^.!?]+[?]', text))

    # Средняя длина предложения в символах (только слова)
    words = re.findall(r'\b\w+\b', text)
    sentence_lengths = []
    for sentence in sentences:
        words2 = re.findall(r'\b\w+\b', sentence) 
        words_len = [len(word) for word in words2]
        words_sum = sum(words_len)
        sentence_lengths.append(words_sum)
    avg_sentence_length = round(sum(sentence_lengths) / len(sentence_lengths))

    # Средняя длина слова в тексте в символах
    word_lengths = [len(word) for word in words]
    avg_word_length = round(sum(word_lengths) / len(word_lengths))

    # Количество смайликов в тексте
    smiles = re.findall(r'[:;]-*[\(\[\)\]]+', text)
    num_smiles = len(smiles)

    # Список всех слов текста длиной менее 5 символов
    short_words = re.findall(r'\b\w{1,4}\b', text)
    
    # Выделение пар символов малая/большая латинская буква знаками «_?_»
    modified_text = re.sub(r'([a-z])([A-Z])', r'\1_?_\2', text)

    # Количество слов с четным количеством букв
    even_length_words = [word for word in words if len(word) % 2 == 0]

    # Самое короткое слово, начинающееся на 'a'
    shortest_a_word = min([word for word in words if word.startswith('a')], key=len, default=None)

    # Повторяющиеся слова
    repeated_words = set([word for word in words if words.count(word) > 1])

    return {
        'num_sentences': num_sentences,
        'normal_sentences': normal_sentences,
        'exclamation_sentences': exclamation_sentences,
        'question_sentences': question_sentences,
        'avg_sentence_length': avg_sentence_length,
        'avg_word_length': avg_word_length,
        'num_smiles': num_smiles,
        'short_words': short_words,
        'modified_text': modified_text,
        'even_length_words': even_length_words,
        'shortest_a_word': shortest_a_word,
        'repeated_words': repeated_words
    }