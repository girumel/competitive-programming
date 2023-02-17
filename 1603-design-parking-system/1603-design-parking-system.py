class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big_slot = big
        self.medium_slot = medium
        self.small_slot = small        

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.big_slot > 0:
            self.big_slot -= 1
            return True
        elif carType == 2 and self.medium_slot > 0:
            self.medium_slot -= 1
            return True
        elif carType == 3 and self.small_slot > 0:
            self.small_slot -= 1  
            return True
        else:
            return False
            


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)