#t0: 기본 기능을 배치한다.
#t1: 반복해서 처리할 수 있다.
#t2: 성공과 실패를 적용한다.
import random
import time

#단어장
animals="""1. Ant
2. Antelope
3. Baboon
4. Bat
5. Beagle
6. Bear
7. Bird
8. Butterfly
9. Cat
10. Caterpillar
11. Chicken
12. Cow
13. Dog
14. Dolphin
15. Donkey
16. Eagle
17. Fish
18. Fly
19. Fox
20. Frog
21. Gerbil
22. Goose
23. Gopher
24. Gorilla
25. Heron
26. Honey Bee
27. Horn Shark
28. Horse
29. Ibis
30. Iguana
31. Impala
32. Jackal
33. Jaguar
34. Javanese
35. Jellyfish
36. Kakapo
37. Kangaroo
38. King Penguin
39. Kiwi
40. Koala
41. Lemming
42. Lemur
43. Leopard
44. Saola
45. Scorpion
46. Snake
47. Swan
48. Tuatara
49. Turkey
50. Zebra"""

w = animals.replace("\n"," ")\
    .replace(".","")\
    .replace("0","")\
    .replace("1","")\
    .replace("2","")\
    .replace("3","")\
    .replace("4","")\
    .replace("5","")\
    .replace("6","")\
    .replace("7","")\
    .replace("8","")\
    .replace("9","")\
    .replace("  "," ")\
    .split(" ")
#w = ['cat', 'fox', 'dog', 'monkey']
for a in w:
   print("[{}]".format(a), end=", ")
   
cgt=cbt=0.0
good=bad=0
for i in range(3):
   #추천
   q = random.choice(w)
   #입력
   start = time.time()
   x = input(q+" :")
   #검사
   if q == x:
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


