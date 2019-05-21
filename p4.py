
P=int(input("cantidad invertir?"))
r=float(input("interes?"))
n=12
t=int(input("años de inversión?"))
a=P*(1+(r/n)**(n*t))
print("el beneficio es {0:.3}".format(a))