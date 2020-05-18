def descending_order(num):
    # Bust a move right here
    list = [d for d in str(num)]
    list.sort(reverse=True)
    string = ''
    for n in list:
        string += n
    final  = int(string)
    return final
