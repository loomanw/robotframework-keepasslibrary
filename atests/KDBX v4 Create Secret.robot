*** Settings ***
Documentation       Check KDBX 3 related keywords

Library             String
Library             KeePassLibrary

Test Template       Creating Database With Valid Credentials Should Succeed

Test Tags           database    kdbx_v4   secret  requires_7.4
Variables           secret_variables.py
Resource            ${CURDIR}${/}Resources${/}Robot_utils.resource


*** Variables ***
${KP_DB_BASE}=      ${CURDIR}${/}Data${/}


*** Test Cases ***    DATABASE          PASSWORD          KEY_FILE     ENCRYPTION_ALGORITHM    KDF_ALGORITHM       VERSION    ROOT_GROUP_NAME   # robocop: off=LEN08
KDBX v4               test4_reg.kdbx    ${DB_PASSWORD}    test4.key    aes256                  argon2              (4, 0)     Root              # robocop: off=LEN08


*** Keywords ***
Creating Database With Valid Credentials Should Succeed
    [Documentation]    Opens the given database with the supplied authentications
    [Arguments]    ${DATABASE}  # robocop: off=LEN07
    ...            ${PASSWORD}
    ...            ${KEY_FILE}
    ...            ${ENCRYPTION_ALGORITHM}
    ...            ${KDF_ALGORITHM}
    ...            ${VERSION}
    ...            ${ROOT_GROUP_NAME}
    ${support_secret}=    Get Robot Framework Has Secret
    Skip If   not ${support_secret}
    ${DATABASE}=    Set Variable If    "${DATABASE}" == "${NONE}"    ${DATABASE}    ${KP_DB_BASE}${DATABASE}
    ${KEY_FILE}=    Set Variable If    "${KEY_FILE}" == "${NONE}"    ${KEY_FILE}    ${KP_DB_BASE}${KEY_FILE}
    Create Keepass Database    ${DATABASE}    ${PASSWORD}    ${KEY_FILE}
    Encryption Algorithm Should Be Equal    ${ENCRYPTION_ALGORITHM}
    KDF Algorithm Should Be Equal    ${KDF_ALGORITHM}
    Version Should Be Equal    ${VERSION}
    Root Group Should Be Equal    ${ROOT_GROUP_NAME}
    Close Keepass Database

Encryption Algorithm Should Be Equal
    [Documentation]    Verifies if the open database matches the given algorithm
    [Arguments]    ${ENCRYPTION_ALGORITHM}
    Set Tags    Encryption Algorithm    Encryption Algorithm ${ENCRYPTION_ALGORITHM}
    ${res}=    Get Encryption Algorithm
    Should Be Equal As Strings    ${ENCRYPTION_ALGORITHM}    ${res}

KDF Algorithm Should Be Equal
    [Documentation]    Verifies if the open database matches the given algorithm
    [Arguments]    ${KDF_ALGORITHM}
    Set Tags    KDF Algorithm    KDF Algorithm ${KDF_ALGORITHM}
    ${res}=    Get KDF Algorithm
    Should Be Equal As Strings    ${KDF_ALGORITHM}    ${res}

Version Should Be Equal
    [Documentation]    Verifies if the open database matches the given version
    [Arguments]    ${VERSION}
    ${res}=    Get Version
    Should Be Equal As Strings    ${VERSION}    ${res}

Root Group Should Be Equal
    [Documentation]    Verifies if the open database matches the given version
    [Arguments]    ${ROOT_GROUP_NAME}
    ${res}=    Get Root Group
    ${res_name}=    Get Group Name    ${res}
    Should Be Equal As Strings    ${ROOT_GROUP_NAME}    ${res_name}
