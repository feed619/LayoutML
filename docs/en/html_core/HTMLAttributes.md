# HTMLAttributes

`HTMLAttributes` contains constant definitions for all HTML attributes, grouped by value type. This is a utility module used by the `HTMLElement` class and its subclasses.

---

## File Structure

### ValueAttributes class

Attributes that require explicit values using the format `attribute="value"`.

---

## ValueAttributes (Attributes with values)

| Attribute      | Description                | Example                                                      |
| -------------- | -------------------------- | ------------------------------------------------------------ |
| id             | Unique element identifier  | `HTMLElement(id_="main-header")`                             |
| name           | Name for forms and scripts | `HTMLElement(name="username")`                               |
| title          | Tooltip text               | `HTMLElement(title="Click for details")`                     |
| lang           | Content language           | `HTMLElement(lang="ru")`                                     |
| dir            | Text direction             | `HTMLElement(dir="ltr")`                                     |
| translate      | Enable/disable translation | `HTMLElement(translate="no")`                                |
| class          | CSS class string           | `HTMLElement(class_="btn btn-primary")`                      |
| style          | Inline styles              | `HTMLElement(style="color: red; font-size: 14px;")`          |
| href           | Hyperlink                  | `HTMLElement(href="/page.html")`                             |
| src            | Media source               | `HTMLElement(src="image.jpg")`                               |
| srcset         | Responsive image sources   | `HTMLElement(srcset="img-320w.jpg 320w, img-640w.jpg 640w")` |
| sizes          | Image sizing rules         | `HTMLElement(sizes="(max-width: 600px) 100vw, 50vw")`        |
| poster         | Video poster image         | `HTMLElement(poster="video.jpg")`                            |
| action         | Form submission URL        | `HTMLElement(action="/submit")`                              |
| formaction     | Alternative form action    | `HTMLElement(formaction="/save")`                            |
| width          | Element width              | `HTMLElement(width="300")`                                   |
| height         | Element height             | `HTMLElement(height="200")`                                  |
| size           | Input size                 | `HTMLElement(size="20")`                                     |
| value          | Element value              | `HTMLElement(value="default")`                               |
| placeholder    | Input placeholder          | `HTMLElement(placeholder="Enter name")`                      |
| pattern        | Validation pattern         | `HTMLElement(pattern="[A-Za-z]{3,}")`                        |
| min            | Minimum value              | `HTMLElement(min="0")`                                       |
| max            | Maximum value              | `HTMLElement(max="100")`                                     |
| step           | Step value                 | `HTMLElement(step="0.1")`                                    |
| maxlength      | Max text length            | `HTMLElement(maxlength="50")`                                |
| minlength      | Min text length            | `HTMLElement(minlength="3")`                                 |
| charset        | Character encoding         | `HTMLElement(charset="UTF-8")`                               |
| content        | Meta content               | `HTMLElement(content="width=device-width")`                  |
| http-equiv     | HTTP equivalent            | `HTMLElement(http-equiv="refresh")`                          |
| property       | Open Graph property        | `HTMLElement(property="og:title")`                           |
| colspan        | Column span                | `HTMLElement(colspan="2")`                                   |
| rowspan        | Row span                   | `HTMLElement(rowspan="3")`                                   |
| headers        | Associated headers         | `HTMLElement(headers="col1 col2")`                           |
| scope          | Table scope                | `HTMLElement(scope="col")`                                   |
| start          | List start value           | `HTMLElement(start="10")`                                    |
| list           | datalist reference         | `HTMLElement(list="browsers")`                               |
| form           | Associated form            | `HTMLElement(form="myForm")`                                 |
| srcdoc         | iframe HTML content        | `HTMLElement(srcdoc="<p>hello</p>")`                         |
| sandbox        | iframe restrictions        | `HTMLElement(sandbox="allow-scripts")`                       |
| allow          | iframe permissions         | `HTMLElement(allow="camera; microphone")`                    |
| preload        | Media preload mode         | `HTMLElement(preload="metadata")`                            |
| crossorigin    | CORS policy                | `HTMLElement(crossorigin="anonymous")`                       |
| usemap         | Image map reference        | `HTMLElement(usemap="#map")`                                 |
| accept         | Accepted file types        | `HTMLElement(accept=".pdf,.doc,image/*")`                    |
| integrity      | Subresource integrity      | `HTMLElement(integrity="sha256-...")`                        |
| nonce          | CSP nonce                  | `HTMLElement(nonce="abc123")`                                |
| accesskey      | Shortcut key               | `HTMLElement(accesskey="s")`                                 |
| tabindex       | Tab order                  | `HTMLElement(tabindex="1")`                                  |
| inputmode      | Input keyboard mode        | `HTMLElement(inputmode="numeric")`                           |
| enterkeyhint   | Enter key hint             | `HTMLElement(enterkeyhint="search")`                         |
| referrerpolicy | Referrer policy            | `HTMLElement(referrerpolicy="no-referrer")`                  |

---

## BooleanAttributes class

Boolean attributes are attributes where presence means `True`, and absence means `False`.

They are passed via `boolean_attributes`.

---

## BooleanAttributes (Boolean attributes)

| Attribute       | Description                    | Example                                               |
| --------------- | ------------------------------ | ----------------------------------------------------- |
| hidden          | Hide element                   | `HTMLElement(boolean_attributes=["hidden"])`          |
| inert           | Ignore element                 | `HTMLElement(boolean_attributes=["inert"])`           |
| required        | Required field                 | `HTMLElement(boolean_attributes=["required"])`        |
| disabled        | Disabled element               | `HTMLElement(boolean_attributes=["disabled"])`        |
| readonly        | Read-only field                | `HTMLElement(boolean_attributes=["readonly"])`        |
| checked         | Checked checkbox/radio         | `HTMLElement(boolean_attributes=["checked"])`         |
| selected        | Selected option                | `HTMLElement(boolean_attributes=["selected"])`        |
| multiple        | Multiple selection             | `HTMLElement(boolean_attributes=["multiple"])`        |
| autofocus       | Auto focus                     | `HTMLElement(boolean_attributes=["autofocus"])`       |
| formnovalidate  | Skip form validation           | `HTMLElement(boolean_attributes=["formnovalidate"])`  |
| controls        | Media controls                 | `HTMLElement(boolean_attributes=["controls"])`        |
| autoplay        | Auto play media                | `HTMLElement(boolean_attributes=["autoplay"])`        |
| loop            | Loop media                     | `HTMLElement(boolean_attributes=["loop"])`            |
| muted           | Mute media                     | `HTMLElement(boolean_attributes=["muted"])`           |
| playsinline     | Inline playback                | `HTMLElement(boolean_attributes=["playsinline"])`     |
| ismap           | Server-side image map          | `HTMLElement(boolean_attributes=["ismap"])`           |
| reversed        | Reverse list                   | `HTMLElement(boolean_attributes=["reversed"])`        |
| open            | Open state (details/accordion) | `HTMLElement(boolean_attributes=["open"])`            |
| contenteditable | Editable content               | `HTMLElement(boolean_attributes=["contenteditable"])` |
| draggable       | Draggable element              | `HTMLElement(boolean_attributes=["draggable"])`       |
| spellcheck      | Spell checking                 | `HTMLElement(boolean_attributes=["spellcheck"])`      |
| allowfullscreen | Fullscreen allowed             | `HTMLElement(boolean_attributes=["allowfullscreen"])` |
| async           | Async script loading           | `HTMLElement(boolean_attributes=["async"])`           |
| defer           | Deferred script loading        | `HTMLElement(boolean_attributes=["defer"])`           |
| scoped          | Scoped styles                  | `HTMLElement(boolean_attributes=["scoped"])`          |
| popover         | Popover element                | `HTMLElement(boolean_attributes=["popover"])`         |
| nowrap          | No text wrapping               | `HTMLElement(boolean_attributes=["nowrap"])`          |
| noshade         | No shadow (hr)                 | `HTMLElement(boolean_attributes=["noshade"])`         |
| noresize        | Disable resizing               | `HTMLElement(boolean_attributes=["noresize"])`        |
