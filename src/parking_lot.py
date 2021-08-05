import heapq

class ParkingLot:
    def __init__(self):
        self.carID_slot_mapping = dict()
        self.available_parkinglots = []
        self.slot_car_mapping = dict()
        
    def create_parking_lot(self,in_slots):
        print("Created a parking lot with {} lots".format(in_slots))
        for s in range(1,in_slots+1):
            heapq.heappush(self.available_parkinglots,s)
        return True