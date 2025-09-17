### Конкордансеры. Практикум AntConc

__AntConc__ -- корпусный менеджер

* [Страница программы](http://www.laurenceanthony.net/software/antconc/), где её можно скачать и посмотреть инструкции

#### Знакомство с основными функциями

* Загрузите файл, проверьте, что он отображается нормально (вкладка FileView).  
* Если нужно, настройте кодировку (меню Global Settings - Char Encoding).  
* Чтобы слова с дефисами считались одним токеном, добавьте Connector и Dash в меню Global Settings - Token Definition.  
* Постройте частотный список слов романа (вкладка **Word List**, нажмите кнопку Start). Кликнув на слово, вы сможете попасть в конкорданс, построенный для этого слова.  
* В Word List отсортируйте частотный список по алфавиту (Sort by Word внизу страницы).  
* Постройте частотный список двух-, трех- и т.д. -словных словосочетаний (вкладка **Cluster/N-Grams**, поставьте галочку на N-Grams, укажите, сколько слов в ngram-е вы хотите видеть, например, Min:3, Max:3, установите порог вхождений в корпусе, например, 10). Кликнув на n-грам, вы также можете попасть в его конкорданс.  
* Постройте списки коллокатов выбранного вами слова (вкладка **Collocates**), указав границы окна справа / слева.  

#### Работа с размеченными файлами 

* Постройте частотный список, игнорируя теги xml (см. xml-файл с расширением xhtml. Чтобы его открыть, укажите Все типы файлов). В настройках Global Settings - Tag - Hide tags. 

#### Ключевые слова (лексические маркеры - токены)

Чтобы определить характерные для некоторого корпуса слова, мы должны сравнить их частоты в данном корпусе с частотами в другом корпусе - reference corpus. 

* Загрузите SynTagRus в качестве reference corpus:  
Settings > Tool Preferences > Keyword List  
Use raw files -- Add files

<img src="https://raw.githubusercontent.com/olesar/lingdata/gh-pages/fig/antconc_3.png" width = "800"/>

* Там же в настройках установите Log-Likelyhood (4-term) в качестве статистической метрики определения keyness и Длину списка в 1000 слов (Keyword Effect Size Threshold). 
 -- Apply 
 
* Перейдите на вкладку Keyword List 
 \> Start 
Для новых файлов AntConc начнет генерацию словника (выдаст предупреждение jump to Word List). 
В результате на вкладке Keyword List появится список ключевых слов, отсортированный по убыванию метрики Keyness (Log-Likelyhood). 

<img src="https://raw.githubusercontent.com/olesar/lingdata/gh-pages/fig/antconc_4.png" width = "800"/>

* Чтобы найти интересующее слово в этом списке, введите его в поле Search Term и нажмите кнопку Search Only (не Start!). Кликнув на слово в списке, можно перейти к конкордансу. 


#### Частотные списки лемм и списки ключевых слов (леммы)  

Чтобы построить частотный список лемм, ваш корпус должен быть лемматизирован (reference corpus, естественно, тоже). Мы будем использовать версии корпусов с подстановкой вместо токена метки леммы и части речи (в формате lemma_POS).


#### Коллокаты

Во вкладке Collocates укажите слово, сочетаемость которого вы хотите изучить. Справа укажите контекстное окно поиска коллокатов (например, 0 слов слева, 2 слова справа - 2R) и частотный порог (Min. Collocate Frequency). Start!  
Списки коллокатов можно сортировать по абсолютной частоте, метрике коллокационной связи (Stat) и алфавиту.  
В `Settings > Tool Preferences > Collocates` можно выбрать метрики MI, Log-Likelihood, T-Score.   
* T-Score - самая консервативная метрика, при ранжировании по ней уменьшается частотный ранг самых частотных слов корпуса и несколько увеличивается частотный ранг редких слов, но в целом ранги по абсолютной частоте и по T-Score похожи.  
* MI (Mutual Information) - напротив, поднимает очень высоко в рейтинге слова, которые редко встречаются в корпусе в целом. Поэтому рекомендуют использовать эту метрику вместе с порогом отсечения очень редких слов.  
* Log-Likelihood (LL-score, G2) - ближе к T-Score и больше понижает в рейтиге высокочастотные слова. Превосходит T-Score по соотношению точность/полнота, как показывает ряд исследований для английского языка.    
В целом, идеальной метрики для поиска коллокатов не существует. Для разных языков, корпусов разного размера и жанра, типа коллокаций та или иная метрика может быть лучше или хуже.  

<img src="https://raw.githubusercontent.com/olesar/lingdata/gh-pages/fig/antconc_1.png" width = "800"/>

#### Поиск с использованием регулярных выражений  

* Конкордансы и частотные списки можно строить с использованием Regex в Search Term. Например, `\w+ну` найдет любое слово, содержащее -_ну_, но не частицу _ну_. Вот так я предполагаю найти все глаголы на _-ну-_.

<img src="https://raw.githubusercontent.com/olesar/lingdata/gh-pages/fig/antconc_6.png" width = "800"/>

`э+ ` (второй символ - плюсик, третий - пробел) позволит найти _э_, _ээ_, _эээ_ (AntConc по умолчанию считает пробел маркером конца слова).  


#### Материал для работы на семинаре
[зеркало со всеми материалами](https://disk.yandex.ru/d/QoZPtWuZ_raV1Q)  

Анна Каренина: [plain text](https://drive.google.com/file/d/0B6-5pzCmb8MOVFBjajZJUHhNNmM/view?usp=sharing), [xml](https://drive.google.com/file/d/0B6-5pzCmb8MOTktNVlpjaDdOY2M/view?usp=sharing), [lemma_POS](https://disk.yandex.ru/d/kQ1dA7miJva6qw)  

Война и Мир, т. 1: [plain text](https://github.com/olesar/lingdata/blob/gh-pages/data/TolstoyVojnaIMir1.txt)

Тихий Дон: [plain text](https://github.com/olesar/lingdata/blob/gh-pages/data/tihiyd.txt) 

СинТагРус: [tokens](https://github.com/olesar/lingdata/blob/gh-pages/data/syntagrus_tokens.txt) [lemma_POS](https://github.com/olesar/lingdata/blob/gh-pages/data/syntagrus_lemmas.txt) 

LiveCorpus: 
[tokens](https://github.com/olesar/lingdata/blob/gh-pages/data/LiveCorpus2019.txt) [lemma_POS](https://github.com/olesar/lingdata/blob/gh-pages/data/LiveCorpus2019_lemmas.txt)  

LiveCorpus 2021:  
tokens: см. файлы livecorpus2021-text-1.txt ... livecorpus2021-text-10.txt в архиве по ссылке выше. lemma_POS: см. livecorpus2021_lemma_pos.1.txt там же.    


#### Полезное  
* [Руководство по AntConc](http://www.laurenceanthony.net/software/antconc/resources/help_AntConc321_english.pdf) (на английском)  
* [Видео-тьюториал от автора](https://www.youtube.com/playlist?list=PLiRIDpYmiC0Ta0-Hdvc1D7hG6dmiS_TZj)  
<!--- * [Тьюториал для семинара](https://drive.google.com/file/d/0B6-5pzCmb8MOblpzRXI3elFFeFU/view?usp=sharing)--->
* [Формулы и оценка коллокационных мер](https://elex.link/elex2017/wp-content/uploads/2017/09/paper32.pdf)  


#### Дополнительные материалы  

#### Voyant Tools 

Еще одно полезное онлайн-приложение, которое используется гуманитариями - [Voyant Tools](https://voyant-tools.org).

* Изучить основные возможности инструмента можно на примере романов Дж. Остин
\> Open > Choose a corpus > Austen's Novels 

<img src="https://raw.githubusercontent.com/olesar/lingdata/gh-pages/fig/voyant-tools_1.png" width = "800"/>

* Voyant Tools умеет строить облака слов (для всего корпуса и отдельных документов)   
* показывает распределение частоты слов в документах  
* показывает свойства документов, такие как длина в словах, среднее количество слов в предложении и т. д. [пример](https://voyant-tools.org/?corpus=austen)  
* вернувшись на исходную страницу, вы можете загрузить и исследовать свой пользовательский корпус  

<img src="https://raw.githubusercontent.com/olesar/lingdata/gh-pages/fig/voyant-tools_2.png" width = "800"/>

* [Справка](https://voyant-tools.org/docs/#!/guide/start) по Voyant Tools 
