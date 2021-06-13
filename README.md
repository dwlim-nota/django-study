# django-study

30분 장고(후반으로 갈 수록 60분 장고..!! 🛫)





## 1. 목표

study 후에 스터디를 끝까지 진행한 모든 구성원이 django를 이용해 CRUD(Create, Read, Update, Delete)에 대한 훈련이 되어있는 상태가 되는 것

즉, 로그인, 게시판 만들기, DB 연동, 프론트에 대한 연동 등에 대해서 훈련된 상태가 되는 것이 목표입니다.



## 2. 대상

python 기초 문법을 알고 있는 노타 구성원(netspresso dev team + django에 관심 있는 분 누구나)



## 3. 기간 / 장소 / 시간

- 진행 기간: 2021-05-20 ~ 2021-06-11 (working day 기준: 14일)
- 서울 Nota 건물 3층 회의실
- 매일 오전 11시 30분(KST 기준. UST + 9시간)



## 4. online 주소

whereby에서 진행했음(general-project 채널)



## 5. 진행 방법

- 30분간 진행됩니다. 첫 15분 이후에 git을 push하기 때문에 잘 진행이 안 되셨던 분들은 git clone 하셔서 계속 진행하시면 됩니다.
- 통합개발 환경(Integrated Development Environment, IDE)는 vscode 혹은 pycharm을 추천드립니다. (vim x)
- 이론 위주 보다는 반복된 코드 작업을 통해서 손에 익도록 하는 것(체득)을 지향합니다.
- 30분의 시간은 이론 -> 설명 -> 실습 + Q&A 순으로 진행됩니다.
- 질문은 질문이 생기셨을 때 바로바로 해주셔도 좋습니다.



## 6. 진행 상황

나중에 복습하실 때, 보기 편하도록 실제 진행했던 날짜 기준 기록이 아니고, working day(5일 = 일주일) 기준으로 기록했습니다.

### week 1

- [day 1: django 설치](day1/)
- [day 2: MTV, GET - path parameter로 인자 받기](day2/)
- [day3: DTL(Django Template Language)](day3/)
- [day4: get으로 요청하고 받기(query string)](day4/)
- [day5: post method, bootstrap, template 상속](day5/)



## week 2

- [day6: static file 제공](day6/)
- [day6-2: ORM](day6-2/)
- [day7: ORM, CRUD](day7/)
- [day8: 게시판 만들기 - list + CRUD에서 list, C, R까지 구현](day8/)
- [day9: 게시판 만들기 - 마무리](day9/)
- [day10: 게시판 만들기 실습](day10/)

 

## week 3

- [day11: ORM의 1:N 관계(e.g. comment)](day11/)
- [day12: 인증 (1) - 기본 User Model 활용 CRUD](day12/)
- [day13: 인증 (2) - AbstractUser, AbstractBaseUser](day13/)
- [day14: 마무리](day14/)
  - ORM M:N 관계(e.g. 의사와 환자의 예약 관계, 인스타그램에서 user와 게시물의 좋아요 관계)
  - network debugging(wireshark / fiddler)
  - final project 선정



## final project(optional)

참여하고 싶은 사람에 한정해서 진행. 

- 도서 관리 시스템(동욱)
- 자유 주제 - 배운 내용 recap(정훈)
- 익명 tweeter(호인)



## 7. 진행하지 못 했던 주제들

30분을 목표로 잡고 했던 스터디라서, 시간 제약상 진행하지 못했습니다.

한편으로는 하지 않았던게 긴장감 있게 진행되어서 오히려 나았나 싶기도 합니다. :happy:



- django form(html의 validation)
  - 요즘 웹 개발 트렌드는 backend와 frontend를 완벽하게 분리해서 개발하는 것이 트렌드인데, frontend부분을 장고로 너무 많이 제어하려는 것 같아서 의도적으로 제외
- django test(10 분 정도 분량)
  - 마지막에 한꺼번에 하려다가 시간 관계상 진행하지 못 했습니다.

- static file upload/download(40분 분량)
  - 우선순위에서 조금 뒤로 밀리다가 못 했음.
- ORM 연습(40분 분량)
  - ORM 체득 / 성능 향상을 위해서 필요한 부분들인데 진행하지 못 해서 조금 아쉽습니다.

- html + css(40분 분량)
  - block element / inline element / size 등...

