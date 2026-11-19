
import math




 # Oppgave 1
alder=int(input("Hvilket år er du født?"))
alder_2024=2024-alder
print(f"Du blir {alder_2024} år i løpet av 2024")

print()




    # Oppgave 2
antall_elever = int(input("Skriv inn antall elever:"))
pizzaer = math.ceil(antall_elever*0.25)
print("Det må handles inn", pizzaer, "pizzaer til festen.")

print()





    # Oppgave 3
import math

grader=float(input("Skriv inn grader:"))
radianer=grader*math.pi/180
print("Det blir",radianer,"radianer.")

print()







    # Oppgave 4a
data = {
        "Norge": ["Oslo",0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
}

    # Oppgave 4b
svar=input("Skriv inn et land (f.eks. England):").strip().capitalize()

if svar in data:
    hovedstad = data[svar][0]
    innbyggere = data[svar][1]
    print(f"{hovedstad} er hovedstaden i {svar} og det er {innbyggere} mill. innbyggere i {hovedstad}.")
else:
    print("Landet finnes ikke i oversikten.")
    
    # Oppgave 4c
nytt_land = input("Skriv inn et nytt land:"). strip().capitalize()
ny_hovedstad = input(f"Skriv inn hovedstaden i {nytt_land}:").strip()
nye_innbyggere = float(input(f"Skriv inn antall innbyggere (i mill.) i {ny_hovedstad}:"))

data[nytt_land] = [ny_hovedstad, nye_innbyggere]
print(data)

print()

    
    
    
    

    # Oppgave 5
def beregn_figur(a, b):
    r=a/2
    hypotenus=math.sqrt(a**2 + b**2)
    areal =(a*b)/2+0.5*math.pi*r**2
    ytre_omkrets=b+hypotenus+math.pi*r
    return areal, ytre_omkrets

a=float(input("Skriv inn lengden a:"))
b=float(input("Skriv inn lengden b:"))

areal, ytre_omkrets=beregn_figur(a, b)
print(f"Arealet av figuren er {areal:.2f} og ytre omkrets er {ytre_omkrets:.2f}.")

print()





    #Oppgave 6
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-10, 10, 200)
y=-x**2-5

plt.plot(x, y)
plt.title("f(x)=-x^2-5")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()




        
        

