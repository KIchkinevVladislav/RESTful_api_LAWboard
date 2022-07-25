# API for LAWboard

Учебный проект по реализации доступа посредством RESTful API к сайту LAWboard. 

## Описание

Сайт LAWboard реализизует возможности публикации новостей и иной информации, с целью правового просвещения несовершеннолетних.
Помипо публикации постов на сайте возможно их комментирование, через авторизованный аккаунт, подписка на интересующих авторов.

## API

Описание доступных для взаимодейстия ресурсов с указанием методов:

**Взаимодействие с постами:**

  GET  http://localhost:8000/api/v1/posts/        #просмотреть все посты 
   
  GET  http://localhost:8000/api/v1/posts/{id}/   #Получить публикацию по id 
        
  POST  http://localhost:8000/api/v1/posts/       #создание поста 
   
  PUT   http://localhost:8000/api/v1/posts/{id}/  #Обновить публикацию по id 
   
  PATCH http://localhost:8000/api/v1/posts/{id}/  #Частично обновить публикацию по id 
   
  DELETE http://localhost:8000/api/v1/posts/{id}/ #Удалить публикацию по id 

**Взаимодействие с тематиками сообщений:**

   Работа с GROUP: 
     
   GET http://localhost:8000/api/v1/group/  #Получить список всех групп 
    
   POST http://localhost:8000/api/v1/group/ #Создать новую группу

**Взаимодействие с комментариями:**

   GET  http://localhost:8000/api/v1/posts/{post_id}/comments/                #Получить список всех комментариев публикации 
    
   GET  http://localhost:8000/api/v1/posts/{post_id}/comments/{comment_id}/   #Получить комментарий для публикации по id 
         
   POST http://localhost:8000/api/v1/posts/{post_id}/comments/                #Создать новый комментарий для публикации 
    
   PUT  http://localhost:8000/api/v1/posts/{post_id}/comments/{comment_id}/   #Обновить комментарий для публикации по id 
    
   PATCH http://localhost:8000/api/v1/posts/{post_id}/comments/{comment_id}/  #Частично обновить комментарий для публикации по id 
    
   DELETE http://localhost:8000/api/v1/posts/{post_id}/comments/{comment_id}/ #Удалить комментарий для публикации по id 

**Взаимодействие с подписчиками:**

   GET http://localhost:8000/api/v1/follow/  #Получить список всех подписчиков 
    
   POST http://localhost:8000/api/v1/follow/ #Создать подписку 

**JWT-токен:**

   http://localhost:8000/api/v1/token/           #Получить JWT-токен 
    
   http://localhost:8000/api/v1/token/refresh/   #Обновить JWT-токен 
