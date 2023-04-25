print('Adoptar gato')
print('Inicio')
x=0;
while x==0:
    print('Buscar gatos en adopción')
    ga=input('Es macho')
    ga=ga.lower()
    if ga=='si':
        edad=input('Es menor de dos años')
        edad=edad.lower()
        if edad=='si':
           esti=input('Esta esterilizado')
           esti=esti.lower()
           if esti=='si':
              encu=input('Se puede acordar un encuentro')
              encu=encu.lower()
              if encu=='si':
                    x=1;
                    print('Adoptar al gatito')
              else:           x=0
           else:        x=0
        else:     x=0
    else:  x=0
          
print('FIN')
