print('Receta')
print('Inicio')
x=0;
while x==0:
    print('Buscar receta a realizar')
    rec=input('Puedo hacerla')
    rec=rec.lower()
    if rec=='si':
        print('Identificar ingredientes')
        ingre=input('Estan disponibles los ingredientes')
        ingre=ingre.lower()
        if ingre=='si':
           fresco=input('Estan frescos')
           fresco=fresco.lower()
           if fresco=='si':
              boletos=input('Hay la cantidad necesaria')
              boletos=boletos.lower()
              if boletos=='si':
                    x=1;
                    print('Comprar')
              else:           x=0
           else:        x=0
        else:     x=0
    else:  x=0
          
print('FIN')
