# SRDL Lab Website

## 🚀 서버 시작 방법

```bash
# 터미널(명령 프롬프트)에서 폴더 안에서 실행:
python server.py

# 또는 포트 변경:
python server.py 3000
```
브라우저에서 `http://localhost:8080` 접속

---

## ✏️ 콘텐츠 업데이트 방법

**모든 콘텐츠는 `content/site.json` 파일 하나에서 관리합니다.**
텍스트 편집기(메모장, VS Code 등)로 열어서 수정 후 저장하면 새로고침 시 바로 반영됩니다.

---

### 📰 뉴스 추가하기

`"news"` 배열에 항목 추가:

```json
{
  "id": "news2025a",
  "date": "2025-03-15",
  "type": "paper",
  "title": "New paper accepted in Nature Nanotechnology",
  "content": "논문 내용 설명..."
}
```

**type 종류:** `paper` | `award` | `member` | `conference`

---

### 📄 논문 추가하기

`"publications"` 배열에 항목 추가:

```json
{
  "id": "pub2025a",
  "year": 2025,
  "title": "논문 제목",
  "authors": "Kim A, Lee B, [PI Name]*",
  "journal": "Nature Nanotechnology",
  "volume": "20",
  "pages": "100–108",
  "doi": "10.1038/s41565-025-XXXXX",
  "highlight": true
}
```

`"highlight": true` → 강조 표시됨

---

### 👤 멤버 추가/수정하기

`"members"` 배열에 항목 추가:

```json
{
  "id": "phd2",
  "name": "박XX",
  "role": "Ph.D. Student",
  "email": "student@university.ac.kr",
  "photo": "assets/images/members/student.jpg",
  "bio": "Research on perovskite photodetectors.",
  "joined": "2024"
}
```

**role 예시:** `Ph.D. Student` | `M.S. Student` | `Undergraduate Researcher` | `Postdoctoral Researcher`

사진 파일은 `assets/images/members/` 폴더에 저장하고 파일명을 `photo` 항목에 입력.

---

### 🔬 연구분야 수정하기

`"research"` 배열의 해당 항목 수정.

---

### 🏫 기본 정보 수정하기

`"lab"` 섹션에서 교수님 이름, 이메일, 전화번호 등 수정.

---

## 📁 폴더 구조

```
lab-website/
├── index.html          ← 홈페이지 (수정 불필요)
├── server.py           ← 서버 실행 파일
├── content/
│   └── site.json       ← ★ 여기서 모든 콘텐츠 수정
└── assets/
    └── images/
        └── members/    ← 멤버 사진 저장
```

---

## 🌐 외부 공개 (연구실 PC → 인터넷)

1. **방화벽 설정**: Windows 방화벽에서 8080 포트 인바운드 허용
2. **공유기 포트포워딩**: 외부 80포트 → 내부 PC IP:8080
3. **IP 확인**: `ipconfig`로 내부 IP 확인 후 공유기 설정
4. (선택) **도메인 연결**: 무료 DDNS 서비스(DuckDNS 등) 사용

---

## 💡 자동 시작 설정 (Windows)

서버 자동 시작을 원할 경우 `server.py`를 작업 스케줄러에 등록하거나,
`start_server.bat` 파일 생성:

```bat
@echo off
cd /d "C:\경로\lab-website"
python server.py
```

바탕화면에 바로가기로 만들어 두면 편리합니다.
