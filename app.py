import serial.tools.list_ports # pip install pyserial

ports = serial.tools.list_ports.comports() # list of COM ports
serialInst = serial.Serial()
portsList = [] #starting with an empty list 


for one in ports:
    portsList.append(str(one))
    print(str(one)) # detecting all the COM ports


com = input("Select COM port # for Arduino being connected: ")

for i in range(len(portsList)):
    if portsList[i].startswith("COM" + str(com)):
        use = "COM" + str(com)
        print(use)


# Setup the Serial Port
serialInst.baudrate = 9600
serialInst.port = use
serialInst.open()


# Exit using the word "Exit"
while True:
    command = input("Arduino Command (ON/OFF/exit): ")
    serialInst.write(command.encode('utf-8'))
    
    if command == 'exit': #exit
        exit()

    
