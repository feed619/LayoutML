# HTMLEvents

`HTMLEvents` contains constant definitions for all HTML events, grouped by categories.
This module provides a convenient way to reference standard DOM events when working with the `HTMLElement` class.

---

## File Structure

The file contains 13 classes, each grouping events by interaction type:

- MouseEvents — mouse, pointer, and touch events
- KeyboardEvents — keyboard and text input events
- FormEvents — form and input element events
- MediaEvents — audio and video events
- DocumentEvents — document and browser window events
- ClipboardEvents — clipboard events
- AnimationEvents — CSS animations and transitions
- StorageEvents — Web Storage events
- MessageEvents — cross-window messaging events
- ResourceEvents — resource loading events
- DragDropEvents — Drag-and-Drop API events
- GamepadEvents — game controller events
- SensorEvents — device sensor events

---

# Full Event Reference

## MouseEvents

### Mouse Events

| Event         | Description                | Example                                |
| ------------- | -------------------------- | -------------------------------------- |
| onclick       | Mouse left click           | onclick="handleClick(event)"           |
| ondblclick    | Double click               | ondblclick="openDetails()"             |
| onmousedown   | Mouse button pressed       | onmousedown="startDrag(event)"         |
| onmouseup     | Mouse button released      | onmouseup="endDrag()"                  |
| onmousemove   | Mouse movement             | onmousemove="updateCoordinates(event)" |
| onmouseover   | Mouse enters element       | onmouseover="showTooltip()"            |
| onmouseout    | Mouse leaves element       | onmouseout="hideTooltip()"             |
| onmouseenter  | Mouse enters (no bubbling) | onmouseenter="highlight()"             |
| onmouseleave  | Mouse leaves (no bubbling) | onmouseleave="unhighlight()"           |
| oncontextmenu | Right click                | oncontextmenu="showContextMenu(event)" |
| onwheel       | Mouse wheel scroll         | onwheel="handleScroll(event)"          |
| onscroll      | Element scroll             | onscroll="updateScrollPosition()"      |

---

## Drag Events

| Event       | Description        | Example                                 |
| ----------- | ------------------ | --------------------------------------- |
| ondrag      | Element is dragged | ondrag="updateDragPosition(event)"      |
| ondragstart | Drag starts        | ondragstart="startDragOperation(event)" |
| ondragend   | Drag ends          | ondragend="cleanupDrag()"               |
| ondragenter | Enters drop zone   | ondragenter="showDropZone()"            |
| ondragleave | Leaves drop zone   | ondragleave="hideDropZone()"            |
| ondragover  | Drag over element  | ondragover="preventDefault(event)"      |
| ondrop      | Drop event         | ondrop="handleDrop(event)"              |

---

## Pointer Events (Modern)

| Event                | Description            | Example                                    |
| -------------------- | ---------------------- | ------------------------------------------ |
| onpointerdown        | Pointer pressed        | onpointerdown="handlePointerDown(event)"   |
| onpointerup          | Pointer released       | onpointerup="handlePointerUp(event)"       |
| onpointermove        | Pointer movement       | onpointermove="trackPointer(event)"        |
| onpointerover        | Pointer enters element | onpointerover="activateElement()"          |
| onpointerout         | Pointer leaves element | onpointerout="deactivateElement()"         |
| onpointerenter       | Pointer enters         | onpointerenter="enterElement()"            |
| onpointerleave       | Pointer leaves         | onpointerleave="leaveElement()"            |
| onpointercancel      | Pointer cancelled      | onpointercancel="cleanupPointer()"         |
| ongotpointercapture  | Pointer captured       | ongotpointercapture="handleCapture()"      |
| onlostpointercapture | Pointer lost capture   | onlostpointercapture="handleLostCapture()" |

---

## Touch Events

| Event         | Description     | Example                                |
| ------------- | --------------- | -------------------------------------- |
| ontouchstart  | Touch start     | ontouchstart="handleTouchStart(event)" |
| ontouchend    | Touch end       | ontouchend="handleTouchEnd(event)"     |
| ontouchmove   | Touch move      | ontouchmove="handleTouchMove(event)"   |
| ontouchcancel | Touch cancelled | ontouchcancel="handleTouchCancel()"    |

---

# KeyboardEvents

## Keyboard Input

| Event      | Description            | Example                            |
| ---------- | ---------------------- | ---------------------------------- |
| onkeydown  | Key pressed            | onkeydown="handleKeyDown(event)"   |
| onkeyup    | Key released           | onkeyup="handleKeyUp(event)"       |
| onkeypress | Key press (deprecated) | onkeypress="handleKeyPress(event)" |

---

## Text Input

| Event               | Description           | Example                                |
| ------------------- | --------------------- | -------------------------------------- |
| oninput             | Input changed         | oninput="validateInput(event)"         |
| onbeforeinput       | Before input changes  | onbeforeinput="preprocessInput(event)" |
| oncompositionstart  | IME composition start | oncompositionstart="startIME()"        |
| oncompositionupdate | IME update            | oncompositionupdate="updateIME()"      |
| oncompositionend    | IME end               | oncompositionend="endIME()"            |

---

# FormEvents

## Form Events

| Event     | Description       | Example                           |
| --------- | ----------------- | --------------------------------- |
| onsubmit  | Form submitted    | onsubmit="validateForm(event)"    |
| onreset   | Form reset        | onreset="confirmReset()"          |
| onchange  | Value changed     | onchange="updateSelection()"      |
| onselect  | Text selected     | onselect="highlightSelection()"   |
| oninvalid | Validation failed | oninvalid="showValidationError()" |

---

## Focus Events

| Event      | Description         | Example                     |
| ---------- | ------------------- | --------------------------- |
| onfocus    | Element focused     | onfocus="highlightField()"  |
| onblur     | Element lost focus  | onblur="validateField()"    |
| onfocusin  | Focus in (bubbles)  | onfocusin="prepareField()"  |
| onfocusout | Focus out (bubbles) | onfocusout="cleanupField()" |

---

## Other Form Events

| Event         | Description  | Example                              |
| ------------- | ------------ | ------------------------------------ |
| onsearch      | Search input | onsearch="performSearch(event)"      |
| onbeforecut   | Before cut   | onbeforecut="preventCut(event)"      |
| onbeforecopy  | Before copy  | onbeforecopy="preventCopy(event)"    |
| onbeforepaste | Before paste | onbeforepaste="validatePaste(event)" |

---

# MediaEvents

| Event          | Description      | Example                             |
| -------------- | ---------------- | ----------------------------------- |
| onplay         | Playback started | onplay="startPlaybackTimer()"       |
| onpause        | Playback paused  | onpause="updatePlayButton()"        |
| onended        | Playback ended   | onended="playNext()"                |
| ontimeupdate   | Time updated     | ontimeupdate="updateTimeDisplay()"  |
| onvolumechange | Volume changed   | onvolumechange="updateVolumeIcon()" |
| onloadeddata   | Data loaded      | onloadeddata="showContent()"        |
| onerror        | Load error       | onerror="showErrorMessage()"        |

---

# DocumentEvents

| Event              | Description        | Example                                       |
| ------------------ | ------------------ | --------------------------------------------- |
| onload             | Page loaded        | onload="initializeApp()"                      |
| onunload           | Page unloading     | onunload="cleanupResources()"                 |
| onbeforeunload     | Before unload      | onbeforeunload="confirmExit(event)"           |
| onpageshow         | Page shown         | onpageshow="restoreState()"                   |
| onpagehide         | Page hidden        | onpagehide="saveState()"                      |
| onvisibilitychange | Visibility changed | onvisibilitychange="handleVisibilityChange()" |

---

# ClipboardEvents

| Event   | Description | Example                             |
| ------- | ----------- | ----------------------------------- |
| oncopy  | Copy        | oncopy="formatCopiedText(event)"    |
| oncut   | Cut         | oncut="handleCut(event)"            |
| onpaste | Paste       | onpaste="sanitizePastedText(event)" |

---

# AnimationEvents

| Event                | Description         | Example                                |
| -------------------- | ------------------- | -------------------------------------- |
| onanimationstart     | Animation start     | onanimationstart="logAnimationStart()" |
| onanimationend       | Animation end       | onanimationend="enableInteraction()"   |
| onanimationiteration | Animation iteration | onanimationiteration="updateCounter()" |
| onanimationcancel    | Animation cancel    | onanimationcancel="cleanupAnimation()" |

---

## Transition Events

| Event              | Description       | Example                                  |
| ------------------ | ----------------- | ---------------------------------------- |
| ontransitionstart  | Transition start  | ontransitionstart="measureStart()"       |
| ontransitionend    | Transition end    | ontransitionend="finalizeTransition()"   |
| ontransitionrun    | Transition run    | ontransitionrun="prepareTransition()"    |
| ontransitioncancel | Transition cancel | ontransitioncancel="cleanupTransition()" |

---

# StorageEvents

| Event     | Description     | Example                        |
| --------- | --------------- | ------------------------------ |
| onstorage | Storage changed | onstorage="syncChanges(event)" |

---

# MessageEvents

| Event          | Description      | Example                                    |
| -------------- | ---------------- | ------------------------------------------ |
| onmessage      | Message received | onmessage="handleMessage(event)"           |
| onmessageerror | Message error    | onmessageerror="handleMessageError(event)" |

---

# ResourceEvents

| Event       | Description      | Example                            |
| ----------- | ---------------- | ---------------------------------- |
| onload      | Resource loaded  | onload="useResource()"             |
| onerror     | Load error       | onerror="loadFallback()"           |
| onprogress  | Loading progress | onprogress="updateProgress(event)" |
| onabort     | Load aborted     | onabort="handleAbort()"            |
| onloadstart | Load started     | onloadstart="showLoader()"         |
| onloadend   | Load ended       | onloadend="cleanupLoader()"        |
| ontimeout   | Timeout          | ontimeout="handleTimeout()"        |

---

# DragDropEvents

| Event       | Description     | Example                             |
| ----------- | --------------- | ----------------------------------- |
| ondrag      | Dragging        | ondrag="updateDragUI(event)"        |
| ondragstart | Drag start      | ondragstart="setupDragData(event)"  |
| ondragend   | Drag end        | ondragend="cleanupDrag()"           |
| ondragenter | Enter drop zone | ondragenter="highlightDropZone()"   |
| ondragleave | Leave drop zone | ondragleave="unhighlightDropZone()" |
| ondragover  | Over drop zone  | ondragover="allowDrop(event)"       |
| ondrop      | Drop            | ondrop="processDrop(event)"         |

---

# GamepadEvents

| Event                 | Description          | Example                                  |
| --------------------- | -------------------- | ---------------------------------------- |
| ongamepadconnected    | Gamepad connected    | ongamepadconnected="setupGamepad(event)" |
| ongamepaddisconnected | Gamepad disconnected | ongamepaddisconnected="cleanupGamepad()" |

---

# SensorEvents

| Event               | Description        | Example                                        |
| ------------------- | ------------------ | ---------------------------------------------- |
| ondevicemotion      | Device motion      | ondevicemotion="handleMotion(event)"           |
| ondeviceorientation | Device orientation | ondeviceorientation="handleOrientation(event)" |
| ondeviceproximity   | Proximity change   | ondeviceproximity="handleProximity(event)"     |
| onuserproximity     | User proximity     | onuserproximity="handleUserPresence(event)"    |

---
