class AutoParking:
    id_count = [1]
    def __init__(self):
        self.angars = []

    def add_angars(self,*args):
        for arg in args:
            self.angars.append(arg)

    def insert_car(self, car):
        for angar in self.angars:
            if angar.insert_car_angar(car):
                car.set_id(self.id_count[0])
                self.id_count[0] +=1
                return car.get_id()
        return False

    def extract_car(self,id):
        for angar in self.angars:
            if angar.check_car_angar(id):
                return angar.extract_car_angar(id)
        return False







class Angar:
    def __init__(self):
        self.boxes = []

    def add_boxes(self,*args):
        for arg in args:
            self.boxes.append(arg)
        #STRANGE



    def insert_car_angar(self,car):
        # SIMILAR NAMES
        for box in self.boxes:
            if box.insert_car_box(car):
                return True
        return False

    def extract_car_angar(self,id):
        for box in self.boxes:
            if box.check_id(id):
                return box.extract_car_box()
        return False

    def check_car_angar(self,id):
        for box in self.boxes:
            if box.check_id(id):
                return True
        return False













class Box:
    def __init__(self, length, width, height, weight):
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight
        self.content = []


    def insert_car_box(self, car):
        if self.length > car.get_length() and self.width > car.get_width() and self.height > car.get_height() and self.weight > car.get_id() and not self.content:
            self.content += [car]
            return True
        else:
            return False


    def extract_car_box(self):
        if self.content:

            safe_car = self.content.pop()
            safe_car.set_id(0)
            return safe_car
        else:
            return False

    def check_id(self,id):
        if self.content:
            if self.content[-1].get_id() == id:
                return True




class Car:
    def __init__(self, length, width, height, weight):
        self.length =length
        self.width = width
        self.height = height
        self.weight = weight
        self.id = 0

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def get_id(self):
        return self.id

    def set_id(self,value):
        self.id = value


#Проверочный код
firstAutoParking = AutoParking()

firstAngar = Angar()
secondAngar = Angar()

firstBox = Box(10,10,10,100)
secondBox = Box(20,20,20,200)
thirdBox = Box(20,20,20,200)
fourthBox = Box(10,10,10,100)

firstCar = Car(9,9,9,99)  #влезает в первый бокс
secondCar= Car(19,19,19,199)  #влезает в второй бокс
thirdCar = Car(29,29,29,299)  #никуда не влезает
fourthCar = Car(9,9,9,99) # влезает в третий бокс
fifthCar = Car(6,5,4,60)  #влезает в четвертый бокс

firstAutoParking.add_angars(firstAngar,secondAngar)

firstAngar.add_boxes(firstBox,secondBox,thirdBox)
secondAngar.add_boxes(fourthBox)

firstAutoParking.insert_car(firstCar)
firstAutoParking.insert_car(secondCar)
firstAutoParking.insert_car(thirdCar)
firstAutoParking.insert_car(fourthCar)
firstAutoParking.insert_car(fifthCar)

print(firstAutoParking.extract_car(3))
firstAutoParking.extract_car(1)
firstAutoParking.extract_car(2)