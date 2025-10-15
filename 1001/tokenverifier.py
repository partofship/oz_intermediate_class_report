import time, json
import templib, tokenmaker

# 토큰 검증 함수
# 1. 토큰 형식이 올바른가요? header.payload.signature 형식인지
# 2. 서명이 올바른가요? 위조 여부 확인
# 3. 만료되지 않았나요? (payload 내에서 time 확인)

def verify_token(token):
    try:
        parts = token.split('.')

        # 토큰 형식 확인
        if len(parts) != 3:
            print("토큰 형식이 올바르지 않습니다.")
            return None

        # 2. 서명 위조 여부
        header_string = parts[0]
        payload_string = parts[1]
        signature_string = int(parts[2])

        header_payload = f"{header_string}.{payload_string}"
        signature_source = header_payload + templib.SECRET_KEY
        expected_signature = tokenmaker.simple_hash(signature_source)

        if signature_string != expected_signature:
            print("토큰이 위변조 됐습니다.")
            return None

        # 3. 만료시간 확인!
        payload = json.loads(payload_string)
        current_time = int(time.time())
        if current_time > payload["exp"]:
            print(f"토큰이 만료됐습니다.")
            return None

        # 모든 검증 통과 시
        return payload

    except Exception as e:
        print(f"토큰 검증 중 오류: {e}")
        return None