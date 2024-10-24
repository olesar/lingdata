## Домашнее задание 3

#### Разработка фрагмента корпуса, часть 2 (ELAN-1)  

Это домашнее задание предполагает, что каждый из вас подобрал себе материал для разметки. [Как подобрать](https://github.com/olesar/lingdata/blob/gh-pages/livecorpus-intro.md)  
Задание состоит из двух частей - метаразметки и разметки реплик говорящих в ELAN. В конце работы загрузите файл разметки (он имеет расширение .eaf) на GitHub.

### Метаразметка записей  

Добавьте в [таблицу](https://docs.google.com/spreadsheets/d/1DrainUM6S2Exe2D0lMdqnUjhUQEiakvNptsKhrKObJQ/edit?usp=sharing) больше метаинформации о ваших видео. Сверьтесь с примером (первые две строки), все ли данные вы указали.  

### Папка для проекта   
* `livecorpus` (все строчными буквами) - папка в вашем репозитории курса (lingdata), сюда кладем `.eaf` файлы. 
* Напомним, один из способов создать папку на GitHub - в вашем репозитории GitHub выбрать  
  * `Add file` > `Create new file` > создать файл с именем `livecorpus/readme.md`> `Commit`  
* Имя файла с видео и имя файла разметки должны совпадать. Пример: - файлы `Cherepovets_pal1964_life.avi` и `Cherepovets_pal1964_life.eaf`.  

(Советы: ELAN по умолчанию сохраняет .eaf файл в кодировке Юникод (UTF8), не меняйте ее.  Не используйте кириллицу в названиях папок на пути к редактору ELAN, мультимедийным файлам и файлам, которые создает ELAN.)   

### Расшифровка в ELAN  
Более подробную информацию о том, что нужно делать на каждом этапе см. ниже, п. 1-3.

#### Рассказ о жизни (всем):
* разметить фрагмент, разделив речь говорящих на реплики (ЭДЕ) и расшифровав их в аннотациях (каждого говорящего - в отдельном слое)
* объем разметки на оценку - минимум 1 минута.
* должен получиться слой `text@aaa1988f` (и слой text@aaa2003f, если во фрагменте есть речь интервьюера). Инициалы: имя, отчество, фамилия
  
#### Назови картинку (порядок записи А):
* завести (или проверить, что в вашем файле они заведены) типы слоев: utterance и stimulus (стереотип у последнего Symbolic Association). Напомним, что типы слоев и слои можно импортировать из [шаблона](data/elan_livecorpus_template.eaf)   
* завести (или проверить, что они заведены) слои вида: text@aaa1988f (тип `utterance`) для информанта, называющего картинки, picnumber@aaa1988f (тип `stimulus`, родительский слой `text...`) для обозначения номера картинки (переименуйте слой в picnumber@..., если это нужно)  
* создать аннотации для фрагментов, в которых информант называет предмет (`голубь`), шум, не имеющие отношения к делу реплики, подробное описание картинки, избыточные определения и т.п. оставляем без аннотации  
* в слое `picnumber` подписать номера картинок, например `101`  для файла `101. голубь (pigeon).jpg`  

#### Игра (порядок записи Б):
* выбрать правильный фрагмент ~30 сек (с предложениями с разной интонацией) 
* завести типы слоев: `utterance` и `utterance_type`. Напомним, что типы слоев и слои можно импортировать из шаблона    
* завести слои:  text@aaa1988f и text@sss2003m для двух говорящих, eduType@aa1988f и eduType@sss2003m (родительский слой `text...`)(EDU - elementary discourse unit)
* расшифровать реплики во фрагменте  
* в слоях eduType разметить реплики, выбрав из инвентаря: "вопрос да/нет", "вопрос частный", "ответ", "повествование" (если это не ответ на вопрос или комментарий к своему ответу), "побуждение" (давай скорее), "другое"  

____________________________
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
* Shift + Space -- проиграть выделенную аннотацию    
В выделенной аннотации:
* Аннотация > Разбить... - разобъет посередине на две  
Чтобы разбить в конкретном месте аннотации, в контекстном меню выбрать Разбить аннотацию...
* Аннотация > Объединить со следующей / c предыдущей  
```

Совет 1: можете установить замедленное проигрывание: Регулировка > Скорость...

Совет 2: Не забывайте **регулярно сохранять** файл. Можно установить автосохранение: `Файл > Автосохранение резервной копии > 5 минут`

Совет 3: если вы пишете не очень грамотно, экспортируйте файл с разметкой в текст с разделителями (`Файл > Экспорт`) и проверьте его в любом сервисе проверки орфографии. Это сохранит много сил на следующих этапах работы.

Комментарий: если в Опциях выбрать метод сдвига таймкодов Bulldozer Mode, то при вставке новых реплик реплика справа, на которую вы случайно "наехали" по таймкоду, не будет стираться, а сдвинется вправо.  


#### 3. Сохраните файлы .eaf, залейте на гитхаб в папку livecorpus
* один файл .eaf с рассказами о жизни/вопросами/ответами  
* один файл .eaf с картинками ИЛИ игрой
Напоминаем про метатаблицу!  

### Об особенностях расшифровки записей  

Расшифруйте запись так, как вы ее слышите, отражая все оговорки, неправильности, морфологические особенности, порядок слов, сниженную лексику, если есть. Например, _то глишь_ вместо _того глядишь_, _не знам_ вместо _не знаю_, _сёдни_ вместо _сегодня_. 
Фиксируйте все оговорки, фальстарты и прочие шероховатости спонтанной речи. Вставьте междометия, поддерживающие разговор (_ага_, _ну_), слова-паразиты (_гм_, _ммм_, _эээ_), недоговоренные слова (_и тут она по= вышла_), запинки (_гово= сказала_) - т. е. все, что вы можете расслышать.
Не используйте знаки препинания (исключение - знак вопроса в вопросе), микропаузы внутри реплики обозначайте одинарным слэшем.
  
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
* __Ммм__. Запись междометий как _м_, _мм_ или _ммм_ мы оставляем на ваше усмотрение, но для растянутого произнесения лучше не использовать более трех одинаковых буквы подряд. Растянутое произнесение гласных в других словах отображать в расшифровке не надо.     
* __Индивидуальные особенности произнесения__. Если говорящий имеет акцент, фонетические региональные особенности (например, фрикативное _г_), шепелявит и т. д., то есть его речь системно отличается от литературного стандарта, отражать эти особенности в расшифровке не нужно.
* __Речевые маски и искажения__. Другое дело - если говорящий в отдельных словах изображает "кавказский", "чукотский" и т. п. акцент или специально искажает слово, тогда попытайтесь это отобразить в расшифровке (например, _дэушка_ или _облизьяна_).   
* __Особые знаки препинания__: используйте `!`, `?` для обозначения восклицательных и вопросительных реплик, а также `=` для обозначения обрыва слова. 
* __Кавычки__ убедительно просим не использовать в разметке, тексты с ними потом тяжело обрабатывать (пишите _стадион Динамо_ без кавычек)   
* __Заглавные буквы__ нужны только в именах собственных  

Примечание: Мы во многом, но не во всем, ориентируемся на правила расшифровки в [Мультимедийном корпусе](https://processing.ruscorpora.ru/search.xml?env=alpha&env=alpha&api=1.0&mycorp=&mysent=&mysize=&mysentsize=&dpp=&spp=&spd=&mydocsize=&mode=murco&lang=ru&sort=i_grtagging&nodia=1&text=lexgramm&ext=10&nolinks=1&ell=1&parent1=0&level1=0&lex1=%D0%B2%D0%BE) Национального корпуса русского языка. 

### Бонусное задание   
Идеально выполненное домашнее задание оценивается в 8 баллов. Бонусное задание не является обязательным и позволяет получить 9-10 баллов, если основная часть выполнена на 8.
Выполнение бонусного задания требует много времени. Ассистенты не консультируют по поводу бонусных заданий.   

Так выглядит гораздо более сложная разметка реплик в корпусе "[Рассказы о сновидениях](http://www.spokencorpora.ru/showtrans.py?file=00dreams/NDS_021-m-z)".  
Изучите [правила](http://www.spokencorpora.ru/showtranshelp.py) упрощённой (не полной, не минимальной) транскрипции и выполните расшировку 1 минуты вашего фрагмента согласно им.   
В ELAN для таких транскрипций нужно создать новые слои с названием вида `spokencorpora@aaa1988f`.    
