import heapq as hq

class ParkingLot:
    def __init__(self):
        self.available_parkinglots = []
        self.slot_car_mapping = dict()
       
    def create_parking_lot(self,in_slots):
        print("Created a parking lot with {} slots".format(in_slots))
        for s in range(1,in_slots+1):
            hq.heappush(self.available_parkinglots,s)
        return True
        
    def getNearestEmptySlot(self):
        if self.available_parkinglots:
            return hq.heappop(self.available_parkinglots)
        else:
            return -1
    
    def park(self,car):
        slot = self.getNearestEmptySlot()
        if slot == -1:
            print("Sorry, parking lot is full")
            return
        print("Allocated slot number: {}".format(slot))
        self.slot_car_mapping[slot] = car
        return slot
    
    def leave(self,tobe_free_slot):
        req_carID = -1
        for slot,car in self.slot_car_mapping.items():
            if tobe_free_slot == slot:
                req_carID = car.get_car_id()
                
        if req_carID != -1:
            hq.heappush(self.available_parkinglots,tobe_free_slot)
            del self.slot_car_mapping[tobe_free_slot]
            print("Slot number {} is free".format(tobe_free_slot))
            return True
        else:
            print("Slot number {} is not in use".format(tobe_free_slot))
            return False
        
    def getStatus(self):
        print("Slot No.\tID\tColor")
        for slot,car in self.slot_car_mapping.items():
            print("{}\t\t{}\t{}".format(slot,car.get_car_id(),car.get_car_color()))
        return True
    
    def ids_for_cars_with_color(self,reqcolor):
        carIDList = []
        for slot,car in self.slot_car_mapping.items():
            if car.get_car_color() == reqcolor:
                carIDList.append(car.get_car_id())
        if carIDList:
            print(", ".join(map(str,carIDList)))
            return carIDList
        else:
            print("No cars parked in parkinglot with {} color".format(reqcolor))
            return False
        
    def slot_numbers_for_cars_with_color(self,reqcolor):
        slotList = []
        for slot,car in self.slot_car_mapping.items():
            if car.get_car_color() == reqcolor:
                slotList.append(slot)
        if slotList:
            print(", ".join(map(str,slotList)))
            return slotList
        else:
            print("No slots parked with {} color car in parkinglot".format(reqcolor))
            return False
        
    def slot_number_for_id(self,carID):
        reqslot = 0
        for slot,car in self.slot_car_mapping.items():
            if car.get_car_id() == carID:
                reqslot = slot
        if reqslot > 0:
            print(reqslot)
            return reqslot
        else:
            print("Not Found")
            return False