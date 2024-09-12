### Первый практикум. Организация курса. GitHub. Личная страничка с использованием HTML    

* Знакомимся

* О структуре курса

* GitHub

* Личная страничка  


### Основы работы с GitHub

На занятиях по Python вы научитесь полноценно пользоваться GitHub как системой контроля версий. Для выполнения заданий в классе и домашнего задания достаточно, чтобы вы  

* завели аккаунт на GitHub  

* сделали форк (копию) репозитория [lingdata](https://github.com/nestorica/lingdata)  

* загрузили файлы в репозиторий  

Все эти действия можно совершать с помощью браузера, особенно если вы не знаете заклинаний `git add`, `git commit`, `git push` в командной строке.  


#### 1. Создаем аккаунт на GitHub

На странице [github.com](https://github.com/) нажмите Sing Up, заведите аккаунт (имя - любое), подтвердите его по электронной почте.

<img src="fig/github-signup.png" alt="sign up" width="70%"/>

Возможно, вам предложат пройти дополнительные тесты, чтобы убедиться, что вы не робот:

<img src="fig/github-notarobot.png" alt="not a robot" width="50%"/>


#### 2. Копируем репозиторий lingdata  

Убедитесь, что вы залогинены на гитхабе. Откройте страницу по ссылке (https://github.com/nestorica/lingdata) и нажмите кнопку `fork`. В результате в вашем аккаунте появится копия этого репозитория, с которой вы дальше будете работать. (Пожалуйста, не меняйте имя репозитория `lingdata` и его статуса Public, чтобы мы могли автоматически проверять ваши задания.)   

<img src="fig/github-forkrepo.png" alt="fork repo" width="70%"/>


#### 3. Работаем с _вашим_ репозиторием lingdata  

В репозиторий можно зайти по ссылке вида `https://github.com/<your-account>/lingdata` (иными словами, вместо nestorica впишите ваше имя пользователя).  

1. Структура файлов

Чтобы увидеть структуру файлов, нажмите на **Code** в левом верхнем углу. 


2. История изменений

GitHub является системой контроля версий. С помощью коммитов (commit - команда обновления содержания репозитория) фиксируются с привязкой ко времени все изменения в файлах, произошедшие с прошлого коммита. Это дает возможность работать с кодом нескольким разработчикам, отменять коммиты, анализировать активность разработки проекта. На GitHub можно посмотреть историю изменения файла, сравнить версии файлов в разных коммитах, посмотреть на историю изменений в вашем аккаунте в целом (в открытых репозиториях).   


3. Ветки репозитория

Ветки (branch) - это способ параллельной работы с репозиторием, когда разные разработчики вносят изменения (делают коммиты) в разные версии репозитория. В ветках может быть разный состав файлов. Например, у проекта может быть основная ветка, предлагаемая как релиз проекта для пользователей, и другая для текущей разработки. В какой-то момент такие ветки могут объединить (смерджить версии в единую, автоматически или вручную), а потом снова начать развивать ветки независимо.  

<img src="https://www.develer.com/wp-content/uploads/2021/08/image-9.png" alt="branches and commits" width="40%"/>

Сейчас у нашего репозитория есть две ветки - `main` и `gh-pages`. Одна из веток, `main`, дефолтная - это значит, что она открывается в браузере по умолчанию и вы по умолчанию вносите изменения в нее. Вторая ветка -- для GitHub pages, сервиса, который позволяет представлять содержание репозитория как сайта.  

<img src="fig/github-branches.png" alt="branches" width="30%"/>  

В новой вкладке откройте ссылку [https://nestorica.github.io/lingdata/], чтобы увидеть страницу, представляющую содержание файла README.md в корне репозитория.  


4. Создайте новый файл

   с помощью кнопки `Add files` > `+ Create new file` создайте файл и назовите его `test.txt`.

<img src="fig/github-newfile.png" alt="create new file" width="70%"/>  
  
Напишите в нем любой текст и сохраните изменения -- `Commit changes...` (зеленая кнопка). При коммите полезно описывать в специальном поле, какие изменения вы внесли и почему.  

<img src="fig/github-newfile1.png" alt="new file created" width="70%"/>  

Проверьте, что изменилось в структуре репозитория и в истории изменений.  


5. Отредактируйте существующий файл

Кликните на файл `test.txt`. Кликните на "карандашик" справа вверху. Измените текст. Снова сохраните изменения -- Commit!


6. Чтобы создать папку внутри репозитория

  нажмите `Create file` и создайте файл с именем `newfolder/readme.txt` или `newfolder/readme.md`, где `newfolder` - имя вашей папки. В файл readme рекомендуется написать краткий комментарий, для чего эта папка. Сохраните изменения.  


7. Кнопка `Raw`

Когда вы кликаете на файл, то открывается страница GitHub со всеми кнопками и сервисами, позволяющими работать с этим файлом. Кнопка `Raw` позволяет увидеть файл в "сыром" текстовом виде (со всеми тегами разметки, если они есть).  


8. Удаление файла

На странице файла, нажмите три точки справа от имени файла, а затем красную ссылку `Delete file`. Удаление всех файлов в папке удалит и саму папку.  

Удалите последний созданный файл. (Но его содержание и история операций с ним будут доступны через историю изменений).  


#### 4. Markdown   

Markdown (md) - это облегченный язык для разметки форматирования текстов. Он часто используется для написания документации на GitHub. 

Самое основное   

```markdown

# Заголовок 1
## Заголовок 2
### Заголовок 3

* ненумерованный
* список
  * элементы второго уровня
  * элементы второго уровня

1. нумерованный 
2. список

**Bold** и _Italic_ и `ключевые слова`

[Link](url) and ![Image](src)

Три обратных апострофа  (```) выделяют и конец блока текста, обычно кода программы
```

Более подробно тут [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

Отредактируйте файл `test.txt` (см. п. 5 выше), добавив форматирование шрифта полужирным и курсивом, добавив ненумерованный список, а затем добавив ссылку.  

Вы можете переключаться между режимами `Edit` и `Preview`, чтобы увидеть визуальные эффекты форматирования.



### HTML

HTML - язык разметки оформления веб-страниц. HTML-код работает также в файлах Markdown-а.  

Большинство тегов  html - парные, закрывающий тег содержит слэш. Например. <p> - открывающий тег, </p> -- закрывающий. Перенос строки <br> и тег <img> -- непарные теги.  

```
<html>
<body>

  <h1>Заголовок 1 уровня</h1>
  <h2>Заголовок 2 уровня</h2>
  <h3>Заголовок 3 уровня</h3>

  <p>Абзац</p>

  <p>Принудительный перенос <br> строки (line break)

  <b>полужирный</b> и <i>курсив</i> и <i><u>подчеркнутый</u> курсив</i>

    с помощью CSS стилей в <span style="font-weight:bold; color:blue;">тексте</span>. 

  <a href="github.com">гиперссылка</a>

  <img src="https://ruscorpora.ru/i/logo.gif"> картинка
  </p>

</body>
</html>
```

У тегов бывают атрибуты и значения. В вышеприведенном примере у тега `<img src="https://ruscorpora.ru/i/logo.gif">` есть атрибут src (ссылка на файл-источник) и его значение (URL-ссылка).  

Некоторые html-теги требуют обязательно "обвязки" другими тегами. Например, теги списка `<li>` (_li_st) не будут работать без обвязки тегами `<ul>` (*u*nordered *l*ist) или `ol` (*o*rdered *l*ist) и т.п.

```
<ul>
  <li>Гагарин</li>
  <li>Титов</li>
  <li>Николаев</li>
</ul>
```

До кода, начинающегося с тега `<body>` (основной код страницы), может идти раздел, заключенный в теги <head> ... </head> -- это шапка файла с метаданными и ссылками на внешние файлы и скрипты, используемые для оформления страницы.  

В более продвинутых вариантах html-страниц код внутри `<body> ... </body>` делится на логические блоки c помощью тегов `<div>`, `<article`, `<header>`, `<footer>`, `<nav>` и т. п. Такие блоки выделяют шапку с названием страницы и меню, "подвал" внизу, другие визуально выделяющиеся разделы страницы, а также служат для объединения нескольких абзацев или таблиц. Теги <div> могут быть последовательно вложены друг в друга:

```
<div>
  Раздел "Новости"
  <div>
    Текст первой новости
  </div>
  <div>
    Текст второй новости
  </div>
</div>
```

Аргумент `id` у такого рода тегов позволяет приписать им уникальный идентификатор, а `class` -- приписать класс. Это позволяет в дальнейшем блоки внутри тегов одного класса, например `<div class="nav1">`, оформлять одинаковыми шрифтами, цветами и т. п.  

**Задание**  

Начните в классе выполнять [задание](hw1-html.md) по редактированию шаблона личной страницы. В конце работы загрузите все измененные и новые файлы в репозиторий. 

Вы сможете увидеть результат вашей работы по ссылке вида `https://<your-account>.github.io/lingdata/mywebpage/`.  



### Дополнительные материалы

* [Введение в HTML](https://developer.mozilla.org/ru/docs/Learn/HTML/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5_%D0%B2_HTML)

* [Прекрасный учебник HTML и CSS](https://www.w3schools.com/html/)

* Bootstrap [объяснение сеточной системы Bootstrap](https://ktonanovenkogo.ru/html/bootstrap/setochnaya-sistema-bootstrap-3-primer-raboty-chast-2.html)

* Еще один [образец бутстрапа](https://nevmenandr.github.io/work-web-page-example/)


##### Как создать репозиторий GitHub "с нуля" 

<img src="fig/github_new_repo.png" alt="new repo" width="30%"/>

Если так не получилось, зайдите на основную страницу своего гитхаба (например, моя - https://github.com/olesar, где olesar - название моего аккаунта) и нажмите кнопку New на вкладке Repositories

<img src="fig/github_new_repo1.png" alt="another new repo" width="40%"/>

3. Укажите имя репозитория, тип (Public) и добавьте файл README.

<img src="fig/github_repo_type.png" alt="another new repo" width="40%"/>

##### Как удалить репозиторий  

Если вы по ошибки форкнули не тот репозиторий, перейдите в его корень, выберите меню Settings и затем (в самом низу списка) `Delete this repository`. Будут стерты и сами файлы, и история их изменений.  

##### Двухфакторная проверка подлинности (2FA) GitHub   

Время от времени GitHub требует подтверждения доступа к управлению репозиторием через веб-сайт (но не через командную строку!). Скорее всего, вам понадобится установить приложение на телефоне для генерации разовых кодов для входа на сайт или подтверждать вход в этом приложении. (https://docs.github.com/ru/enterprise-cloud@latest/authentication/securing-your-account-with-two-factor-authentication-2fa/accessing-github-using-two-factor-authentication)