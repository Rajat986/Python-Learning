def getcs():
    s=input("server")
    d=input("db")
    u=input("user")
    p=input("pass")
    return "server=%s;db=%s;user=%s;pass=%s"%(s,d,u,p)
cs=getcs()
print(cs)

