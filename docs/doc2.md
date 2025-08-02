# Document for Chpater2
---

# 1. 저장소를 Private → Public으로 전환해 접근성을 테스트한다.
http 주소로 접속 시 404뜸

# 2. 전체 작업을 Visual Studio Code에서 다시 수행하고 CLI 방식과 비교한다.
GUI로 사용하면 대부분의 작업을 마우스 클릭과 단축키로 처리할 수 있습니다. 이슈나 마일스톤 등도 확장 프로그램을 이용하면 확인할 수 있다 -> 별도의 웹페이지 X
CLI 방식과 비교
구분	CLI	Visual Studio Code
명령어/액션	git checkout -b add-menu	상태 표시줄의 브랜치 이름 클릭 → 새 브랜치 생성
장점	명령어를 외우면 키보드만으로 빠르게 처리 가능합니다.	직관적입니다. 현재 브랜치와 다른 브랜치 목록을 한눈에 보며 작업할 수 있습니다.
단점	현재 브랜치를 확인하려면 git branch를 따로 입력해야 합니다.	마우스를 사용해야 하므로 키보드 중심 작업자에게는 느리게 느껴질 수 있습니다.
또 파일 스테이징 (파일 전체 vs Hunk 단위)
이 부분에서 VS Code GUI의 강력함이 가장 잘 드러납니다.

Visual Studio Code 방식
왼쪽 사이드바에서 소스 컨트롤(Source Control) 아이콘(가지 모양)을 클릭합니다.

Changes 목록에 변경된 파일 menu.html과 app.py가 나타납니다.

A. menu.html 파일 전체 스테이징하기

Changes 목록의 menu.html 파일 이름에 마우스를 올리면 나타나는 + (Stage Changes) 아이콘을 클릭합니다.

파일이 Staged Changes 섹션으로 즉시 이동합니다. 이것이 git add menu.html과 동일한 작업입니다.

B. app.py Hunk 단위(선택적) 스테이징하기

Changes 목록에서 app.py 파일을 클릭합니다.

화면에 **Diff 뷰(비교 보기)**가 열리면서 변경된 내용이 이전 버전과 나란히 표시됩니다.

스테이징하고 싶은 코드 라인들을 마우스로 드래그하여 선택합니다.

선택된 영역 위에서 마우스 오른쪽 버튼을 클릭하고 Stage Selected Ranges 를 선택합니다.

이 방법은 CLI의 git add -p보다 훨씬 더 직관적이고, 덩어리(hunk)가 아닌 내가 원하는 특정 줄만 골라서 스테이징할 수 있어 훨씬 강력합니다.

4. 규칙에 맞춰 커밋하기
Visual Studio Code 방식
소스 컨트롤 패널의 상단에 있는 Message 입력 상자를 클릭합니다.

첫 줄에 제목을 입력합니다: Feat: 메뉴 화면추가

Enter를 두 번 눌러 한 줄을 비우고 본문 영역으로 넘어갑니다.

본문 내용을 작성합니다.

text
메뉴 화면을 구성하는 기본 HTML 파일을 추가하고,
서버에서 해당 화면을 렌더링하는 라우팅 로직을 구현함.
다시 Enter를 두 번 눌러 꼬리말을 위한 공간을 만듭니다.

꼬리말을 작성합니다: Resolves: #1

입력이 끝나면 메시지 상자 위의 **체크 표시(✓) 아이콘(Commit)**을 클릭하거나, 단축키 Ctrl+Enter(macOS: Cmd+Enter)를 누릅니다.

이 과정에서 별도의 텍스트 편집기(Vim, Nano 등)가 열리지 않습니다.

