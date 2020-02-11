"""
You are given a string S and width W.
Your task is to wrap the string into a paragraph of width.

Input Format
The first line contains a string, S.
The second line contains the width, W.

Contraints
0 < len(s) < 1000
0 < w < len(s)

"""
import textwrap

def wrap(string, max_width):
    #assign the TextWrapepr method
    wrapper = textwrap.TextWrapper(width=max_width)
    #pass the string parameter and assign to a fomartted string and call the wrapper method.
    format_str = wrapper.fill(text=string)
    #return the formatted wrapped string
    return format_str
