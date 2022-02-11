import network
import time
from machine import Pin, Timer
import dht
from microWebSrv import MicroWebSrv

led = Pin(2, Pin.OUT)

sensor = dht.DHT22(Pin(15))

tm = Timer(0) 

def receiveData(webSocket, msg):
    if msg == "LED_ON":
        print(msg)
        led.value(1)
    elif msg == "LED_OFF":
        print(msg)
        led.value(0)
    else:
        print("Msg: %s" %msg)

    webSocket.SendText("Reply: %s" %msg)

def closed(webSocket):
    tm.deinit()
    print("(server)Close.., Stop Timer")

    
def reading_sensor_timer(timer, websocket):
    print("sensor reading")
    sensor.measure()
    newtemp = sensor.temperature()
    print(newtemp)
    websocket.SendText("temp %s" %newtemp) 
      
    newhumi = sensor.humidity()
    print(newhumi) 
    websocket.SendText("humi %s" %newhumi) 
      
    
def _acceptWebSocketCallback(webSocket, httpClient):
    webSocket.RecvTextCallback = receiveData
    webSocket.ClosedCallback = closed
    cb = lambda timer: reading_sensor_timer(timer, webSocket)  
    tm.init(period=3000, callback=cb)  
    print("(server)Connect..")


# start server
mws=MicroWebSrv(webPath='')
print("server started")
mws.MaxWebSocketRecvLen     = 256
mws.WebSocketThreaded       = True
mws.AcceptWebSocketCallback = _acceptWebSocketCallback
mws.Start(threaded=False)
# sending data 




