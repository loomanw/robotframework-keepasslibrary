*** Settings ***
Library          KeePassLibrary
Library          Collections    
Test Tags        Group
Documentation    Check Group related keywords
Test Setup       Open Keepass Database    ${KEEPASS_DATABASE}    ${KEEPASS_PASSWORD}    ${KEEPASS_KEYFILE}
Test Teardown    Close Keepass Database    

*** Variables ***
${DATADIR}             ${CURDIR}${/}Data${/}
${KEEPASS_DATABASE}    ${DATADIR}test4.kdbx
${KEEPASS_KEYFILE}     ${DATADIR}test4.key 
${KEEPASS_PASSWORD}    password 

*** Test Cases ***
Get Expires
    [Tags]    Set
    [Documentation]    Selected group contains expected expires
    ${group_name}=        Set Variable    foobar_group
    ${value_expected}=    Set Variable    ${FALSE}
    ${group}=    Get Groups By Name    ${group_name}    first=True     
    ${value}=    Get Group Expires    ${group}
    Should Be Equal    ${value_expected}    ${value}    

Get Expired
    [Tags]    Get
    [Documentation]    Selected group contains expected expired 
    ${group_name}=        Set Variable    foobar_group
    ${value_expected}=    Set Variable    False
    ${group}=    Get Groups By Name    ${group_name}    first=True     
    ${value}=    Get Group Expired    ${group} 
    Should Be Equal As Strings    ${value_expected}    ${value}  

Get Entries
    [Tags]    Get
    [Documentation]    Selected group contains expected entries
    ${group_name}=         Set Variable    foobar_group
    @{values_expected}=    Create List    group_entry    foobar_entry
    @{values}=             Create List
    ${group}=      Get Groups By Name    ${group_name}    first=True     
    @{entries}=    Get Group Entries    ${group} 
    FOR  ${entry}  IN  @{entries}
       ${title}=    Get Entry Title    ${entry}
       Append To List    ${values}    ${title}    
    END  
    Lists Should Be Equal    ${values_expected}    ${values}
   
Get Icon
    [Tags]    Get
    [Documentation]    Selected group contains expected icon
    ${group_name}=        Set Variable    foobar_group
    ${value_expected}=    Set Variable    1
    ${group}=    Get Groups By Name    ${group_name}    first=True     
    ${value}=    Get Group Icon    ${group} 
    Should Be Equal As Integers    ${value_expected}    ${value} 

Get Is Root Group
    [Tags]    Get
    [Documentation]    Selected group contains expected root group flag
    ${group_name}=        Set Variable    foobar_group
    ${value_expected}=    Set Variable    False
    ${group}=    Get Groups By Name    ${group_name}    first=True     
    ${value}=    Get Group Is Root Group    ${group}
    Should Be Equal As Strings    ${value_expected}    ${value}    

Get Name
    [Tags]    Get
    [Documentation]    Selected group contains expected rname
    ${group_uuid}=        Set Variable    95155a32-5317-a10f-d4e4-d0c2030264b6
    ${value_expected}=    Set Variable    foobar_group
    ${group}=    Get Groups By Uuid    ${group_uuid}    first=True     
    ${value}=    Get Group Name    ${group}
    Should Be Equal As Strings    ${value_expected}    ${value}    

Get Notes
    [Tags]    Get
    [Documentation]    Selected group contains expected uuid
    ${group_name}=        Set Variable    foobar_group
    ${value_expected}=    Set Variable    group notes
    ${group}=    Get Groups By Name    ${group_name}    first=True     
    ${value}=    Get Group Notes    ${group}
    Should Be Equal As Strings    ${value_expected}    ${value}

Get Parent Group
    [Tags]    Get
    [Documentation]    Selected group contains expected parent group
    ${group_name}=        Set Variable    subgroup
    ${value_expected}=    Set Variable    foobar_group
    ${group}=    Get Groups By Name    ${group_name}    first=True
    ${parent}=    Get Group Parent    ${group}     
    ${value}=    Get Group Name    ${parent} 
    Should Be Equal As Strings    ${value_expected}    ${value}  

Get Path
    [Tags]    Get
    [Documentation]    Selected group contains expected path
    ${group_name}=        Set Variable    subgroup
    ${value_expected}=    Set Variable    foobar_group/subgroup
    ${group}=    Get Groups By Name    ${group_name}    first=True     
    ${value}=    Get Group Path    ${group}
    Should Be Equal As Strings    ${value_expected}    ${value}  

Get Subgroups
    [Tags]    Get
    [Documentation]    Selected group contains expected subgroups
    ${group_name}=         Set Variable    foobar_group
    @{values_expected}=    Create List     subgroup
    @{values}=             Create List
    ${group}=        Get Groups By Name    ${group_name}    first=True     
    @{subgroups}=    Get Group Subgroups    ${group} 
    FOR  ${subgroup}  IN  @{subgroups}
       ${name}=    Get Group Name    ${subgroup}
       Append To List    ${values}    ${name}    
    END  
    Lists Should Be Equal    ${values_expected}    ${values}

Get Uuid
    [Tags]    Get
    [Documentation]    Selected group contains expected uuid
    ${group_name}=        Set Variable    foobar_group
    ${value_expected}=    Set Variable    95155a32-5317-a10f-d4e4-d0c2030264b6
    ${group}=    Get Groups By Name    ${group_name}    first=True     
    ${value}=    Get Group Uuid    ${group}
    Should Be Equal As Strings    ${value_expected}    ${value}    

Set Expires
    [Tags]    Set
    [Documentation]    Selected group expires can be set
    ${group_name}=        Set Variable    foobar_group
    ${value_expected}=    Set Variable    ${TRUE}
    ${group}=    Get Groups By Name    ${group_name}    first=True     
    Set Group Expires    ${group}    ${value_expected}
    ${value}=    Get Group Expires    ${group}
    Should Be Equal    ${value_expected}    ${value}    

Set Icon
    [Tags]    Set
    [Documentation]    Selected group notes can be set
    ${group_name}=        Set Variable    foobar_group
    ${value_expected}=    Set Variable    20
    ${group}=    Get Groups By Name    ${group_name}    first=True     
    Set Group Icon    ${group}    ${value_expected}
    ${value}=    Get Group Icon    ${group}
    Should Be Equal As Integers    ${value_expected}    ${value}    

Set Name
    [Tags]    Set
    [Documentation]    Selected group name can be set
    ${group_name}=        Set Variable    foobar_group
    ${value_expected}=    Set Variable    foobar_group_new
    ${group}=    Get Groups By Name    ${group_name}    first=True     
    Set Group Name    ${group}    ${value_expected}
    ${value}=    Get Group Name    ${group}
    Should Be Equal As Strings    ${value_expected}    ${value}    

Set Notes
    [Tags]    Set
    [Documentation]    Selected group notes can be set
    ${group_name}=        Set Variable    foobar_group
    ${value_expected}=    Set Variable    new_notes
    ${group}=    Get Groups By Name    ${group_name}    first=True     
    Set Group Notes    ${group}    ${value_expected}
    ${value}=    Get Group Notes    ${group}
    Should Be Equal As Strings    ${value_expected}    ${value}    
