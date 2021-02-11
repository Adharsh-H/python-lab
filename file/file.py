inf=False
outf=False
try:
    inf=open('in.txt')
    outf=open('out.txt','w')
    line=inf.read()
    while line:
        outf.write(line)
        inf=False
        inf=open('out.txt')
        line=inf.readline()
    print(line)
    print("text is copied")
except IOError as e:
    print(e)
finally:
    if inf:inf.close()
    if outf:outf.close()
    