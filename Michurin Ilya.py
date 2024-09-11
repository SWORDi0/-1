
import math
#№18
def pip (byte, pages, strokes, simbols):
    peremnozj = pages * strokes * simbols
    bit = byte * 8
    N = bit/peremnozj
    log = 2 ** N
    print(str(log) + " Количество букв в алфавите")


#№19
def ziz (powerz1,powerz2):
    alfm1 = math.log2(powerz1)
    alfm2 = math.log2(powerz2)
    diff = alfm2/alfm1
    print(str(diff)+ " разница между алфавитами")

#№20
def jij (simbols, bit):
    logz = math.log2(simbols)
    otvet = bit/logz
    print(str(otvet) + " количество символов в сообщении")
    inp7 = input("количество символов в алфавите: ")
    inp8 = input("количество бит: ")
    jij(int(inp7), int(inp8))
#№19
def vivo (bit):
    tat = 2 ** bit
    print(str(tat) + " Количество этажей в доме")

#№20
def vpivo (bit):
    tat1 = 2 ** bit
    print(str(tat1) + " Количество подъездов в доме")


#№7
def task(i, K):
    N = 2**i * K
    WB = 8 + 8
    Brown = N - WB
    return Brown


if __name__ == "__main__":
    inp1 = input("количество байт: ")
    inp2 = input("количество cтраниц: ")
    inp3 = input("количество строк: ")
    inp4 = input("количество символов: ")
    pip(int(inp1), int(inp2), int(inp3), int(inp4))
    inp5 = input("мощность алфавита№1: ")
    inp6 = input("мощность алфавита№2: ")
    ziz(int(inp5), int(inp6))
    inp9 = input("информации об этаже: ")
    vivo(int(inp9))
    inp10 = input("информации о подъезде: ")
    vpivo(int(inp10))
    inp11 = int(input("Введите вес 1 банки белой краски: "))
    inp12 = int(input("Введите количество банок синей краски: "))
    print("Количество банок коричневой краски:  ", task(inp11, inp12))






