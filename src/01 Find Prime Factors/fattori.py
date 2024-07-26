def fattorizzazione(numero):
    fattori = []
    divisore = 2
    while divisore <= numero:
        if numero % divisore == 0:
            fattori.append(divisore)
            numero = numero // divisore
        else:
            divisore += 1
    return fattori
if __name__ == '__main__':
    print(fattorizzazione(60))