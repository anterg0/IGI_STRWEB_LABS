text = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."
final_string = [word.strip(".,") for word in text.split()]

def func1():
    """
    The function `func1` calculates the length of words in a string and creates a dictionary with words
    of odd length as keys and their lengths as values.
    :return: The function `func1` is returning a dictionary where the keys are words from the
    `final_string` variable and the values are the lengths of those words, but only for words with odd
    lengths.
    """
    word_count = len(final_string)
    dictionary_odd_length = {key: len(key) for key in final_string if len(key) % 2 != 0}
    return dictionary_odd_length


def func2():
    """
    This function creates a dictionary of words starting with 'i' from a given string and returns the
    shortest word starting with 'i', or "No words starting with 'i'" if there are none.
    :return: The function `func2` returns the shortest word starting with the letter 'i' from the
    `final_string` variable. If there are no words starting with 'i', it will return the string "No
    words starting with 'i'".
    """
    dictionary_i = {key: len(key) for key in final_string if key.startswith("i")}
    shortest_word_starting_with_i = min(dictionary_i, default="No words starting with 'i'")
    return shortest_word_starting_with_i

def func3():
    """
    The function `func3` returns a list of unique duplicate words from the input `final_string`.
    :return: The function `func3` returns a list of unique duplicate words found in the `final_string`
    list.
    """
    duplicate_words = [word for word in final_string if final_string.count(word) > 1]
    return list(set(duplicate_words))