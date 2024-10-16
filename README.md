# cpsc-542-selenium


## Group Project:

**Part A: Python Unit Testing on Odoo v15 modules (om_hospital and fleet).
Part B: Client-side Selenium Testing of Odoo v15 modules.**

For full details on project setup and submission, please refer to the full syllabus.

**Q. What is the group project?**
A. The group project has two parts:
Part A: The Python unit testing of Odoo version 15, module om_hospital and module fleet
Part B: The client-side Selenium testing of Odoo version 15, module om_hospital and module fleet
**Q. How do we install Odoo version 15?**
A. Your group may want to read several tutorials:
https://linuxhint.com/install-odoo-15-ubuntu-22-04/
https://linuxize.com/post/how-to-install-odoo-15-on-ubuntu-20-04/
https://www.rosehosting.com/blog/how-to-install-odoo-15-on-ubuntu-20-04/

https://www.candidroot.com/blog/our-candidroot-blog-1/post/how-to-install-odoo-15-in-ubuntu-18-04-lts-93
**Q. Do we have to use ubuntu?**
A. I use ubuntu 22.04 LTS and highly recommend ubuntu (version 20.04 LTS or 22.04 LTS) or other Linux versions. If your group decides to use Windows OS, I am fine with it.
**Q. Where to find the free Odoo 3rd party module om_hospital?**
A. https://apps.odoo.com/apps/modules/15.0/om_hospital/
**Q. Where to find the Odoo SA module fleet?**
A. It comes with Odoo 15 source code.
**Q. How many unit tests should we develop?**
A. You need to develop at least 5 unit test cases for the module om_hospital and 5 unit test cases for the module fleet.
**Q. Where do we start?**
A. I think you need to play Odoo first.
**Q. How do I play?**
A. If you prefer, you can set up a trial account (free, no credit card) at https://www.odoo.com/trial
You can play the fleet module (Odoo calls it fleet app). You won’t find the om_hospital module there (since it is a 3rd party module).
**Q. How do I start Part A (Python unit testing)?**
A. To run python unit testing, you need to have an Odoo development system (no way to get around it). Your group needs to install the Odoo 15 (open source, community version) on your computer. It is a bit tedious but achievable.
**Q. Can I read some Odoo testing documentation?**
A. Please read https://www.odoo.com/documentation/15.0/developer/reference/backend/testing.html#testing-js-code
**Q. I visited the link and found three kinds of tests (Python unit tests, JS unit tests and Tours/Integration Testing). Do I need to do all three kinds?**
A. No. We only do the Python unit tests (maybe, if more people want, we can add Part C of the group project to cover the other two kinds).
**Q. Any odoo python unit testing example?**
A. It is not that hard. Most Odoo SA modules (if not all) come with unit test cases. You may want to study them a bit. How to run test cases is explained in the link

[https://www.odoo.com/documentation/15.0/developer/reference/backend/testing.html#testing-js-code]()
**Q. How about Part B (The client-side Selenium testing)?**
A. Your group needs to write five test programs/test cases (in Python if possible) that test the targeted site (Odoo) via a browser.
**Q. Any starting point?**
A. There are many good Selenium tutorials on the Internet. Maybe you want to read this one:
https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test
**Q. Since Selenium supports other languages, may I use another language (not Python)?**
A. Other languages are acceptable too.
**Q. Do I have to use Odoo as the targeted system (system under test)?**
A. Yes.
**Q. Five Selenium test cases?**
A. Yes. Please note that one of them needs to be the testing of the Odoo login. Also, you need to have at least two test negative cases (you found a bug). You may want to purposely add some programming bugs in your odoo module om_hospital and fleet source code (you have access to all source code) to demonstrate your negative cases.
**Q. Still not that clear! Can you give an example of those five Selenium test cases?**
A. One example is
Test case 1: Odoo login (you need to log into Odoo to do other tests anyway)
Test case 2: a positive test case of om_hospital (the feature you want to check is fine)
Test case 3: a negative test case of om_hosptial (modify om_hospital source code in some way to create a programming bug)
Test case 4: a positive test case of fleet
Test case 5: a negative test case of fleet (modify fleet source code in some way to create a programming bug)
**Q. It is possible to place five test Selenium test cases in one python file. Can I do that?**
A. Sure.
**Q. I don't want to place all test cases in one file. May I break those into several files and have some kind of manager program as the front end?**
A. It is a more professional approach – I agree. BTW, this is optional.
**Q. What should I submit for the group project?**
A. For the group project, each group, via the group coordinator, needs to submit one copy of the following:
Part A: Unit Testing - five files: pdf, ppt, and mp3 (mp4 is fine), demo mp4, source code file (zip)

**Part B: Client-Side Testing (Selenium)** – five files: pdf, ppt, and mp3 (mp4 is fine), demo mp4, source code file (zip)
where
ppt, mp3(mp4 if you prefer) is a 20 minutes presentation of Part A/B
pdf is a report of Part A/B (title page, introduction, whatever sections you see fit, conclusion, references)
zip contains all your test code
demo mp4 proves that your test cases are all successful (or do catch bugs).
