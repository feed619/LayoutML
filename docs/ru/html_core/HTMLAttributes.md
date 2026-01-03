# HTMLAttributes

`HTMLAttributes` - содержит определения констант для всех HTML атрибутов, сгруппированных по типам значений. Это служебный модуль для использования в классе HTMLElement и его наследниках.

---

## Структура файла

### Класс ValueAttributes

Атрибуты, требующие явного указания значения через знак равенства (attribute="value").

ValueAttributes - Атрибуты со значениями

| Атрибут        | Описание                          | Пример                                                     |
| -------------- | --------------------------------- | ---------------------------------------------------------- |
| id\_           | Уникальный идентификатор элемента | HTMLElement(id\_="main-header")                            |
| name           | Имя элемента для форм и скриптов  | HTMLElement(name="username")                               |
| title          | Всплывающая подсказка             | HTMLElement(title="Нажмите для подробностей")              |
| lang           | Язык содержимого элемента         | HTMLElement(lang="ru")                                     |
| dir            | Направление текста                | HTMLElement(dir="ltr")                                     |
| translate      | Разрешить перевод                 | HTMLElement(translate="no")                                |
| class\_        | строк CSS классы                  | HTMLElement(class\_="btn btn-primary")                     |
| style          | Встроенные стили                  | HTMLElement(style="color: red; font-size: 14px;")          |
| href           | Гиперссылка                       | HTMLElement(href="/page.html")                             |
| src            | Источник медиа                    | HTMLElement(src="image.jpg")                               |
| srcset         | Набор адаптивных изображений      | HTMLElement(srcset="img-320w.jpg 320w, img-640w.jpg 640w") |
| sizes          | Размеры для srcset                | HTMLElement(sizes="(max-width: 600px) 100vw, 50vw")        |
| poster         | Постер для видео                  | HTMLElement(poster="video-preview.jpg")                    |
| action         | URL обработки формы               | HTMLElement(action="/submit")                              |
| formaction     | Альтернативный URL отправки       | HTMLElement(formaction="/save-draft")                      |
| width          | Ширина элемента                   | HTMLElement(width="300")                                   |
| height         | Высота элемента                   | HTMLElement(height="200")                                  |
| size           | Размер поля ввода                 | HTMLElement(size="20")                                     |
| value          | Значение элемента                 | HTMLElement(value="По умолчанию")                          |
| placeholder    | Подсказка в поле                  | HTMLElement(placeholder="Введите имя")                     |
| pattern        | Паттерн валидации                 | HTMLElement(pattern="[A-Za-z]{3,}")                        |
| min            | Минимальное значение              | HTMLElement(min="0", min="2024-01-01")                     |
| max            | Максимальное значение             | HTMLElement(max="100", max="2024-12-31")                   |
| step           | Шаг изменения                     | HTMLElement(step="0.1")                                    |
| maxlength      | Макс. длина текста                | HTMLElement(maxlength="50")                                |
| minlength      | Мин. длина текста                 | HTMLElement(minlength="3")                                 |
| charset        | Кодировка                         | HTMLElement(charset="UTF-8")                               |
| content        | Содержимое meta                   | HTMLElement(content="width=device-width")                  |
| http-equiv     | HTTP-эквивалент                   | HTMLElement(http-equiv="refresh")                          |
| property       | Open Graph свойство               | HTMLElement(property="og:title")                           |
| colspan        | Объединение колонок               | HTMLElement(colspan="2")                                   |
| rowspan        | Объединение строк                 | HTMLElement(rowspan="3")                                   |
| headers        | ID Заголовки для ячейки           | HTMLElement(headers="col1 col2")                           |
| scope          | Область ячейки                    | HTMLElement(scope="col")                                   |
| start          | Начальное значение списка         | HTMLElement(start="10")                                    |
| list           | связь с datalist                  | HTMLElement(list="browsers")                               |
| form           | связь с формой                    | HTMLElement(form="myForm")                                 |
| srcdoc         | HTML для iframe                   | HTMLElement(srcdoc="<p>Привет</p>")                        |
| sandbox        | Ограничения iframe                | HTMLElement(sandbox="allow-scripts allow-forms")           |
| allow          | разрешения iframe                 | HTMLElement(allow="camera; microphone; geolocation")       |
| preload        | Предзагрузка медиа                | HTMLElement(preload="metadata")                            |
| crossorigin    | CORS настройки                    | HTMLElement(crossorigin="anonymous")                       |
| usemap         | Карта изображения                 | HTMLElement(usemap="#imagemap")                            |
| accept         | принимаемые файлы                 | HTMLElement(accept=".pdf,.doc,.docx,image/\*")             |
| integrity      | Целостность скрипта               | HTMLElement(integrity="sha256-...")                        |
| nonce          | Одноразовый код CSP               | HTMLElement(nonce="abc123")                                |
| accesskey      | Клавиша быстрого доступа          | HTMLElement(accesskey="s")                                 |
| tabindex       | Порядок табуляции                 | HTMLElement(tabindex="1")                                  |
| inputmode      | Режим клавиатуры                  | HTMLElement(inputmode="numeric")                           |
| enterkeyhint   | Подсказка Enter                   | HTMLElement(enterkeyhint="search")                         |
| referrerpolicy | Политика реферера                 | HTMLElement(referrerpolicy="no-referrer")                  |

### Класс BooleanAttributes

Булевые атрибуты, где наличие атрибута означает True, а отсутствие - False (синтаксис: attribute без значения).
Все булевые атрибуты передаются в список boolean_attributes.

BooleanAttributes - Булевые атрибуты

| Атрибут         | Описание                     | Пример                                             |
| --------------- | ---------------------------- | -------------------------------------------------- |
| hidden          | Скрыть элемент               | HTMLElement(boolean_attributes=["hidden"]          |
| inert           | Игнорировать элемент         | HTMLElement(boolean_attributes=["inert"]           |
| required        | Обязательное поле            | HTMLElement(boolean_attributes=["required"]        |
| disabled        | Отключенный элемент          | HTMLElement(boolean_attributes=["disabled"]        |
| readonly        | Только для чтения            | HTMLElement(boolean_attributes=["readonly"]        |
| checked         | Выбранный checkbox/radio     | HTMLElement(boolean_attributes=["checked"]         |
| selected        | Выбранная опция              | HTMLElement(boolean_attributes=["selected"]        |
| multiple        | Множественный выбор          | HTMLElement(boolean_attributes=["multiple"]        |
| autofocus       | Автофокус                    | HTMLElement(boolean_attributes=["autofocus"]       |
| formnovalidate  | Без валидации формы          | HTMLElement(boolean_attributes=["formnovalidate"]  |
| controls        | Элементы управления медиа    | HTMLElement(boolean_attributes=["controls"]        |
| autoplay        | Автовоспроизведение          | HTMLElement(boolean_attributes=["autoplay"]        |
| loop            | Зацикливание                 | HTMLElement(boolean_attributes=["loop"]            |
| muted           | Без звука                    | HTMLElement(boolean_attributes=["muted"]           |
| playsinline     | Встроенное воспроизведение   | HTMLElement(boolean_attributes=["playsinline"]     |
| ismap           | Карта изображения сервера    | HTMLElement(boolean_attributes=["ismap"]           |
| reversed        | Обратный список              | HTMLElement(boolean_attributes=["reversed"]        |
| open            | Открытый details/accordion   | HTMLElement(boolean_attributes=["open"]            |
| contenteditable | Редактируемый контент        | HTMLElement(boolean_attributes=["contenteditable"] |
| draggable       | Перетаскиваемый элемент      | HTMLElement(boolean_attributes=["draggable"]       |
| spellcheck      | Проверка орфографии          | HTMLElement(boolean_attributes=["spellcheck"]      |
| allowfullscreen | Полноэкранный режим          | HTMLElement(boolean_attributes=["allowfullscreen"] |
| async           | Асинхронная загрузка скрипта | HTMLElement(boolean_attributes=["async"]           |
| defer           | Отложенная загрузка скрипта  | HTMLElement(boolean_attributes=["defer"]           |
| scoped          | Ограниченные стили           | HTMLElement(boolean_attributes=["scoped"]          |
| popover         | Всплывающий элемент          | HTMLElement(boolean_attributes=["popover"]         |
| nowrap          | Без переноса текста          | HTMLElement(boolean_attributes=["nowrap"]          |
| noshade         | Без тени у hr                | HTMLElement(boolean_attributes=["noshade"]         |
| noresize        | Без изменения размера        | HTMLElement(boolean_attributes=["noresize"]        |
