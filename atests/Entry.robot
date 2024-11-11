*** Settings ***
Documentation       Check Entry related keywords

Library             KeePassLibrary
Library             Collections

Test Setup          Open Keepass Database    ${KEEPASS_DATABASE}    ${KEEPASS_PASSWORD}    ${KEEPASS_KEYFILE}
Test Teardown       Close Keepass Database

Test Tags           entry


*** Variables ***
${DATADIR}              ${CURDIR}${/}Data${/}
${KEEPASS_DATABASE}     ${DATADIR}test4.kdbx
${KEEPASS_KEYFILE}      ${DATADIR}test4.key
${KEEPASS_PASSWORD}     password


*** Test Cases ***
Get Custom Properties
    [Documentation]    Selected entry contains expected custom properties.
    [Tags]    get
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Create Dictionary    foobar_attribute=foobar
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${value}=    Get Entry Custom Properties    ${entry}
    Dictionaries Should Be Equal    ${value_expected}    ${value}

Get Custom Property
    [Documentation]    Selected entry contains expected custom property
    [Tags]    get
    ${entry_title}=    Set Variable    root_entry
    ${entry_property_key}=    Set Variable    foobar_attribute
    ${value_expected}=    Set Variable    foobar
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${value}=    Get Entry Custom Property    ${entry}    ${entry_property_key}
    Should Be Equal As Strings    ${value_expected}    ${value}

Get Expired
    [Documentation]    Selected entry contains expected expired
    [Tags]    get
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    False
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${value}=    Get Entry Expired    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}

Get Expires
    [Documentation]    Selected entry contains expected expires
    [Tags]    get
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    False
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${value}=    Get Entry Expires    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}

Get Icon
    [Documentation]    Selected entry contains expected icon
    [Tags]    get
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    0
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${value}=    Get Entry Icon    ${entry}
    Should Be Equal As Integers    ${value_expected}    ${value}

Get Notes
    [Documentation]    Selected entry contains expected icon
    [Tags]    get
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    root entry notes
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${value}=    Get Entry Notes    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}

Get Pasword
    [Documentation]    Selected entry contains expected password
    [Tags]    get
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    passw0rd
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${value}=    Get Entry Password    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}

Get Tags
    [Documentation]    Selected entry contains expected tags
    [Tags]    get
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Create List
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${value}=    Get Entry Tags    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}

Get Title
    [Documentation]    Selected entry contains expected title
    [Tags]    get
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    ${entry_title}
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${value}=    Get Entry Title    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}

Get URL
    [Documentation]    Selected entry contains expected URL
    [Tags]    get
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    http://example.com
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${value}=    Get Entry Url    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}

Get Username
    [Documentation]    Selected entry contains expected username
    [Tags]    get
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    foobar_user
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${value}=    Get Entry Username    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}

Get Uuid
    [Documentation]    Selected entry contains expected uuid
    [Tags]    get
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    eb90914e-5dd3-8f78-9669-dd1fb39791dc
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${value}=    Get Entry Uuid    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}

Set Custom Property Existing
    [Documentation]    Selected entry custom porperty (existing) can be set with a string
    [Tags]    set
    ${entry_title}=    Set Variable    root_entry
    ${custom_property_key}=    Set Variable    foobar_attribute
    ${value_expected}=    Set Variable    new_value
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    Set Entry Custom Property    ${entry}    ${custom_property_key}    ${value_expected}
    ${value}=    Get Entry Custom Property    ${entry}    ${custom_property_key}
    Should Be Equal    ${value_expected}    ${value}

Set Custom Property New
    [Documentation]    Selected entry custom porperty (new) can be set with a string
    [Tags]    set
    ${entry_title}=    Set Variable    root_entry
    ${custom_property_key}=    Set Variable    new_key
    ${value_expected}=    Set Variable    new_value
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    Set Entry Custom Property    ${entry}    ${custom_property_key}    ${value_expected}
    ${value}=    Get Entry Custom Property    ${entry}    ${custom_property_key}
    Should Be Equal    ${value_expected}    ${value}

Set Expires
    [Documentation]    Selected entry expires can be set with a boolean
    [Tags]    set
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    ${TRUE}
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    Set Entry Expires    ${entry}    ${value_expected}
    ${value}=    Get Entry Expires    ${entry}
    Should Be Equal    ${value_expected}    ${value}

Set Icon
    [Documentation]    Selected entry icon can be set with a integer
    [Tags]    set
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    10
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    Set Entry Icon    ${entry}    ${value_expected}
    ${value}=    Get Entry Icon    ${entry}
    Should Be Equal As Integers    ${value_expected}    ${value}

Set Notes
    [Documentation]    Selected entry notes can be set with a string
    [Tags]    set
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    very important\nnotes\nfor this entry
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    Set Entry Notes    ${entry}    ${value_expected}
    ${value}=    Get Entry Notes    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}

Set Password
    [Documentation]    Selected entry passowrd can be set with a string
    [Tags]    set
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    P@$$w0rd
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    Set Entry Password    ${entry}    ${value_expected}
    ${value}=    Get Entry Password    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}

Set Tags With List
    [Documentation]    Selected entry tags can be set with a list
    [Tags]    set
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Create List    tag1    tag2
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    Set Entry Tags    ${entry}    ${value_expected}
    ${value}=    Get Entry Tags    ${entry}
    Lists Should Be Equal    ${value_expected}    ${value}

Set Tags With String
    [Documentation]    Selected entry tags can be set with a string
    [Tags]    set
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    tag1;tag2
    ${list_expected}=    Create List    tag1    tag2
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    Set Entry Tags    ${entry}    ${value_expected}
    ${value}=    Get Entry Tags    ${entry}
    Lists Should Be Equal    ${list_expected}    ${value}

Set Title
    [Documentation]    Selected entry title can be set with a string
    [Tags]    set
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    new title
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    Set Entry Title    ${entry}    ${value_expected}
    ${value}=    Get Entry Title    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}

Set URL
    [Documentation]    Selected entry url can be set with a string
    [Tags]    set
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    http://pypi.org
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    Set Entry Url    ${entry}    ${value_expected}
    ${value}=    Get Entry Url    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}

Set Username
    [Documentation]    Selected entry username can be set with a string
    [Tags]    set
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    set_foobar_user
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    Set Entry Username    ${entry}    ${value_expected}
    ${value}=    Get Entry Username    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}
