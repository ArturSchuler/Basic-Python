

def mylazygenerator(number):
    index=0 
    while index < number:
        yield index **2
        index += 1


print()        