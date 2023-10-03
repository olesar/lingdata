### ELAN - разметка просодии и жестов     

#### 1. Типы и слои  
Создайте слои (и типы слоев, если нужно) для каждого говорящего, вида (для условного спикера @aaa1989f, а вы подставьте своего):       
* `eduType@aaa1989f` (Тип слоев со стереотипом `Symbolic Association`, родительский слой text@...)  
* `gesture@aaa1989f` - для разметки плана выражения жеста (Тип слоев `gesture`, слой не имеет родителя)
* `gestMeaning@aaa1989f` - для разметки значения жеста (Тип слоев `gesture_meaning`, родительский слой - gesture@...).
* `gestActiveOrgan@aaa1989f` - для разметки активного органа жеста (Тип слоев `gesture_organs`, родительский слой - gesture@...).

#### 2. Классы реплик

Упрощенная разметка просодии предполагает определить интонационный паттерн (по движению тона), указать паузы и слова, на которые приходится эмфатическое выделение, если оно есть.  

Мы будем использовать упрощенную классификацию типов интонации:

* `вопрос да-нет`  
* `вопрос частный`  
* `повествование`
* `побуждение`  
* `незавершённость`
* `другое`

Отредактируйте список значений `utterance types` для типа `utterance_types` (в разделе Правка).

Примеры использования похожих меток вы можете посмотреть на сайте проекта [PRuD](https://lingconlab.github.io/PRuD/data.html).

#### 3. Разметка жестов  

В слое `gesture@...` мы будем характеризовать жестовые реплики по внешнему виду: активный орган, конфигурация, ориентация (например, левая ладонь обращена вверх или к говорящему), характер движения, а также наличие препятствий/[спойлеров](https://ruscorpora.ru/new/search-murco.html) или участие предметов/[аксессуаров](https://processing.ruscorpora.ru/search.xml?env=alpha&env=alpha&api=1.0&mycorp=&mysent=&mysize=&mysentsize=&dpp=&spp=&spd=&mydocsize=&mode=murco&lang=ru&sort=i_grtagging&nodia=1&text=lexgramm&ext=10&nolinks=1&ell=1&parent1=0&level1=0&lex1=&gramm1=&sem1=&flags1=&orphoGr1=&orpho1=&strAccent1=&accent1=&before1=&after1=&number1=&parent2=0&level2=0&min2=1&max2=1&lex2=&gramm2=&sem2=&flags2=&orphoGr2=&orpho2=&strAccent2=&accent2=&before2=&after2=&number2=&doc_act_speakersamount=&doc_act_sex=&doc_act_lang=&doc_act_situation=&doc_act_acttypes=&doc_act_appeals=&doc_act_questions=&doc_act_imperatives=&doc_act_modals=&doc_act_negation=&doc_act_pejoratives=&doc_act_praise=&doc_act_consent=&doc_act_trade=&doc_act_assertion=&doc_act_othersspeech=&doc_act_mocking=&doc_act_etiquette=&doc_act_completeness=&doc_act_repetitions=&doc_act_manner=&doc_act_vocals=&doc_gesture_actorname=&doc_gesture_actorsex=&doc_gesture_sex=&doc_gesture_actorage=&doc_gesture_age=&doc_gesture_mainorgan=&doc_gesture_palmorientation=&doc_gesture_handorientation=&doc_gesture_activeorgan=&doc_gesture_passiveorgan=&doc_gesture_adaptor=&doc_gesture_direction=&doc_gesture_mult=&doc_gesture_gesturename=&doc_gesture_gesturetype=&doc_gesture_gesturemeaning=&doc_gesture_extenders=&doc_gesture_spoilers=&doc_gesture_emotions=&doc_gesture_completeness=&doc_gesture_authenticity=&doc_gesture_accessories=%D0%BF%D0%BE%D1%81%D1%83%D0%B4%D0%B0). Характеристики даются в свободной форме: описательно или с использованием известных названий для жестов. Вам может помочь [терминологический справочник](https://ruscorpora.ru/page/corpus-multimedia-index/).

Граница жестовой реплики включает в себя экскурсию (выход на жест), активную фазу и удержание/рекурсию. Если жесты переходят один в другой, то граница между ними ставится в начале перехода к следующему жесту.  

В слое `gestMeaning@...` указывается тип, а затем значение жеста как в [МУРКО](https://ruscorpora.ru/new/attrs-murco-gestures-mixed.html)

В слое `gestActiveOrgan@...` указывается активный орган жеста в упрощённой системе разметки (более подробную можно посмотреть в [МУРКО](https://ruscorpora.ru/new/attrs-murco-gestures-mixed.html))
```
Пример:
`gesture@...` правая ладонь, расслабленная, вращает от себя, вверх под углом 
`gestMeaning@...` поисковый жест: поиск слова
`gestActiveOrgan@...` hand
```

Если у говорящего один жест накладывается на другой, сделайте два спана подряд (граница будет условной).
