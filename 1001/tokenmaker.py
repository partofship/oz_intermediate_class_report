import time, json
import templib

# 해쉬 만들기: 숫자는 내버려두고, 문자열을 숫자로 바꾸기. 문자의 ASCII 값에 위치를 곱한다.
def simple_hash(text):
    result = 0
    for i, char in enumerate(text):
        result += ord(char) * (i + 1)
    return result % 9604

# 토큰 생성.
# 헤더 - 토큰타입 JWT, 알고리즘 커스텀
# 페이로드 - 사용자 정보(id, 유저이름, 만료 시간)
def create_token(user_id, username, expiry_minutes = 10):

    header = {"typ": "JWT", "alg": "custom"}

    current_time = int(time.time())
    payload = {
        "sub": user_id,
        "name": username,
        "iat": current_time,
        "exp": current_time + (expiry_minutes * 60)
    }

    header_json_string = json.dumps(header, separators=(',', ':'))
    payload_json_string = json.dumps(payload, separators=(',', ':'))

    # header.payload 형태로 결합!
    header_plus_payload = f"{header_json_string}.{payload_json_string}"

    # 서명 생성!
    signature_source = header_plus_payload + templib.SECRET_KEY
    signature = simple_hash(signature_source)

    # 토큰 반환~
    token = f"{header_plus_payload}.{signature}"
    return token

access_token = input("Token: ")