### Практикум AncConc и Voyant Tools

__AntConc__ -- корпусный менеджер

* [Страница программы](http://www.laurenceanthony.net/software/antconc/), где её можно скачать и посмотреть инструкции

#### Материал для работы на семинаре
Анна Каренина: [plain text](https://drive.google.com/file/d/0B6-5pzCmb8MOVFBjajZJUHhNNmM/view?usp=sharing), [xml](https://drive.google.com/file/d/0B6-5pzCmb8MOTktNVlpjaDdOY2M/view?usp=sharing)

Война и Мир, т. 1: [plain text](https://github.com/olesar/lingdata/blob/gh-pages/data/TolstoyVojnaIMir1.txt)

Тихий Дон: [plain text](https://github.com/olesar/lingdata/blob/gh-pages/data/tihiyd.txt) 

СинТагРус: [tokens](https://github.com/olesar/lingdata/blob/gh-pages/data/syntagrus_tokens.txt) [lemma_POS](https://github.com/olesar/lingdata/blob/gh-pages/data/syntagrus_lemmas.txt) 

LiveCorpus: 
[tokens](https://github.com/olesar/lingdata/blob/gh-pages/data/LiveCorpus2019.txt) [lemma_POS](https://github.com/olesar/lingdata/blob/gh-pages/data/LiveCorpus2019_lemmas.txt) 

#### Знакомство с основными функциями

* Загрузите файл, проверьте, что он отображается нормально (вкладка FileView). 
* Если нужно, настройте кодировку (меню Global Settings - Char Encoding). Чтобы слова с дефисами считались одним токеном, добавьте Connector и Dash в меню Global Settings - Token Definition.
* Постройте частотный список слов романа (вкладка Word List, нажмите кнопку Start). Кликнув на слово, вы сможете попасть в конкорданс, построенный для этого слова. 
* В Word List отсортируйте частотный список по алфавиту (Sort by Word внизу страницы). 
* Постройте частотный список двух-, трех- и т.д. -словных словосочетаний (вкладка Cluster/N-Grams, поставьте галочку на N-Grams, укажите, сколько слов в ngram-е вы хотите видеть, например, Min:3, Max:3, установите порог вхождений в корпусе, например, 10). Кликнув на n-грам, вы также можете попасть в его конкорданс. 
* Постройте списки коллокатов выбранного вами слова (вкладка Collocates), указав границы окна справа / слева. 

#### Работа с регулярными выражениями 

* Конкордансы и частотные списки можно строить с использованием Regex в Search Term. Например, `\w+ну` найдет любое слово, содержащее -_ну_, но не частицу _ну_. Вот так я предполагаю найти все глаголы на _-ну-_.

<img src="https://raw.githubusercontent.com/olesar/lingdata/gh-pages/fig/antconc_1.png" width = "800"></img>

#### Работа с размеченными файлами 

* Постройте частотный список, игнорируя теги xml (см. xml-файл с расширением xhtml. Чтобы его открыть, укажите Все типы файлов). В настройках Global Settings - Tag - Hide tags. 

#### Ключевые слова (лексические маркеры)

Чтобы определить характерные для некоторого корпуса слова, мы должны сравнить их частоты в данном корпусе с частотами в другом корпусе - reference corpus. 

* Загрузите SynTagRus в качестве reference corpus:  
Settings > Tool Preferences > Keyword List  
Use raw files -- Add files

<img src="https://raw.githubusercontent.com/olesar/lingdata/gh-pages/fig/antconc_3.png" width = "800"></img>

* Там же в настройках установите Log-Likelyhood (4-term) в качестве статистической метрики определения keyness и Длину списка в 1000 слов (Keyword Effect Size Threshold). 
 -- Apply 
 
* Перейдите на вкладку Keyword List 
 \> Start 
Для новых файлов AntConc начнет генерацию словника (выдаст предупреждение jump to Word List). 
В результате на вкладке Keyword List появится список ключевых слов, отсортированный по убыванию метрики Keyness (Log-Likelyhood). 

<img src="https://raw.githubusercontent.com/olesar/lingdata/gh-pages/fig/antconc_4.png" width = "800"></img>

* Чтобы найти интересующее слово в этом списке, введите его в поле Search Term и нажмите кнопку Search Only (не Start!). Кликнув на слово в списке, можно перейти к конкордансу. 


#### Частотные списки лемм и списки ключевых слов-леммы  

Чтобы построить частотный список лемм, ваш корпус должен быть лемматизирован (reference corpus, естественно, тоже). Мы будем использовать версии корпусов с подстановкой вместо токена метки леммы и части речи (в формате lemma_POS).


#### Самостоятельное исследование корпуса устной спонтанной речи. 

С помощью AntConc постройте частотные списки словоформ и лемм корпуса LiveCorpus. Определите лексические маркеры этого корпуса. (Для сравнения мы снова возьмем SynTagRus). 


#### Voyant Tools 

Еще одно полезное онлайн-приложение, которое активно используют литературоведы и историки - [Voyant Tools](https://voyant-tools.org).

* Изучите основные возможности инструмента на примере романов Дж. Остин
\> Open > Choose a corpus > Austen's Novels 

<img src="https://raw.githubusercontent.com/olesar/lingdata/gh-pages/fig/voyant-tools_1.png" width = "800"></img>

* Voyant Tools умеет строить облака слов (для всего корпуса и отдельных документов)   
* показывает распределение частоты слов в документах  
* показывает свойства документов, такие как длина в словах, среднее количество слов в предложении и т. д. [пример](https://voyant-tools.org/?corpus=austen)  
* вернувшись на исходную страницу, вы можете загрузить и исследовать свой пользовательский корпус  

<img src="https://raw.githubusercontent.com/olesar/lingdata/gh-pages/fig/voyant-tools_2.png" width = "800"></img>

#### Полезное  
* [Мануал](http://www.laurenceanthony.net/software/antconc/resources/help_AntConc321_english.pdf) (на английском)
* [Видео-тьюториал от автора](https://www.youtube.com/playlist?list=PLiRIDpYmiC0Ta0-Hdvc1D7hG6dmiS_TZj)
* [Тьюториал для семинара](https://drive.google.com/file/d/0B6-5pzCmb8MOblpzRXI3elFFeFU/view?usp=sharing)
* Зеркало AntConc (файлы для скачивания программы)  [downloads](https://github.com/olesar/lingdata/tree/gh-pages/data/antconc_downloads/)
* [Справка](https://voyant-tools.org/docs/#!/guide/start) по Voyant Tools 