from classes import Recipiente, Copo


if __name__ == "__main__":
    # Execute suas testagens manuais aqui
    
    r = Recipiente(100)

    print(r)

    print(r.esta_limpo())

    print(r.estado())

    print(r.sujar())

    print(r.esta_limpo())

    print(r.lavar())

    print(r.esta_limpo())

    c = Copo(300.0)

    print(c)

    c.encher('cafe')
    print(c.bebida)

    print(c)

    c.beber(30)

    print(c)

    c.lavar()

    print(c.esta_limpo())

    print(c.tamanho)