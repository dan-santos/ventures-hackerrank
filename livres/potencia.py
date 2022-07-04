def potencia(base: int, expoente: int) -> int:
    if expoente == 1:
        return base
        
    return base*potencia(base, expoente - 1)
    
    
if __name__ == '__main__':
    resultado = potencia(2, 3)
    print(resultado)