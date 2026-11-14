    # Oppgave 1
fodselsaar=int(input("Hvilket år er du født?"))
alder=2026-fodselsaar
print("Du blir",alder,"år i år.")

print()


    # Oppgave 2
personer=int(input("Hvor mange kommer på pizzakveld?"))
pizzaer=personer*0.25
print("Dere trenger",pizzaer,"pizzaer.")

print()


    # Oppgave 3
import math

grader=float(input("Skriv inn grader:"))
radianer=grader*math.pi/180
print("Det blir",radianer,"radianer.")

print()


    # Oppgave 4
land={"norge":"Oslo","sverige":"Stockholm","danmark":"København"}
svar=input("Skriv inn et land (norge,sverige,danmark):")

if svar in land:
    print("Hovedstaden er", land[svar])
else:
    print("Landet finnes ikke i listen.")
        
    print()


    # Oppgave 5
a=float(input("Skriv inn kastet a:"))
b=float(input("Skriv inn kastet b:"))
hypotenus=math.sqrt(a**2+b**2)
print("Hypotenusen er:",hypotenus)

print()


    #Oppgave 6
import matplotlib.pyplot as plt
import numpy as np

x=np.linespace(0,10,100)
y=x**2 - 5*x + 2

plt.plot(x,y)
plt.show()


        
        

