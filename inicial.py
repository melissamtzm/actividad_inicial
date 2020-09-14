#A01720572 Luciana Montalvo Barragán
#matricula y nombre 2
#Calcular el área y perímetro de un rectángulo dado sus medidas de los lados

#funcion1  calcular área del rectángulo


#funcion2  calcular perímetro del rectángulo
def perimetro (l1,l2):
    p = (l1*2) + (l2*2)
    return p

#instrucciones de accion
#pedir datos
print("medida de un lado del rectángulo")
l1 = float(input())

print("medida de un lado del rectángulo")
l2 = float(input())

#desplegar calculo funcion1

#desplegar calculo funcion 2
perimetro = perimetro(l1,l2)
print(perimetro)