class Car:
    def __init__(self, driver: "Driver"):
        self.driver = driver

    def drive(self):
        print(f"Car is being driven by {self.driver.name}")


class CarProxy:
    def __init__(self, driver: "Driver"):
        self.driver = driver
        self._car = Car(driver)

    def drive(self):
        if self.driver.age >= 16:
            self._car.drive()
        else:
            print("Driver too young")


class Driver:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


if __name__ == "__main__":
    d = Driver(name="John", age=12)
    c = CarProxy(driver=d)
    c.drive()
