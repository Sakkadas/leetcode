class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.store_big = big
        self.store_med = medium
        self.store_sml = small

    def addCar(self, carType):
        # Computing space for park lots
        if carType == 1:
            if self.store_big > 0:
                self.store_big -= 1
                return True
            else:
                return False
        elif carType == 2:
            if self.store_med > 0:
                self.store_med -= 1
                return True
            else:
                return False
        elif carType == 3:
            if self.store_sml > 0:
                self.store_sml -= 1
                return True
            else:
                return False


parkingSystem = ParkingSystem(1, 1, 0)
print(parkingSystem.addCar(1))
print(parkingSystem.addCar(2))
print(parkingSystem.addCar(3))
print(parkingSystem.addCar(1))
