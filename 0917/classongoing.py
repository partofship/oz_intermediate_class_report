from abc import ABC, abstractmethod # 이게 추상화인가..?

class CaffeineBeverage(ABC):
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pourincup()
        if self.customer_request_condiments():
            self.add_condiments()
    
    @abstractmethod
    def brew(self):
        raise NotImplementedError
    # 만들 순 있는데 일단 이렇게 생략함
    
    @abstractmethod
    def add_condiments(self):
        raise NotImplementedError
    
    def boil_water(self):
        print("boiling water")

    def pourincup(self):
        print("pouring water in cup")

    def customer_request_condiments():
        answer = input("anything to add: Y/N").lower()
        if answer == "y":
            return True
        return False

class Coffee(CaffeineBeverage):
    def brew(self):
        print("coffee is extracting")

class Tea(CaffeineBeverage):
    def steep_tea_bag(self):
        print("찻잎을 우려내는 중")