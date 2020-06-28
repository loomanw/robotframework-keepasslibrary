*** Comments ***
Requires Robot Framework Version 3.1  
Check if valid composed combinations work
                    
*** Settings ***
Library    KeePassLibrary
library    String      
Test Template    Opening database with with valid credentials should succeed 

*** Variable ***
${KP_DB_BASE}=        ${CURDIR}${/}data${/}

*** Test Cases ***              DATABASE                    PASSWORD    KEY_FILE           
KDBX v3 KeyFile And Password    test3.kdbx                  password    test3.key
KDBX v4 KeyFile And Password    test4.kdbx                  password    test4.key
KDBX v4 Only Keyfile            test4_only_keyfile.kdbx     ${NONE}     test4.key
KDBX v4 Only Password           test4_only_password.kdbx    password    ${NONE}

*** Keywords ***
Opening database with with valid credentials should succeed    
    [Arguments]    ${DATABASE}    ${PASSWORD}    ${KEY_FILE} 
    ${DATABASE}=           Set Variable If    "${DATABASE}" == "${NONE}"    ${DATABASE}    ${KP_DB_BASE}${DATABASE}
    ${KEY_FILE}=           Set Variable If    "${KEY_FILE}" == "${NONE}"    ${KEY_FILE}    ${KP_DB_BASE}${KEY_FILE}
    #Convert string to bytes    
    Load Database    ${DATABASE}    ${PASSWORD}    ${KEY_FILE}
    Close Database   
