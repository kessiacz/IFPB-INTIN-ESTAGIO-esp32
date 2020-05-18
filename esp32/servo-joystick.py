import machine
from machine import Pin, PWM, ADC

potenciometro = ADC(Pin(34))
potenciometro.atten(ADC.ATTN_11DB)
potenciometro.width(ADC.WIDTH_12BIT)

while True:
  leitura = potenciometro.read()
  leitura = leitura * 3.3 / 4095
  
  if leitura == 0.0 or leitura == 00.0 or leitura == 0.00:
    servo = PWM(Pin(2), freq=100)
    servo.duty(250)
    
  elif leitura == 3.3:
    servo = PWM(Pin(2), freq=100)
    servo.duty(40)

  else:
    servo = PWM(Pin(2), freq=100)
    servo.duty(0)



