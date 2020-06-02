decryption = {
    'a': 'b',
    'b': 'd',
    'c': 'f',
    'd': 'h',
    'e': 'i',
    'f': 'm',
    'g': 'o',
    'h': 'r',
    'i': 't',
    'j': 'v',
    'k': 'x',
    'l': 'z',
    'm': 'a',
    'n': 'c',
    'o': 'e',
    'p': 'g',
    'q': 'j',
    'r': 'k',
    's': 'l',
    't': 'n',
    'u': 'p',
    'v': 'q',
    'w': 's',
    'x': 'u',
    'y': 'w',
    'z': 'y',
}


message = 'ec zgx mho hombetp idew zgx dmjo bongbob ido fowwmpo'
code = ''
for x in message:
    if x in decryption:
        code += decryption[x]
    elif x == ' ':
        code += ' '
print(code)
