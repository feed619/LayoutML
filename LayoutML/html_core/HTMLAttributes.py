class ValueAttributes:
    """Атрибуты, требующие значения через '='"""

    # Базовые атрибуты
    id_ = "id"
    name = "name"
    title = "title"
    lang = "lang"
    dir = "dir"  # ltr/rtl/auto
    translate = "translate"  # yes/no

    # Стили и классы
    class_ = "class"
    style = "style"

    # Ссылки и пути
    href = "href"
    src = "src"
    srcset = "srcset"
    sizes = "sizes"
    poster = "poster"
    action = "action"
    formaction = "formaction"

    # Размеры
    width = "width"
    height = "height"
    size = "size"

    # Формы и ввод
    value = "value"
    placeholder = "placeholder"
    pattern = "pattern"
    min = "min"
    max = "max"
    step = "step"
    maxlength = "maxlength"
    minlength = "minlength"

    # Мета-атрибуты
    charset = "charset"
    content = "content"
    http_equiv = "http-equiv"
    property = "property"  # Open Graph

    # Таблицы
    colspan = "colspan"
    rowspan = "rowspan"
    headers = "headers"
    scope = "scope"  # col/row/colgroup/rowgroup

    # Списки
    start = "start"

    # Связи
    list = "list"
    form = "form "

    # Iframe
    srcdoc = "srcdoc"
    sandbox = "sandbox"  # allow-forms allow-scripts...
    allow = "allow"

    # Медиа
    preload = "preload"  # none/metadata/auto
    crossorigin = "crossorigin"
    usemap = "usemap"
    accept = "accept"

    # Скрипты и стили
    integrity = "integrity"
    nonce = "nonce"

    # Вспомогательные
    accesskey = "accesskey"
    tabindex = "tabindex"
    inputmode = "inputmode"  # none/text/decimal/numeric
    enterkeyhint = "enterkeyhint"  # enter/done/go/next
    referrerpolicy = "referrerpolicy"

    # Устаревшие
    align = "align"
    bgcolor = "bgcolor"
    border = "border"
    cellpadding = "cellpadding"
    cellspacing = "cellspacing"
    frame = "frame"
    rules = "rules"
    summary = "summary"
    valign = "valign"

    # Пользовательские data-атрибуты (префикс)
    data_prefix = "data-"


class BooleanAttributes:
    """Булевые атрибуты (присутствие = True)"""

    # Видимость
    hidden = "hidden"
    inert = "inert"

    # Формы
    required = "required"
    disabled = "disabled"
    readonly = "readonly"
    checked = "checked"
    selected = "selected"
    multiple = "multiple"
    autofocus = "autofocus"
    formnovalidate = "formnovalidate"

    # Медиа
    controls = "controls"
    autoplay = "autoplay"
    loop = "loop"
    muted = "muted"
    playsinline = "playsinline"

    # Изображения
    ismap = "ismap"

    # Списки
    reversed = "reversed"

    # Детали/аккордеон
    open = "open"

    # Редактирование
    contenteditable = "contenteditable"  # также может иметь значения

    # Перетаскивание
    draggable = "draggable"  # также может иметь true/false

    # Проверка
    spellcheck = "spellcheck"  # также может иметь true/false

    # Iframe
    allowfullscreen = "allowfullscreen"

    # Скрипты
    async_ = "async"
    defer = "defer"

    # Стили (устаревший)
    scoped = "scoped"

    # Современные
    popover = "popover"

    # Устаревшие булевые
    nowrap = "nowrap"
    noshade = "noshade"
    noresize = "noresize"


class EnumAttributes:
    """Атрибуты с предопределенными значениями"""

    # Направление текста
    dir_values = {"ltr", "rtl", "auto"}

    # Автозаполнение
    autocomplete_values = {"on", "off", "name", "email", "username", "current-password", "new-password"}

    # Метод формы
    method_values = {"get", "post", "dialog"}

    # Тип кнопки/ввода
    type_values = {
        "button",
        "submit",
        "reset",  # button
        "text",
        "password",
        "email",
        "number",
        "tel",
        "url",
        "search",  # input
        "date",
        "time",
        "datetime-local",
        "month",
        "week",  # дата/время
        "color",
        "range",
        "file",
        "hidden",
        "image",  # другие input
        "checkbox",
        "radio",  # выбор
    }

    # Тип кодировки формы
    enctype_values = {"application/x-www-form-urlencoded", "multipart/form-data", "text/plain"}

    # Цель ссылки/формы
    target_values = {"_blank", "_self", "_parent", "_top"}

    # Отношение ссылки
    rel_values = {
        "alternate",
        "author",
        "bookmark",
        "external",
        "help",
        "license",
        "next",
        "nofollow",
        "noopener",
        "noreferrer",
        "prev",
        "search",
        "tag",
    }

    # Предзагрузка медиа
    preload_values = {"none", "metadata", "auto"}

    # Загрузка изображений/iframe
    loading_values = {"lazy", "eager"}

    # Декодирование изображений
    decoding_values = {"sync", "async", "auto"}

    # Режим ввода
    inputmode_values = {"none", "text", "decimal", "numeric", "tel", "search", "email", "url"}

    # Подсказка клавиши Enter
    enterkeyhint_values = {"enter", "done", "go", "next", "previous", "search", "send"}

    # Политика реферера
    referrerpolicy_values = {"no-referrer", "no-referrer-when-downgrade", "origin", "origin-when-cross-origin", "unsafe-url"}

    # Область таблицы
    scope_values = {"col", "row", "colgroup", "rowgroup"}

    # Выравнивание (устаревшее)
    align_values = {"left", "right", "center", "justify"}
    valign_values = {"top", "middle", "bottom", "baseline"}


class SpecialFormatAttributes:
    """Атрибуты со специальным форматом значений"""

    # Source set для изображений
    srcset_format = "srcset"  # "image.jpg 1x, image-2x.jpg 2x"

    # Размеры для srcset
    sizes_format = "sizes"  # "(max-width: 600px) 100vw, 50vw"

    # Список заголовков для таблиц
    headers_format = "headers"  # "header1 header2 header3"

    # Политика безопасности iframe
    sandbox_format = "sandbox"  # "allow-forms allow-scripts"

    # Политика разрешений iframe
    allow_format = "allow"  # "camera; microphone"

    # Атрибут приема файлов
    accept_format = "accept"  # ".jpg,.png,.pdf" или "image/*"

    # Множественный выбор
    list_format = "list"  # ID элемента datalist

    # Форма
    form_format = "form"  # ID формы
