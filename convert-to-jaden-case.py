def to_jaden_case(string):
    string = string.upper()
    list = string.split()
    list = [x[0].upper() + x[1:].lower() for x in list]
    string = ''
    for x in list:
        string = string + x + ' '
    string = string[:-1]
    return string
