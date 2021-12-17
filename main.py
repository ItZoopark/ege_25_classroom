# 27422
# def getDels(x):
#     dels = []
#     for i in range(2, round(x ** 0.5)):
#         if x % i == 0:
#             dels.append(i)
#             dels.append(x // i)
#         if len(dels) > 2:
#             break
#     if len(dels) == 2:
#         return dels
#     return []
#
#
# for x in range(174457, 174505 + 1):
#     res = getDels(x)
#     if len(res) != 0:
#         print(res)
# -----------------------------------------
# 33104
# def isPrime(x):
#     for i in range(2, round(x ** 0.5)):
#         if x % i == 0:
#             return False
#     return True
#
#
# start = round(289123456 ** 0.25)
# finsh = 389123456
# while start ** 4 < finsh:
#     if isPrime(start):
#         print(start ** 4, start ** 3)
#     start += 1
# -------------------------------------------
# 4523












