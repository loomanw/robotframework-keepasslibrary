*** Settings ***
Documentation       Robot framework related keywords


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
