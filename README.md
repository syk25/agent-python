# 로컬 AI Agent CLI 채팅봇

## 사용법
### 1. API키 등록
google.gemini.app에서 api키를 발급 받은 후에 .env 파일에 다음과 같이 설정합니다.
```
GEMINI_API_KEY='발급받은 API키 입력'
```

### 2. CLI에 프롬프트 입력
CLI를 연 후에 작업폴더(working directory)로 들어간 후 프롬프트를 입력합니다.

```
uv main.py "프롬프트 입력"
```

## 참고
### 시스템 프롬프트 설정
prompts.py 파일에서 시스템 프롬프트를 조작하여 AI Agent의 응답을 조절할 수 있습니다.