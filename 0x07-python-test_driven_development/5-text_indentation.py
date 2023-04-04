#!/usr/bin/python3

def text_indentation(text):
    """
     prints a text with 2 new lines after
     each of these characters: ., ? and :
     """
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    else:
        a = 0
        tester = not True
        txt_len = len(text)
        for i in range(txt_len):
            if text[i] in ('.', '?', ':'):
                tester = True
                print(text[a:(i + 1)])
                print()
                a = i + 2

        if i + 1 == txt_len and tester is not True:
            print(text)
