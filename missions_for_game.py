from car_marks import *
missions_for_game = {
    'Возгорание урны': [M1],
    'Возгорание контейнера': [M1],
    'Горящий автомобиль': [M1],
    'Горящий мотоцикл': [M1],
    'Горящая трава': [M1],
    'Возгорание в квартире': [M2, M1],
    'Возгорание в сарае': [M1, M1],
    'Горящая листва': [M1],
    'Возгорание мусора': [M1],
    'Возгорание тюка соломы': [M1],
    'Возгорание трактора': [M1],
    'Горящая телефонная будка': [M1],
    'Дерево на дороге': [M1],
    'Горящий грузовик': [M1, M1],
    'Небольшое возгорание на поле': [M1, M1],
    'Небольшой лесной пожар': [M1],
    'Возгорание в автодоме': [M1, M1],
    'Возгорание почтового ящика': [M1],
    'Куча хвороста': [M1],
    'Горящий прицеп': [M1],
    'Возгорание в подвале': [M3, M1, M1, M4, M5],
    'Возгорание в камине': [M2, M4],
    'Пожар на крыше': [M2, M3, M1, M5, M4],
    'Возгорание ГСМ': [M1],
    'Горящая автобусная остановка': [M1],
    'ДТП': [M1],
    'Небольшое возгорание в супермаркете': [M1, M1, M1, M1, M5, M5, M4],
    'Возгорание в гараже': [M1, M1],
    'Горящий механизм': [M3, M1, M1, M4, M5, M5],
    'Разлив неизвестной цистерны': [M3, M3, M4, M4, M20, M20, M20, M6, M6, M1, M1],
    'Утечка газа': [M1],
    'Возгорание в очаге': [M2, M4],
    'Горящий комбайн': [M1, M1],
    'Возгорание в больнице': [M2, M2, M2, M3, M3, M3, M1, M1, M1, M1, M4, M4, M5, M5, M9, M9],
    'Алкогольное отравление': [],
    'Боли в груди': [],
    'Острый приступ астмы': [],
    'Cудороги': [],
    'Жар': [],
    'Упавший человек': [],
    'Возгорание в автомастерской': [M2, M2, M3, M1, M1, M1, M1, M1, M4, M4, M5, M5, M5, M5, M6, M20, M20, M10, M10, M10],
    'Магазинная кража': [M20],
    'ДТП с припаркованным автомобилем': [M20],
    'Кража металла со взломом': [M20],
    'Карманная кража': [M20],
    'Безбилетник': [M20],
    'Драка': [M20, M20, M20],
    'Нарушитель порядка': [M20, M20],
    'Возгорание на кухне': [M1, M1],
    'Спасение животного': [M3],
    'Возгорание в спортзале': [M2, M3, M1, M1, M1, M4, M5, M5, M9],
    'Жалоба на шум': [M20],
    'Микроинсульт': [],
    'ДТП с автобусом': [M3, M1],
    'Большое возгорание в супермаркете': [M2, M3, M1, M1, M1, M1, M4, M4, M5, M5, M5, M8, M9, M20],
    'Кровотечение из носа': [],
    'Крушение легкомоторного самолёта': [M3, M1, M1, M1, M4, M6, M5, M5, M5],
    'Крупное ДТП с автобусом': [M2, M3, M3, M1, M4, M20, M20],
    'Автокатастрофа': [M3, M1, M1, M1, M4, M20, M31, M31],
    'Грузовик с полуприцепом в огне': [M3, M1, M1, M5],
    'Инцидент с трактором': [M1, M1, M1, M4, M31],
    'Текущая крыша': [M2],
    'Возгорание большегрузного автомобиля': [M1, M1, M1, M4, M5, M5, M5, M20],
    'Возгорание мусоровоза': [M1, M1, M1, M4, M4, M5, M5, M5, M20],
    'Авария на мотоцикле': [M1, M1, M1, M4, M20],
    'Опрокидывание автомобиля': [M3, M1, M1, M4, M20, M20],
    'Вооруженное ограбление': [M20, M20, M20, M20, M20],
    'Отравление газом': [M3, M1, M7, M20],
    'Задыхаясь': [],
    'Пожар в кафетерии': [M3, M3, M3, M4],
    'Пожар в кафетерии (Система пожарной тревоги)': [M3, M3, M3, M4],
    'Застрявший альпинист': [M2, M3, M30, M31],
    'Угроза насилия': [M20, M20],
    'Возгорание силоса': [M2, M3, M1, M1, M1, M1, M1, M1, M4, M4, M9],
    'Человек на высоковольтном столбе': [M2, M3],
    'Травма позвоночника': [],
    'Частичное обрушение здания': [M2, M2, M2, M3, M3, M4, M20, M20],
    'Обрушение здания': [M2, M2, M3, M3, M3, M1, M1, M4, M4, M20],
    'Ожоги 3й степени': [],
    'Черепно-мозговая травма': [],
    'Травматическая ампутация конечности': [],
    'Большой пожар на ферме': [M2, M2, M2, M4, M4, M3, M1, M1, M1, M1, M1, M5, M5, M5, M5],
    'Боли в спине': [],
    'Возгорание соломенного тюка': [M3, M3, M3, M3, M3, M4, M5],
    'Полицейский обыск жилого района': [M20, M20, M20, M20],
    'Побег заключенного': [M20, M20, M20, M20, M20, M20, M20, M20, M20, M21, M23],
    'Подозреваемый убегает': [M20, M20, M20, M20, M20, M23],
    'Пропажа человека': [M20, M20, M20, M20, M20, M1, M1, M4, M23],
    'Похищение ребёнка': [M20, M20, M20, M21, M23],
    'Полицейский ранен': [M20, M20, M20, M20, M20, M20],
    'Розыск автомобиля': [M20, M21],
    'Компания хулиганов': [M20, M20, M20, M21],
    'Групповая драка': [M20, M20, M20, M20, M20, M20, M21, M23],
    'Продажа наркотиков': [M20, M20, M20, M21],
    'Ограбление АЗС': [M20, M20, M20, M20, M22, M22, M23],
    'Вооруженное нападение': [M20, M20, M20, M20, M20, M20, M21, M21, M22, M23],
    'Незаконное вторжение': [M20, M20, M20, M21, M22, M23],
    'Попытка убийства': [M20, M20, M20, M20, M20, M20, M21, M22, M30, M31],
    'Ограбление музея': [M20, M20, M20, M21, M22],
    'Сход с рельсов товарного поезда': [M2, M2, M2, M2, M3, M3, M3, M3, M1, M1, M4, M4, M6, M6,
                                        M7, M7, M8, M20, M20],
    'Спасение человека из траншеи': [M3, M3, M1, M4, M20],
    'Анафилактический шок': [],
    'Травмированный бегун': [],
    'Пропавший ребёнок': [M20, M20, M20],
    'Пожар на свалке': [M2, M3, M3, M3, M1, M4, M5, M5],
    'Незаконное владение оружием': [M20, M20, M20, M20],
    'ДТП с участием животного': [M20],
    'Поломка водопровода': [M3, M1, M4],
    'Перелом руки': [],
    'Перелом ноги': [],
    'Обезвоживание': [],
    'Пищевое отравление': [],
    'Солнечный удар': [],
    'Тепловой удар': [],
    'Тепловые судороги': [],
    'Обезвоживание организма': [],
    'Возгорание гриля': [M1],
    'Малый пожар в гостинице': [M3, M3, M3, M3],
    'средний  пожар в гостинице': [M2, M3, M3, M3, M3, M3, M4],
    'Крупный пожар в гостинице': [M2, M3, M3, M3, M3, M3, M3, M3, M4, M4, M5, M7, M20, M20, M20],
    'Огромный пожар в гостинице': [M2, M2, M3, M3, M3, M3, M3, M3, M3, M3, M3, M3, M3, M3, M4, M4,
                                   M4, M4, M5, M7, M8, M20, M20, M20, M20, M20, M20],
    'Аллергическая реакция': [],
    'Человек на путях': [M20, M20, M20],
    'Сбитый на путях человек': [M3, M1, M4, M4, M20, M20],
    'Автомобиль в тоннеле': [M3, M1, M1, M4, M5],
    'Ордер на обыск': [M20, M22],
    'Пожар на электростанции': [M2, M2, M2, M3, M3, M3, M3, M3, M4, M4, M4, M4, M5, M5, M5, M7, M7, M8, M6,
                                M20, M20, M20, M20],
    'Массовая паника на дискотеке': [M20, M20, M20, M20, M20, M20, M20, M20, M20],
    'Пожар в офисном здании': [M3, M3, M3, M3, M3, M3, M2, M2, M2, M2, M4, M4, M5, M5, M5, M5,
                               M5, M7, M9, M9, M20, M20, M20],
    'Пожар на предприятии по переработке отходов': [M2, M2, M3, M3, M3, M3, M3, M3, M3, M3, M3,
                                                    M3, M5, M5, M5, M4, M4, M7, M8, M20, M20, M9,
                                                    M9, M9, M10],
    'Происшествие с химическими ожогами': [],
    'Небольшой пожар на фабрике': [M3, M3, M3, M3, M4, M4, M8, M9],
    'Крупный пожар на фабрике': [M2, M2, M3, M3, M3, M3, M3, M3, M4, M4, M4, M4, M5, M5, M8, M7,
                                 M20, M20, M9, M9, M10, M10],
    'Провоз контрабанды': [M20, M20, M21],
    'Пожар в люке': [M1, M1, M4],
    'Человек под поваленным деревом': [M1, M30, M31],
    'Пожар в музее': [M2, M2, M3, M3, M3, M3, M4, M4, M5, M5, M7, M7, M8, M20, M20],
    'Инцидент с бензопилой': [],
    'Пожар товарного вагона': [M3, M3, M3, M3, M3, M4],
    'Пожар в столярной мастерской': [M2, M2, M3, M3, M3, M3, M3, M3, M3, M3, M4, M4, M4, M4, M5,
                                     M7, M8, M9, M9, M20, M20],
    'Пожар в ресторане': [M2, M3, M3, M3, M4, M5, M5, M7, M20, M20],
    'Подозрительная личность': [M20],
    'Поражение электротоком': [],
    'Пожар в автобусе': [M3, M3, M3, M4],
    'Оползень': [M3, M3, M1, M1, M4],
    'Мотоавария на горной трассе': [],
    'Пожар в высотном здании': [M2, M4, M4, M4, M4, M3, M3, M3, M3, M3, M3, M3, M3, M3],
    'Перевернувшийся грузовой автомобиль': [M2, M4],
    'Незаконная деятельность в интернете': [M20],
    'Кот застрял на дереве': [M1],
    'Подозрительная посылка': [M20, M21],
    'Ограбление ювелирного магазина': [M20, M20],
    'Травмированный паркурщик': [M3],
    'Осколок стекла в руке': [],
    'Пожар на пирсе': [M2, M3, M3, M3, M3, M4],
    'Паническая атака': [],
    'Пожар на ж/д станции (крупный)': [M2, M2, M3, M3, M3, M3, M3, M3, M3, M3, M4, M4, M4, M5, M5,
                                       M6, M7, M8, M9, M9, M9, M10,M20, M20, M20, M20, M20, M20,
                                       M20, M20],
    'Авария с участием строительной техники': [M3, M3, M1, M4],
    'Обломки на взлетно-посадочной полосе': [M1],
    'Рейд против поставщиков поддельных товаров': [M20, M20, M20, M20],
    'Удушье предметом, застрявшим в горле': [],
    'Человек застрявший на оборудовании детской площадки': [M1],
    'Остановка дыхания': [],
    'Сильная травма головы': [],
    'Парашютист на дереве': [M2, M3, M3, M4],
    'Приступ': [],
    'Роды': [],
    'Нарушение дыхания': [],
    'Авария на мотокроссе': [],
    'Пожар в школе (малый)': [M3, M3, M3, M3, M4],
    'Пожар в школе (большой)': [M2, M3, M3, M3, M3, M3, M4],
    'Пожар в закрытом помещении': [M3, M3, M3, M3, M4, M4, M9, M9],
    'Атака огнестрельным оружием': [M20, M20, M20, M20, M20, M20, M20, M20],
    'Пожар в доме': [M2, M1, M1, M1, M4, M5, M5],
    'Авария на атомной электростанции (крупная авария)': [M2, M2, M8, M7, M7, M6, M6, M6, M6, M5,
                                                          M5, M4, M4, M4, M4, M4, M4, M4, M4,
                                                          M20, M20, M20, M20, M20, M20, M20, M20,
                                                          M3, M3, M3, M3, M3, M3, M3, M3, M3, M3,
                                                          M3, M3, M3, M3, M3, M3, M3, M3, M3, M3,
                                                          M3, M3, M3],
    'Крушение пассажирского поезда': [M3, M3, M3, M3, M1, M1, M1, M1, M1, M1, M1, M4, M4, M4, M8, M20, M20, M20],
    'Человек под поездом': [M3, M3, M1, M1, M4, M4, M4, M4, M20, M20, M20, M20, M20],
    'Массовое поражение в общественном месте': [M3, M1, M1, M1, M4, M4, M4, M4, M4, M4, M6, M6,
                                                M20, M20, M20, M20, M20, M20, M20, M20, M20, M20],
    'Загрязненная тележка с мороженным': [M20],
    'Незаконное разведение костра в парке': [M1, M20],
    'Падение с обрыва': [M3, M3, M3, M3, M4, M4, M20, M20, M1, M1, M1, M1, M1],
    'Гипогликемия': [],
    'Бегство с места аварии': [M3, M3, M20, M20, M20, M20],
    'Возгорание на дискотеке': [M2, M2, M3, M3, M3, M3, M3, M4, M5, M6, M7, M8, M20, M20, M20],
    'Падение с небольшой металлической конструкции': [M2, M3, M4, M20, M20],
    'Падение с большой металлической конструкции': [M2, M2, M3, M3, M3, M4, M20, M20, M20],
    'Серьезное ранение стеклом': [M1],
    'Очистка загрязненной почвы': [M1, M6,],
    'Взрыв банкомата': [M1, M1, M20, M20, M20, M20, M20],
    'Расчистка пути': [M3, M20],
    'В лифте застрял человек, которому нездоровится': [M1, M30, M31],
    'Авария на лесопилке': [M3, M20],
    'Упавший вертолёт': [M3, M3, M1, M1, M4, M6, M20, M20, M20, M20],
    'Беспорядки на концерте': [M20, M20, M20],
    'Возгорание на поезде (грузовой поезд)': [M3, M3, M3, M3, M4, M4, M4, M5, M7, M8, M9],
    'Большое ДТП в тоннеле': [M3, M3, M3, M3, M3, M3, M4, M4, M5, M6, M7, M8, M9, M9, M20, M20, M20],
    'Возгорание в ресторане быстрого питания': [M2, M3, M3, M3, M3, M4, M7, M9, M10, M5],
    'Возгорание на промышленном предприятии (небольшое)': [M2, M3, M3, M3, M4, M5, M6, M9, M10],
    'Возгорание на промышленном предприятии (среднее)': [M2, M2, M3, M3, M3, M4, M4, M5, M6, M8, M9,
                                                         M9, M9, M10],
    'Возгорание на промышленном предприятии (большое)': [M2, M2, M3, M3, M3, M3, M3, M3, M4, M4, M4, M4, M5,
                                                         M6, M8, M9, M9, M9, M10, M10, M10],
    'Возгорание в спальне': [M1, M1, M4, M7],
    'Возгорание на нефтеперерабатывающем заводе': [M3, M3, M3, M3, M3, M3, M4, M4, M6, M6, M9, M10, M10],
    'Передозировка': [],
    'Возгорание на складе шин': [M2, M2, M3, M1, M1, M1, M1, M1, M4, M4, M5, M5, M6, M8, M20, M20, M20],
    'Ограбление офиса': [M20, M20],
    'Угон автомобиля': [M20, M20, M20],
    'Пожар в небоскребе': [M2, M2, M3, M3, M3, M3, M1, M1, M4, M4, M5, M7, M8, M20, M20, M20],
    'Ограбление банка': [M20, M20, M20, M20, M21, M22],
    'Паника в клубе': [M20, M20, M20, M20, M20, M20],
    'Перевернутый автовоз': [M3, M4, M20, M20],
    'Подозрение на аппендицит': [],
    'Горящая трансформаторная станция': [M1, M1, M4, M20],
    'Сбитый велосипедист': [M20, M20, M20, M20, M20],
    'Пожар на стадионе (Слабый)': [M1, M1, M1, M1, M1, M1, M4, M5, M5, M20, M20, M20],
    'Пожар на стадионе (Средний)': [M1, M1, M1, M1, M1, M1, M1, M1, M4, M4, M4, M5, M5,  M5, M20, M20,
                                    M20],
    'Контрабанда экзотических животных': [M20, M20, M20, M20, M20],
    'Пожар на стадионе (Сильный)': [M2, M2, M3, M3, M3, M1, M1, M1, M1, M1, M4, M4, M4, M5, M5, M5, M6,
                                    M7, M8, M10, M20, M20, M20, M20, M20],
    'Пожар на стадионе (Крупный)': [M2, M2, M2, M3, M3, M3, M3, M1, M1, M1, M1, M1, M1, M1, M1, M4, M4,
                                    M4, M5, M5, M5, M5, M5, M6, M6, M6, M7, M8, M10, M20, M20, M20, M20, M20],
    'Незаконная уличная торговля': [M20, M20, M20, M20, M20],
    'Угон при водителе': [M20, M20, M20, M20, M20],
    'Травма грудной клетки': [],
    'Крупная утечка топлива из машины': [M1, M1, M20, M20],
    'Крупная утечка топлива из машины (скоростная дорога)': [M1, M1, M20, M20],
    'Столкновение мотоциклов': [M3, M3, M20, M20, M20],
    'Ожесточенная ссора': [M20, M20],
    'Горящая мебель': [M3],
    'Возможная инфекция': [],
    'Вандализм': [M20, M20],
    'Пожар в жилом доме': [M2, M2, M2, M1, M1, M1, M4, M7, M20, M20, M20, M20],
    'Авария с несколькими автомобилями': [M3, M3, M3, M3, M1, M1, M1, M4, M20, M20, M20, M20, M20],
    'Незаконная уличная гонка': [M20, M20, M20, M20, M20, M20],
    'Автомобиль в канаве': [M3, M3, M1, M1, M1, M1, M1, M4, M4, M20, M20],
    'Пожар в столовой': [M1, M1, M1, M4, M20],
    'Обыск дома': [M20, M20, M20, M20],
    'Происшествие в шахте': [M1, M1, M1, M1, M1, M1, M1, M1, M4, M4, M6, M20, M20],
    'Обрушение шахты': [M3, M3, M3, M3, M1, M1, M1, M1, M1, M1, M4, M4, M4, M4, M6, M6, M20, M20, M20],
    'Падение осветительного столба': [M3, M1, M4,],
    'Нападение на ювелирный магазин': [M20, M20],
    'Животное в ловушке в колодце': [M1],
    'Животное в ловушке в реке': [M1],
    'Гнездо шершней в жилом доме': [M1],
    'Взрыв в ресторане': [M2, M2, M3, M3, M3, M4, M5, M20, M20, M6],
    'Поврежденное имущество': [M20],
    'Человек, лежащий на земле': [],
    'Кража произведений искусства': [M20, M20],
    'Пожар в церкви': [M2, M2, M3, M3, M1, M1, M1, M1, M1, M1, M4, M4, M4, M5, M5, M7, M8, M20, M20, M20, M20],
    'Несчастный случай с биологическими продуктами': [M1, M1, M1, M1, M1, M1, M1, M1, M4, M4, M5, M5, M6, M6,
                                                      M20, M20, M31, M31, M31, M31, M31],
    'Пожар в пустующем здании': [M1, M1, M4, M5, M20],
    'Незаконное хранение оружия - hож': [M20, M20],
    'Видимый дым': [M1, M1, M4],
    'задымление в жилом здании': [M2, M1, M1, M4],
    'Курение в доме на одну семью': [M1, M1, M1, M1, M4],
    'Гипертонический криз': [],
    'Разлив топлива на автозаправочной станции': [M3, M3, M1, M1, M4, M4, M6, M20, M20, M20],
    'Пожар в аптеке': [M1, M1,  M1, M1, M1, M4, M10, M20, M20],
    'Агрессивный пассажир поезда': [M20, M20, M20, M20],
    'Кража лекарств': [M20, M20, M20, M20, M20],
    'Пожар в поезде с горючими продуктами': [M3, M3, M3, M3, M3, M4, M4, M6, M8, M9, M9, M20, M20, M20],
    'Очистка дорожек': [M3, M20],
    'Синкопа восстановлена': [],
    'Взрыв газового баллона': [M2, M2, M1, M1, M1, M4, M5, M5, M6, M6, M10, M20, M20, M20],
    'Пожар на коммутаторе': [M1],
    'Незаконное хранение огнестрельного оружия': [M20, M20, M20, M20, M22],
    'Авария с вилочным погрузчиком': [M3, M20, M20],
    'Нападение на остановке': [M20, M20, M20, M22],
    'Попытка поджога': [M1, M1, M4, M5, M20, M20, M20],
    'Пожар на бумажной фабрике': [M1, M1, M1, M1],
    'Огонь в яме для барбекю': [M1, M1, M1, M1, M1, M1, M4, M4, M20, M20, M20, M20],
    'Нападение в торговом центре': [M20, M20, M20, M21, M21],
    'Спонтанный пневмоторакс': [],
    'Мониторинг светофоров': [M20],
    'Мирная демонстрация (малая)': [M20, M20, M20, M20, M21],
    'Мирная демонстрация (большая)': [M20, M20, M20, M20, M20, M20, M20, M20, M20, M20, M20, M20, M20, M20,
                                      M21],
    'Гиповолемический шок': [],
    'обыск транспортного средства': [M20, M20],
    'Авария, повлекшая за собой глубокий порез': [M3],
    'Принудительная госпитализация': [M20, M20, M31],
    'Пожар на строительной площадке': [M1, M1, M1, M1, M1, M1, M1, M1, M1, M1, M1, M1, M4, M4, M4, M5, M5, M5,
                                       M5, M6, M6, M8, M10, M10, M20, M20, M20, M20, M20, M20],
    'Кровотечение из пищеварительного тракта': [],
    'Автомобиль врезается в плотину': [M1, M1, M1, M1, M1, M4, M4, M20, M20, M20, M20],
    'Нападение в супермаркете': [M20, M20, M20, M20],
    'Арест поддельных спасателей': [M20],
    'Пожар в библиотеке (небольшой': [M1, M1, M4, M20],
    'Пожар в библиотеке (средний)': [M2, M1, M1, M4, M4, M20, M5, M20],
    'Пожар в библиотеке (большой)': [M2, M2, M1, M1, M1, M1, M4, M4, M4, M4, M5, M7, M8, M10, M20,
                                     M20, M20, M20],
    'Пожар в библиотеке (майор)': [M2, M2, M2, M2, M3, M1, M1, M1, M1, M1, M4, M4, M4, M4, M4, M5,
                                   M5, M7, M8, M8, M10, M10, M20, M20, M20, M20, M20, M20],
    'Взрыв силосной башни': [M2, M2, M3, M3, M3, M3, M3, M3, M3, M4, M4, M4, M4, M4, M5, M5, M5,
                             M5, M5, M5, M5, M5, M5, M5, M5, M5, M6, M8, M10, M20, M20, M20, M20,
                             M20, M21, M21, M23],
    'Пожар в автобусном парке': [M2, M2, M1, M1, M1, M4, M4, M4, M5, M6, M8, M10, M10, M20, M20,
                                 M20, M31],
    'Подводный автобус': [M1, M4, M4, M4, M6, M8, M20, M20, M20, M20],
    'Отравление при вдыхании дыма': [M1, M1, M4, M20, M20],
    'Мотоцикл сбивает пешехода': [M3, M4, M20, M31],
    'Демонстрация против проекта строительства автомагистрали': [M20, M20, M20, M20],
    'Пожар в кемпинговом автомобиле': [M1, M1, M1, M4, M20, M10],
    'горит здание фермы': [M2, M1, M1, M1, M1, M4, M20, M20, M5],
    'Пожар в здании для хранения твердых удобрений': [M2, M2, M2, M3, M1, M1, M1, M1, M4, M4, M4,
                                                      M4, M4, M4, M5, M6, M6, M6, M6, M6, M7, M8,
                                                      M9, M9, M9, M10, M10, M20, M20, M20, M20, M20, M20, M30],
    'возгорание электромобиля': [M3, M1, M4, M20, M20],
    'Срабатывание пожарной сигнализации в аквариуме': [M1, M1, M4, M20, M20],
    'Пожар в аквариуме': [M2, M2, M3, M3, M3, M3, M3, M3, M4, M4, M4, M4, M5, M5, M5, M5, M5, M5,
                          M5, M7, M8, M9, M9, M10, M20, M20, M20, M20, M20, M20, M20, M20,],
    'взрыв в аквариумном парке': [M2, M2, M1, M1, M1, M1, M1, M1, M1, M1, M5, M5, M7, M7, M8, M8,
                                  M9, M9, M10, M10, M20, M20, M20, M20, M20, M20, M20, M20, M21,
                                  M21],
    'Огонь в камере': [M2, M3, M3, M3, M4, M4, M7, M20, M20, ],
    'Пожар в тюрьме': [M2, M2, M3, M3, M3, M3, M3, M3, M4, M4, M4, M4, M5, M5, M5, M5, M7, M7,
                       M8, M8, M9, M9, M20, M20, M20, M20, M20],
    'Пожар во флигеле': [M1, M1, M1, M1, M4, M5, M5, M10, M20, M20, M30, M31],
    'Пожар на станции метро': [M1, M1, M1, M1, M1, M1, M1, M1, M1, M1, M4, M4, M4, M6, M6, M7, M8, M10,
                               M10, M20, M20, M20, M20, M20],
    'Небольшой пожар в национальном архиве': [M1, M1, M10]
}
