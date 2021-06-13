# day11: ORM 1:N 관계



지난 번에 했던 소스코드에 이어서 합니다.

저는 pages 라는 앱을 만들었는데, 앱 이름을 article로 만들었고, model 이름도 Article로 만드셨으면,

그대로 진행하셔도 괜찮습니다.



오늘은 model 부분 먼저 시작하겠습니다.



## Comment 모델 생성

일반적인 게시물과 comment는 1:N 관계입니다.

하나의 article에 대해서 comment는 여러 개가 될 수 있습니다.

반대로 comment는 여러 개의 게시물에 대한 comment가 될 수 없고, 단 하나의 게시물과 관계가 있습니다.



Comment에 대해서는 다음과 같이 모델을 만듭니다.

Foreign Key는 Article(좀 더 정확하게는 Article의 PK)이 됩니다.

| Article    | Comment         |
| ---------- | --------------- |
| PK         | PK              |
| title      | FK(Foreign Key) |
| content    | content         |
| created_at | created_at      |
| updated_at | updatedat       |



```python
# articles/models.py
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # models.CASCADE 외래키의 부모가 삭제 되었을 때 함께 삭제하도록 하는 옵션.
    # SET_NULL, SET_DEFAULT 옵션도 있음.
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta: # 메타 클래스를 지정해서, 순서를 정렬할 수도 있음
        # 맨 마지막에 생성된 것 기준으로 내림차순 정렬함
        ordering = ['-pk', ]
    
    def __str__(self):
        return self.content

```



변경된 모델의 적용을 위해서 migrate를 해주어야 합니다.

```shell
(venv) $ python manage.py makemigrations
(venv) $ python manage.py migrate
```



## comment 만들기

```python
>>> article = Article.objects.get(pk=1)
>>> article
<Article: 제목>
>>> comment = Comment()
>>> comment
<Comment: <Article(None):Comment(None)->>
>>> comment.content = '댓글입니다'
>>> comment.article = article
>>> comment.save()
>>> comment
<Comment: <Article(1):Comment(1)-댓글입니다>>
>>> comment.pk
1
>>>
```



comment에서는 comment.article 로 article에 대한 참조를 할 수 있습니다.

게시물에서도 해당 게시물에 관한 comment에 접근할 수 있습니다.

```python
>>> article = Article.objects.get(pk=1)
>>> article.comment_set.all()
<QuerySet [<Comment: <Article(1):Comment(2)-second comment>>, <Comment: <Article(1):Comment(1)-댓글입니다>>]>
```



방금 위에서는 article.comment_set.all()로 접근했지만, 이름을 바꿀 수도 있습니다.

models.ForeignKey에서 related_name을 'comments'로 설정해 주면, 이제부터 article에서 comments.all()로 접근할 수 있습니다.

```python
# articles/models.py
...

class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # models.CASCADE 외래키의 부모가 삭제 되었을 때 함께 삭제하도록 하는 옵션.
    # SET_NULL, SET_DEFAULT 옵션도 있음.
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')

...
```

또한, comments.all() 대신에 django ORM의 다른 문법들도 그대로 사용하실 수 있습니다.



## urls.py



```python
# articles/urls.py

from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('articles/', views.index, name="index"),
    path('articles/create/', views.create, name='create'),
    path('articles/<int:pk>/', views.detail, name='detail'),
    path('articles/<int:pk>/delete/', views.delete, name='delete'),
    path('articles/<int:pk>/update/', views.update, name='update'),

    # Comment의 url
    path('articles/<int:pk>/comments/create/', views.comment_create, name='comment_create'),
    path('articles/<int:article_pk>/comments/<int:comment_pk>/update/', views.comment_update, name='comment_update'),
    path('articles/<int:article_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete')
]
```



## views.py

```python
# articles/views.py

from django.shortcuts import render, redirect
from .models import Article, Comment

...

def comment_create(request, pk):
    # 댓글을 달 게시물
    article = Article.objects.get(pk=pk)

    if request.method == "POST": # POST로 요청이 오면, 댓글을 생성합니다.
        comment = Comment()
        content = request.POST.get('content')
        comment.content = content
        comment.article = article
        comment.save()
        return redirect(article)
    else:
        # return redirect('articles:detail', article.pk)
        return redirect("articles:details", pk=pk) # absolute url을 설정했기 때문에 가능합니다.

def comment_update(request, article_pk, comment_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST': # POST로 요청이 오면 댓글을 업데이트합니다.
        content = request.POST.get('content')
        comment = Comment.objects.get(pk=comment_pk)
        comment.content = content
        comment.save()
        return redirect(article)
    else:
        article = Article.objects.get(pk=article_pk) # GET으로 요청이 오면 업데이트하는 화면을 보여줍니다.
        comments = article.comments.all()

        context = {
            'article': article,
            'comments': comments,
            'comment_pk': comment_pk
        }

        return render(request, 'articles/comment_update.html', context)
    

def comment_delete(request, article_pk, comment_pk):
    article = Article.objects.get(pk=article_pk)
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect(article)

```





## templates

```html
<!-- articles/templates/articles/detail.html-->
...

<ol>
    {% for comment in comments %}
    <li>{{comment.content}} -
        <small>생성일자: {{comment.created_at|date:"SHORT_DATE_FORMAT"}}</small> / 
        <small>수정일자 : {{comment.updated_at|date:"SHORT_DATE_FORMAT"}}</small>
    </li>
    {% empty %}
    <p><strong>댓글이 없습니다!</strong></p>
    {% endfor %}
</ol>

...

```



comment에 대해서도 나머지 CRUD를 만들어야 합니다.

Read 동작에 대한 것은 별도로 필요가 없습니다.

article의 상세 페이지에서 comment의 list를 출력하는 것으로 충분합니다.



(TODO: CRUD 내용 추가해서 마감하기)



## 다음 시간에 진행할 내용

- User 인증