*** Settings ***
Library          KeePassLibrary
library          String      
Documentation    Requires Robot Framework Version 3.1 Check if valid composed key combinations work 
Test Template    Loading Database With Valid Credentials Should Succeed 

*** Variable ***
${KP_DB_BASE}=        ${CURDIR}${/}Data${/}

*** Test Cases ***              DATABASE                    PASSWORD    KEY_FILE           
KDBX v3 KeyFile And Password    test3.kdbx                  password    test3.key
KDBX v4 KeyFile And Password    test4.kdbx                  password    test4.key
KDBX v4 Only Keyfile            test4_only_keyfile.kdbx     ${NONE}     test4.key
KDBX v4 Only Password           test4_only_password.kdbx    password    ${NONE}

*** Keywords ***
Loading Database With Valid Credentials Should Succeed    
    [Arguments]    ${DATABASE}    ${PASSWORD}    ${KEY_FILE}
    [Documentation]    Load and close a KeePass database with provided credentials 
    ${DATABASE}=           Set Variable If    "${DATABASE}" == "${NONE}"    ${DATABASE}    ${KP_DB_BASE}${DATABASE}
    ${KEY_FILE}=           Set Variable If    "${KEY_FILE}" == "${NONE}"    ${KEY_FILE}    ${KP_DB_BASE}${KEY_FILE}
    Open Keepass Database    ${DATABASE}    ${PASSWORD}    ${KEY_FILE}
    Close Keepass Database   
