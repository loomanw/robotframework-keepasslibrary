*** Setting ***
Library          KeePassLibrary
Library          Collections        
Force Tags       Entry
Documentation    Check Entry related keywords
Test Setup       Open Keepass Database    ${KEEPASS_DATABASE}    ${KEEPASS_PASSWORD}    ${KEEPASS_KEYFILE}
Test Teardown    Close Keepass Database    

*** Variable ***
${DATADIR}             ${CURDIR}${/}Data${/}
${KEEPASS_DATABASE}    ${DATADIR}test4.kdbx
${KEEPASS_KEYFILE}     ${DATADIR}test4.key 
${KEEPASS_PASSWORD}    password

*** Test Cases ***
Get Custom Properties
    [Tags]    Get
    [Documentation]    Selected entry contains expected custom properties.
    ${entry_title}=       Set Variable    root_entry
    ${value_expected}=    Create Dictionary    foobar_attribute=foobar               
    ${entry}=    Get Entries By Title    ${entry_title}    first=True     
    ${value}=    Get Entry Custom Properties    ${entry}
    Dictionaries Should Be Equal    ${value_expected}    ${value} 

Get Custom Property
    [Tags]    Get
    [Documentation]    Selected entry contains expected custom property
    ${entry_title}=           Set Variable    root_entry
    ${entry_property_key}=    Set Variable    foobar_attribute
    ${value_expected}=        Set Variable    foobar
    ${entry}=    Get Entries By Title    ${entry_title}    first=True     
    ${value}=    Get Entry Custom Property    ${entry}    ${entry_property_key}
    Should Be Equal As Strings    ${value_expected}    ${value}    

Get Expired
    [Tags]    Get
    [Documentation]    Selected entry contains expected expired 
    ${entry_title}=       Set Variable    root_entry
    ${value_expected}=    Set Variable    False
    ${entry}=    Get Entries By Title    ${entry_title}    first=True     
    ${value}=    Get Entry Expired    ${entry} 
    Should Be Equal As Strings    ${value_expected}    ${value}    

Get Expires
    [Tags]    Get
    [Documentation]    Selected entry contains expected expires
    ${entry_title}=       Set Variable    root_entry
    ${value_expected}=    Set Variable    False
    ${entry}=    Get Entries By Title    ${entry_title}    first=True     
    ${value}=    Get Entry Expires    ${entry} 
    Should Be Equal As Strings    ${value_expected}    ${value} 
    
Get Icon
    [Tags]    Get
    [Documentation]    Selected entry contains expected icon
    ${entry_title}=       Set Variable    root_entry
    ${value_expected}=    Set Variable    0
    ${entry}=    Get Entries By Title    ${entry_title}    first=True     
    ${value}=    Get Entry Icon    ${entry} 
    Should Be Equal As Integers    ${value_expected}    ${value} 

Get Notes
    [Tags]    Get
    [Documentation]    Selected entry contains expected icon
    ${entry_title}=       Set Variable    root_entry
    ${value_expected}=    Set Variable    root entry notes
    ${entry}=    Get Entries By Title    ${entry_title}    first=True      
    ${value}=    Get Entry Notes    ${entry} 
    Should Be Equal As Strings    ${value_expected}    ${value} 
    
Get Pasword
    [Tags]    Get
    [Documentation]    Selected entry contains expected password
    ${entry_title}=       Set Variable    root_entry
    ${value_expected}=    Set Variable    passw0rd
    ${entry}=    Get Entries By Title    ${entry_title}    first=True     
    ${value}=    Get Entry Password    ${entry} 
    Should Be Equal As Strings    ${value_expected}    ${value}     

Get Tags
    [Tags]    Get
    [Documentation]    Selected entry contains expected tags
    ${entry_title}=       Set Variable    root_entry
    ${value_expected}=    Set Variable    ${NONE}
    ${entry}=    Get Entries By Title    ${entry_title}    first=True     
    ${value}=    Get Entry Tags    ${entry} 
    Should Be Equal As Strings    ${value_expected}    ${value} 

Get Title
    [Tags]    Get
    [Documentation]    Selected entry contains expected title
    ${entry_title}=       Set Variable    root_entry
    ${value_expected}=    Set Variable    ${entry_title}
    ${entry}=    Get Entries By Title    ${entry_title}    first=True     
    ${value}=    Get Entry Title    ${entry} 
    Should Be Equal As Strings    ${value_expected}    ${value}       

Get URL
    [Tags]    Get
    [Documentation]    Selected entry contains expected URL
    ${entry_title}=       Set Variable    root_entry
    ${value_expected}=    Set Variable    http://example.com
    ${entry}=    Get Entries By Title    ${entry_title}    first=True     
    ${value}=    Get Entry Url    ${entry} 
    Should Be Equal As Strings    ${value_expected}    ${value}       

Get Username
    [Tags]    Get
    [Documentation]    Selected entry contains expected username
    ${entry_title}=           Set Variable    root_entry
    ${value_expected}=        Set Variable    foobar_user
    ${entry}=    Get Entries By Title    ${entry_title}    first=True     
    ${value}=    Get Entry Username    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}    
    
Get Uuid
    [Tags]    Get
    [Documentation]    Selected entry contains expected uuid
    ${entry_title}=           Set Variable    root_entry
    ${value_expected}=        Set Variable    eb90914e-5dd3-8f78-9669-dd1fb39791dc
    ${entry}=    Get Entries By Title    ${entry_title}    first=True     
    ${value}=    Get Entry Uuid    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}    

Set Custom Property Existing
    [Tags]    Set
    [Documentation]    Selected entry custom porperty (existing) can be set with a string
    ${entry_title}=            Set Variable    root_entry
    ${custom_property_key}=    Set Variable    foobar_attribute
    ${value_expected}=         Set Variable    new_value
    ${entry}=    Get Entries By Title    ${entry_title}    first=True          
    Set Entry Custom Property    ${entry}    ${custom_property_key}    ${value_expected}
    ${value}=    Get Entry Custom Property    ${entry}    ${custom_property_key}
    Should Be Equal    ${value_expected}    ${value} 
         
Set Custom Property New
    [Tags]    Set
    [Documentation]    Selected entry custom porperty (new) can be set with a string
    ${entry_title}=            Set Variable    root_entry
    ${custom_property_key}=    Set Variable    new_key
    ${value_expected}=         Set Variable    new_value
    ${entry}=    Get Entries By Title    ${entry_title}    first=True          
    Set Entry Custom Property    ${entry}    ${custom_property_key}    ${value_expected}
    ${value}=    Get Entry Custom Property    ${entry}    ${custom_property_key}
    Should Be Equal    ${value_expected}    ${value} 

Set Expires
    [Tags]    Set
    [Documentation]    Selected entry expires can be set with a boolean
    ${entry_title}=       Set Variable    root_entry
    ${value_expected}=    Set Variable    ${TRUE}
    ${entry}=    Get Entries By Title    ${entry_title}    first=True          
    Set Entry Expires    ${entry}    ${value_expected}
    ${value}=    Get Entry Expires    ${entry}
    Should Be Equal    ${value_expected}    ${value} 

Set Icon
    [Tags]    Set
    [Documentation]    Selected entry icon can be set with a integer
    ${entry_title}=       Set Variable    root_entry
    ${value_expected}=    Set Variable    10
    ${entry}=    Get Entries By Title    ${entry_title}    first=True          
    Set Entry Icon    ${entry}    ${value_expected}
    ${value}=    Get Entry Icon    ${entry}
    Should Be Equal As Integers    ${value_expected}    ${value} 

Set Notes
    [Tags]    Set
    [Documentation]    Selected entry notes can be set with a string
    ${entry_title}=       Set Variable    root_entry
    ${value_expected}=    Set Variable    very important\nnotes\nfor this entry
    ${entry}=    Get Entries By Title    ${entry_title}    first=True          
    Set Entry Notes    ${entry}    ${value_expected}
    ${value}=    Get Entry Notes    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value} 

Set Password
    [Tags]    Set
    [Documentation]    Selected entry passowrd can be set with a string
    ${entry_title}=       Set Variable    root_entry
    ${value_expected}=    Set Variable    P@$$w0rd
    ${entry}=    Get Entries By Title    ${entry_title}    first=True          
    Set Entry Password    ${entry}    ${value_expected}
    ${value}=    Get Entry Password    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value} 

Set Tags With List
    [Tags]    Set
    [Documentation]    Selected entry tags can be set with a list
    ${entry_title}=       Set Variable    root_entry
    ${value_expected}=    Create List     tag1    tag2
    ${entry}=    Get Entries By Title    ${entry_title}    first=True     
    Set Entry Tags    ${entry}    ${value_expected}    
    ${value}=    Get Entry Tags    ${entry} 
    Lists Should Be Equal    ${value_expected}    ${value}

Set Tags With String
    [Tags]    Set
    [Documentation]    Selected entry tags can be set with a string
    ${entry_title}=       Set Variable    root_entry
    ${value_expected}=    Set Variable    tag1;tag2
    ${list_expected}=     Create List     tag1    tag2
    ${entry}=    Get Entries By Title    ${entry_title}    first=True     
    Set Entry Tags    ${entry}    ${value_expected}    
    ${value}=    Get Entry Tags    ${entry} 
    Lists Should Be Equal    ${list_expected}    ${value}    
    
Set Title
    [Tags]    Set
    [Documentation]    Selected entry title can be set with a string
    ${entry_title}=       Set Variable    root_entry
    ${value_expected}=    Set Variable    new title
    ${entry}=    Get Entries By Title    ${entry_title}    first=True          
    Set Entry Title    ${entry}    ${value_expected}
    ${value}=    Get Entry Title    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value} 

Set URL
    [Tags]    Set
    [Documentation]    Selected entry url can be set with a string
    ${entry_title}=       Set Variable    root_entry
    ${value_expected}=    Set Variable    http://pypi.org
    ${entry}=    Get Entries By Title    ${entry_title}    first=True          
    Set Entry Url    ${entry}    ${value_expected}
    ${value}=    Get Entry Url    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value} 
    
Set Username
    [Documentation]    Selected entry username can be set with a string
    ${entry_title}=       Set Variable    root_entry
    ${value_expected}=    Set Variable    set_foobar_user
    ${entry}=    Get Entries By Title    ${entry_title}    first=True          
    Set Entry Username    ${entry}    ${value_expected}
    ${value}=    Get Entry Username    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value} 
