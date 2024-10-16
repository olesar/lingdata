### Домашнее задание № 2
Поиск и замена c использованием регулярных выражений  

Результат выполнения домашнего задания загрузите в папку `HW2` вашего репозитория на github.

(Вам нужно создать папку `HW2`в вашем репозитории `lingdata`.)

### 1. Кодировки и простая замена

Скачайте файл [tln_voskr_strange.txt](https://disk.yandex.ru/d/x9QjEXFxSVgZPg). Он представляет текст в неизвестной для вас кодировке.  

1.1 Подберите такую кодировку, чтобы файл в редакторе отображался кириллицей.

Подсказка: это одна из кодировок, которая обычно используется для японского.

Сохраните файл в кодировке UTF-8 под именем russian11.txt   

1.2 Замените в сохраненном файле все двойные сочетания `нн` на `н(н)` (то есть поставьте в скобки вторую букву _н_).

Сохраните файл под именем russian12.txt  


### 2. Конвертирование форматов с помощью регулярных выражений   

[Скачайте файл](https://disk.yandex.ru/d/rpErxz5-hcoyzw) в формате tsv (tab separated values). Название нужного вам файла находится в [таблице с оценками](https://docs.google.com/spreadsheets/d/1_TkpAaQNKIiIAtKA3AgGxrB6BkqHgESa5gHfTFCZ9tE/edit?usp=sharing) на листе HW2.
В нём представлена разметка предложений из Исторического корпуса исландского языка следующей структуры:  
`Token`   `Lemma`   `Part-of-speech` 
```
eða	eða	CCONJ
lög	lög	NOUN
sín	sinn	PRON
setja	setja	VERB
menn	maður	NOUN
...
``` 

2.1 Уберите разметку  и представьте предложение (предложения) в виде одной строки. Все токены, включая знаки препинания, должны отделяться друг от друга пробелом, предложение заканчивается пробелом. 
  Пример:

``` 
eða lög sín setja menn á bækur hver þjóð á sína tungu . En af því að tungurnar eru ólíkar hver annarri . 
``` 

Во второй строке файла запишите регулярное выражение, которое вы использовали для поиска, в третьей строке - регулярное выражение, которое вы использовали для замены.  

По желанию (не оценивается), в четвертой строке вы можете записать автоматический перевод одного староисландского предложения на английский язык, сделанный с помощью google.translate или любого другого онлайн-переводчика.  

Сохраните файл под именем `icepahc21.txt`  

  
2.2 Откройте исходный файл tsv. Теперь сохраним лингвистическую разметку, но в другом формате, XML. Пример выше должен выглядеть вот так (каждое слово на своей строке):  
```
<word pos="CCONJ" lemma="eða" />eða</word>
<word pos="NOUN" lemma="lög" />lög</word>
<word pos="PRON" lemma="sinn" />sín</word>
<word pos="VERB" lemma="setja" />setja</word>
<word pos="NOUN" lemma="maður" />menn</word>
```

В конце файла допишите две строки с регулярными выражениями, которые вы использовали для поиска и для замены. 
(Если вам понадобилось более одной такой операции поиска и замены, допишите их все — но хорошо бы, чтобы вы сконвертировали формат с помощью одной операции поиска и замены).

Измените формат конца строки на формат Windows (CR+LF).  

Сохраните файл в формате Western Windows Latin (Windows-1252) под именем icepahc22.xml  

### 3. Задание повышенной трудности

Задание повышенной трудности предназначено для тех, кто хочет получить оценку 9 или 10 (вы получите ее при условии, что все предыдущие задания выполнены идеально). Ассистенты с этим заданием не помогают.

Напишите как можно более короткое регулярное выражение, которое найдёт все варианты написания имени философа Кьеркегора по-русски (Кьеркегор, Киркегор, Керкегор...). 
Для простоты давайте считать, что мы ищем это имя в начальной форме (именительный падеж единственного числа).  

Результат представьте в файле kierkegaard.txt  

Мы хотим увидеть там как само регулярное выражение, так и список всех вариантов, на которые вы ориентировались. Опишите, какими ресурсами вы пользовались для составления списка, если пользовались.    
