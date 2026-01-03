
# ========== СОБЫТИЯ МЫШИ ==========
class MouseEvents:
    """События мыши и указателя"""

    onclick = "onclick"  # Щелчок левой кнопкой
    ondblclick = "ondblclick"  # Двойной щелчок
    onmousedown = "onmousedown"  # Нажатие кнопки мыши
    onmouseup = "onmouseup"  # Отпускание кнопки мыши
    onmousemove = "onmousemove"  # Движение мыши над элементом
    onmouseover = "onmouseover"  # Курсор мыши над элементом
    onmouseout = "onmouseout"  # Курсор мыши покидает элемент
    onmouseenter = "onmouseenter"  # Курсор мыши входит в элемент
    onmouseleave = "onmouseleave"  # Курсор мыши покидает элемент
    oncontextmenu = "oncontextmenu"  # Щелчок правой кнопкой
    onwheel = "onwheel"  # Вращение колесика мыши
    onscroll = "onscroll"  # Прокрутка элемента

    # События перетаскивания
    ondrag = "ondrag"  # Элемент перетаскивается
    ondragstart = "ondragstart"  # Начало перетаскивания
    ondragend = "ondragend"  # Конец перетаскивания
    ondragenter = "ondragenter"  # Перетаскиваемый объект входит в элемент
    ondragleave = "ondragleave"  # Перетаскиваемый объект покидает элемент
    ondragover = "ondragover"  # Перетаскиваемый объект над элементом
    ondrop = "ondrop"  # Перетаскиваемый объект сброшен на элемент

    # События указателя (современные)
    onpointerdown = "onpointerdown"  # Нажатие указателя
    onpointerup = "onpointerup"  # Отпускание указателя
    onpointermove = "onpointermove"  # Движение указателя
    onpointerover = "onpointerover"  # Указатель над элементом
    onpointerout = "onpointerout"  # Указатель покидает элемент
    onpointerenter = "onpointerenter"  # Указатель входит в элемент
    onpointerleave = "onpointerleave"  # Указатель покидает элемент
    onpointercancel = "onpointercancel"  # Отмена указателя
    ongotpointercapture = "ongotpointercapture"  # Захват указателя
    onlostpointercapture = "onlostpointercapture"  # Потеря захвата указателя

    # События касания
    ontouchstart = "ontouchstart"  # Начало касания
    ontouchend = "ontouchend"  # Конец касания
    ontouchmove = "ontouchmove"  # Движение касания
    ontouchcancel = "ontouchcancel"  # Отмена касания

# ========== СОБЫТИЯ КЛАВИАТУРЫ ==========
class KeyboardEvents:
    """События клавиатуры"""

    onkeydown = "onkeydown"  # Нажатие клавиши
    onkeyup = "onkeyup"  # Отпускание клавиши
    onkeypress = "onkeypress"  # Нажатие и отпускание (устаревает)

    # События ввода текста
    oninput = "oninput"  # Изменение значения элемента
    onbeforeinput = "onbeforeinput"  # Перед изменением значения
    oncompositionstart = "oncompositionstart"  # Начало композиции (IME)
    oncompositionupdate = "oncompositionupdate"  # Обновление композиции
    oncompositionend = "oncompositionend"  # Конец композиции

# ========== СОБЫТИЯ ФОРМ ==========
class FormEvents:
    """События форм и элементов ввода"""

    onsubmit = "onsubmit"  # Отправка формы
    onreset = "onreset"  # Сброс формы
    onchange = "onchange"  # Изменение значения элемента
    onselect = "onselect"  # Выбор текста в поле ввода
    oninvalid = "oninvalid"  # Элемент не прошел валидацию

    # Фокус
    onfocus = "onfocus"  # Элемент получает фокус
    onblur = "onblur"  # Элемент теряет фокус
    onfocusin = "onfocusin"  # Элемент получает фокус (всплывает)
    onfocusout = "onfocusout"  # Элемент теряет фокус (всплывает)

    # События поиска
    onsearch = "onsearch"  # Поиск в поле search

    # Проверка до вставки
    onbeforecut = "onbeforecut"  # Перед вырезанием
    onbeforecopy = "onbeforecopy"  # Перед копированием
    onbeforepaste = "onbeforepaste"  # Перед вставкой

# ========== СОБЫТИЯ МЕДИА ==========
class MediaEvents:
    """События аудио, видео и других медиа"""

    onabort = "onabort"  # Загрузка прервана
    oncanplay = "oncanplay"  # Медиа может начать воспроизведение
    oncanplaythrough = "oncanplaythrough"  # Медиа может воспроизводиться до конца
    ondurationchange = "ondurationchange"  # Изменение длительности
    onemptied = "onemptied"  # Медиа стало пустым
    onended = "onended"  # Воспроизведение завершено
    onerror = "onerror"  # Ошибка при загрузке
    onloadeddata = "onloadeddata"  # Данные загружены
    onloadedmetadata = "onloadedmetadata"  # Метаданные загружены
    onloadstart = "onloadstart"  # Начало загрузки
    onpause = "onpause"  # Воспроизведение приостановлено
    onplay = "onplay"  # Воспроизведение начато
    onplaying = "onplaying"  # Воспроизведение после паузы или задержки
    onprogress = "onprogress"  # Прогресс загрузки
    onratechange = "onratechange"  # Изменение скорости воспроизведения
    onseeked = "onseeked"  # Поиск завершен
    onseeking = "onseeking"  # Начало поиска
    onstalled = "onstalled"  # Задержка загрузки
    onsuspend = "onsuspend"  # Загрузка приостановлена
    ontimeupdate = "ontimeupdate"  # Изменение текущего времени
    onvolumechange = "onvolumechange"  # Изменение громкости
    onwaiting = "onwaiting"  # Ожидание данных для воспроизведения

    # События треков текста
    oncuechange = "oncuechange"  # Изменение активного текстового трека

    # События для Picture-in-Picture
    onenterpictureinpicture = "onenterpictureinpicture"
    onleavepictureinpicture = "onleavepictureinpicture"
    onresize = "onresize"  # Изменение размера PIP окна

# ========== СОБЫТИЯ ДОКУМЕНТА И ОКНА ==========
class DocumentEvents:
    """События документа и окна"""

    onload = "onload"  # Загрузка завершена
    onunload = "onunload"  # Документ выгружается
    onbeforeunload = "onbeforeunload"  # Перед выгрузкой документа
    onpageshow = "onpageshow"  # Страница показана
    onpagehide = "onpagehide"  # Страница скрыта

    # События DOM
    onreadystatechange = "onreadystatechange"  # Изменение состояния готовности
    onDOMContentLoaded = "onDOMContentLoaded"  # DOM загружен

    # События печати
    onafterprint = "onafterprint"  # После печати
    onbeforeprint = "onbeforeprint"  # Перед печатью

    # События полноэкранного режима
    onfullscreenchange = "onfullscreenchange"  # Изменение полноэкранного режима
    onfullscreenerror = "onfullscreenerror"  # Ошибка перехода в полноэкранный режим

    # События видимости
    onvisibilitychange = "onvisibilitychange"  # Изменение видимости страницы

# ========== СОБЫТИЯ КОПИРОВАНИЯ И ВСТАВКИ ==========
class ClipboardEvents:
    """События буфера обмена"""

    oncopy = "oncopy"  # Копирование текста
    oncut = "oncut"  # Вырезание текста
    onpaste = "onpaste"  # Вставка текста

    # Расширенные события буфера обмена
    onbeforecut = "onbeforecut"  # Перед вырезанием
    onbeforecopy = "onbeforecopy"  # Перед копированием
    onbeforepaste = "onbeforepaste"  # Перед вставкой

# ========== СОБЫТИЯ АНИМАЦИИ И ПЕРЕХОДОВ ==========
class AnimationEvents:
    """События CSS анимаций и переходов"""

    onanimationstart = "onanimationstart"  # Начало CSS анимации
    onanimationend = "onanimationend"  # Конец CSS анимации
    onanimationiteration = "onanimationiteration"  # Итерация CSS анимации
    onanimationcancel = "onanimationcancel"  # Отмена CSS анимации

    # События переходов
    ontransitionstart = "ontransitionstart"  # Начало CSS перехода
    ontransitionend = "ontransitionend"  # Конец CSS перехода
    ontransitionrun = "ontransitionrun"  # CSS переход запущен
    ontransitioncancel = "ontransitioncancel"  # Отмена CSS перехода

# ========== СОБЫТИЯ ХРАНЕНИЯ ==========
class StorageEvents:
    """События Web Storage"""

    onstorage = "onstorage"  # Изменение данных в localStorage/sessionStorage

# ========== СОБЫТИЯ СООБЩЕНИЙ ==========
class MessageEvents:
    """События сообщений между окнами/воркерами"""

    onmessage = "onmessage"  # Получение сообщения
    onmessageerror = "onmessageerror"  # Ошибка при получении сообщения

    # События для Service Workers
    onstatechange = "onstatechange"  # Изменение состояния Service Worker

# ========== СОБЫТИЯ РЕСУРСОВ ==========
class ResourceEvents:
    """События загрузки ресурсов"""

    onerror = "onerror"  # Ошибка загрузки ресурса
    onload = "onload"  # Ресурс загружен
    onloadend = "onloadend"  # Загрузка завершена (успешно или с ошибкой)
    onloadstart = "onloadstart"  # Начало загрузки
    onprogress = "onprogress"  # Прогресс загрузки
    ontimeout = "ontimeout"  # Таймаут загрузки
    onabort = "onabort"  # Загрузка прервана пользователем

# ========== СОБЫТИЯ ДРАГ-ЭНД-ДРОП API ==========
class DragDropEvents:
    """События Drag-and-Drop API"""

    ondrag = "ondrag"  # Перетаскивание элемента
    ondragstart = "ondragstart"  # Начало перетаскивания
    ondragend = "ondragend"  # Конец перетаскивания
    ondragenter = "ondragenter"  # Вход в зону сброса
    ondragleave = "ondragleave"  # Выход из зоны сброса
    ondragover = "ondragover"  # Наведение над зоной сброса
    ondrop = "ondrop"  # Сброс в зону

# ========== СОБЫТИЯ ИГРОВЫХ КОНТРОЛЛЕРОВ ==========
class GamepadEvents:
    """События игровых контроллеров"""

    ongamepadconnected = "ongamepadconnected"  # Подключение контроллера
    ongamepaddisconnected = "ongamepaddisconnected"  # Отключение контроллера

# ========== СОБЫТИЯ СЕНСОРОВ ==========
class SensorEvents:
    """События датчиков устройства"""

    ondevicemotion = "ondevicemotion"  # Изменение движения устройства
    ondeviceorientation = "ondeviceorientation"  # Изменение ориентации устройства
    ondeviceorientationabsolute = "ondeviceorientationabsolute"  # Абсолютная ориентация

    # События освещенности
    ondevicelight = "ondevicelight"  # Изменение уровня освещенности

    # События приближения
    ondeviceproximity = "ondeviceproximity"  # Изменение расстояния до объекта
    onuserproximity = "onuserproximity"  # Приближение/удаление пользователя