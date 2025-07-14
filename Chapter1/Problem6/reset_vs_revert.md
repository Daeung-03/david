# Document for Problem_2 by Daeung-03
---


## git reset vs git revert
모두 이전 커밋을 되돌리는 명령어이지만 동작 방식에 차이가 있다.
**git reset**: 과거 특정 커밋으로 이력을 되돌림 -> 그 위의 이력이 사라짐.
**git revert**: 되돌리고 싶은 커밋을 취소하는 새로운 커밋을 생성한다! -> 이력이 유지됨(새로운 log가 생길뿐)

이력을 공유하기 때문에 git revert는 협업 시에 혼란은 회피할 수 있다. 또 git reset은 작업중인 사람에게 충돌 위협을 준다! 동료의 작업 내역을 지워버릴수도 있다.
