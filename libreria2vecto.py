# vectoresLib
def sumaMatri(a, b):
    return [sumaVec(a[i], b[i]) for i in range(len(a))]


def restaMatri(a, b):
    return [restaVec(a[i], b[i]) for i in range(len(a))]


def matriInverAd(a):
    return [vectoInverAd(a[i]) for i in range(len(a))]


def matriPorEsca(r, a):
    return [vectoPorEsca(r, a[i]) for i in range(len(a))]


def transptaMatri(a):
    return [
        [a[j][i] for j in range(len(a))] for i in range(len(a[0]))]


def conjuMatri(a):
    return [conjuVecto(a[i]) for i in range(len(a))]


def adjuntaMatri(a):
    b = transptaMatri(a)
    return conjuMatri(b)


def multipliMatri(a, b):
    if len(a[0]) == len(b):
        filas = len(a)
        columnas = len(b[0])
        res = [[(0, 0) for i in range(columnas)] for j in range(filas)]
        for i in range(0, filas):
            for j in range(0, columnas):
                temp = (0, 0)
                for k in range(0, len(b)):
                    temp = suma(temp, multipli(a[i][k], b[k][j]))
                res[i][j] = temp
        return res
    else:
        print(" no se pueden multiplicar")
        return False


def matriporvecto_h(a, v):
    return multiplicacionMatriz(a, transpuestaVector_h(v))


def matriporvecto_v(a, v):
    return multipliMatri(a, v)


def matriHermi(a):
    if len(a) == len(a[0]):
        temp = transpMatri(a)
        temp = conjuMatri(temp)
        if temp == a:
            return True
        else:
            return False
    else:
        print("no  cuadrada")
        return False


def matriUni(a):
    if len(a) == len(a[0]):
        temp = transpMatri(a)
        temp = conjuMatri(temp)
        c = multipliMatri(a, temp)
        d = multipliMatri(temp, a)
        if c == d:
            return True
        else:
            return False
    else:
        print("no  cuadrada")
        return False


def tenMatri(a, b):
    res = []
    for i in range(len(a)):
        for j in range(len(b)):
            c = []
            for x in range(len(a[i])):
                for y in range(len(b[j])): c.append(multipli(a[i][x], b[j][y]))
            res.append(c)

    return res


def imprimir_matriz(a):
    for i in range(len(a)):
        print(a[i])

