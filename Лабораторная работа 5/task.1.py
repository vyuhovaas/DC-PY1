from pprint import pprint

keys = ['dec', 'bin', 'oct', 'hex']
i = 16
dict_ = [{'dec': i, 'bin': bin(i), 'oct': oct(i), 'hex': hex(i)} for i in range(16)]

pprint(dict_)

