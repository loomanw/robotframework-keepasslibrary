*** Setting ***
Library          KeePassLibrary
Library          Collections    
Force Tags       Entries
Documentation    Requires Robot Framework Version 3.1 Check if Entries selecion keywords
Test Setup       Open Keepass Database    ${KEEPASS_DATABASE}    ${KEEPASS_PASSWORD}    ${KEEPASS_KEYFILE}
Test Teardown    Close Keepass Database    

*** Variable ***
${DATADIR}             ${CURDIR}${/}Data${/}
${KEEPASS_DATABASE}    ${DATADIR}test4.kdbx
${KEEPASS_KEYFILE}     ${DATADIR}test4.key 
${KEEPASS_PASSWORD}    password 

*** Test Cases ***
Selected By Arguments Are Found
    [Documentation]    Retrieved entries by arguments should match name list
    @{values_expected}=    Create List    root_entry    group_entry   
    @{values}=     Create List
    @{entries}=    Get Entries    title=.*entry    username=.*user    notes=.*entry notes    regex=True
    FOR  ${entry}  IN  @{entries}
       ${title}=    Get Entry Title    ${entry}
       Append To List    ${values}    ${title}    
    END
    Lists Should Be Equal    ${values_expected}    ${values}    

Selected By All Are Found
    [Documentation]    Retrieved entries should match title list
    @{values_expected}=    Create List    root_entry    foobar_entry    testing_new    quote test -> " <-    group_entry    foobar_entry    subentry    subentry2    Тест            
    @{values}=     Create List              
    @{entries}=    Get Entries All           
    FOR  ${entry}  IN  @{entries}
       ${title}=    Get Entry Title    ${entry}
       List Should Contain Value    ${values_expected}    ${title}    
    END

Selected By Notes Are Found    
    [Documentation]    Retrieved entries by notes should match title list
    @{values_expected}=    Create List    root_entry    group_entry
    @{values}=    Create List              
    @{entries} =       Get Entries By Notes    notes           
    FOR  ${entry}  IN  @{entries}
       ${title}=    Get Entry Title    ${entry}     
       List Should Contain Value    ${values_expected}    ${title}     
    END

Selected By Password Are Found    
    [Documentation]    Retrieved entries by passowrd should match uuid list
    @{values_expected}=    Create List    eb90914e-5dd3-8f78-9669-dd1fb39791dc    cc5f7ecd-2a00-48ca-9621-c222a347b0bb
    @{values}=     Create List              
    @{entries}=    Get Entries By Password    passw0rd          
    FOR  ${entry}  IN  @{entries}
       ${uuid}=    Get Entry Uuid    ${entry}
       Append To List    ${values}    ${uuid}    
    END
    Lists Should Be Equal    ${values_expected}    ${values} 

Selected By Path Are Found    
    [Documentation]    Retrieved entries by path should match uuid list
    ...    Note, only 1 entry can be selected by path
    ${value_expected}=    Set Variable        cc5f7ecd-2a00-48ca-9621-c222a347b0bb
    @{values}=    Create List              
    ${entry} =    Get Entries By Path    foobar_group/group_entry         
    ${uuid}=      Get Entry Uuid    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${uuid}   

Selected By String Are Found    
    [Documentation]    Retrieved entries by string should match uuid list
    @{values_expected}=    Create List    eb90914e-5dd3-8f78-9669-dd1fb39791dc
    &{string}=    Create Dictionary    Password=passw0rd    Title=root_entry
    @{values}=    Create List 
    @{entries} =       Get Entries By String    ${string}          
    FOR  ${entry}  IN  @{entries}
       ${uuid}=    Get Entry Uuid    ${entry}
       Append To List    ${values}    ${uuid}    
    END
    Lists Should Be Equal    ${values_expected}    ${values}     

Selected By Title Are Found    
    [Documentation]    Retrieved entries by title should match uuid list
    @{values_expected}=    Create List    5060e2e0-29aa-11e8-8aa8-0021ccb990c2    5da63f9a-29aa-11e8-8aa8-0021ccb990c2    6a7f0742-29aa-11e8-8aa8-0021ccb990c2
    @{values}=     Create List              
    @{entries}=    Get Entries By Title    foobar_entry          
    FOR  ${entry}  IN  @{entries}
       ${uuid}=    Get Entry Uuid    ${entry}
       Append To List    ${values}    ${uuid}    
    END
    Lists Should Be Equal    ${values_expected}    ${values} 

Selected By Url Are Found    
    [Documentation]    Retrieved entries by username should match title list
    @{values_expected}=    Create List    root_entry    group_entry
    @{values}=     Create List              
    @{entries}=    Get Entries By Url    http://example.com          
    FOR  ${entry}  IN  @{entries}
       ${title}=    Get Entry Title    ${entry}
       Append To List    ${values}    ${title}    
    END
    Lists Should Be Equal    ${values_expected}    ${values} 

Selected By Username Are Found
    [Documentation]    Retrieved entries by username should match uuid list
    @{values_expected}=    Create List    eb90914e-5dd3-8f78-9669-dd1fb39791dc    cc5f7ecd-2a00-48ca-9621-c222a347b0bb
    @{values}=     Create List              
    @{entries}=    Get Entries By Username    foobar_user           
    FOR  ${entry}  IN  @{entries}
       ${uuid}=    Get Entry Uuid    ${entry}
       Append To List    ${values}    ${uuid}    
    END
    Lists Should Be Equal    ${values_expected}    ${values}    
    
Selected By Username Are Found First
    [Documentation]    Retrieved first entry by username should match uuid
    ${value_expected}=    Set Variable        eb90914e-5dd3-8f78-9669-dd1fb39791dc
    ${entry} =       Get Entries By Username    foobar_user    first=True     
    ${uuid}=    Get Entry Uuid    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${uuid}    

Selected By Username Are Found Using RegEx Ignore Case 
    [Documentation]    Retrieved first entry by username should match uuid
    @{values_expected}=    Create List    eb90914e-5dd3-8f78-9669-dd1fb39791dc    cc5f7ecd-2a00-48ca-9621-c222a347b0bb
    @{values}=     Create List
    @{entries} =       Get Entries By Username    foobar_User    regex=True    flags=i      
    FOR  ${entry}  IN  @{entries}
       ${uuid}=    Get Entry Uuid    ${entry}
       Append To List    ${values}    ${uuid}    
    END
    Lists Should Be Equal    ${values_expected}    ${values} 
    
Selected By Uuid Are Found 
    [Documentation]    Retrieved entries by uuid should match title list
    @{values_expected}=    Create List    foobar_entry
    @{values}=     Create List              
    @{entries}=    Get Entries By Uuid    5da63f9a-29aa-11e8-8aa8-0021ccb990c2        
    FOR  ${entry}  IN  @{entries}
       ${title}=    Get Entry Title    ${entry}
       Append To List    ${values}    ${title}    
    END
    Lists Should Be Equal    ${values_expected}    ${values}    
 