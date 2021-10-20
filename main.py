def citire_lista():
    lista = [int(elem) for elem in input('Introduceti elementele separate prin cate un spatiu').split(' ')]
    return lista


def print_menu():
    print('''
1. Citire lista
2. Afisare numere negative
3. Afisare cel mai mic numar cu ultima cifra egala cu cea citita
4. Afisare numere superprime
5. Afisare lista obtinuta din lista initiala in care numerele pozitive si nenule au fost inlocuite cu CMMDC-ul lor si numerele negative au cifrele in orgine inversa 
x. Iesire / Stop   
    ''')


# Problema 2
def afisare_numere_negative(lista: list):
    '''
    Afișarea tuturor numerelor negative nenule din listă (de ex. -1, -56).
    :param lista: lista
    :return: lista cu numerele negative
    '''
    lista_finala = []
    for elem in lista:
        if elem < 0:
            lista_finala.append(elem)
    return lista_finala


def test_afisare_numere_negative():
    assert afisare_numere_negative([1, -1, 0, 3, -3, 5, -4, 10, -20]) == [-1, -3, -4, -20]
    assert afisare_numere_negative([1, 0, -1, -3, 0, 2]) == [-1, -3]


# Problema 3
def afisare_numar_mic_egal_cu_cifra_introdusa(lista, cifra):
    '''
    Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.
    :param lista: lista
    :return: numarul
    '''
    min = 100
    for elem in lista:
        if elem % 10 == cifra and min > elem:
            min = elem
    return min


def test_afisare_numar_mic_egal_cu_cifra_introdusa():
    assert afisare_numar_mic_egal_cu_cifra_introdusa([1, 6, 34, 68, 40, 48, 20], 8) == 48
    assert afisare_numar_mic_egal_cu_cifra_introdusa([1, 123, 123, 12, 31, 23, 123, 543, 34, 65, 645], 3) == 23
    assert afisare_numar_mic_egal_cu_cifra_introdusa([11, 21, 31, 41, 51, 61, 71, 81, 91], 1) == 11
    assert afisare_numar_mic_egal_cu_cifra_introdusa([21, 31, 41, 51, 61, 71, 81, 91, 11], 1) == 11


# Problema 4
def prim(numar):
    '''
    Verifica daca numarul este prim
    :param numar: numarul
    :return: True daca este prim sau False daca nu este
    '''
    if numar < 2:
        return False
    if numar == 2 or numar == 3:
        return True
    if numar % 2 == 0 or numar % 3 == 0:
        return False
    for i in range(3, numar // 2, 2):
        if numar % i == 0:
            return False
    return True


def superprim(lista):
    '''
    Afișarea tuturor numerelor din listă care sunt superprime. Un număr este superprim dacă este
strict pozitiv și toate prefixele sale sunt prime. De exemplu, 173 nu este superprim deoarece 1 nu
este prim, iar 239 este superprim deoarece 2, 23 și 239 sunt toate prime.
    :param lista: lista
    :return: lista cu numerele superprime
    '''
    lista_finala = []
    for elem in lista:
        string_elem = str(elem)
        lungime_numar = len(string_elem)
        memorare = True
        for cifre in range(0, lungime_numar):
            numarul = str(string_elem[0:cifre + 1])
            if prim(int(numarul)) is True:
                memorare = True
            else:
                memorare = False
                break

        if memorare is True:
            lista_finala.append(elem)

    return lista_finala


def test_superprim():
    assert superprim([239, 1, 123, 23]) == [239, 23]
    assert superprim([239, 1, 12, 3, 33, 37]) == [239, 3, 37]


# Problema 5
def CMMDC(numarul_1, numarul_2):
    while numarul_1 != numarul_2:
        if numarul_1 > numarul_2:
            numarul_1 -= numarul_2
        else:
            numarul_2 -= numarul_1
    return numarul_1


def inversul_numarului(numar):
    '''
    Calculeaza inversul numarului
    :param numar: numarul
    :return: inversul lui
    '''
    invers = 0
    while numar != 0:
        rest = numar % 10
        invers = invers * 10 + rest
        numar //= 10

    return invers


def afisare_numere_din_lista_initiala(lista):
    '''
    Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu
CMMDC-ul lor și numerele negative au cifrele în ordine inversă.
    :param lista: lista
    :return: lista finala
    '''
    lista_finala = []
    cmmdc = 0
    for elem in lista:
        if elem > 0:
            if cmmdc == 0:
                cmmdc = elem
            lista_finala.append(CMMDC(cmmdc, elem))
        if elem < 0:
            elementul_inversat = -inversul_numarului(-elem)
            lista_finala.append(elementul_inversat)

    return lista_finala


def test_inversul_numarului():
    assert inversul_numarului(123) == 321
    assert inversul_numarului(321) == 123


def test_afisare_numere_din_lista_initiala():
    assert afisare_numere_din_lista_initiala([-76, 12, 24, -13, 144]) == [-67, 12, 12, -31, 12]


def teste():
    test_afisare_numere_negative()x`
    test_afisare_numar_mic_egal_cu_cifra_introdusa()
    test_superprim()
    test_inversul_numarului()
    test_afisare_numere_din_lista_initiala()


def meniu():
    teste()
    lista = []
    while True:
        print_menu()
        cmd = input('Introduceti comanda: ')
        if cmd == '1':
            lista = citire_lista()[:]
        elif cmd == '2':
            print(afisare_numere_negative(lista))
        elif cmd == '3':
            cifra = int(input('Introduceti cifra: '))
            print(afisare_numar_mic_egal_cu_cifra_introdusa(lista, cifra))
        elif cmd == '4':
            print(superprim(lista))
        elif cmd == '5':
            print(afisare_numere_din_lista_initiala(lista))
            pass
        elif cmd == 'x':
            break
        pass


meniu()
