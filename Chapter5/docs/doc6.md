# Document for Problem3 by Daeung
---

# DockerHub를 사용하는 이유

## 1. 이미지 저장 및 배포

DockerHub는 Docker 이미지를 저장하고 쉽게 배포할 수 있는 중앙 저장소입니다. 개발자가 만든 애플리케이션 컨테이너 이미지를 저장소에 올려두면, 다른 개발자나 서버에서 손쉽게 pull 하여 동일한 환경을 재현할 수 있습니다.

- 이미지를 다른 시스템으로 전송할 필요 없음
- `docker pull <이미지이름>` 한 줄로 어디서든 사용 가능

## 2. 협업과 팀 개발 지원

한 저장소에 여러 사람이 접근할 수 있어 팀 협업에 용이합니다.

- 조직 계정 및 팀별 권한 설정 기능 제공
- Private/Public 설정으로 내부 프로젝트 또는 오픈소스 프로젝트 활용 가능
- 자동화된 CI/CD와 연동 가능 (GitHub, GitLab 등)

# 주요 Container Registry 3가지

## 1. DockerHub

- 가장 널리 사용되는 공개 및 개인용 Docker 이미지 저장소
- 무료로 Public 저장소 무제한 제공, Private 저장소도 지원
- 공식 이미지 및 커뮤니티 이미지가 풍부하며, 간편한 웹 UI 제공
- 자동 빌드, 웹훅 등 CI/CD 연동 기능 탑재

## 2. Google Container Registry (GCR)

- Google Cloud Platform에서 제공하는 컨테이너 이미지 저장 서비스
- Google Cloud와 긴밀하게 통합되어 보안, 권한 관리가 강화됨
- 전 세계 여러 리전에 이미지 저장 가능해 높은 가용성과 빠른 배포 지원
- Cloud Build 등 Google의 CI/CD 도구와 연동 용이

## 3. Amazon Elastic Container Registry (ECR)

- AWS에서 제공하는 컨테이너 이미지 저장 서비스
- AWS IAM과 통합하여 세밀한 권한 제어 및 인증 제공
- AWS Fargate, ECS, EKS 등 AWS 컨테이너 서비스와 완벽 연동
- 이미지 스캔, 라이프사이클 정책 등 보안 및 관리 기능 내장