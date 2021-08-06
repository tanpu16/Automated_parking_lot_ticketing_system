class Car:
    def __init__(self,carID,carColor):
        self.carID = carID
        self.carColor = carColor
        
    def get_car_id(self):
        return self.carID
    
    def get_car_color(self):
        return self.carColor