# def is_leap_year(year):
#     """
#     gfgjkhgjfhgmhggthfj
#     :param year: ryyfjghjh,iyut
#     :return: uugyjfhvmj,hg
#     """
#
#     if year % 4 == 0:
#         if year % 100 ==0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#
#         else:
#             return False
#
#     else:
#         return False
#
# print(is_leap_year(2000))
from importlib.resources.simple import TraversableReader


def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide (n1, n2):
    return n1/n2

operation = {
    "+": add,
    "_": subtract,
    "*": multiply,
    "/": divide
}
def calculator ():
    anngka_1 =float(input("Masukan angka pertama: "))
    for symbol in operation:
        print(symbol)
    lanjut = True
    while lanjut:

        pilih_operasi = input("pilih operasi: ")
        anngka_2 = float(input("masukan angka kedua: "))
        calculation_function = operation[pilih_operasi]
        answer = calculation_function(anngka_1,anngka_2)
        print(f"{anngka_1}{pilih_operasi}{anngka_2}={answer}")
        mau_lanjut_atau_tidak = input(f"ketik 'y' untuk lanjut hitung dengan {answer}, atau 'n' untuk selesai:").lower()
        if mau_lanjut_atau_tidak == "y":
            anngka_1=answer
        else :
            lanjut = False
            print("calculator selesai")

calculator()


















