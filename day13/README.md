# day13: custom User 모델



Custom User 모델을 이용해서 User의 특정 field(예를 들어 age)를 추가하거나, 인증 방법을 바꾸는 등의 작업을 할 수 있습니다.



저번시간에 말씀드린 것처럼 User 모델을 구현 하는 방식은 3가지가 있습니다.

- django의 User 모델을 그대로 사용하는 방법
- django의 User 모델을 상속받아서 확장하는 방법
- django의 User 모델을 사용하지 않고, basic한 부분만 가져와서 구현하는 방법



오늘은 두 번째, 세 번째 내용에 대해서 진행하겠습니다.



TODO1: AbstractUser를 이용해서 model 확장 하는 방법

- 상속 받기
- 1:1 관계(OneToOne Field) 사용해서 새로운 모델 만들어서 user에 붙이기



TODO2: AbstractBaseUser를 만들어서 기존의 model을 대체하는 방법





## 다음 시간에 진행할 내용

- django 마무리
  - M:N 관계
  - network 디버깅(wireshark, fiddler)
  - final project 논의

