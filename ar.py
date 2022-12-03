import serial
import time

# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM7',115200, timeout=1)

print(ser.close())