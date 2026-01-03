# HTMLEvents

`HTMLEvents` - содержит определения констант для всех HTML событий, сгруппированных по категориям. Этот модуль предоставляет удобный способ ссылаться на стандартные DOM события при работе с классом HTMLElement.

---

## Структура файла

Файл содержит 13 классов, каждый из которых группирует события по типу взаимодействия:

- MouseEvents - события мыши, указателя и касания
- KeyboardEvents - события клавиатуры и ввода текста
- FormEvents - события форм и элементов ввода
- MediaEvents - события аудио и видео элементов
- DocumentEvents - события документа и окна браузера
- ClipboardEvents - события буфера обмена
- AnimationEvents - события CSS анимаций и переходов
- StorageEvents - события Web Storage
- MessageEvents - события межоконных сообщений
- ResourceEvents - события загрузки ресурсов
- DragDropEvents - события Drag-and-Drop API
- GamepadEvents - события игровых контроллеров
- SensorEvents - события датчиков устройства

## Полный справочник событий

### MouseEvents

- События мыши:

| Событие       | Описание                                    | Пример использования                   |
| ------------- | ------------------------------------------- | -------------------------------------- |
| onclick       | Щелчок левой кнопкой мыши                   | onclick="handleClick(event)"           |
| ondblclick    | Двойной щелчок                              | ondblclick="openDetails()"             |
| onmousedown   | Нажатие кнопки мыши                         | onmousedown="startDrag(event)"         |
| onmouseup     | Отпускание кнопки мыши                      | onmouseup="endDrag()"                  |
| onmousemove   | Движение мыши над элементом                 | onmousemove="updateCoordinates(event)" |
| onmouseover   | Курсор мыши над элементом                   | onmouseover="showTooltip()"            |
| onmouseout    | Курсор мыши покидает элемент                | onmouseout="hideTooltip()"             |
| onmouseenter  | Курсор мыши входит в элемент (не всплывает) | onmouseenter="highlight()"             |
| onmouseleave  | Курсор мыши покидает элемент (не всплывает) | onmouseleave="unhighlight()"           |
| oncontextmenu | Щелчок правой кнопкой мыши                  | oncontextmenu="showContextMenu(event)" |
| onwheel       | Вращение колесика мыши                      | onwheel="handleScroll(event)"          |
| onscroll      | Прокрутка элемента                          | onscroll="updateScrollPosition()"      |

- События перетаскивания

| Событие     | Описание                                  | Пример использования                    |
| ----------- | ----------------------------------------- | --------------------------------------- |
| ondrag      | Элемент перетаскивается                   | ondrag="updateDragPosition(event)"      |
| ondragstart | Начало перетаскивания                     | ondragstart="startDragOperation(event)" |
| ondragend   | Конец перетаскивания                      | ondragend="cleanupDrag()"               |
| ondragenter | Перетаскиваемый объект входит в элемент   | ondragenter="showDropZone()"            |
| ondragleave | Перетаскиваемый объект покидает элемент   | ondragleave="hideDropZone()"            |
| ondragover  | Перетаскиваемый объект над элементом      | ondragover="preventDefault(event)"      |
| ondrop      | Перетаскиваемый объект сброшен на элемент | ondrop="handleDrop(event)"              |

- События указателя (современные)

| Событие              | Описание                                | Пример использования                       |
| -------------------- | --------------------------------------- | ------------------------------------------ |
| onpointerdown        | Нажатие указателя (мышь, перо, касание) | onpointerdown="handlePointerDown(event)"   |
| onpointerup          | Отпускание указателя                    | onpointerup="handlePointerUp(event)"       |
| onpointermove        | Движение указателя                      | onpointermove="trackPointer(event)"        |
| onpointerover        | Указатель над элементом                 | onpointerover="activateElement()"          |
| onpointerout         | Указатель покидает элемент              | onpointerout="deactivateElement()"         |
| onpointerenter       | Указатель входит в элемент              | onpointerenter="enterElement()"            |
| onpointerleave       | Указатель покидает элемент              | onpointerleave="leaveElement()"            |
| onpointercancel      | Отмена указателя                        | onpointercancel="cleanupPointer()"         |
| ongotpointercapture  | Захват указателя элементом              | ongotpointercapture="handleCapture()"      |
| onlostpointercapture | Потеря захвата указателя                | onlostpointercapture="handleLostCapture()" |

- События касания

| Событие       | Описание         | Пример использования                   |
| ------------- | ---------------- | -------------------------------------- |
| ontouchstart  | Начало касания   | ontouchstart="handleTouchStart(event)" |
| ontouchend    | Конец касания    | ontouchend="handleTouchEnd(event)"     |
| ontouchmove   | Движение касания | ontouchmove="handleTouchMove(event)"   |
| ontouchcancel | Отмена касания   | ontouchcancel="handleTouchCancel()"    |

### KeyboardEvents

- События клавиатуры

| Событие    | Описание             | Пример использования                            |
| ---------- | -------------------- | ----------------------------------------------- |
| onkeydown  | Нажатие клавиши      | onkeydown="handleKeyDown(event)"                |
| onkeyup    | Отпускание клавиши   | onkeyup="handleKeyUp(event)"                    |
| onkeypress | Нажатие и отпускание | (устаревает) onkeypress="handleKeyPress(event)" |

- События ввода текста

| Событие             | Описание                    | Пример использования                   |
| ------------------- | --------------------------- | -------------------------------------- |
| oninput             | Изменение значения элемента | oninput="validateInput(event)"         |
| onbeforeinput       | Перед изменением значения   | onbeforeinput="preprocessInput(event)" |
| oncompositionstart  | Начало композиции (IME)     | oncompositionstart="startIME()"        |
| oncompositionupdate | Обновление композиции       | oncompositionupdate="updateIME()"      |
| oncompositionend    | Конец композиции            | oncompositionend="endIME()"            |

### FormEvents

- События форм

| Событие   | Описание                    | Пример использования              |
| --------- | --------------------------- | --------------------------------- |
| onsubmit  | Отправка формы              | onsubmit="validateForm(event)"    |
| onreset   | Сброс формы                 | onreset="confirmReset()"          |
| onchange  | Изменение значения элемента | onchange="updateSelection()"      |
| onselect  | Выбор текста в поле ввода   | onselect="highlightSelection()"   |
| oninvalid | Элемент не прошел валидацию | oninvalid="showValidationError()" |

- События фокуса

| Событие    | Описание                           | Пример использования        |
| ---------- | ---------------------------------- | --------------------------- |
| onfocus    | Элемент получает фокус             | onfocus="highlightField()"  |
| onblur     | Элемент теряет фокус               | onblur="validateField()"    |
| onfocusin  | Элемент получает фокус (всплывает) | onfocusin="prepareField()"  |
| onfocusout | Элемент теряет фокус (всплывает)   | onfocusout="cleanupField()" |

- Другие события форм

| Событие       | Описание            | Пример использования                 |
| ------------- | ------------------- | ------------------------------------ |
| onsearch      | Поиск в поле search | onsearch="performSearch(event)"      |
| onbeforecut   | Перед вырезанием    | onbeforecut="preventCut(event)"      |
| onbeforecopy  | Перед копированием  | onbeforecopy="preventCopy(event)"    |
| onbeforepaste | Перед вставкой      | onbeforepaste="validatePaste(event)" |

### MediaEvents

- События медиа

| Событие          | Описание                                 | Пример использования                       |
| ---------------- | ---------------------------------------- | ------------------------------------------ |
| onabort          | Загрузка прервана                        | onabort="handleAbort()"                    |
| oncanplay        | Медиа может начать воспроизведение       | oncanplay="enablePlayButton()"             |
| oncanplaythrough | Медиа может воспроизводиться до конца    | oncanplaythrough="autoPlayIfAllowed()"     |
| ondurationchange | Изменение длительности                   | ondurationchange="updateDurationDisplay()" |
| onemptied        | Медиа стало пустым                       | onemptied="resetPlayer()"                  |
| onended          | Воспроизведение завершено                | onended="playNext()"                       |
| onerror          | Ошибка при загрузке                      | onerror="showErrorMessage()"               |
| onloadeddata     | Данные загружены                         | onloadeddata="showContent()"               |
| onloadedmetadata | Метаданные загружены                     | onloadedmetadata="showMetadata()"          |
| onloadstart      | Начало загрузки                          | onloadstart="showLoadingIndicator()"       |
| onpause          | Воспроизведение приостановлено           | onpause="updatePlayButton()"               |
| onplay           | Воспроизведение начато                   | onplay="startPlaybackTimer()"              |
| onplaying        | Воспроизведение после паузы или задержки | onplaying="hideBuffering()"                |
| onprogress       | Прогресс загрузки                        | onprogress="updateProgressBar(event)"      |
| onratechange     | Изменение скорости воспроизведения       | onratechange="updateSpeedDisplay()"        |
| onseeked         | Поиск завершен                           | onseeked="hideSeekingIndicator()"          |
| onseeking        | Начало поиска                            | onseeking="showSeekingIndicator()"         |
| onstalled        | Задержка загрузки                        | onstalled="showBuffering()"                |
| onsuspend        | Загрузка приостановлена                  | onsuspend="pauseDownload()"                |
| ontimeupdate     | Изменение текущего времени               | ontimeupdate="updateTimeDisplay()"         |
| onvolumechange   | Изменение громкости                      | onvolumechange="updateVolumeIcon()"        |
| onwaiting        | Ожидание данных для воспроизведения      | onwaiting="showWaitingIndicator()"         |

- Специальные медиа события

| Событие                 | Описание                             | Пример использования                 |
| ----------------------- | ------------------------------------ | ------------------------------------ |
| oncuechange             | Изменение активного текстового трека | oncuechange="updateSubtitles()"      |
| onenterpictureinpicture | Вход в режим картинка в картинке     | onenterpictureinpicture="enterPiP()" |
| onleavepictureinpicture | Выход из режима картинка в картинке  | onleavepictureinpicture="exitPiP()"  |
| onresize                | Изменение размера PIP окна           | onresize="adjustPiPSize()"           |

### DocumentEvents

- События документа

| Событие        | Описание                  | Пример использования                |
| -------------- | ------------------------- | ----------------------------------- |
| onload         | Загрузка завершена        | onload="initializeApp()"            |
| onunload       | Документ выгружается      | onunload="cleanupResources()"       |
| onbeforeunload | Перед выгрузкой документа | onbeforeunload="confirmExit(event)" |
| onpageshow     | Страница показана         | onpageshow="restoreState()"         |
| onpagehide     | Страница скрыта           | onpagehide="saveState()"            |

- События DOM

| Событие            | Описание                       | Пример использования                   |
| ------------------ | ------------------------------ | -------------------------------------- |
| onreadystatechange | Изменение состояния готовности | onreadystatechange="checkReadyState()" |
| onDOMContentLoaded | DOM загружен                   | onDOMContentLoaded="setupDOM()"        |

- События печати

| Событие       | Описание      | Пример использования              |
| ------------- | ------------- | --------------------------------- |
| onafterprint  | После печати  | onafterprint="cleanupPrint()"     |
| onbeforeprint | Перед печатью | onbeforeprint="prepareForPrint()" |

- События полноэкранного режима

| Событие            | Описание                              | Пример использования                      |
| ------------------ | ------------------------------------- | ----------------------------------------- |
| onfullscreenchange | Изменение полноэкранного режима       | onfullscreenchange="toggleFullscreenUI()" |
| onfullscreenerror  | Ошибка перехода в полноэкранный режим | onfullscreenerror="showFullscreenError()" |

- События видимости

| Событие            | Описание                     | Пример использования                          |
| ------------------ | ---------------------------- | --------------------------------------------- |
| onvisibilitychange | Изменение видимости страницы | onvisibilitychange="handleVisibilityChange()" |

### ClipboardEvents

- События буфера обмена

| Событие | Описание           | Пример использования                |
| ------- | ------------------ | ----------------------------------- |
| oncopy  | Копирование текста | oncopy="formatCopiedText(event)"    |
| oncut   | Вырезание текста   | oncut="handleCut(event)"            |
| onpaste | Вставка текста     | onpaste="sanitizePastedText(event)" |

- Расширенные события буфера
  | Событие | Описание | Пример использования |
  | ------- | -------- | -------------------- |
  onbeforecut Перед вырезанием onbeforecut="validateCut(event)"
  onbeforecopy Перед копированием onbeforecopy="validateCopy(event)"
  onbeforepaste Перед вставкой onbeforepaste="validatePaste(event)"

### AnimationEvents

- События анимаций

| Событие              | Описание              | Пример использования                   |
| -------------------- | --------------------- | -------------------------------------- |
| onanimationstart     | Начало CSS анимации   | onanimationstart="logAnimationStart()" |
| onanimationend       | Конец CSS анимации    | onanimationend="enableInteraction()"   |
| onanimationiteration | Итерация CSS анимации | onanimationiteration="updateCounter()" |
| onanimationcancel    | Отмена CSS анимации   | onanimationcancel="cleanupAnimation()" |

- События переходов

| Событие            | Описание            | Пример использования                     |
| ------------------ | ------------------- | ---------------------------------------- |
| ontransitionstart  | Начало CSS перехода | ontransitionstart="measureStart()"       |
| ontransitionend    | Конец CSS перехода  | ontransitionend="finalizeTransition()"   |
| ontransitionrun    | CSS переход запущен | ontransitionrun="prepareTransition()"    |
| ontransitioncancel | Отмена CSS перехода | ontransitioncancel="cleanupTransition()" |

### StorageEvents

- События хранилища

| Событие   | Описание                                       | Пример использования           |
| --------- | ---------------------------------------------- | ------------------------------ |
| onstorage | Изменение данных в localStorage/sessionStorage | onstorage="syncChanges(event)" |

### MessageEvents

- События сообщений

| Событие        | Описание                       | Пример использования                       |
| -------------- | ------------------------------ | ------------------------------------------ |
| onmessage      | Получение сообщения            | onmessage="handleMessage(event)"           |
| onmessageerror | Ошибка при получении сообщения | onmessageerror="handleMessageError(event)" |

- События Service Workers

| Событие       | Описание                           | Пример использования             |
| ------------- | ---------------------------------- | -------------------------------- |
| onstatechange | Изменение состояния Service Worker | onstatechange="updateSWStatus()" |

### ResourceEvents

- События ресурсов

| Событие     | Описание           | Пример использования                  |
| ----------- | ------------------ | ------------------------------------- |
| onerror     | Ошибка загрузки    | ресурса onerror="loadFallback()"      |
| onload      | Ресурс загружен    | onload="useResource()"                |
| onloadend   | Загрузка завершена | onloadend="cleanupLoader()"           |
| onloadstart | Начало загрузки    | onloadstart="showLoader()"            |
| onprogress  | Прогресс загрузки  | onprogress="updateProgress(event)"    |
| ontimeout   | Таймаут загрузки   | ontimeout="handleTimeout()"           |
| onabort     | Загрузка прервана  | пользователем onabort="handleAbort()" |

### DragDropEvents

- События перетаскивания

| Событие     | Описание                   | Пример использования                |
| ----------- | -------------------------- | ----------------------------------- |
| ondrag      | Перетаскивание элемента    | ondrag="updateDragUI(event)"        |
| ondragstart | Начало перетаскивания      | ondragstart="setupDragData(event)"  |
| ondragend   | Конец перетаскивания       | ondragend="cleanupDrag()"           |
| ondragenter | Вход в зону сброса         | ondragenter="highlightDropZone()"   |
| ondragleave | Выход из зоны сброса       | ondragleave="unhighlightDropZone()" |
| ondragover  | Наведение над зоной сброса | ondragover="allowDrop(event)"       |
| ondrop      | Сброс в зону               | ondrop="processDrop(event)"         |

### GamepadEvents

- События контроллеров

| Событие               | Описание                | Пример использования                     |
| --------------------- | ----------------------- | ---------------------------------------- |
| ongamepadconnected    | Подключение контроллера | ongamepadconnected="setupGamepad(event)" |
| ongamepaddisconnected | Отключение контроллера  | ongamepaddisconnected="cleanupGamepad()" |

#### SensorEvents

- События датчиков

| Событие                     | Описание                          | Пример использования                           |
| --------------------------- | --------------------------------- | ---------------------------------------------- |
| ondevicemotion              | Изменение движения устройства     | ondevicemotion="handleMotion(event)"           |
| ondeviceorientation         | Изменение ориентации устройства   | ondeviceorientation="handleOrientation(event)" |
| ondeviceorientationabsolute | Абсолютная ориентация             | ondeviceorientationabsolute="handleAO(event)"  |
| ondevicelight               | Изменение уровня освещенности     | ondevicelight="adjustBrightness(event)"        |
| ondeviceproximity           | Изменение расстояния до объекта   | ondeviceproximity="handleProximity(event)"     |
| onuserproximity             | Приближение/удаление пользователя | onuserproximity="handleUserPresence(event)"    |
