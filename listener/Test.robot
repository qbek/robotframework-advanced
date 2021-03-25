*** Settings ***
Resource    resource.robot


*** Test Cases ***
Simple test to debug
    Log To Console    message to Log
    Set Test Variable    ${test_var}    test init
    User defined keyword
    Set Test Variable    ${test_var}   test end
