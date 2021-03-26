*** Settings ***
Library     lib/restapi.py

*** Keywords ***
Create project
    [Arguments]    ${name}
    Create project with name    ${name}


Check if project is created
    [Arguments]    ${name}
    ${actual} =    Check if project was created with name    ${name}
    Should Match    ${actual}    ${name}

Select project
    [Arguments]     ${name}
    Log    not implemented

Create task with name
    [Arguments]   ${name}
    Log    not implemented
