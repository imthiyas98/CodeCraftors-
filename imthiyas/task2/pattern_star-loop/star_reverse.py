for i in range (1, 6):
    str = ""
    for j in range (1, i):
       str= str+ "  "
 
    for j in range (1,12 - 2*i):
       str= str+"* "
    for j in range (1, i):
       str= str+"  "
    print(str)