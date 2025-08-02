# Document for chapter1
---

## 0. 무료, 유료 요금제 차이
## 개인 계정 기준 (Free vs Pro)

| **구분** | **GitHub Free** | **GitHub Pro** |
| --- | --- | --- |
| 비용 | 무료 | 월 $4 (2025년 8월 기준) |
| 퍼블릭/프라이빗 저장소 | 무제한 | 무제한 |
| 협업자 인원 제한 | 무제한 | 무제한 |
| GitHub Actions | 월 2,000분 제공 | 월 3,000분 제공 |
| GitHub Packages | 500MB 저장, 1GB 데이터 전송 | 2GB 저장, 10GB 데이터 전송 |
| Codespaces | 코어 시간 120, 스토리지 15GB | 더 많은 리소스, 고급 개발 환경 |
| 지원 | GitHub Community Support | 이메일 지원 |
| 고급 리포지토리 기능 | 제한적 (코어 기능은 가능) | 보호 브랜치, 코드 소유자, 인사이트 등 활용 가능 → private |
| 권장 대상 | 개인, 학생, 오픈소스 개발자 | 발전된 기능이 필요한 개인 개발자 |

## GitHub Actions

**GitHub Actions**는 코드 빌드, 테스트, 배포 과정을 자동화하는 CI/CD(지속적 통합/지속적 배포) 플랫폼입니다. 저장소에 YAML로 작성한 워크플로를 저장해, 코드 푸시, PR 생성, 이슈 발생 등 여러 이벤트에 맞춰 작업을 자동으로 실행할 수 있습니다.

주요 개념은 아래와 같습니다.

- **워크플로(Workflow):** 자동화된 프로세스를 정의하는 YAML 파일(.github/workflows)에 저장.
- **이벤트(Event):** 워크플로를 트리거(실행)하는 작업(예: push, pull_request 등).
- **잡(Job):** 워크플로 안에서 독립 실행되는 작업 단위. 각 잡은 별도의 VM에서 동작할 수도 있음.
- **스텝(Step):** 잡 안에서 순차적으로 실행되는 개별 명령 또는 액션.
- **액션(Action):** 반복적으로 쓰기 쉬운, 커뮤니티 또는 직접 만든 재사용 모듈.

워크플로 하나에 여러 잡을 정의해 병렬, 순차 실행이 모두 가능하며, 액션은 npm, Docker, 자체 정의 등 다양한 방식으로 제공됩니다.

빌드, 테스트, PR 라벨링, 배포, 코드 품질 체크 등 다양한 자동화에 활용됩니다.

## GitHub Packages

**GitHub Packages**는 코드와 연결된 상태로 패키지를 저장, 공유, 관리할 수 있게 해주는 패키지(아티팩트) 레지스트리 서비스입니다.

- **지원 포맷:** npm, Maven, Gradle, Docker, RubyGems, NuGet 등 다양한 패키지 매니저 포맷을 지원.
- **권한 관리:** 저장소 권한과 연동되어, 패키지도 퍼블릭/프라이빗 또는 팀별로 접근 권한 관리가 쉬움.
- **종속성 관리:** 저장소와 패키지를 하나로 관리하여, 외부 레지스트리 따로 운영할 필요 없이 의존성 관리, 배포가 용이.
- **통계 및 정보:** 각 패키지에 대한 다운로드 수, 버전, 라이선스 등의 메타 정보 확인 가능.

GitHub Actions와 연동해 CI 빌드 결과물을 바로 패키지로 배포, 설치도 가능합니다.

## GitHub Codespaces

**GitHub Codespaces**는 브라우저 또는 VS Code에서 바로 사용할 수 있는 클라우드 기반 개발 환경입니다.

- **완전히 설정된 개발 환경:** 저장소의 **`devcontainer.json`** 등 설정 파일을 읽어 환경을 자동 세팅(언어, 빌드툴, 확장팩, OS 등).
- **다양한 진입점:** 저장소, 브랜치, 커밋, PR에서 환경 생성 가능.
- **VM 리소스:** 2~32코어 머신, 8~64GB RAM, 32~128GB 저장소 선택 가능.
- **즉시 사용:** 클론, 빌드, 서버 셋업 등 반복 작업 없이 즉시 개발 시작.

교육 환경이나 팀 단위 표준화된 개발환경 제공, 로컬세팅 최소화, 강력한 협업에 유리합니다.

## 고급 리포지토리 기능

GitHub의 **고급 리포지토리 기능(Advanced Repository Features)**는 코드/보안/협업/관리의 품질을 높여줍니다.

- **브랜치 보호(Protected Branches):** 강제 PR 리뷰, 자동 머지 제한, 커밋 권한 제한 등 규칙 설정.
- **코드 소유자(Code Owners):** 파일, 폴더별 코드 리뷰 담당자 지정.
- **인사이트 및 통계:** 커밋/이슈/PR 등 개발 현황, 참여자 통계, 보안 취약점 대시보드 제공.
- **Secret/Dependency/Code Scanning:** 코드에 잠재된 비밀키, 의존성 오류, 보안 취약점 분석 및 자동 알림. CodeQL이나 Dependabot을 통해 자동 패치 및 경고.
- **아티팩트 원본성(Artifact Attestations):** 빌드 아티팩트의 무결성 및 소스 증명 제공.
- **리포지토리 룰셋:** 브랜치/태그별 코드 관리 정책 설정, 코드 표준화와 컴플라이언스 요구 충족.
- **Security Advisory 등 알림:** 커뮤니티에 보안 이슈 조기 알림, 비공개 논의, 공개 패치 가이드 제공.

이러한 고급 기능들은 Pro/Team 이상 플랜에서 더 폭넓게 제공됩니다.

## 1.Personal Access Token을 텍스트 파일로 저장한 뒤 삭제해야 하는 이유를 조사한다.
토큰의 유효 기간을 최소화하여 보안 위협을 줄이는 좋은 습관입니다
보안 침해: 토큰이 외부에 유출되었다고 의심될 때 즉시 폐기해야 합니다.

불필요: 토큰을 사용하던 프로젝트나 서비스가 종료되었을 때 폐기합니다.

주기적인 관리: 보안 정책에 따라 정기적으로 토큰을 교체하고 이전 토큰을 폐기합니다.

## 2. 파이썬 개발 시 __pycache__와 .venv 디렉토리가 생성되는 이유를 조사한다.
__pycache__ 디렉토리는 파이썬이 소스 코드를 **바이트코드(bytecode)**로 컴파일한 결과를 저장하는 공간입니다 .

생성 이유: 파이썬은 인터프리터 언어이지만, 내부적으로는 실행 속도를 높이기 위해 소스 코드(.py 파일)를 더 낮은 수준의 명령어 집합인 바이트코드로 변환하는 컴파일 과정을 거칩니다 . __pycache__는 이 바이트코드 파일(.pyc 파일)을 저장하는 캐시 역할을 합니다 .

성능 최적화: 프로그램의 시작 및 실행 속도를 개선하는 것이 주된 목적입니다 .

자동 관리: 이 디렉토리와 파일들은 파이썬 인터프리터에 의해 자동으로 생성되고 관리되므로 개발자가 직접 수정할 필요는 거의 없습니다 .

소스 코드 분리: 컴파일된 파일을 소스 코드와 분리하여 프로젝트 디렉토리를 깔끔하게 유지합니다 .

.venv 디렉토리: 독립적인 개발 환경 구성
.venv(또는 venv)는 프로젝트별로 패키지 의존성을 격리하기 위한 **가상 환경(Virtual Environment)**입니다 .

생성 이유: 여러 파이썬 프로젝트를 진행하다 보면 각 프로젝트가 요구하는 라이브러리(패키지)의 버전이 다른 경우가 발생할 수 있습니다 . 예를 들어, A 프로젝트는 requests 2.1.0 버전을, B 프로젝트는 2.31.0 버전을 필요로 할 수 있습니다. 이때 시스템 전역에 패키지를 설치하면 버전 충돌이 발생하게 됩니다 . .venv는 각 프로젝트가 자신만의 파이썬 인터프리터와 설치된 패키지들을 갖는 독립된 공간을 만들어 이러한 문제를 해결합니다 .

동작 방식:

사용자가 python -m venv .venv와 같은 명령어로 특정 프로젝트 폴더 내에 가상 환경을 생성합니다.

## 3. GitHub에서 .gitignore 템플릿 중 Python을 선택했을 때 포함되는 항목
\# Byte-compiled / optimized / DLL files
__pycache__/
*.py[codz]
*$py.class

\# C extensions
*.so

\# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

\# PyInstaller
\#  Usually these files are written by a python script from a template
\#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

\# Installer logs
pip-log.txt
pip-delete-this-directory.txt

\# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py.cover
.hypothesis/
.pytest_cache/
cover/

\# Translations
*.mo
*.pot

\# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

\# Flask stuff:
instance/
.webassets-cache

\# Scrapy stuff:
.scrapy

\# Sphinx documentation
docs/_build/

\# PyBuilder
.pybuilder/
target/

\# Jupyter Notebook
.ipynb_checkpoints

\# IPython
profile_default/
ipython_config.py

\# pyenv
\#   For a library or package, you might want to ignore these files since the code is
\#   intended to run in multiple environments; otherwise, check them in:
\# .python-version

\# pipenv
\#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
\#   However, in case of collaboration, if having platform-specific dependencies or dependencies
\#   having no cross-platform support, pipenv may install dependencies that don't work, or not
\#   install all needed dependencies.
#Pipfile.lock

\# UV
\#   Similar to Pipfile.lock, it is generally recommended to include uv.lock in version control.
\#   This is especially recommended for binary packages to ensure reproducibility, and is more
\#   commonly ignored for libraries.
#uv.lock

\# poetry
\#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
\#   This is especially recommended for binary packages to ensure reproducibility, and is more
\#   commonly ignored for libraries.
\#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock
#poetry.toml

\# pdm
\#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
\#   pdm recommends including project-wide configuration in pdm.toml, but excluding .pdm-python.
\#   https://pdm-project.org/en/latest/usage/project/#working-with-version-control
#pdm.lock
#pdm.toml
.pdm-python
.pdm-build/

\# pixi
\#   Similar to Pipfile.lock, it is generally recommended to include pixi.lock in version control.
#pixi.lock
\#   Pixi creates a virtual environment in the .pixi directory, just like venv module creates one
\#   in the .venv directory. It is recommended not to include this directory in version control.
.pixi

\# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

\# Celery stuff
celerybeat-schedule
celerybeat.pid

\# SageMath parsed files
*.sage.py

\# Environments
.env
.envrc
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

\# Spyder project settings
.spyderproject
.spyproject

\# Rope project settings
.ropeproject

\# mkdocs documentation
/site

\# mypy
.mypy_cache/
.dmypy.json
dmypy.json

\# Pyre type checker
.pyre/

\# pytype static type analyzer
.pytype/

\# Cython debug symbols
cython_debug/

\# PyCharm
\#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
\#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
\#  and can be added to the global gitignore or merged into this file.  For a more nuclear
\#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/

\# Abstra
\# Abstra is an AI-powered process automation framework.
\# Ignore directories containing user credentials, local state, and settings.
\# Learn more at https://abstra.io/docs
.abstra/

\# Visual Studio Code
\#  Visual Studio Code specific template is maintained in a separate VisualStudioCode.gitignore 
\#  that can be found at https://github.com/github/gitignore/blob/main/Global/VisualStudioCode.gitignore
\#  and can be added to the global gitignore or merged into this file. However, if you prefer, 
\#  you could uncomment the following to ignore the entire vscode folder
\# .vscode/

\# Ruff stuff:
.ruff_cache/

\# PyPI configuration file
.pypirc

\# Cursor
\#  Cursor is an AI-powered code editor. `.cursorignore` specifies files/directories to
\#  exclude from AI features like autocomplete and code analysis. Recommended for sensitive data
\#  refer to https://docs.cursor.com/context/ignore-files
.cursorignore
.cursorindexingignore

\# Marimo
marimo/_static/
marimo/_lsp/
__marimo__/


## 4. Flask 기반 프로젝트를 기준으로 .gitignore에 추가되어야 할 항목들을 나열한다.
# Created by https://www.toptal.com/developers/gitignore/api/flask
# Edit at https://www.toptal.com/developers/gitignore?templates=flask

\### Flask ###
instance/*
!instance/.gitignore
.webassets-cache
.env

\### Flask.Python Stack ###
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class
---

Flask 관련 파일 및 디렉토리
Flask 애플리케이션 운영 시 생성되는 특정 파일 및 디렉토리입니다.

/instance/: 인스턴스 폴더는 데이터베이스 파일이나 설정 파일과 같이 저장소에 커밋하고 싶지 않은 파일들을 담는 곳입니다. 민감한 정보가 포함될 수 있으므로 제외합니다 .

/.flaskenv: flask run 명령어 실행 시 적용될 환경 변수를 담는 파일입니다. FLASK_APP, FLASK_ENV 등이 포함될 수 있으며, 개발 환경에 따라 다를 수 있습니다 .

/uploads/: 사용자가 업로드한 파일이 저장되는 디렉토리입니다. 이 파일들은 버전 관리 대상이 아닙니다 .

설정 파일 및 민감 정보
데이터베이스 접속 정보, API 키, 시크릿 키 등 민감한 정보가 포함된 파일은 절대 원격 저장소에 올리면 안 됩니다.

*.env 

config.py 또는 settings.py (민감 정보를 포함하는 경우) 

*.db 또는 *.sqlite3 (SQLite 데이터베이스 파일) 

테스트 및 커버리지 리포트
테스트 실행 후 생성되는 캐시 파일이나 커버리지 리포트는 매번 달라지며, CI/CD 환경에서 새로 생성되므로 제외합니다.

/.pytest_cache/ 

/.coverage 

/htmlcov/ (HTML 형식의 커버리지 리포트) 

/.tox/ 

nosetests.xml 

빌드 및 배포 관련 파일
패키지를 빌드하거나 배포할 때 생성되는 아티팩트입니다.

/dist/ 

/build/ 

/*.egg-info/ 

/*.egg 

