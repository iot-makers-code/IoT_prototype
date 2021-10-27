#t0: 기본 기능을 배치한다.
#t1: 반복해서 처리할 수 있다.
import random
import time

#단어장
w = ['cat', 'fox', 'dog', 'monkey']
start = time.time()
print("start time :{:.2f}".format(start))
for i in range(3):
   #추천
   q = random.choice(w)
   #입력
   x = input(q+" :")
   #검사
   if q == x:
      print('pass')
   else:
      print('fail')
end = time.time()
et = end - start
print("time: {:.2f} sec".format(et))   
#출력

