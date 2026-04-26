# HTMLEvents

`HTMLEvents` contains constant definitions for all HTML events, grouped by categories. This module provides a convenient way to reference standard DOM events when working with the `HTMLElement` class.

---

## File Structure

The file contains 13 classes, each grouping events by interaction type:

- MouseEvents — mouse, pointer, and touch events
- KeyboardEvents — keyboard and text input events
- FormEvents — form and input element events
- MediaEvents — audio and video element events
- DocumentEvents — document and browser window events
- ClipboardEvents — clipboard events
- AnimationEvents — CSS animation and transition events
- StorageEvents — Web Storage events
- MessageEvents — cross-window messaging events
- ResourceEvents — resource loading events
- DragDropEvents — Drag-and-Drop API events
- GamepadEvents — game controller events
- SensorEvents — device sensor events

---

## Full Event Reference

### MouseEvents

- Mouse events:

| Event         | Description                        | Example usage                          |
| ------------- | ---------------------------------- | -------------------------------------- |
| onclick       | Left mouse button click            | onclick="handleClick(event)"           |
| ondblclick    | Double click                       | ondblclick="openDetails()"             |
| onmousedown   | Mouse button pressed               | onmousedown="startDrag(event)"         |
| onmouseup     | Mouse button released              | onmouseup="endDrag()"                  |
| onmousemove   | Mouse moved over element           | onmousemove="updateCoordinates(event)" |
| onmouseover   | Mouse enters element               | onmouseover="showTooltip()"            |
| onmouseout    | Mouse leaves element               | onmouseout="hideTooltip()"             |
| onmouseenter  | Mouse enters element (no bubbling) | onmouseenter="highlight()"             |
| onmouseleave  | Mouse leaves element (no bubbling) | onmouseleave="unhighlight()"           |
| oncontextmenu | Right mouse button click           | oncontextmenu="showContextMenu(event)" |
| onwheel       | Mouse wheel scroll                 | onwheel="handleScroll(event)"          |
| onscroll      | Element scrolling                  | onscroll="updateScrollPosition()"      |

- Drag events:

| Event       | Description                 | Example usage                           |
| ----------- | --------------------------- | --------------------------------------- |
| ondrag      | Element is being dragged    | ondrag="updateDragPosition(event)"      |
| ondragstart | Drag start                  | ondragstart="startDragOperation(event)" |
| ondragend   | Drag end                    | ondragend="cleanupDrag()"               |
| ondragenter | Dragged item enters element | ondragenter="showDropZone()"            |
| ondragleave | Dragged item leaves element | ondragleave="hideDropZone()"            |
| ondragover  | Drag over element           | ondragover="preventDefault(event)"      |
| ondrop      | Drop event                  | ondrop="handleDrop(event)"              |

- Pointer events (modern):

| Event                | Description                      | Example usage                              |
| -------------------- | -------------------------------- | ------------------------------------------ |
| onpointerdown        | Pointer down (mouse, pen, touch) | onpointerdown="handlePointerDown(event)"   |
| onpointerup          | Pointer up                       | onpointerup="handlePointerUp(event)"       |
| onpointermove        | Pointer movement                 | onpointermove="trackPointer(event)"        |
| onpointerover        | Pointer enters element           | onpointerover="activateElement()"          |
| onpointerout         | Pointer leaves element           | onpointerout="deactivateElement()"         |
| onpointerenter       | Pointer enters element           | onpointerenter="enterElement()"            |
| onpointerleave       | Pointer leaves element           | onpointerleave="leaveElement()"            |
| onpointercancel      | Pointer interaction canceled     | onpointercancel="cleanupPointer()"         |
| ongotpointercapture  | Pointer captured                 | ongotpointercapture="handleCapture()"      |
| onlostpointercapture | Pointer capture lost             | onlostpointercapture="handleLostCapture()" |

- Touch events:

| Event         | Description    | Example usage                          |
| ------------- | -------------- | -------------------------------------- |
| ontouchstart  | Touch start    | ontouchstart="handleTouchStart(event)" |
| ontouchend    | Touch end      | ontouchend="handleTouchEnd(event)"     |
| ontouchmove   | Touch move     | ontouchmove="handleTouchMove(event)"   |
| ontouchcancel | Touch canceled | ontouchcancel="handleTouchCancel()"    |

---

### KeyboardEvents

- Keyboard events:

| Event      | Description              | Example usage                      |
| ---------- | ------------------------ | ---------------------------------- |
| onkeydown  | Key pressed              | onkeydown="handleKeyDown(event)"   |
| onkeyup    | Key released             | onkeyup="handleKeyUp(event)"       |
| onkeypress | Key pressed (deprecated) | onkeypress="handleKeyPress(event)" |

- Input events:

| Event               | Description           | Example usage                          |
| ------------------- | --------------------- | -------------------------------------- |
| oninput             | Value changed         | oninput="validateInput(event)"         |
| onbeforeinput       | Before value change   | onbeforeinput="preprocessInput(event)" |
| oncompositionstart  | IME composition start | oncompositionstart="startIME()"        |
| oncompositionupdate | IME update            | oncompositionupdate="updateIME()"      |
| oncompositionend    | IME end               | oncompositionend="endIME()"            |

---

### FormEvents

- Form events:

| Event     | Description       | Example usage                     |
| --------- | ----------------- | --------------------------------- |
| onsubmit  | Form submission   | onsubmit="validateForm(event)"    |
| onreset   | Form reset        | onreset="confirmReset()"          |
| onchange  | Value change      | onchange="updateSelection()"      |
| onselect  | Text selection    | onselect="highlightSelection()"   |
| oninvalid | Validation failed | oninvalid="showValidationError()" |

- Focus events:

| Event      | Description            | Example usage               |
| ---------- | ---------------------- | --------------------------- |
| onfocus    | Element focused        | onfocus="highlightField()"  |
| onblur     | Element lost focus     | onblur="validateField()"    |
| onfocusin  | Focus enters (bubbles) | onfocusin="prepareField()"  |
| onfocusout | Focus leaves (bubbles) | onfocusout="cleanupField()" |

---

### MediaEvents

- Media events:

| Event          | Description          | Example usage                       |
| -------------- | -------------------- | ----------------------------------- |
| onplay         | Playback started     | onplay="startPlaybackTimer()"       |
| onpause        | Playback paused      | onpause="updatePlayButton()"        |
| onended        | Playback ended       | onended="playNext()"                |
| ontimeupdate   | Current time updated | ontimeupdate="updateTimeDisplay()"  |
| onvolumechange | Volume changed       | onvolumechange="updateVolumeIcon()" |
| onloadeddata   | Data loaded          | onloadeddata="showContent()"        |
| onerror        | Loading error        | onerror="showErrorMessage()"        |

---

### DocumentEvents

- Document events:

| Event              | Description         | Example usage                                 |
| ------------------ | ------------------- | --------------------------------------------- |
| onload             | Page loaded         | onload="initializeApp()"                      |
| onunload           | Page unload         | onunload="cleanupResources()"                 |
| onbeforeunload     | Before leaving page | onbeforeunload="confirmExit(event)"           |
| onvisibilitychange | Visibility changed  | onvisibilitychange="handleVisibilityChange()" |

---

### ClipboardEvents

| Event   | Description | Example usage                       |
| ------- | ----------- | ----------------------------------- |
| oncopy  | Copy text   | oncopy="formatCopiedText(event)"    |
| oncut   | Cut text    | oncut="handleCut(event)"            |
| onpaste | Paste text  | onpaste="sanitizePastedText(event)" |

---

### AnimationEvents

| Event            | Description     | Example usage                          |
| ---------------- | --------------- | -------------------------------------- |
| onanimationstart | Animation start | onanimationstart="logAnimationStart()" |
| onanimationend   | Animation end   | onanimationend="enableInteraction()"   |
| ontransitionend  | Transition end  | ontransitionend="finalizeTransition()" |

---

### StorageEvents

| Event     | Description                    | Example usage                  |
| --------- | ------------------------------ | ------------------------------ |
| onstorage | Storage change (local/session) | onstorage="syncChanges(event)" |

---

### MessageEvents

| Event          | Description      | Example usage                              |
| -------------- | ---------------- | ------------------------------------------ |
| onmessage      | Message received | onmessage="handleMessage(event)"           |
| onmessageerror | Message error    | onmessageerror="handleMessageError(event)" |

---

### DragDropEvents

| Event  | Description | Example usage                |
| ------ | ----------- | ---------------------------- |
| ondrag | Dragging    | ondrag="updateDragUI(event)" |
| ondrop | Drop        | ondrop="processDrop(event)"  |

---

### GamepadEvents

| Event                 | Description          | Example usage                            |
| --------------------- | -------------------- | ---------------------------------------- |
| ongamepadconnected    | Gamepad connected    | ongamepadconnected="setupGamepad(event)" |
| ongamepaddisconnected | Gamepad disconnected | ongamepaddisconnected="cleanupGamepad()" |

---

### SensorEvents

| Event               | Description        | Example usage                                  |
| ------------------- | ------------------ | ---------------------------------------------- |
| ondevicemotion      | Device motion      | ondevicemotion="handleMotion(event)"           |
| ondeviceorientation | Device orientation | ondeviceorientation="handleOrientation(event)" |
| ondevicelight       | Light level change | ondevicelight="adjustBrightness(event)"        |
