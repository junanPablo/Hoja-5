#Laboratorio #5 el cual simula
#los procesos de un CPU

from SimPy.Simulation import *
from random import uniform, Random
import math

#variables
tiempoP = []#variable que contendra todos los procesos que se han hecho


#valores predeterminados del cpu y ram asi como los procesos que puede hacer
ram = 100 #memoria ram
valorInst = 3.0 #es la cantidad de procesos que puede hacer el cpu
tiempo = 0.0 # tiempo final
cantP = 25 #num de procesos que ejecutara e iran cambiando de 25,50, 100, 150 y 200 y que tendra que realizar
inter = 1

envioP = simpy.Environment()
ram = simpy.Container(envioP, 1)
cpu = simpy.Resource(envioP, 1)
espera = simpy.Resource(envioP,1)
random.seed(1234)

def miproceso(envioP, nuevoP, nombre, ram, memoria, instruccion, valorInst):
    global tiempo # este llevara el tiempo que se toma para todos los procesos que ha ejecutado
    global total

    #punto 1 : creando y llegada del nuevo proceso
    yield envioP.timeout(Creart)
    llego = envioP.now #llego el nuevo proceso espera el valor que tendra
    yield ram.get(memoria)#va tener un valor en la memoria cuando solicite
    #Punto2: en este punto es cuando llega al procesador
    #y determina que instruccion tiene que realizar
    contador = 0.0
    while contador < instruccion:
        with cpu.request() as req:
            yield req
            if((instruccion-contador)>=3):
                espacio = 3.0
            else:
                espacio = instruccion - contador
            yield envioP.timeout(espacio/valorInst)
        contador = contador + espacio
        #Punto 3:en este punto ya esta corriendo el proceso y ahora se generara un numero aleatorio
        #para ver si tiene que hacer una espera si es 1 y si es 2 para de nuevo a al punto 2
        enEspera = random.radint(1,2)
        if((enEspera == 1)and(contador<instrucciones)):
            with espera.request() as req2:
                yield req2
                yield envioP.timeout(1)
    ram.put(memoria)
    tiempoP.append(envioP.now - llego)
    tiempo = tiempo + (envioP.now - llego)

#haciendo un for para crear el valor del proceso y el peso que va a tener
for i in range(cantP):
    miRandom = random.expovariate(1.0/intervalo)
    instrucciones = random.randint(1,10)
    memoria = random.randint(1,10)
    envioP.process(miproceso(envioP, nuevoP, nombre, ram, memoria, instruccion, valorInst))

#simulando
envioP.run()
a = tiempo/cantP
total = 0.0
for i in range (cantP):
    total = total + (tiempoP[i]-a)**2
total = math.sqrt(total/cantP)
print("el tiempo promedio de mi proceso es: ",a,"\n")
print("\ncon una margen de error de: ",total)
        
