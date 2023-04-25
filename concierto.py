print('Comprar boletos')
print('Inicio')
x=0;
while x==0:
    print('Buscar concierto')
    musica=input('Es electronica')
    musica=musica.lower()
    if musica=='si':
        zona=input('Es zona VIP')
        zona=zona.lower()
        if zona=='si':
           pago=input('Se puede pagar con tarjeta')
           pago=pago.lower()
           if pago=='si':
              boletos=input('Hay boletos disponibles')
              boletos=boletos.lower()
              if boletos=='si':
                    x=1;
                    print('Comprar')
              else:           x=0
           else:        x=0
        else:     x=0
    else:  x=0
          
print('FIN')
