import re

tokens = []
source_code = 'if True : a = False'.split() #code example

for word in source_code:
    if word in ['if','True','False']:
        tokens.append(['KEYWORD', word])

    elif word in [':','<','>','<=','>=','==','!=','and','or']:
        if word == ':':
            tokens.append(['OPERATOR',word])
        else:
            tokens.append(['LOGICAL OPERATOR', word])

    elif word in ['=']:
        tokens.append(['ASSIGN',word])

    elif re.match("[a-c]", word) or re.match("[A-C]", word):
        if word[len(word)-1] == ':':
            tokens.append(['VAR',word[:-1]])
            tokens.append(['OPERATOR',word[-1:]])
        else:
            tokens.append(['VAR',word])

    elif word in ['+','-','*','/','%','**','//']:
        tokens.append(['ARITHMETIC OPERATOR', word])

print(tokens) #run the code
