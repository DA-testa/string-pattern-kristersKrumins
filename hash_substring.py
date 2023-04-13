# python3

def read_input():
    if "I" in input():
        pat=input().strip()
        txt=input().strip()
    else:
        file=open("tests/06","r")
        pat=file.readline().strip()
        txt=file.readline()
        file.close()

    return (pat, txt)



def print_occurrences(output):
    print(' '.join(map(str, output)))
    
def get_hash(txt):
    x=13
    y=256
    l=len(txt)
    res=0
    for i in range(l):
        res = (x*res+ord(txt[i])) % y
    return res

def get_occurrences(pat, txt):
    ot=[]
    for i in range(0,len(txt)-len(pat)+1):
        if get_hash(txt[i:i+len(pat)])==get_hash(pat):
            if txt[i:i+len(pat)]==pat:
                ot.append(i)
    return [0]


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

