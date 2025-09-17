class Bird():
    
    # 새 : 울음소리, 체중(kg), 근력(속도 대신 대입)
    # 달리면 몸무게 x 속도가 아니력 뭐 근력같은걸로 속도 = 근력 / 몸무게 해야 하는게?
    # 기존  sound 대신 bird_lib 딕셔너리, key 동일 value는 tuple로 값 추가함.
    # modifier 받을 수 있는 튜플 내역 추가: True/False로 지정.
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