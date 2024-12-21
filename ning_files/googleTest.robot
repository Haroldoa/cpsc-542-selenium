*** Settings ***
Library    SeleniumLibrary 
*** Test Cases ***
MyFirstTest
    Log    Hello World!!!    
    
FirstSeleniumTest
    Open Browser    https:google.com    chrome
    Set Browser Implicit Wait    10
    Input Text    name=q    Hello World 
    Sleep   8     
    Press Keys    name=q    ENTER 
    # Click Button    name=btnK     
    Sleep    8    
    Close Browser
    Log    Test1 Completed
