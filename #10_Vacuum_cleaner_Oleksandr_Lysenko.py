import time

from random import randint


class RobotCleaner:
    class_max_battery_charge = 100
    class_max_filling_garbage = 55
    class_max_amount_of_water = 10

    def __init__(self, battery_charge, filling_garbage, amount_of_water):
        self.battery_charge = battery_charge
        self.filling_garbage = filling_garbage
        self.amount_of_water = amount_of_water

    def move(self):
        while True:
            print("Move!")
            try:
                self.vacuum_cleaner()
                time.sleep(1)
                print('*' * 10)
                self.wash()
                time.sleep(1)
                print('*' * 10)
            except LowBattery as low_battery:
                print(low_battery)
                is_connected = randint(0, 1)
                if is_connected == 1:
                    print('The battery starts...<wait 10 times>')
                    time.sleep(10)
                    self.battery_charge = self.class_max_battery_charge
                    print('Battery charging completed successfully!')
                else:
                    print('Not connected to charging...')
                    self.battery_charge = 10
            except CriticalBattery as critical_battery:
                print(critical_battery)
                print('The battery starts...<wait 10 times>')
                time.sleep(10)
                self.battery_charge = self.class_max_battery_charge
                print('Battery charging completed successfully!')
            except LowWater as low_water:
                print(low_water)
                print('The topping up of water has begun...<wait 3 times>')
                time.sleep(3)
                self.amount_of_water = self.class_max_amount_of_water
                print('The water level was restored successfully!')
            except FullGarbageBag as full_garbage_bag:
                print(full_garbage_bag)
                print('Cleaning of the garbage can has started...<wait 5 times>')
                time.sleep(4)
                self.filling_garbage = 0
                print('The cleaning of the garbage can is completed successfully!')
            finally:
                print("Cleaning is complete. I'm going to sleep!")
                print('*' * 30)

    def vacuum_cleaner(self):
        if not self.check_battery_charge():
            print('Start vacuum cleaning.')
            self.filling_garbage += randint(0, 10)
            if self.filling_garbage >= self.class_max_filling_garbage:
                self.filling_garbage = self.class_max_filling_garbage
            print(f'The garbage bag is {self.filling_garbage} percent full.')
            if not self.check_filling_garbage():
                self.battery_charge -= 10
                print("Finished vacuum cleaning.")

    def wash(self):
        if not self.check_battery_charge():
            if not self.check_water_level():
                print('Start wet cleaning.')
                self.battery_charge -= 10
                self.amount_of_water -= 1
                print("Finished wet cleaning")

    def check_battery_charge(self):
        if 10 < self.battery_charge <= 20:
            raise LowBattery(self.battery_charge)
        elif self.battery_charge <= 10:
            raise CriticalBattery(self.battery_charge)
        else:
            print("I'm READY - battery charge is normal!")

    def check_water_level(self):
        if self.amount_of_water <= 1:
            raise LowWater(self.amount_of_water)
        else:
            print("I'm READY - water level is normal!")

    def check_filling_garbage(self):
        if self.filling_garbage >= self.class_max_filling_garbage:
            raise FullGarbageBag()


class RobotException(Exception):
    pass


class LowBattery(RobotException):
    def __init__(self, charging_level):
        self.charging_level = charging_level

    def __str__(self):
        return f'+++ The current battery charge is {self.charging_level}. Connect the charger! NOW!!! +++'


class CriticalBattery(RobotException):
    def __init__(self, charging_level):
        self.charging_level = charging_level

    def __str__(self):
        return f'+++ The current battery charge is CRITICAL. Take me to charge immediately!! +++'


class LowWater(RobotException):
    def __init__(self, water_level):
        self.water_level = water_level

    def __str__(self):
        return f'+++ The current water level is {self.water_level}. Add water!!! +++'


class FullGarbageBag(RobotException):
    def __str__(self):
        return f'+++ The current garbage level is FULL! Needs cleaning!!! +++'


pitonyaka = RobotCleaner(100, 0, 10)
pitonyaka.move()
