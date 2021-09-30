<pre>
여러개 LED 켜기는
1. GPIO에 대한 동시 제어 방법을 배우고
2. 여러 LED를 효과적으로 제어하는 알고리즘을 배운다.

사용 코드 설명
led.py : GPIO18에서 LED켜기
led2.py : GPIO24에서 LED켜기
led_2s.py : GPIO18, 24에서 동시 LED켜기
led_3s.py : GPIO18, 24, 21에서 동시 LED켜기
led_ns.py : GPIO18, 24, 21, ....에서 LED켜기, 코드 재구성#1
led_nsn.py : GPIO18, 24, 12, 16에서 LED켜기, 코드 재구성#2
led_up.py : GPIO18, 24, 12, 16에서 LED켜기, 코드 단순화

led_2gpio.py : GPIO23, GPIO24에서 LED켜기
led_3v.py : GPIO18과 3.3v전원 또는 5v전원을 연결하여 LED켜기

</pre>
