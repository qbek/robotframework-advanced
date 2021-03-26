*** Settings ***
Library    SeleniumLibrary


*** Test Cases ***
Browser test
    Open browser    http://google.com
    Sleep    5s
    Close browser