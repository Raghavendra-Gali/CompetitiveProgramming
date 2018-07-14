
def BaseConverter(s):
    d={}
    for i in range(len(s)):
        d[i]=s[i]
    return d
sURLDict={}
fURLDict={}
count=0
base62=BaseConverter("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
def genShortURL(fullURL):
    if (fullURL in fURLDict):
        print("ShortURL already Exists"+fURLDict[fullURL])
        return
    global count
    s=""
    k=count
    count+=1
    if (k==0):
        s="0000000"
        if (s not in sURLDict):
            sURLDict[s]=fullURL
            fURLDict[fullURL]=s
            print("short url for "+fullURL+" is "+s)
            return
    while(k!=0):
        s=base62[k%62]+s
        k=k//62
    l=len(s)
    if (l<7):
        for i in range(7-l):
            s="0"+s
    if (s not in sURLDict):
        sURLDict[s]=fullURL
        fURLDict[fullURL]=s
    print("short url for "+fullURL+" is https://ca.ke/"+s)

while (1==1):
    print("Enter \n\t1) generate ShortURL\n\t2)redirect ShortURL")
    userInput=int(input())
    if (userInput==1):
        fullURL=input("Enter an URL to shorten it : ")
        genShortURL(fullURL)
    elif (userInput==2):
        shortURL=input("Enter a short url: ")
        if sURLDict.get(shortURL,None) is not None:
            print("redirecting to "+sURLDict[shortURL])
        else:
            print("Doesn't exist")
    else:
        print("Invalid Input")