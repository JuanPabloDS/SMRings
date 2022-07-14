

"""def local_func():

    if 'var' in locals():
        print ('var variable exists')
    else:
        print ('var variable does not exist in the local namespace')

local_func()"""

from numpy import var


def local():
    var = 1

local()
print(var)


