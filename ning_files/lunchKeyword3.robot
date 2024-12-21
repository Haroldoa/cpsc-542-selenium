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
Go To Orders
    Click My Lunch
    Sleep   3s
    Click My Order History
    Sleep   3s
    Expand Date
    Sleep   3s
    Price Should Not Be Empty
    Product Name Should Not Be Empty

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

Click My Lunch
    Click Element       //*[contains(text(),'My Lunch')]

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

Click My Order History
    Click Element       //*[contains(text(),'My Order History')]

Expand Date
    Click Element      //*[contains(@class, 'o_group_name')]

Price Should Not Be Empty
    ${price}=    Get Text    xpath=//span[@name="price"]
    Should Not Be Empty    ${price}

Product Name Should Not Be Empty
    ${product}=    Get Text    xpath=//td[@name="product_id"]
    Should Not Be Empty    ${product}

Welcome Page Should Be Open
    Title Should Be    Odoo - Discuss
