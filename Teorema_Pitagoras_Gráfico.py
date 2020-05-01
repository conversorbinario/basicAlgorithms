import turtle
from math import sqrt, acos, degrees

def poligono_regular(lados, lonx_lado, x, y):
    '''pequena mostra do uso de turtle. 
debuxa poligonos regular de tamaño aleatorio en lugares aletarios'''
    turtle.pencolor('black')
    turtle.penup()
    # x e y son as coordenadas cartesianas de onde imos colocar o boligrafo'
    turtle.setpos(x,y)
    turtle.pendown()
    '''Interesanos usar o angulo interior
    PERO turtle utiliza o ángulo exterior
    ex: un triangulo equilatero ten tres angulos interiores de 60 º
    se introducimos 60 en turtle.left(), pensariamos que dibuzaria angulo interiores
    de 60 grados. sucede que debuxa ángulos EXTERIORES de 60 graos, por tanto os interiores
    son de 120 graos'''
    angulo=180-(180*(lados-2))/lados 
    turtle.color('brown')
    for n in range(lados):
        turtle.forward(lonx_lado)
        turtle.right(angulo)
        
        
def deb_triangulo_Rectangulo(l1, l2, l3):
    ''' Crea un triangulo irregular.
    Usa como parámetros a lonxitude de dous dos seus lados
    e o angulo que estes forman'''
    turtle.pencolor('black')
    turtle.penup()
    turtle.setpos(0,0)
    turtle.pendown()   
    turtle.forward(l1)
    turtle.write('Cateto 1 de ' + str(l1) + ' unidades')
    turtle.left(90)
    turtle.forward(l2)
    turtle.write('Cateto 1 de ' + str(l2) + ' unidades')
    turtle.setpos(0,0)
    turtle.write('Hipotenusa de ' + str(l3) + ' unidades')


def calculo_angulos(l1, l3):
    ''' dados os tres lados dun triangulo, devolta un array
     cos ángulos formados pola interseccion 
     cat-cat, cat1-hipotenusa and cat2-hipotenusa, nesta orde'''
   
    angles= [90] #ambos catetos
    coscat1hip=l1/l3 #adxacente entre hipotenusa
    angulo=degrees(acos(coscat1hip)) #pasamos a graos
    angles.append(angulo)
    angles.append(90-angulo)#calculamos o angulo faltante
    return angles


def cadrado(lonx_lado, color, x, y):
    '''Crea un cadrado '''
    turtle.pencolor('red')
    turtle.penup()
    # x e y son as coordenadas cartesianas de onde imos colocar o boligrafo'
    turtle.setpos(x,y)
    turtle.pendown()
 
    angulo=90
    turtle.color('brown')
    turtle.begin_fill()
    for n in range(4):
        turtle.forward(lonx_lado)
        turtle.right(angulo)
    turtle.end_fill()
    
def amosar(l1, l2, l3):
    print('hipotenusa ' + str(l3))
    print('cateto ' + str(l2))
    print('cateto ' + str(l1))
    
def calculo_Pitagoras(l1, l2, hipotenusa):
    if hipotenusa is False:
        l3=(pow(l1,2) + pow(l2,2))
        l3 = sqrt(l3)
    else:
        l3=max(l1, l2)
        l1=min(l1, l2)
        l2=abs(pow(l3, 2) - pow(l1,2))
        l2 = sqrt(l2)
    amosar(l1, l2, l3)
    return(l1, l2, l3)


def demostracion_teoremaPitagoras():
    valor=int(input('1. Lonxitude da Hipotenusa.\n'
              + '2. Lonxitude dun dos catetos'))
    hipotenusa=False
    if valor==1:
        l1=float(input('Hipotenusa: '))
        hipotenusa=True;
    else:
        l1=float(input('Cateto: '))
    valor=int(input('1. Lonxitude da Hipotenusa.\n'
              + '2. Lonxitude dun dos catetos'))
    if valor==1:
        l2=float(input('Hipotenusa: '))
        hipotenusa=True
    else:
        l2=float(input('Cateto: '))
    l1, l2, l3 =calculo_Pitagoras(l1, l2, hipotenusa)
    angulos= calculo_angulos(l1, l3)
    print(angulos)
    deb_triangulo_Rectangulo(l1, l2, l3)
    
demostracion_teoremaPitagoras()
#lados=random.randrange(3, 10)
#poligono_regular(lados, 80, random.randrange(-400, 200), random.randrange(-400, 200), 'red')


