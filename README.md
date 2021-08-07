# parking_lot

Name : Priyanka Prakash Tanpure
Email address : priyankatanpure1995@gmail.com

Programming Language : Python
Tested on Linux and Windows

Files included:
1. bin folder (Permissin need to be changed for setup and parking_lot -> chmod 777 <filename> or chmod x+ <filename>)
	a. setup : No need to install dependencies, compilation and bulit not required
			   Added script to run the unit test suit
					
	b. parking_lot : Added Script to run code in both ways (file input and Interactive)
	
2. src folder
	a. car.py : Car class and required methods
	b. parking_lot.py : ParkingLot class and required methods
	c. pl_auto_ticketing.py : pl_auto_ticketing_process method which perform parking lot operations by calling methods from car.py and parking_lot.py
	d. driver.py : take command line arguments and call pl_auto_ticketing_process method from pl_auto_ticketing.py accordingly
	e. test.py : unit test suit
	d. input folder : input files (valid and invalid)

Check for alphanumeric car ID : only carID's having both alphabets and numbers are accepted (ex 514KZE) with size 6


How to Run:
$ bin/setup						   #unit test suit
$ bin/parking_lot 				   #for interactive
$ bin/parking_lot <input file path>    #for file input ($ bin/parking_lot inputfile.txt)
(Put inputfile.txt in project root directory or else provide absolute path)



