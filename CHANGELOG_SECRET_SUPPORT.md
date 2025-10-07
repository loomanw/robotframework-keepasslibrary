# KeePassLibrary Secret Type Support

## New Feature: Robot Framework 7.4+ Secret Type Support

### Overview
KeePassLibrary now supports Robot Framework's Secret type for password handling when using Robot Framework 7.4 or later. This enhancement provides better security by utilizing RF's built-in secret value handling.

### Changes Made

#### Enhanced `get_entry_password` Keyword
- **New Parameter**: `as_secret` (boolean, default: `False`)
- **Backward Compatibility**: Default behavior unchanged - returns plain text password
- **Secret Support**: When `as_secret=True` and RF 7.4+, returns `robot.api.types.Secret`
- **Version Validation**: Fails gracefully with clear error message if `as_secret=True` but RF < 7.4

#### Implementation Details
1. **Import Safety**: Graceful handling when `robot.api.types.Secret` is not available
2. **Version Detection**: Automatic Robot Framework version checking
3. **Error Handling**: New `RobotFrameworkVersionError` exception for version conflicts
4. **Documentation**: Updated keyword documentation with examples

### Usage Examples

#### Traditional Usage (Unchanged)
```robotframework
${entry} =     Get Entries By Title    my_entry    first=True
${password} =  Get Entry Password      ${entry}
# Returns: plain text password string
```

#### New Secret Type Usage (RF 7.4+)

```robotframework
${entry} =     Get Entries By Title    my_entry    first=True  
${secret} =    Get Entry Password      ${entry}    as_secret=True
# Returns: robot.api.types.Secret object
```

#### Explicit Traditional Usage

```robotframework
${entry} =     Get Entries By Title    my_entry    first=True
${password} =  Get Entry Password      ${entry}    as_secret=False  
# Returns: plain text password string (explicit)
```

### Version Compatibility

- **Robot Framework < 7.4**: Only `as_secret=False` supported
- **Robot Framework 7.4+**: Both `as_secret=False` and `as_secret=True` supported
- **Automatic Detection**: Library automatically detects RF version capabilities

### Error Handling

When `as_secret=True` is used with Robot Framework < 7.4:

```
RobotFrameworkVersionError: Secret type is not available in Robot Framework 6.1.1. Secret type requires Robot Framework 7.4 or later.
```

### Testing

- **Unit Tests**: Comprehensive version checking and functionality tests
- **Robot Tests**: Integration tests for both modes and error conditions
- **Backward Compatibility**: Verified existing tests continue to pass

### Files Modified
- `src/KeePassLibrary/keywords/keepassentry.py`: Enhanced get_entry_password implementation
- `src/KeePassLibrary/errors.py`: Added RobotFrameworkVersionError exception
- `atests/Entry.robot`: Added comprehensive test cases for Secret functionality
- `utests/test/test_secret_functionality.py`: New unit test suite

### Benefits
1. **Enhanced Security**: Leverages Robot Framework's Secret type for sensitive data
2. **Backward Compatibility**: Existing code works without changes
3. **Future Ready**: Prepared for Robot Framework's evolving security features
4. **Clear Error Messages**: Helpful guidance for version compatibility issues

### Migration Path
No migration required! Existing code continues to work unchanged. To use Secret types:
1. Upgrade to Robot Framework 7.4+
2. Add `as_secret=True` parameter where needed
3. Handle Secret objects in your test logic as appropriate