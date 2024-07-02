
import datetime
# def fInputAndCheckName(typename):
#     while True:
#         userInput = input(f"Input {typename} :")
#         isLetter = True
#         for letter in userInput:
#             if letter.lower().isalpha() or letter == " " or letter == "-":
#                 continue
#             else:
#                 isLetter = False
#                 break
#         if isLetter == True and userInput != "":
#             return userInput
#         else:
#             print(f"Incorrect {typename}. {typename} should contain only letters, LeerZeichen and '-'")
#
# def fInputAndCheckTitle():
#     while True:
#         userInput = input(f"Input Title :")
#         isLetter = True
#         for letter in userInput:
#             if letter.lower().isalpha() or letter == " " or letter == "-" or letter == ".":
#                 continue
#             else:
#                 isLetter = False
#                 break
#         if isLetter == True and userInput != "":
#             return userInput
#         else:
#             print(f"Incorrect Title. Title should contain only letters, LeerZeichen, Punkt and '-'")
#
# def fInputAndCheckTel():
#     while True:
#         userInput = input(f"Input Telefonnummer :")
#         isNum = True
#         for letter in userInput:
#             if letter.isnumeric() or letter == " " or letter == ")" or letter == "(" or "+":
#                 continue
#             else:
#                 isLetter = False
#                 break
#         if isNum == True and userInput != "":
#             return userInput
#         else:
#             print(f"Incorrect Title. Title should contain only numbers, LeerZeichen, '(', ')', and '+'")
#
#
#
# def fInputAndCheckEmail():
#     while True:
#         userInput = input(f"Input Email :")
#         isLetter = True
#         for letter in userInput:
#             if letter.lower().isalpha() or letter == "." or letter == "@":
#                 continue
#             else:
#                 isLetter = False
#                 break
#         if isLetter == True and userInput != "":
#             return userInput
#         else:
#             print(f"Incorrect Email. Email should contain only letters, LeerZeichen and '-'")

def fInputAndCheckStartDate():
    while True:
        userInput = input(f"Arbeitet im Unternehmen seit (format: dd.mm.yyyy): ")
        dataList = userInput.rsplit(".")
        try:
            startDay = datetime.datetime(dataList[0], dataList[1], dataList[2])
            if startDay <= datetime.datetime.now():
                return userInput
            else:
                continue
        except:
            print(f"Incorrect Date. Format: dd.mm.yyyy")


