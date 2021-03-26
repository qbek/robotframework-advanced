*** Settings ***
Library    Dialogs
Library    WebServer.py    test-nginx


*** Test Cases ***
Modify file
    Start container
    Execute Manual Step    check
    Modify file
    Restart container
    Execute Manual Step    check
    Stop container
