#a simple function that takes a space seperated string, reverses the order of words and inverts the casing.

def reverse_words_order_and_swap_cases(sentence):
    reverse_sentence = sentence.split(' ')

    string_to_list = ' '.join(reverse_sentence[::-1])

    for i in range(len(string_to_list)):
      if string_to_list[i].isupper():
        string_to_list[i].lower()
      else:
        string_to_list[i].upper()
    
    return string_to_list.swapcase()


print(reverse_words_order_and_swap_cases('aWESOME is cODING'))