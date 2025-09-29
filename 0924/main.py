from abc import ABC, abstractmethod

# D: 인터페이스
# 추 상 화
class Pizza(ABC):
    def __init__(self, name:str):
        self.name = name
    
    @abstractmethod
    def pizza_prepare(self)-> None: # 스타일별로 다름!
        raise NotImplementedError

    def pizza_order(self) -> None:
        print(f"{self.name} 피자 주문을 받습니다.")

    def slice_my_pizza(self) -> None:
        print(f"{self.name} 피자를 자릅니다.")

    def box_my_pizza(self) -> None:
        print(f"{self.name} 피자를 박스에 담습니다.")

    def deliver_my_pizza(self) -> None:
        print(f"{self.name} 피자를 배송 중.")

# B: 팩토리. 알고리즘의 틀 보유
# 사실상 이것부터 먼저 짜야 함.
# 1. 어떤 피자를 만들지 결정. 생성 책임을 하위로 위임
# 2. 탬플릿 메서드! 공통 절차(흐름)은 고정.
class PizzaMasterCompany(ABC):
    @abstractmethod
    def factory_method(self, pizza_type: str) -> Pizza:
        pass

# 탬플릿 메서드, 공통 절차는 고정.
    def pizza_process(self, pizza_type: str) -> None:
        print(f"\n ===== {pizza_type} 피자 주문 처리 =====")
        pizza = self.factory_method(pizza_type) # 위에 있는 팩토리 메서드 있죠? 그걸로 피자 인스턴스를 생성합니다.
        
        # 프로세스 처리 단계.
        pizza.pizza_order()
        pizza.pizza_prepare()
        pizza.slice_my_pizza()
        pizza.box_my_pizza()
        pizza.deliver_my_pizza()

        print(f" ===== {pizza_type} 피자 주문 완료 ===== ")

# C: ConcreteCreator
# 여기서 실제 구현을 진행한다.
# Creator - Seoul
class SeoulStore(PizzaMasterCompany):
    def factory_method(self, pizza_type: str) -> Pizza:
        if pizza_type == "Combination":
            return SeoulCombinationPizza()
        elif pizza_type == "4 Cheese":
            return SeoulQuatroCheese()
        else:
            raise ValueError(f"서울 지점에는 {pizza_type}이 없습니다.")

# Creator - Busan
class BusanStore(PizzaMasterCompany):
    def factory_method(self, pizza_type: str) -> Pizza:
        if pizza_type == "Pepperoni":
            return BusanPepperoniPizza()
        elif pizza_type == "Shrimp":
            return BusanShrimpPizza()
        else:
            raise ValueError(f"부산 지점에는 {pizza_type}이 없습니다.")

# C : ConcreteProduct
# 구체적인 예시 - 서울에서 파는 피자, 부산에서 파는 피자.
class SeoulQuatroCheese(Pizza):
    def __init__(self):
        super().__init__("4 Cheese")
    
    def pizza_prepare(self) -> None:
        print("4 Cheese Pizza going")

class SeoulCombinationPizza(Pizza):
    def __init__(self):
        super().__init__("Combination")
    
    def pizza_prepare(self) -> None:
        print("Combination Pizza going")

class BusanPepperoniPizza(Pizza):
    def __init__(self):
        super().__init__("Pepperoni")
    
    def pizza_prepare(self) -> None:
        print("마 니 무봤나 뻬뻐로니피자")

class BusanShrimpPizza(Pizza):
    def __init__(self):
        super().__init__("Shrimp")
    
    def pizza_prepare(self):
        print("새우 양식은 부산이 아니라는 사실")

# A: 클라이언트
if __name__ == "__main__":
    print(" 🍕 Pizza Day ")
    
    seoul_store = SeoulStore()
    seoul_store.pizza_process("4 Cheese")
    seoul_store.pizza_process("Combination")

    busan_store = BusanStore()
    busan_store.pizza_process("Shrimp")
    busan_store.pizza_process("Pepperoni")

    try:
        seoul_store.pizza_process("Shrimp")
    except ValueError as e:
        print(f"🚫 주문 실패: {e}")