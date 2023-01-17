import serial

# for generic GPS module connected to a computer via a serial connection
# arguments - serial port and baudrate
# returns - raw NMEA data from the GPS module

import serial

def read_gps(port, baudrate):
    try:
        # open serial connection
        ser = serial.Serial(port, baudrate)
        # variable to store the data
        data = ""
        while True:
            # read a line of data from the GPS module
            raw_data = ser.readline()
            # check if the data is not empty
            if len(raw_data)> 0:
                # decode the data and store it in the data variable
                data = raw_data.decode("utf-8")
                print(data)
    except serial.SerialException as e:
        # handle any serial connection errors
        print(f'An error occurred: {e}')
    except Exception as e:
        # handle any other errors
        print(f'An error occurred: {e}')
    finally:
        # close serial connection
        ser.close()
        return data

