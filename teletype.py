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

stdin = os.fdopen(sys.stdin.fileno(), 'rb', buffering=0)
stdout = os.fdopen(sys.stdout.fileno(), 'wb', buffering=0)
stderr = os.fdopen(sys.stderr.fileno(), 'rb', buffering=0)
flag = fcntl.fcntl(sys.stdin.fileno(), fcntl.F_GETFD)
fcntl.fcntl(sys.stdin.fileno(), fcntl.F_SETFL, flag | os.O_NONBLOCK)
flag = fcntl.fcntl(sys.stdout.fileno(), fcntl.F_GETFD)
fcntl.fcntl(sys.stdout.fileno(), fcntl.F_SETFL, flag | os.O_NONBLOCK)
flag = fcntl.fcntl(sys.stderr.fileno(), fcntl.F_GETFD)
fcntl.fcntl(sys.stderr.fileno(), fcntl.F_SETFL, flag | os.O_NONBLOCK)

input=1

#stdout.write(b"echo -n \"$(pwd)\\nSKYNET> \" \n")
while 1 :
    # get term output
    input = stdin.read(1)
    if input:
        if input==b"\n":
            ser.write(b"\r\n")
        else:
            ser.write(input)
        ser.flush()

    # get term output
    input = stderr.read(1)
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
            #ser.write(b"\r\n")
#            stdout.write(b"echo -n \"$(pwd)\\nSKYNET> \" \n")
        else:
            #ser.write(out)
            stdout.write(out)
        stdout.flush()