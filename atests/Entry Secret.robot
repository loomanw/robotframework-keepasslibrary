*** Settings ***
Documentation       Check Entry related keywords

Library             Collections
Library             DateTime
Library             String
Library             KeePassLibrary

Test Setup          Open Keepass Database    ${KEEPASS_DATABASE}    ${KEEPASS_PASSWORD}    ${KEEPASS_KEYFILE}
Test Teardown       Close Keepass Database

Test Tags           entry   secret  requires_7.4
Resource            ${CURDIR}${/}Resources${/}Robot_utils.resource
Variables           secret_variables.py


*** Variables ***
${DATADIR}              ${CURDIR}${/}Data${/}
${KEEPASS_DATABASE}     ${DATADIR}test4.kdbx
${KEEPASS_KEYFILE}      ${DATADIR}test4.key
${KEEPASS_PASSWORD}     password


*** Test Cases ***
Get Password As Secret, fails no secret support
    [Documentation]    Get password as secret fails with Robot Framework 7.3 or prior.
    [Tags]    get
    ${expected_error}=    Set Variable    Secret type requires Robot Framework 7.4 or later.
    ${support_secret}=    Get Robot Framework Has Secret
    Skip If   ${support_secret}
    ${entry_title}=    Set Variable    root_entry
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    Run Keyword And Expect Error    ${expected_error}    Get Entry Password    ${entry}    secret=${True}

Set Password With String
    [Documentation]    Selected entry password can be set with a string and retrieved as as secret, not recommended.
    [Tags]    set
    ${support_secret}=    Get Robot Framework Has Secret
    Skip If   not ${support_secret}
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable   P@$$w0rd
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    Set Entry Password    ${entry}    ${value_expected}
    ${value}=    Get Entry Password    ${entry}    secret=${True}
    Should Be Equal As Strings    <secret>    ${value}
    Should Be Equal As Strings    ${value_expected}    ${value.value}

Set Password With Secret
    [Documentation]    Selected entry password can be set with a secret
    [Tags]    set
    ${support_secret}=    Get Robot Framework Has Secret
    Skip If   not ${support_secret}
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    ${NEW_PASSWORD_AS_SECRET}
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    Set Entry Password    ${entry}    ${value_expected}
    ${value}=    Get Entry Password    ${entry}    secret=${True}
    Should Be Equal As Strings    ${value_expected}    ${value}
    Should Be Equal As Strings    ${value_expected.value}    ${value.value}

Get Password As Secret
    [Documentation]    Selected entry contains expected password
    [Tags]    get
    ${support_secret}=    Get Robot Framework Has Secret
    Skip If   not ${support_secret}
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    ${PASSWORD_AS_SECRET}
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${value}=    Get Entry Password    ${entry}    secret=${True}
    Should Be Equal As Strings    ${value_expected}    ${value}
    Should Be Equal As Strings    ${value_expected.value}    ${value.value}

Entry Can Be Created With Secret Password
    [Documentation]    Validate existense of newly created group
    [Tags]    create    set
    ${support_secret}=    Get Robot Framework Has Secret
    Skip If   not ${support_secret}
    ${value_expected}=    Set Variable    ${NEW_PASSWORD_AS_SECRET}
    ${root_group}=   Get Root Group
    ${new_entry}=    Add Entry   ${root_group}    title    username    ${value_expected}
    ${value}=    Get Entry Password    ${new_entry}    secret=${True}
    Should Be Equal As Strings    ${value_expected}    ${value}
    Should Be Equal As Strings    ${value_expected.value}    ${value.value}
