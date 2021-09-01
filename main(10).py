print("Type of client (1, 2 or 3): ")
tipo_member=int(input())
print("Number of store visits (400<x<=100):")
numero_visitas=int(input())
print("Final price with discount is:")

def calcular_costo1(numero_visitas):
  base=1000
  if numero_visitas>=100 and numero_visitas<200:
    return base*.90
  if numero_visitas>=200 and numero_visitas<300:
    return base*.80
  if numero_visitas>=300 and numero_visitas<400:
    return base*.70

def calcular_costo2(numero_visitas):
  base=700
  if numero_visitas>=100 and numero_visitas<200:
    return base*.90
  if numero_visitas>=200 and numero_visitas<300:
    return base*.80
  if numero_visitas>=300 and numero_visitas<400:
    return base*.70

def calcular_costo3(numero_visitas):
  base=500
  if numero_visitas>=100 and numero_visitas<200:
    return base*.90
  if numero_visitas>=200 and numero_visitas<300:
    return base*.80
  if numero_visitas>=300 and numero_visitas<400:
    return base*.70

if tipo_member==1:
  costo=calcular_costo1(numero_visitas)
if tipo_member==2:
  costo=calcular_costo2(numero_visitas)
if tipo_member==3:
  costo=calcular_costo3(numero_visitas)

print(costo)