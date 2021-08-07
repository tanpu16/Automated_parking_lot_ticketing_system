from parking_lot import ParkingLot
from car import Car

pl = ParkingLot()

cars = [Car('EUS687', 'White'),Car('510IBD', 'White'),Car('6TRJ24', 'Black'),
		Car('EK3333', 'Red'),Car('IYTE32', 'Blue'),Car('MNG728', 'Black')]
	
assert pl.create_parking_lot(6) is True
assert len(pl.available_parkinglots) == 6
for i in range(0, len(cars)):
    assert pl.park(cars[i]) == i + 1
    
assert len(pl.available_parkinglots) == 0
assert pl.leave(4) is True
assert len(pl.available_parkinglots) == 1
assert pl.getStatus() is True
assert pl.park(Car('AU7367', 'White')) == 4

assert pl.ids_for_cars_with_color('White') == ['EUS687', '510IBD','AU7367']
assert pl.slot_numbers_for_cars_with_color('White') == [1, 2, 4]
assert pl.slot_number_for_id('MNG728') == 6
assert pl.slot_number_for_id('045BKRf') is False