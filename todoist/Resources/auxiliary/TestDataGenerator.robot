*** Settings ***
Library    FakerLibrary

*** Variables ***
${TOKEN} =    d469ce54eca3a7ca5b6b5e7d4c8d51ced8d4c7b1


*** Keywords ***
Setup PROJECT_NAME test data
    ${data} =    Country
    Set Test Variable    ${PROJECT_NAME}    ${data}


Setup TASK_NAME test data
    ${data} =    Sentence
    Set Test Variable    ${TASK_NAME}    ${data}
