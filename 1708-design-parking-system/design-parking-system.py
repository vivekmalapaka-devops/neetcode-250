class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.carSize = list((big,medium,small))

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.carSize[0]!=0:
                self.carSize[0] = self.carSize[0]-1
                return True
            return False
        if carType == 2:
            if self.carSize[1]!=0:
                self.carSize[1] = self.carSize[1]-1
                return True
            return False
        if carType == 3:
            if self.carSize[-1]!=0:
                self.carSize[-1] = self.carSize[-1]-1
                return True
            return False  
            

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)