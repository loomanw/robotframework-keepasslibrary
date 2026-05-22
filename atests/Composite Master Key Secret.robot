*** Settings ***
Documentation       Check valid composed key combinations using Robot Framework Secret variable

Library             String
Library             KeePassLibrary

Test Template       Loading Database With Valid Credentials Should Succeed

Test Tags           database   secret  requires_7.4
Variables           secret_variables.py
Resource            ${CURDIR}${/}Resources${/}Robot_utils.resource


*** Variables ***
${KP_DB_BASE}=      ${CURDIR}${/}Data${/}


*** Test Cases ***                  DATABASE                                PASSWORD          KEY_FILE
KDBX v3 KeyFile And Password        test3.kdbx                              ${DB_PASSWORD}    test3.key
KDBX v4 KeyFile And Password        test4.kdbx                              ${DB_PASSWORD}    test4.key
KDBX v4 Only Password               test4_only_password.kdbx                ${DB_PASSWORD}    ${NONE}
KDBX v4 Keyfile v2 And Password     test4_v2_keyfile_and_password.kdbx      ${DB_PASSWORD}    test4_v2.keyx


*** Keywords ***
Loading Database With Valid Credentials Should Succeed
    [Documentation]    Load and close a KeePass database with provided credentials
    [Arguments]    ${DATABASE}    ${PASSWORD}    ${KEY_FILE}
    ${support_secret}=    Get Robot Framework Has Secret
    Skip If   not ${support_secret}
    ${DATABASE}=    Set Variable If    "${DATABASE}" == "${NONE}"    ${DATABASE}    ${KP_DB_BASE}${DATABASE}
    ${KEY_FILE}=    Set Variable If    "${KEY_FILE}" == "${NONE}"    ${KEY_FILE}    ${KP_DB_BASE}${KEY_FILE}
    Open Keepass Database    ${DATABASE}    ${PASSWORD}    ${KEY_FILE}
    Close Keepass Database
