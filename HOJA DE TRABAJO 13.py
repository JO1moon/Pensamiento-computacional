matriz_inicial = [
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
]

def verificar_fila(fila):
    fila_str = ''.join(map(str, fila))
    if '11' in fila_str:
        return "Vivo"
    elif '1' in fila_str:
        return 'muerto por soledad'
    elif '1111' in fila_str:
        return "muerte por sobrepoblacion"
    else:
        return "Ninguno"
for i, fila in enumerate(matriz_inicial):
    estado = verificar_fila(fila)
    print(f"Fila {i + 1}: {estado}")