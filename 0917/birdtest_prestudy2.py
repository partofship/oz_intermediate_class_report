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
    def __init__(self, birdtype, birdsound, weight, strength, isallow_modifier, fly_check, run_check, sound_check):
        self.birdtype = birdtype   # 새의 종류str
        self.birdsound = birdsound #새의 소리str
        self.weight = weight   # 새의 무게int
        self.strength = strength    # 새의 근력int
        self.isallow_modifier = isallow_modifier #새의 modifier 허용여부boolean

        # 파이프라인 연결해 주는 친구들
        self._fly_check = fly_check
        self._sound_check = sound_check
        self._run_check = run_check
    
    # 전략으로 위임하게끔실행
    def perform_fly(self):
        return self._fly_check.perform(self)
    
    def perform_run(self):
        return self._run_check.perform(self)

    def perform_sound(self):
        return self._sound_check.perform(self)

class FlyUnvalid:
    def perform(self, bird):
        return bird.birdtype + "은/는 날 수 없습니다."
    

class FlyValid:
# 조건에 맞지 않으면 날 수 없음을 다르게 출력.
# 해당 규칙이 자주 변경될 예정이기에 쉽게 고칠 수 있게 Capsulification? capsulation? 캡슐화. 그래서 이것만 교체하면 됨.
    def perform(self, bird):
        if bird.weight > 0 and bird.strength >= bird.weight:
            fly_altitude = round(bird.weight/(2*bird.strength), 2)
            return bird.birdtype + f"이/가 날고 있습니다. 높이: {fly_altitude}"
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

class Chirpsound:
# 소리 내는 애들용. 소리를 못 내는 새는...있나?
    def perform(self, bird):
        return bird.birdsound

# BIRD_LIB에서 birdtype을 받습니다.
# 이후 Bird 인스턴스와 전략(함수)를 연결해 반환하는 형태로 짰습니다.
def weareproducing(birdtype):
    if birdtype not in BIRD_LIB:
        raise ValueError("알 수 없는 새입니다. 가능한 종류: "+ ", ".join(BIRD_LIB.keys()))   
# 도메인 값을 라이브러리에서 꺼내오기
    sound, weight, strength, isallow_modifier = BIRD_LIB[birdtype]
    
# 실제 실행되는, 전략
    action_fly = FlyValid() if strength > 0 else FlyUnvalid()
    action_run = RunValid() if strength > 0 else RunUnvalid()
    action_sound = Chirpsound() if bool(sound) is True else ChirpMuted()
    
    # Bird 객체 생성 및 반환.
    return Bird(birdtype, sound, weight, strength, isallow_modifier, action_fly, action_run, action_sound)

if __name__ == "__main__":
    print("새장에 새가 많아요.")
    print("사용법: [새 종류], [행동] (ex) 펭귄, 달리기")
    while True:
        try:
            user_input_01 = input("새의 종류와 행동을 하나 입력하세요.\n").strip()
            if not user_input_01:
                continue
                # 빈 입력은 무시하고 다시 입력받습니다.

# 문자열을 "," 기준으로 1번만 나놈(split(",", 1)), [새종류, 행동] 이렇게.
# 좌우 공백 제거split, 으로 앵무새, 울기 같은 식으로 입력되어도 안전하게 처리.
# b=Bird(birdtype)으로 입력한 새 종류를 Bird 내 인스턴스로 생성함.
            birdtype, action = [s.strip() for s in user_input_01.split(",", 1)]
            b = weareproducing(birdtype)
# 인스턴스 메서드 호출을 하되,
# 생성한 b로 불러야 self가 전달되서 우리가 원하는 효과 발생.
            if action == "날기":
                print(b.perform_fly())
            elif action == "울기":
                print(b.perform_sound())            
            elif action == "달리기":
                print(b.perform_run())
            else:
                print("지원하지 않는 행동입니다.")
                print("다음의 양식을 지켜주세요: [새의 종류], [울기, 날기, 달리기 중 선택 1]")
            
        except ValueError as wronginput_01:
            print(wronginput_01)

# 예외 처리. split(",",1) 결과가 2개 아니면 ValueError 발생.
# 이 경우 형식 오류 안내와 함께 사용 가능한 새 종류를 제시
# ', ' 로 어떻게 이을지 제시, .join으로 엮음.

        check_cont = input("계속 하시겠습니까? Y/N ").strip().lower()
        if check_cont == "n":
            print("새장을 떠납니다.")
            break
# 루프 지속 여부.
# 입력을 소문자로 바꿔(.lower()) N일 경우 n으로 받음. (다른 경우 마찬가지)
# break로 while 문 자체를 종료.