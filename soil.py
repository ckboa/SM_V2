import time
from machine import ADC, Pin 

adc35 = ADC(Pin(35))        
adc35.read()               

#adc35.atten(ADC.ATTN_11DB)    
adc35.width(ADC.WIDTH_12BIT)   
adc35.read()  
while(1):
  print(adc35.read())
  time.sleep(1)
  
