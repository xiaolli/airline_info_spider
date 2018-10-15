import numpy as np
a = ['CA1608', '中国国航', '21:50', '--', '--', 'T3', '23:25', '--', '2018-10-11']

with open('a.txt','w') as f:
    #f.writelines(a)
    #f.write(','.join(a))
    f.write(str(a))

