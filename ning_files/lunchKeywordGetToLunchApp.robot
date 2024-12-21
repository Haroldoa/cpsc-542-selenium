*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}      http://localhost:8069/web/login/
${BROWSER}        Chrome

*** Test Cases ***
Valid Login
    Open Browser To Login Page
    Sleep   3s
    Input Username    haroldoalt@gmail.com
    Sleep   3s
    Input Password    openpgpwd
    Submit Credentials
    Sleep   3s
    Welcome Page Should Be Open
    Sleep   3s
    Click Menu
    Sleep   3s
    Click Lunch
    Sleep   3s
    [Teardown]    Close Browser

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Title Should Be    Login | My Website

Input Username
    [Arguments]    ${username}
    Input Text    login    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    password    ${password}

Submit Credentials
    Click Element       //*[contains(text(),'Log in')]

Click Menu
    Click Element       xpath=//button[@title="Home Menu"]

Click Lunch
    Click Element       //*[contains(text(),'Lunch')]

Welcome Page Should Be Open
    Title Should Be    Odoo - Discuss
