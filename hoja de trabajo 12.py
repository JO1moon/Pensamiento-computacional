dias = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes']
niveles_de_azucar = [130, 160, 95, 175, 160] 
niveles_de_sal = [2000, 2400, 1800, 2400, 2700]
niveles_de_presion = [115, 130, 110, 125, 175] 
niveles = []
niveles_sal=[]
niveles_azucar=[]
for i in range(len(niveles_de_presion)):
    presion = niveles_de_presion[i]
    if presion < 120:
        niveles.append('Normal')
    elif 120 <= presion <= 129:
        niveles.append('Elevada')
    elif 130 <= presion <= 139:
        niveles.append('Hipertensión etapa 1')
    elif presion >= 140:
        niveles.append('Hipertensión etapa 2')
for i in range(len(niveles_de_sal)):
    sal = niveles_de_sal[i]
    if sal <= 2300:
        niveles_sal.append('Saludable')
    else:
        print('no saludable')
for i in range(len(niveles_de_azucar)):
    azucar = niveles_de_azucar[i]

    if 70 >= azucar <= 140:
        niveles_azucar.append('normal')
    else:
        niveles_azucar.append('mal')
print(dias)
print(niveles_azucar)
print(niveles)
print(niveles_sal)

