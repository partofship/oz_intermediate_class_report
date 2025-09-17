"""
디자인 패턴!
패턴 쓰는 이유?
- 변화의 고립: 자주 바뀌는 것을 분리해 둡니다.
- 결합도를 낮추고 사용성을 높입니다. 구현에 집중하지 않고, 역할(=인터페이스) 위주로 짠다면 대체와 확장이 용이합니다.
- 의사소통을 쉽게 하기 위해 용어를 통일할 수 있습니다.

핵심 원칙
- 변하는 부분을 찾아 캡슐화
- 구현X 인터페이스(역할) 맞춰 프로그래밍
- 구성 > 상속

보충설명:
- 바뀌는 부분을 별도 모듈, 클래스 등으로 분리해 둬요.
- 추상화 할 것.
- is - a (상속) 보다 has - a (구성) 식으로 유연성, 테스트 용이성을 확보.

전략 패턴
선요약: 알고리즘을 교체 가능한 부품으로 바꾼다
1. 공통 역할로 캡슐화
2. 문맥으로 구성해 사용
when? 동일한 일을 하는 게 여러 개 있으면 등.

옵저버? (잘 모르겠음)
느슨한 결합?으로 한 번 변경 - 여러 반응 유?도?
"""

"""새 : 울음소리, 체중(kg), 근력(속도 대신 대입), 모디파이어 허용 용도의 True/False
달리면 몸무게 x 속도가 아니력 뭐 근력같은걸로 속도 = 근력 / 몸무게 해야 하는게?
"""

BIRD_LIB : dict[str, tuple[str, float, float, bool]] ={
    "앵무새": ("안녕하세요?", 3, 3, True),
    "참새": ("짹짹", 2, 2, True),
    "비둘기" : ("9999", 3, 2, True),
    "닭" : ("교촌교촌", 4, 3, False),
    "러버덕" : ("QUACK", 0, 0, False),
    "펭귄" : ("꾸르륵", 5, 3, False)
}

# 구성: 전략 객체 - 전략 연결하는 허브 - 위임 호출 - 결과
# Bird - 
# Bird는 행동을 가지고만 있음(has - a,b,c) 직접 구현 X
# 구체적 행동은 전략 객체에 위임
# 각 전략 클래스는 perform을 통일

class Bird():
    def __init__(self, birdtype, weight, strength, isallow_modifier):
        self.birdtype = birdtype   # 새의 종류str
        self.weight = weight   # 새의 무게int
        self.strength = strength    # 새의 근력int
        self.isallow_modifier = isallow_modifier #새의 modifier 허용여부boolean
    
    # 실행
    def perform_fly(self):
        return self.perform_fly
    
    def perform_run(self):

    def perform_sound(self):
        return fdasfd # 수정예정

class FlyUnvalid:
    def perform(self, bird):
        return bird.birdtype + "은/는 날 수 없습니다."
    

class FlyValid:
# 조건에 맞지 않으면 날 수 없음을 다르게 출력.
# 해당 규칙이 자주 변경될 예정이기에 쉽게 고칠 수 있게 Capsulification? capsulation? 캡슐화. 그래서 이것만 교체하면 됨.
    def perform(self, bird):
        if bird.weight > 0 and bird.strength >= bird.weight:
            return bird.birdtype + f"이/가 날고 있습니다. 높이: {bird.weight/(2*bird.strength)}"
        return bird.birdtype + "은/는 너무 무거워서 못 날아요."

class RunUnvalid:
# 달리기 자체가 불가능한 경우 정의
    def perform(self, bird):
        return bird.birdtype + "은/는 뛸 수 없습니다."

class RunValid:
# 조건에 맞지 않으면 뛸 수 없음 출력.
# 조건에 맞으면 얼마만큼으로 뛰는지 표현.
# 달리기 관련 규칙이 변경될 시 해당 클래스만 교체하면 됨.
    def perform(self, bird):
        if bird.weight > 0 and bird.strength > 0:
            speed = round(bird.strength / bird.weight, 2)
            return bird.birdtype + "이/가 달립니다. 속도:" + str(speed)
        return bird.birdtype + "은/는 뛸 수 없습니다."

class ChirpMuted:
# 이 새는 소리를 낼 수 없습니다.
    def perform(self, bird):
        return bird.birdtype + "은/는 과묵하군요."

class chirpsound:
# 소리 내는 애들용. 소리를 못 내는 새는...있나?
    def perform(self, bird):
        return bird.sound


"""
class Bird():
    
    bird_lib = {
        "앵무새": ("안녕하세요?", 3, 3, True),
        "참새": ("짹짹", 2, 2, True),
        "비둘기" : ("9999", 3, 2, True),
        "닭" : ("교촌교촌", 4, 3, False),
        "러버덕" : ("QUACK", 0, 0, False),
        "펭귄" : ("꾸르륵", 5, 3, False)
    }

    def __init__(self, birdtype: str):
        # 초기화 메서드, 새의 종류를 인스턴스에 저장
        # self.birdtype으로 현재 인스턴스 지정 
        self.birdtype = birdtype
        self.sound, self.weight, self.strength, self.get_modifier = Bird.bird_lib.get(birdtype, ("짹짹", 1, 1))
        # 사전에 없을 경우 "짹짹"을 기본으로 사용.

    def birdfly(self) -> None:
        if self.strength >= self.weight:     # 수정: 기존의 "러버덕" 여부에서, 힘이 체중보다 크거나 같을 경우에만 날 수 있게 지정.
            print(f"{self.birdtype}이/가 날고 있습니다.")
        else:
            print(f"{self.birdtype}은 날 수 없습니다.")

    def birdsing(self) -> None:
        print(self.sound)
    
    def birdrun(self) -> None:
        if self.strength > 0:    # 수정: 기존의 "러버덕" 여부 → 힘이 0 이상일 경우에만 달릴 수 있음.
            print(f"{birdtype}이 달립니다!\n{birdtype}의 속도: {self.strength / self.weight}")
        else:
            print(f"{birdtype}은 뛸 수 없어요.")
    
    def birdmodifier(self) -> None:
        if self.get_modifier == True:
            print("아효")

# 사용자가 그만두겠다 할 때까지 계속 입력을 받음.
while True:
    try:
        user_input = input("새의 종류와 행동(울기, 날기, 달리기)을 입력하세요: ")
        birdtype, action = [s.strip() for s in user_input.split(",", 1)]
        b = Bird(birdtype)

# 문자열을 "," 기준으로 1번만 나놈(split(",", 1)), [새종류, 행동] 이렇게.
# 좌우 공백 제거split, 으로 앵무새, 울기 같은 식으로 입력되어도 안전하게 처리.
# b=Bird(birdtype)으로 입력한 새 종류를 Bird 내 인스턴스로 생성함.

        if birdtype not in Bird.bird_lib:    # 유효성 검사
            print("다시 작성해 주세요.")
        else: 
            if action == "날기":
                b.birdfly()
# 인스턴스 메서드 호출을 하되,
# 생성한 b로 불러야 self가 전달되서 우리가 원하는 효과 발생.
            elif action == "울기":
                b.birdsing()
            
# 달리기 추가
            elif action == "달리기":
                b.birdrun()

            else: # 허용되지 않는 행동 문자열에 대한 안내
                print("지원하지 않는 행동입니다: 울기/날기/달리기 중 선택")
                
    except ValueError:
        print("오류가 발생했습니다. 다시 작성해 주세요!")
        print(f"새 종류: {', '.join(Bird.bird_lib.keys())}")
#Birdsong 대신 bird_lib으로 변경.

# 예외 처리. split(",",1) 결과가 2개 아니면 ValueError 발생.
# 이 경우 형식 오류 안내와 함께 사용 가능한 새 종류를 제시
# ', ' 로 어떻게 이을지 제시, .join으로 엮음.

    finally:
        check_cont = input("계속 하시겠습니까? Y/N ").strip().lower()
        if check_cont == "n":
            print("새장을 떠납니다.")
            break

# 루프 지속 여부.
# 입력을 소문자로 바꿔(.lower()) N일 경우 n으로 받음. (다른 경우 마찬가지)
# break로 while 문 자체를 종료.
"""