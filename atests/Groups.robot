*** Setting ***
Library          KeePassLibrary
Library          Collections    
Force Tags       Groups
Documentation    Check Group selection related keywords
Test Setup       Open Keepass Database    ${KEEPASS_DATABASE}    ${KEEPASS_PASSWORD}    ${KEEPASS_KEYFILE}
Test Teardown    Close Keepass Database    

*** Variable ***
${DATADIR}             ${CURDIR}${/}Data${/}
${KEEPASS_DATABASE}    ${DATADIR}test4.kdbx
${KEEPASS_KEYFILE}     ${DATADIR}test4.key 
${KEEPASS_PASSWORD}    password 

*** Test Cases ***
Selected By Arguments Are Found
    [Documentation]    Retrieved groups by arguments should match name list
    @{values_expected}=    Create List    subgroup    subgroup2    foobar_group2   
    @{values}=     Create List
    @{groups}=    Get Groups    name=.*group    notes=^.{0}$    regex=True    
    FOR  ${group}  IN  @{groups}
       ${name}=    Get Group Name    ${group}
       Append To List    ${values}    ${name}    
    END
    Lists Should Be Equal    ${values_expected}    ${values}    

Selected By All Are Found
    [Documentation]    Retrieved groups should match name list
    @{values_expected}=    Create List    Root    foobar_group    subgroup    subgroup2    foobar_group2    Работа            
    @{values}=     Create List              
    @{groups}=    Get Groups All           
    FOR  ${group}  IN  @{groups}
       ${name}=    Get Group Name    ${group}
       Append To List    ${values}    ${name}    
    END
    Lists Should Be Equal    ${values_expected}    ${values}    

Selected By Name Are Found
    [Documentation]    Retrieved groups by name should match name list
    @{values_expected}=    Create List    subgroup            
    @{groups}=    Get Groups By Name    subgroup           
    FOR  ${group}  IN  @{groups}
       ${name}=    Get Group Name    ${group}
       List Should Contain Value    ${values_expected}    ${name}        
    END

Selected By Path Are Found
    [Documentation]    Retrieved groups by path should match name list
    @{values_expected}=    Create List    subgroup            
    ${group}=    Get Groups By Path    foobar_group/subgroup          
    ${name}=    Get Group Name    ${group}
    List Should Contain Value    ${values_expected}    ${name}   
    
Selected By Uuid Are Found
    [Documentation]    Retrieved groups by UUID should match name list
    @{values_expected}=    Create List    subgroup            
    @{groups}=    Get Groups By Uuid    4fea4663-d21a-cb69-243e-3c6967c8eea9           
    FOR  ${group}  IN  @{groups}
       ${name}=    Get Group Name    ${group}
       List Should Contain Value    ${values_expected}    ${name}        
    END

Selected By Notes Are Found
    [Documentation]    Retrieved groups by notes should match name list
    @{values_expected}=    Create List    foobar_group            
    @{groups}=    Get Groups By Notes    group notes           
    FOR  ${group}  IN  @{groups}
       ${name}=    Get Group Name    ${group}
       List Should Contain Value    ${values_expected}    ${name}        
    END
