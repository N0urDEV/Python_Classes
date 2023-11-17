class Player:
    def __init__(self, name, age, rank):
        self.name = name
        self.age = age
        self.rank = rank

    def pass_ball(self):
        print(f"{self.name} passes the ball.")

    def shoot_ball(self):
        print(f"{self.name} shoots the ball.")

    def jump(self):
        print(f"{self.name} jumps.")

class Car:
    def __init__(self, speed, color, nitrospeed, model):
        self.speed = speed
        self.color = color
        self.nitrospeed = nitrospeed
        self.model = model

    def turn(self):
        print(f"The {self.color} {self.model} turns.")

    def accelerate(self):
        print(f"The {self.color} {self.model} accelerates to {self.speed} mph.")

    def brake(self):
        print(f"The {self.color} {self.model} brakes.")

    def boost(self):
        if self.nitrospeed:
            print(f"The {self.color} {self.model} boosts with nitro speed!")
        else:
            print(f"The {self.color} {self.model} doesn't have nitro speed.")

class Employee:
    def __init__(self, basesalary, bonushrs, sales, name):
        self.basesalary = basesalary
        self.bonushrs = bonushrs
        self.sales = sales
        self.name = name

    def calculatenetsalary(self):
        bonusamount = self.bonushrs * 10 
        commission = 0.05 * self.sales 
        netsalary = self.basesalary + bonusamount + commission
        return netsalary

class Mobile:
    def __init__(self, company_name, storage, serial_num, name, dual_sim, support_4k):
        self.company_name = company_name
        self.storage = storage
        self.serial_num = serial_num
        self.name = name
        self.dual_sim = dual_sim
        self.support_4k = support_4k

    def call(self):
        print(f"{self.name} is making a call.")

    def send_message(self):
        print(f"{self.name} is sending a message.")

    def play_media(self):
        if self.support_4k:
            print(f"{self.name} is playing 4K media.")
        else:
            print(f"{self.name} is playing media.")