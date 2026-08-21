*** Settings ***
Library    Browser

*** Test Cases ***
Verify OrangeHRM Login Page
    New Browser    chromium    headless=false
    New Page    https://opensource-demo.orangehrmlive.com/
    Get Text    h5    ==    Login
    Close Browser

        