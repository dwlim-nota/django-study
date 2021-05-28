# day6: static files 제공



## 복습

- post method로 요청하기
- bootstrap
- template 상속



## 오늘 학습 내용

- static file을 제공하는 방법에 대해서 배웁니다.



아래의 내용들은 복습입니다.

1. settings에서는 기본 세팅은 같고, templates로 템플릿을 나눕니다.
2. pages 앱을 만들고, urls.py(router)를 분리해줍니다.
3. views.py에서 index.html을 렌더링 해줍니다.



static file을 페이지에 삽입하기 위해서는 다음과 같은 과정을 거칩니다.

pages 앱 하위에 pages/templates/pages/index.html 를 만들어주고 수정합니다.

```html
<!-- pages/templates/pages/index.html -->
{% extends 'base.html' %}
{% load static %}

{% block content %}

hello static files
<img src="{% static 'images/bonobono.jpg' %}" alt="bonobono">
{% endblock %}
```



pages/static/images/bonobono.jpg

위의 폴더에 그림 파일을 다운로드 받아서 집어넣어주고,

`python manage.py runserver`로 서버를 실행시켜 줍니다.

![image-20210528100611611](img/README/image-20210528100611611.png)

위와 같이 그림이 실행되어 있는 것을 볼 수 있습니다.

django에서 static file을 사용할 때에는, `{% load static %}` 구문으로 static file을 사용할 것이라고 선언해주고, `{% static 'images/bonobono.jpg' %}` 이 구문으로 실제 static file을 제공할 url을 만들어서, 그 url을 집어넣어 주는 방식입니다.



다음으로, ORM을 이어서 하겠습니다.