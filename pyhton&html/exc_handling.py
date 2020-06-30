try:
    f=open('simple.txt','r')
    s=f.read()

except IOError:
    print("ERROR : Could not find the file or read data")
else:
    print(s)
    f.close()
    g=open('simple.txt','w')
    g.write('Rohit')
    g.close()
