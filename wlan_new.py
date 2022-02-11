from time import sleep_ms
import network
import config

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(config.wifi_ssid(), config.wifi_password())
while not wlan.isconnected():
    sleep_ms(100)
print('Network config:', wlan.ifconfig())
sleep_ms(2000)



