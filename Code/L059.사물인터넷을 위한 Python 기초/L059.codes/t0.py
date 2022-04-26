import random

#단어장
w = ['cat', 'fox', 'dog', 'monkey']
#추천
q = random.choice(w)
#입력
x = input(q+" :")

#검사
if q == x:
   print('pass')
else:
   print('fail')
   
#출력

