## ДЗ3. "Разработка фрагмента учебного корпуса", часть 1

Задачей этого блока заданий является подготовка материалов для учебного корпуса LiveCorpus. Вам предстоит:
* записать видеоматериалы для корпуса  
* сделать метаразметку (информация о говорящих и текстах в целом)  
* отобрать фрагменты записи для корпуса и расшифровать 
* разбить текст на реплики (минимальные диалогические единицы)
* сделать лексико-грамматическую разметку со снятой неоднозначностью  
* сделать жестовую разметку  
* провести валидацию формата и подготовить файлы к заливке на сайт корпуса
  
Но не всё сразу.

### Запись видеоматериалов для корпуса

#### Информант 

В этом году мы будем записывать речь *носителей регионального русского* (не *москвичей*). Предлагаем студентам не из Москвы, Московской области и Эквадора побыть в роли информантов, а остальным потренироваться в записи видео.

Если вы категорически против быть информантом (имеете право), напишите нам.

Мы [распределили рандомным образом](https://docs.google.com/spreadsheets/d/1_TkpAaQNKIiIAtKA3AgGxrB6BkqHgESa5gHfTFCZ9tE/edit?usp=sharing) *не-москвичей* по *москвичам* (вас не чётко поровну, поэтому есть несколько троек, а не пар). Вы можете меняться как угодно, но желательно, чтобы все *не-москвичи* побыли информантами.

#### Запись

Длительность: около 20 минут (минимум 15, но лучше больше)

Формат: любой при хорошем качестве (идеальный - формат с минимальным сжатием)

Должна быть хорошо видна жестикуляция (то есть как минимум верхняя часть туловища, РУКИ)

Перед началом содержательной части записи информант должен дать устное согласие на запись: "Я, такой-то такой-то, не возражаю, что эта и другие сегодняшние записи моей речи будут использованы в учебных и научных целях", дальше нужно назвать город и дату. Согласие должно остаться на видео/аудио.  

Что записываем: спонтанную речь. Придумайте нестандартную речевую активность для информанта, попросите объяснить, как добраться от одного места до другого (от школы информанта до дома), как играть в настольную игру (не самую его любимую, чтобы это не было заученным текстом), спросите, как человек будет действовать в гипотетической ситуации, можно задавать неочевидные вопросы о жизни и т.д.

#### Выбор фрагмента для разметки

В ходе проекта вам предстоит разметить 5 минут видео. (В этом дз от вас требуется первоначальная разметка только 30 секунд из 5 минут.)

*Как выбрать фрагмент?*
- Фрагмент заполнен речью, информант не замолкает надолго
- Говорящий много жестикулирует, его лицо и руки хорошо видны
- Языковые ошибки, запинки, шероховатости - не страшно, будет что размечать и анализировать
- Интервьюер не сильно перебивает
- Для корпуса ценен материал с особенностями фонетики, интонации, лексики

Выберите в паре два фрагмента по 5 минут (а в тройке три фрагмента). Они не обязательно должны идти подряд. Фрагменты должны быть разные, не пересекаться.

Один фрагмент интервьюеру, другой информанту.
"Немосквичи" при желании могут между собой поменяться фрагментами, чтобы размечать не себя, а кого-то другого.

***Не режьте видео! Работайте дальше с целиковым!***

#### Файлохранилище
Файлы должны быть названы в формате `Irkutsk_jms2005.avi`, где первая часть - название города/региона информанта (Saint-Petersburg, NizhnyNovgorod), затем идут инициалы информанта (например, _jms_ для _Юлия Михайловна Щепкина_) и его год рождения.
Положите файл в [папку](https://drive.google.com/drive/folders/1Lq6iXyNv8CP_nqQzUr6os6ROHhN6nmhD?usp=sharing) и дайте ссылку на него [в таблице](https://docs.google.com/spreadsheets/d/1so6XokH4ZV2rIGABVyGCsmWzZ4GGWcG4IgHOrFiWICM/edit?usp=sharing), заполнив поля с метаинформацией. Если запись по каким-то причинам разбилась на несколько файлов, соедините их. (Не рекомендуется выкладывать медиафайлы на GitHub, так как он не предназначен для хранения объемных данных.)

Видео в папку загружается 1 раз, а в таблице должно быть по строчке на разметчика.

### Расшифровка 30 секунд фрагмента

* разметить фрагмент в ELAN, разделив речь говорящих на реплики (ЭДЕ) и расшифровав их в аннотациях (каждого говорящего - в отдельном слое)
* объем разметки на оценку - минимум 30 секунд
* должен получиться слой `text@imp1988f` (и слой text@abl2006f, если во фрагменте есть речь интервьюера). Инициалы: имя, отчество, фамилия
* имя файла с видео и имя файла разметки должны совпадать. Пример: - файлы `Cherepovets_pal2006.avi` и `Cherepovets_pal2006.eaf`.
* загрузите файл разметки (он имеет расширение .eaf) на GitHub в папку `livecorpus` (в вашем репозитории `lingdata`)
* проверьте, что вы загружаете в ветку `main` (не `gh-pages`) - ветка указана слева сверху над файлами вашего репозитрия

(Совет: Не используйте кириллицу в названиях папок на пути к редактору ELAN, мультимедийным файлам и файлам, которые создает ELAN.)

### Бонусное задание   
Идеально выполненное домашнее задание оценивается в 8 баллов. Бонусное задание не является обязательным и позволяет получить 9-10 баллов, если основная часть выполнена на 8.
Выполнение бонусного задания требует много времени. Ассистенты не консультируют по поводу бонусных заданий.   

Так выглядит гораздо более сложная разметка реплик в корпусе "[Рассказы о сновидениях](http://www.spokencorpora.ru/showtrans.py?file=00dreams/NDS_021-m-z)".  
Изучите [правила](http://www.spokencorpora.ru/showtranshelp.py) упрощённой (не полной, не минимальной) транскрипции и выполните расшировку 30 секунд вашего фрагмента согласно им.   
В ELAN для таких транскрипций нужно создать новые слои с названием вида `spokencorpora@aaa1988f`. 

____________________________
## Подробная инструкция по расшифровке

#### 1. Настройка проекта  

* Cоздайте новый проект, подключите к нему видеофайл, сохраните файл разметки, назвав так же, как видео     

* Если вы хотите использовать визуализацию звуковой дорожки в ELAN, переконвертируйте ваше видео в *.wav - файл (с помощью любого онлайн-конвертора, погуглите, например, "mpg to wav online"). 
В этом случае присоедините сразу видео и аудио к новому проекту.  

* Импортируйте типы слоев из образца ([.eaf файл](https://github.com/olesar/lingdata/blob/gh-pages/data/elan_livecorpus_template.eaf)): Тип > Импорт...      

* Создайте слой реплик для каждого говорящего: Слой > Новый...   

```
Установите свойства слоя (для говорящего @aaa1988f так, но вы укажите ники ваших говорящих):  
* Название слоя `text@aaa1988f`  
* Родительский слой - none   
* Тип - utterance  
Обязательно заполните поля "говорящий" (@aaa1988f), "разметчик" (латиницей - например, название вашего аккаунта на GitHub), язык по умолчанию (русский).  
```

#### 2. Разметка реплик

* Сделайте слой активным для разметки (дабл-клик на его названии в левой части экрана)  
* Прослушайте фрагмент, определите приблизительное время начала и конца реплики.  
* Кликните в слое на месте начала релики - туда переместится бегунок - красная вертикальная полоса.  
* Создайте аннотацию, проведя мышкой с зажатой кнопкой от начала до конца отрезка.  
* Два раза кликните посередине, - и вы сможете вписать расшифровку. Нажмите Enter.   
* Повторно прослушайте фрагмент, уточните время начала и конца реплики, отредактируйте аннотации, если нужно.   
Ниже мы даем советы по расшифровке, прочитайте их внимательно.  

``` 
* ALT + потянуть мышкой в середине аннотации -- чтобы подвинуть всю аннотацию влево/вправо  
* ALT + потянуть мышкой на левой/правой границе аннотации -- чтобы подвинуть левую/правую границу  
* ALT + d - удалить реплику (работает также копипейст и контекстное меню по правой кнопке мышки)  
* Двойной клик - редактировать содержание   
* Shift + Space - проиграть выделенную аннотацию    
В выделенной аннотации:
* Аннотация > Разбить... - разобъет посередине на две  
Чтобы разбить в конкретном месте аннотации, в контекстном меню выбрать Разбить аннотацию...
* Аннотация > Объединить со следующей / c предыдущей  
```

Совет 1: можете установить замедленное проигрывание: Регулировка > Скорость...

Совет 2: Не забывайте **регулярно сохранять** файл. Можно установить автосохранение: `Файл > Автосохранение резервной копии > 5 минут`

Совет 3: если вы пишете не очень грамотно, экспортируйте файл с разметкой в текст с разделителями (`Файл > Экспорт`) и проверьте его в любом сервисе проверки орфографии. Это сохранит много сил на следующих этапах работы.

### Об особенностях расшифровки записей  

Расшифруйте запись так, как вы ее слышите, отражая все оговорки, неправильности, морфологические особенности, порядок слов, сниженную лексику, если есть. Например, _то глишь_ вместо _того глядишь_, _не знам_ вместо _не знаю_, _сёдни_ вместо _сегодня_. 
Фиксируйте все оговорки, фальстарты и прочие шероховатости спонтанной речи. Записывайте междометия, поддерживающие разговор (_ага_, _ну_), слова-паразиты (_гм_, _ммм_, _эээ_), недоговоренные слова (_и тут она по= вышла_), запинки (_гово= сказала_) - т. е. все, что вы можете расслышать.
Не используйте знаки препинания (исключение - знак вопроса в вопросе и восклицательный при восклицании), микропаузы внутри реплики обозначайте одинарным слэшем.
  
Примеры расшифровок: 
```
там спрашивают фамилию-то 
Поликарпова / ты с какого года?
ну / это / ро= родители сказали
а / ну да / эээ
```

Расшифровка записывается в стандартной русской орфографии. Мы не пишем фонетическую транскрипцию, если информант, например, якает ("ой / бяда бяда / огорчение" (с) Домовёнок Кузя), всё равно пишем `ой / беда беда / огорчение`. При этом лексические, морфологические и синтаксические особенности речи отражаем.
Если из-за ударения меняется слово, отражаем это, считаем, что это лексическая особенность. `ростить` (при ударении на о не пишем "растить`")

Букву ё на письме отражаем. Пишем "ёлка", а не "елка".

Если говорящий говорит очень долго совсем без пауз, ориентируйтесь на синтаксическую и смысловую структуру, интонацию, чтобы разбить его речь на реплики.  

* __Аббревиатуры__ записываются обычным образом (ср. ЦСКА)  
* __Неразборчиво__. Если текст в том или ином месте не удается разобрать, то пишите `#нрзб#` (в решетках, без пробелов, именно эти четыре буквы)   
* __Одновременно__. Когда говорят несколько человек одновременно и разобрать ничего не удается, нужно использовать ремарку `#одновременно#` 
В случаях невербального общения (например, общий гул без ясно вычлененных реплик, смех, хмыканье) допустимо поставить отдельную реплику, например, `#смеется#`. 
Увлекаться комментированием всех действий, в том числе заполняющих паузы ("берет сковородку", "долго глядит в окно") не нужно. Пожалуйста, не используйте пробелы внутри ремарок. 
* __Что__. _Что_ в устной речи стандартно произносится как _што_, но записывать его нужно в стандартной орфографии (т. е. _что_). Это относится ко всем другим случаям стандартных расхождений между орфографией и произношением.  
* __Щас__. Варианты частиц (_сейчас_, _щас_, _ща_) в расшифровке различаются.  
* __Ммм__. Запись междометий как _м_, _мм_ или _ммм_, (_э_, _ээ_ или _эээ_) мы оставляем на ваше усмотрение, но для растянутого произнесения лучше не использовать более трех одинаковых буквы подряд. Растянутое произнесение гласных в других словах отображать в расшифровке не надо (_большой_, а не _баальшой)_.     
* __Индивидуальные особенности произнесения__. Если говорящий имеет акцент, фонетические региональные особенности (например, фрикативное _г_), шепелявит и т. д., то есть его речь системно отличается от литературного стандарта, отражать эти особенности в расшифровке не нужно.
* __Речевые маски и искажения__. Другое дело - если говорящий в отдельных словах изображает "кавказский", "чукотский" и т. п. акцент или специально искажает слово, тогда попытайтесь это отобразить в расшифровке (например, _дэушка_ или _облизьяна_).   
* __Особые знаки препинания__: используйте `!`, `?` для обозначения восклицательных и вопросительных реплик, а также `=` для обозначения обрыва слова. 
* __Кавычки__ убедительно просим не использовать в разметке, тексты с ними потом тяжело обрабатывать (пишите _стадион Динамо_ без кавычек)   
* __Заглавные буквы__ нужны только в именах собственных
* __Заимствования и переключение кода__. Заимствования пишем кириллицей (*хеллоу*, *ол инклюзив* (и *олонклюзив* при таком произнесении)). При этом сложные и редкие названия (например, название нераспространённой музыкальной группы), а также переключение кода (фразы на другом языке) стоит записывать в их орфографии.
* __(Не)кириллические символы__. Помимо случаев описанных выше мы используем буквы русского алфавита. Не стоит использовать дополнительные символы для обозначения необычных (вау, не wау; огород, не оɣород и не оґород).

Примечание: Мы во многом, но не во всем, ориентируемся на правила расшифровки в [Мультимедийном корпусе](https://processing.ruscorpora.ru/search.xml?env=alpha&env=alpha&api=1.0&mycorp=&mysent=&mysize=&mysentsize=&dpp=&spp=&spd=&mydocsize=&mode=murco&lang=ru&sort=i_grtagging&nodia=1&text=lexgramm&ext=10&nolinks=1&ell=1&parent1=0&level1=0&lex1=%D0%B2%D0%BE) Национального корпуса русского языка.    
  
## Пояснения про запись

Запись должна проводиться в тихом месте (не в кафе и не на улице, где ездят машины, желательно закрыть окна), по возможности без посторонних звуков. Плохо, если в комнате голые стены, лучше, чтобы были книги, картины, ковры и т.п. Старайтесь не говорить параллельно с информантом, дожидайтесь конца реплики.

Если качество записи аудио на диктофоне(телефоне) лучше, чем на камере(телефоне), можете записать дополнительно аудиодорожку, а потом свести аудио и видео. (Чтобы было легко синхронизировать две дорожки, пусть информант в начале записи хлопнет, тогда можно будет соединить по резкому пику на записях.)

Мы записываем именно видео, потому что так можно зафиксировать не только голос, но и жесты, мимику говорящего. Запись можно делать на телефон или видеокамеру. Должно быть хорошо видно лицо и руки говорящего.

\- А можно мы в зуме запишем?
- Нет, нужно вживую. Говорение перед экраном компьютера  - немного другой жанр. Жестикуляции скорее всего будет меньше, качество записи хуже и т.д.

\- Нашей паре (тройке) совсем неудобно состыковываться по времени. Что делать?
- Поменяйтесь, договоритесь с теми, с кем вам удобнее встретиться.

\- Мой информант пропал (исчез). Заболел, не выходит на связь и т.д.
- К сожалению, такое с информантами случается. Попробуйте присоединиться к одной из пар и договоритесь, чтобы вам досталось 5 минут записи.

\- Я безумно хочу записать своего знакомого не с курса и размечать запись с ним.
- Если всех однокурсников, готовых записаться, кто-нибудь записывает, можете. Требование к информанту: информант *не-москвич* (не проживал в Москве более 2-3 лет, носитель русского языка), старше 18 лет.

\- Я "немосквич", меня записывают, но я тоже хочу потренироваться в записи видео с информантом.
- Поучаствуйте в работе другой пары или см. предыдущий пункт.
