import tabulate



humano={
    'nombre':'Alex',
    'apellido':'Perez',
    'edad':25,
    'altura':1.80,
    'mes-n':'mayo',
    
    'peso':63,
    'juegos':[
        'fortnine',
        'warzone',
        'minecraft'
    ]
}

sub_matriz  =[]
matriz      =[]
cabecera    =[]
longitud    = len(humano)

for k,v in humano.items():
    cabecera.append(str(k))
    sub_matriz.append(str(v))

matriz.append(sub_matriz)

print('el JSON humano tiene '+str(longitud)+' atributos')
print('Juego favorito:',humano['juegos'][1])
print(tabulate.tabulate(matriz,headers=cabecera,tablefmt='heavy_outline'))

#for k,v in humano.items():
#    print(k+': '+str(v))