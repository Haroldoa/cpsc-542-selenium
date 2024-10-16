
# Software as a Service – Architecture and Implementation Module  
**Selenium Testing**  
*By Ning Chen, Ph.D., Professor, Department of Computer Science, California State University Fullerton*  
© Ning Chen 2022

---

## Module Objectives

- Use Selenium Python driver
- Play the role of a software tester
- Perform integration testing (or client-side end-to-end testing)

---

## Selenium Python Driver

### What do we want?

- Write a Python program that automatically operates the browser.

### Why?

- It is a cost issue (we don’t want to hire someone to manually operate the browser for testing).

### How?

- Use the Selenium driver (library) in your Python code.

---

## Selenium Python Driver Setup

- **Download** the Selenium driver from:  
  [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
- **Important**: Ensure your Chrome and Selenium driver versions match.

---

## Steps to Perform Testing

- **Download** `SeleniumLibrary.py` from the class website.
- **Approach**:  
  - Play  
  - Observe  
  - Imitate  
  - Innovate
- Review the MP4 lecture.
- Play the role of a tester or SDET (QA team member).

---

## Locating Web Page Elements in Selenium

You can locate elements using:

- `By.ID`
- `By.NAME`
- `By.Xpath`
- `By.LINK_TEXT`
- `By.CLASS_NAME`
- `By.CSS_SELECTOR`

Reference:  
[https://selenium-python.readthedocs.io/locating-elements.html](https://selenium-python.readthedocs.io/locating-elements.html)

---

### My Closing Thoughts

- Locating web page elements can be tedious and tricky.
- If you can't locate, you can't operate.
- Dynamic or inconsistent locations can be particularly tricky.
- The complexity of end-to-end testing opens career opportunities in Software Quality Assurance (SQA).

