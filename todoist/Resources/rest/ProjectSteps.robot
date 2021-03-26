*** Settings ***
Library     lib/restapi.py   ${TOKEN}

*** Keywords ***
Create project
    [Arguments]    ${name}
    Create project with name    ${name}


Check if project is created
    [Arguments]    ${name}
    Check if project was created with name    ${name}

Select project
    [Arguments]     ${name}
    Log    not implemented

Create task with name
    [Arguments]   ${name}
    Log    not implemented
