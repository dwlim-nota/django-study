# day14: django 마무리(ORM M:N 관계, network debugging, final project 논의)



## ORM M:N 관계

환자가 의사에게 진료 예약을 하려는 경우, 동시는 아니지만 한 명의 의사에 대해서 여러 번의 예약에 대해서 의사와 환자의 관계가 M:N이 될 수 있습니다.

기록 상으로 보게 되면, 



- TODO: 중계 테이블 설명
- TODO: ManyToMany Field 설명



## network debugging

- TODO: wireshark 설명
  - wire shark는 컴퓨터로 들어오는 모든 종류의 패킷에 대해 관심이 있음
  - TCP/IP 4계층의 패킷에 대해서 구조적으로 헤더들을 볼 수 있음
- TODO: fiddler 설명
  - network proxy tool(중간에서 패킷들을 받고, 다시 보내고 할 수 있음)
  - 따라서 이 툴을 이용해서 자세하게 디버깅을 할 수 있음

두 가지 툴 다 비슷한 용도로 사용할 수 있는데,

network의 packet들에 대해서 raw하게 보려면 wireshark가 좋고, http의 request, response 에 대해서 주로 관심이 있으면 fiddler가 좋음



## final project 논의

중간에 주제를 바꾸셔도 되고, 일주일 후 월요일에 프로젝트가 완성되지 않아도 좋습니다.



- 자유 주제(recap django) - 정훈
- 주제 제안
  - 도서 관리 프로그램(동욱)
  - 익명 twitter(호인)
  - 다른 분들도 원하시는 분들은 제출하셔도 좋습니다.