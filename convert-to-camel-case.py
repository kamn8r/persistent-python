def to_camel_case(string):
    if len(string) == 0:
        return string
    else:
        string = string.replace('_', ' ');
        string = string.replace('-', ' ');
        list = string.split()
        list2 = list.pop(0)
        list = [x[0].upper() + x[1:].lower() for x in list]
        string2 = ''
        string3 = ''
        for x in list:
            string2 += x
        for x in list2:
            string3 += x
        string4 = ''
        string4 = string3 + string2
        return string4
