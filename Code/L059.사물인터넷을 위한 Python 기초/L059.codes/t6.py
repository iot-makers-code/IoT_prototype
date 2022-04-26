#t0: 기본 기능을 배치한다.
#t1: 반복해서 처리할 수 있다.
#t2: 성공과 실패를 적용한다.
import random
import time

#단어장
with open("animals.txt", "r") as anilist:
    animals=anilist.readlines()
for a in animals:
   print("[{}]".format(a), end=", ")
animals = "".join(animals)

import re
w = re.sub("([0-9\.\\n])*","",animals).split(" ")

#w = ['cat', 'fox', 'dog', 'monkey']
for a in w:
   print("[{}]".format(a), end=", ")
   
cgt=cbt=0.0
good=bad=0

#비교조건 확인
scase = input("\nCase sentitive [Y/n]?")
if scase == "": scase = 'Y'
scase = 'Y' if (scase[0:1].upper() == 'Y') else "N"

for i in range(3):
   #추천
   q = random.choice(w)
   #입력
   start = time.time()
   x = input(q+" :")

   #검사조건 적용
   if scase == 'N':
      match = (q.upper() == x.upper())
   else:
      match = (q == x)
      
   #검사
   if match:
      print('pass')
      good += 1 #good = good + 1
      cgt = cgt + (time.time()-start)
   else:
      print('fail')
      bad += 1
      cbt = cbt + (time.time()-start)
#결과
print("time: {:.2f} sec "\
      "(good: {:.2f}/{}, bad: {:.2f}/{})"\
      .format(cgt+cbt, cgt, good, cbt, bad))
