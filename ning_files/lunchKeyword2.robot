*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}      http://localhost:8069/web/login/
${BROWSER}        Chrome

*** Test Cases ***
Get to Lunch App
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
Order and get confirmation
    Click Meal
    Sleep   3s
    Click Add To Cart
    Sleep   3s
    Click Order
    Sleep   3s
    Page Should Contain    Your order
Navigate to Manager
    Click Manager
    Sleep    3s
    Click Control Vendors
    Sleep    3s
    Expand Orders From Restaurant
    Sleep    3s
    Page Should Contain    Status
    Page Should Contain    Ordered
    Sleep    3s
    Click Confirm Order
    Sleep    3s

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

Click Meal
    Click Element       //*[contains(text(),'The Country')]

Click Save
    Click Element       //*[contains(text(),'Save')]

Click Add To Cart
    Click Element       //*[contains(text(),'Add To Cart')]

Click Manager
    Click Element       //*[contains(text(),'Manager')]

Click Control Vendors
    Click Element       //*[contains(text(),'Control Vendors')]

Expand Orders from Restaurant
    Click Element       //*[contains(text(),'Coin gourmand')]

Click Confirm Order
    Click Element       //*[contains(text(),'Confirm')]

Welcome Page Should Be Open
    Title Should Be    Odoo - Discuss
