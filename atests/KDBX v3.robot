*** Settings ***
Library          KeePassLibrary
library          String        
Force Tags       Database    KDBX v3
Test Template    Opening database with valid credentials should succeed
Documentation    Requires Robot Framework Version 3.1 Check KDBX 3 related keywords

*** Variables ***
${KP_DB_BASE}=    ${CURDIR}${/}Data${/}

*** Test Cases ***                    DATABASE               PASSWORD    TRANSFORMED_KEY    KEY_FILE         ENCRYPTION_ALGORITHM    KDF_ALGORITHM    VERSION     
KDBX v3                               test3.kdbx             password    ${NONE}            test3.key        aes256                  aeskdf           (3, 1)

*** Keywords ***
Opening database with valid credentials should succeed    
    [Arguments]    ${DATABASE}    ${PASSWORD}    ${TRANSFORMED_KEY}    ${KEY_FILE}    ${ENCRYPTION_ALGORITHM}    ${KDF_ALGORITHM}    ${VERSION} 
    [Documentation]    Opens the given database with the supplied authentications 
    #Convert string to bytes
    ${BYTES_KEY}=          Convert To Bytes    M\xb7\x08\xf6\xa7\xd1v\xb1{&\x06\x8f\xae\xe9\r\xeb\x9a\x1b\x02b\xce\xf2\x8aR\xaea)7\x1fs\xe9\xc0 
    ${TRANSFORMED_KEY}=    Set Variable If    "${KEY_FILE}" == "${NONE}"    ${BYTES_KEY}    ${TRANSFORMED_KEY}       
    ${DATABASE}=           Set Variable If    "${DATABASE}" == "${NONE}"    ${DATABASE}    ${KP_DB_BASE}${DATABASE}
    ${KEY_FILE}=           Set Variable If    "${KEY_FILE}" == "${NONE}"    ${KEY_FILE}    ${KP_DB_BASE}${KEY_FILE}
    Open Keepass Database    ${DATABASE}    ${PASSWORD}    ${KEY_FILE}    ${TRANSFORMED_KEY}
    Encryption Algorithm should be equal    ${ENCRYPTION_ALGORITHM}
    KDF Algorithm should be equal           ${KDF_ALGORITHM}
    Version should be equal                 ${VERSION}
    Close Keepass Database   

Encryption Algorithm Should Be Equal
    [Arguments]    ${ENCRYPTION_ALGORITHM}
    [Documentation]    Verifies if the open database matches the given algorithm
    Set Tags    Encryption Algorithm    Encryption Algorithm ${ENCRYPTION_ALGORITHM}    
    ${res}=    Get Encryption Algorithm    
    Should Be Equal As Strings    ${ENCRYPTION_ALGORITHM}    ${res} 
    
KDF Algorithm Should Be Equal
    [Arguments]    ${KDF_ALGORITHM}
    [Documentation]    Verifies if the open database matches the given algorithm
    Set Tags    KDF Algorithm    KDF Algorithm ${KDF_ALGORITHM}
    ${res}=    Get KDF Algorithm    
    Should Be Equal As Strings    ${KDF_ALGORITHM}    ${res} 

Version Should Be Equal
    [Arguments]    ${VERSION}
    [Documentation]    Verifies if the open database matches the given version
    ${res}=    Get Version    
    Should Be Equal As Strings    ${VERSION}    ${res}
