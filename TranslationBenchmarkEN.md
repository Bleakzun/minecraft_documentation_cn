
## Translation Standards

This page is a guide to the rules for translating documents within this github, the current version of which was prepared by L.C.M. Wither.

### 1. Title translation

* **Multi-level headings:**
    * **Principle:** Prioritise translations to preserve the integrity of the message.
    * **Original text:** Generally, the translated title should be followed by the original title in parentheses, e.g., `简介 (Introduction)`; the original text should not be appended to the translated terminology if it has a more homogeneous meaning or if it refers to an object that is not a proprietary attribute, e.g., `Components` subheadings of any structure should not be left untranslated and should not be accompanied by the original title in parentheses.
    * **Exception:** For titles that are too technical or specialised, consideration may be given to retaining the original text with a Chinese translation in full brackets, e.g., `Client Entity Documentation（客户端实体文档）`.
* **Example: **

```html
<h2><p id="Conditions">Conditions（条件）</p></h2>
<h3><p id="Components">组件</p></h3>
```

### 2. Parameters Translation

* **Principle:** Same principle as title translation, priority translation to maintain information integrity.
* **Original text:** Translated parameter names are followed by the original parameter name in parentheses, e.g., `--名称 (—name)`.
* **Special case:** For parameter names that are too technical or specialised, consider retaining the original text and attaching the Chinese translation in parentheses, e.g.: `--registered-id (注册 ID)`.

### 3. Grammatical requirements and terminology specifications

* **Consistency:** Terms, phrases and sentence structures should be consistent to avoid ambiguity or confusion.
* **Accuracy:** Ensure that the translation accurately conveys the meaning of the original text and avoid translation errors or bias.
* **Professionalism:** Use professional and standardised computer terminology and expressions.
* **Conciseness:** Use clear and concise language, avoiding lengthy or complex sentence structures; use sensible and rigorous phrasing, avoiding the use of colloquialisms such as `这个`, `那个`.
* **Conservativeness:** If you encounter difficult-to-translate terms in your translation, you may give possible translations and include the original text in parentheses after the translated term.

* **Examples:**
    * **Original text:** `The application programming interface (API) allows developers to access the functionality of the service.` bb
    * **Translation:** `应用程序接口 (API) 允许开发者访问该服务的功能。`

### 4. Use of spaces


* **Example:**
    * **Correct:** `这是一个示例 (This is an example)。`
    * **Error:** `这是一个示例(This is an example)。`
* **Exception:** Special cases can be made without spaces, e.g. `https://example.com`.

### 5. Use of punctuation

* **Principle:** Follow the custom of Chinese punctuation, full-width punctuation is used for Chinese text, half-width punctuation is used for English text and code.

* **Examples:**
    * **Chinese:** `你好，世界！`
    * **English:** `Hello, world!`
    * **Code:** ``print(‘Hello, world!’);`

### 7. Other recommendations

* **Glossary:** Create a glossary to standardise the translation of commonly used terms and ensure consistency in translation.
* **Proofreading:** After the translation is completed, conduct a comprehensive proofreading to check whether there are any errors or omissions.
* **Feedback:** Collect user feedback to continuously improve translation quality.

### 8. Writing style

* **Reference:** Keep the language simple, accurate and objective.
* **Tone:** Use a neutral tone and avoid subjective or exaggerated descriptions.
### 9. Translation Tools

* **Auxiliary Tools:** Auxiliary tools such as Machine Translation Engine (MTE) can be used to improve translation efficiency and consistency.
* **Human Proofreading:** Regardless of the tools used, human proofreading is required to ensure the quality of the translation.

### 10. Continuous Improvement

* **Update:** Update the Chinese translation in time with the update of Microsoft's code usage documentation.
* **Maintenance:** Regularly maintain and update the glossary to ensure translation quality.

