

bil = {}

bela = bil

bela2 = {'a': '32', 'b': '35'}

def get_key(val):
    for key, value in bela2.items():
         if val == key:
             return key
 
    return "There is no such Key"

print(get_key('c'))
