print('Reserva en linea de restaurante')
print('Inicio')
x=0;
while x==0:
    print('Buscar restaurantnoe')
    ubicacion=input('Queda en el centro')
    if ubicacion=='si':
        comida=input('Es comida italiana')
        if comida=='si':
            reserva=input('Se reserva en linea')
            if reserva=='si':
                mesas=input('Hay mesas disponibles')
                if mesas=='si':
                    x=1;
                    print('Reservar')
                else:           x=0
            else:        x=0
        else:     x=0
    else:  x=0
          
print('FIN')
