#pl_auto_ticketing.py
from parking_lot import ParkingLot
from car import Car

pl = ParkingLot()

def pl_auto_ticketing_process(param):
    param_list = param.strip().split(' ')
    command = param_list[0]
        
    if command == 'create_parking_lot':
        if len(param_list) != 2: 
            print("Invalid number of arguments")
        elif param_list[1].isdigit() == False:
            print("Invalid! Number of slots should be Integer type")
        else:
            pl.create_parking_lot(int(param_list[1]))
    elif command == 'park':
        if len(param_list) !=3:
            print("Invalid number of arguments")
        elif (not param_list[1].isalnum()) or len(param_list[1]) !=6:
            print("Invalid! carID is not alphanumeric or length of carID is not 6")
        elif param_list[2].isalpha() == False:
            print("Invalid! Color should be String type")
        else:
            car = Car(param_list[1],param_list[2])
            pl.park(car)
    elif command == 'leave':
        if len(param_list) != 2: 
            print("Invalid number of arguments")
        elif param_list[1].isdigit() == False:
            print("Invalid! slot should be Integer type")
        else:
            pl.leave(int(param_list[1]))
    elif command == 'status':
        pl.getStatus()
    elif command == 'ids_for_cars_with_color':
        if len(param_list) != 2: 
            print("Invalid number of arguments")
        elif param_list[1].isalpha() == False:
            print("Invalid! Color should be String type")
        else:
            pl.ids_for_cars_with_color(param_list[1])
    elif command == 'slot_numbers_for_cars_with_color':
        if len(param_list) != 2: 
            print("Invalid number of arguments")
        elif param_list[1].isalpha() == False:
            print("Invalid! Color should be String type")
        else:
            pl.slot_numbers_for_cars_with_color(param_list[1])
    elif command == 'slot_number_for_id':
        if len(param_list) != 2: 
            print("Invalid number of arguments")
        elif (not param_list[1].isalnum()) or len(param_list[1]) !=6:
            print("Invalid! carID is not alphanumeric or length of carID is not 6")
        else:
            pl.slot_number_for_id(param_list[1])
    elif command == 'exit':
        exit(0)
    else:
        raise Exception("Incorrect command")