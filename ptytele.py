import time
import serial
import sys
import select
import os
import fcntl

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/cu.usbserial-AL01FCH5',
    baudrate=300,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)

ser.isOpen()

#print 'Enter your commands below.\r\nInsert "exit" to leave the application.'

stdin = open("/dev/ptyp1", 'ab+', buffering=0)
stdout = stdin
#flag = fcntl.fcntl(stdin.fileno(), fcntl.F_GETFD)
#fcntl.fcntl(sys.stdin.fileno(), fcntl.F_SETFL, flag | os.O_NONBLOCK)
#flag = fcntl.fcntl(sys.stdout.fileno(), fcntl.F_GETFD)
#fcntl.fcntl(sys.stdout.fileno(), fcntl.F_SETFL, flag | os.O_NONBLOCK)

input=1
while 1 :
    # get keyboard input
    input = stdin.read(1)
    if input:
        if input==b"\n":
            ser.write(b"\r\n")
        else:
            ser.write(input)
        ser.flush()
    # let's wait one second before reading output (let's give device time to answer)
    #time.sleep(1)
    if ser.inWaiting() > 0:
        out = ser.read(1)
        if out==b"\r":
            stdout.write(b"\n")
            stdout.write(b"echo -n \"SKYNET>\" \n")
        else:
            stdout.write(out)
        stdout.flush()