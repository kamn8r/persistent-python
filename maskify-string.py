def maskify(cc):
    list = []
    string = ''
    for x in cc:
        list.append(x)
    list = list[-4:] 
    for x in list:
        string += x
    newcc = []
    for x in range(len(cc)-4):
        newcc += '#'
    newstring = ''
    for i in newcc:
        newstring += i
    final = newstring+string
    return final
    pass
