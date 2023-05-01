import serial
import matplotlib.pyplot as plt
from drawnow import *

humidity = [] # Nem değerlerini saklamak için bir dizi

arduinoData = serial.Serial('/dev/ttyUSB0', 9600) # Arduino seri portuna bağlanın
plt.ion() # Gerçek zamanlı çizim için interaktif modu etkinleştirin

def plotHumidity():
    plt.title('Nem Oranı Grafiği')
    plt.grid(True)
    plt.ylabel('Nem Oranı (%)')
    plt.plot(humidity, '-ro', label='Nem Oranı')
    plt.legend(loc='upper left')

while True:
    while (arduinoData.inWaiting()==0):
        pass # Arduino'dan veri bekleyin
    arduinoString = arduinoData.readline().decode().strip()
    humidity.append(float(arduinoString))
    drawnow(plotHumidity)