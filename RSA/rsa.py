def gcd(a,b):
    while b:
        a,b =b , a%b
    return a

def rsa(p,q,msg):
    n=p*q
    phi =(p-1)*(q-1)
    for i in range (2, phi):
        if (gcd(i,phi)== 1):
         e =i
         break
    j=0
    while True:
        if(j*e%phi) == 1:
            d=j
            break
        j+= 1
    c= (msg**e)%n
    print("encrypted message:", c)
    d = (c**d)%n
    print("Decrypted message : ",d)

p= int(input("enter the value of p:"))
q= int(input("enter the value of q:"))
msg = int(input("enter the message:"))
rsa(p,q,msg)
