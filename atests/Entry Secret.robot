*** Settings ***
Documentation       Check Entry related keywords

Library             Collections
Library             DateTime
Library             String
Library             KeePassLibrary

Test Setup          Open Keepass Database    ${KEEPASS_DATABASE}    ${KEEPASS_PASSWORD}    ${KEEPASS_KEYFILE}
Test Teardown       Close Keepass Database

Test Tags           entry   secret  requires_7.4
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


*** Keywords ***
Get Robot Version
    [Documentation]    Returns the current Robot Framework version
    ${version}=              Evaluate                robot.__version__
    RETURN                  ${version}

Get Robot Framework Has Secret
    [Documentation]    Returns the current Robot Framework Secret support
    ${version}=    Get Robot Version
    IF  '${version}' < '7.4'
        Log To Console  < 7.4 secret is NOT support
        RETURN  ${False}
    ELSE
        Log To Console  >= 7.4 secret is supported
        RETURN  ${True}
    END
