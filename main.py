#XadievDev
#38-lesson.Standart kutubxona

#-----------------------------------------------#

# import datetime as dt

# hozir = dt.datetime.now()
# print(hozir)
# print(hozir.date())
# print(hozir.time())
# print(hozir.second)
#-----------------------------------------------#

# bugun = dt.date.today()
# print(bugun)

#-----------------------------------------------#

# import math

# print(math.e)
# print(math.cos(0))
# print(math.log(5))
# print(math.log10(100))
# print(math.ceil(4.6))
# print(math.floor(4.6))
# print(math.pow(4,2))
# print(math.sqrt(9))

#-----------------------------------------------#

# from pprint import pprint
# import json

# filename = 'bemor.json'
# with open(filename) as f:
    # bemor = json.load(f)
# pprint(bemor)

#-----------------------------------------------#

import re

word1 = "темир"
word2 = "томир"
word3 = "тулпор"

# andoza = "^т...р"

# print(re.match(andoza, word1))
# print(re.match(andoza, word2))
# print(re.match(andoza, word3))

#-----------------------------------------------#

# from uzwords import words
# andoza = "^т...р$"

# matches = []
# for word in words:
#     if re.match(andoza,word):
#         matches.append(word)
# print(matches)

#-----------------------------------------------#

# matn = """Maqolalar  2020-yilning 20-martiga qadar rtmkonferensiya2021@mail.ru elektron pochtasida qabul qilinadi.
# Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
# 👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
# 👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """

# andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
# email = re.findall(andoza,matn)
# print(email)

#-----------------------------------------------#

# matn = 'Tel nomer: +998912546665'
# andoza = '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
# number = re.findall(andoza,matn)
