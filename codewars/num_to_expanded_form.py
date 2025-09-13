"""You will be given a number and you will need to return it as a string in Expanded Form. For example:

   12 --> "10 + 2"
   45 --> "40 + 5"
70304 --> "70000 + 300 + 4"
All numbers will be whole numbers greater than 0."""

def expanded_form(num):
    num_str = str(num)
    parts = []
    for i, digit in enumerate(num_str):
        if digit != '0':
            parts.append(digit + "0" * (len(num_str) - i - 1))
            
    return " + ".join(parts)
 