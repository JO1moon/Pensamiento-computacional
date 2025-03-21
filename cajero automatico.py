saldo_del_usuario = 3000
intentos = 0
intentos2= 3

while True:
    print(f'Saldo actual: Q{saldo_del_usuario}')
    monto = int(input('Ingrese monto a retirar: '))
    
    if monto == '0':
        print('Gracias por usar el cajero. Adiós.')
        break

    if monto > saldo_del_usuario:
        intentos += 1
        intentos2 -=1
        if intentos >= 3:
            print('Demasiados intentos saldo insuficiente. Adiós.')
            break
        print(f'Saldo insuficiente. Intentos restantes: {intentos2}')
    elif monto <= 0:
        print("Ingrese un monto válido.")
    else:
        saldo_del_usuario -= monto
        print(f"Retiro exitoso. Nuevo saldo: Q{saldo_del_usuario}")
            
        if saldo_del_usuario == 0:
             print("Retiro exitoso. Saldo agotado. Adiós.")
             break
