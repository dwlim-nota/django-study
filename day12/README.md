# day12: 인증 (1)



django에서 user 인증을 하는 방법은 세 가지가 있습니다.

- django의 User 모델을 그대로 사용하기
- django의 User 모델을 확장해서 사용하기
- 새로운 User 모델을 만든 후, django의 User 모델을 대체해서 사용하기
- ~~django  model을 밑 바닥부터 만들어서 django form, admin과 연결~~



오늘 진행할 내용은 django의 기본 User 모델을 이용해서 CRUD를 구현해 보도록 하겠습니다.



TODO1: 기본 User 모델을 이용해서 crud

- 회원 등록
- 회원 탈퇴
- 로그인
- 로그아웃
- 회원 페이지

TODO2: 다른 앱에서 user의 로그인 확인하기

TODO3: 다른 앱에서 user별로 다른 화면이 보이는 것 구현



## 다음 시간에 진행할 내용

- 인증 마무리