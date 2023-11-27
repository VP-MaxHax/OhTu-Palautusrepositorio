*** Settings ***
Resource  resource.robot
Resource  login.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle456
    Set Password confirmation  kalle456
    Submit Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle456
    Set Password confirmation  kalle456
    Submit Register
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  kallekalle
    Set Password confirmation  kallekalle
    Submit Register
    Register Should Fail With Message  Password must contain atleast one number or special character

Register With Nonmatching Password And Password Confirmation
    Set Username  matti
    Set Password  kalle456
    Set Password confirmation  kalle654
    Submit Register
    Register Should Fail With Message  Password and Password confirmation do not match

Login After Successful Registration
    Set Username  lasse
    Set Password  kalle456
    Set Password confirmation  kalle456
    Submit Register
    Register Should Succeed
    Go To Login Page
    Set Username  lasse
    Set Password  kalle456
    Submit Login
    Login Should Succeed

Login After Failed Registration
    Set Username  anttiantti
    Set Password  anttiantti
    Set Password confirmation  anttiantti
    Submit Register
    Register Should Fail With Message  Password must contain atleast one number or special character
    Go To Login Page
    Set Username  anttiantti
    Set Password  anttiantti
    Submit Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Title Should Be   Welcome to Ohtu Application!

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Register
    Click Button  Register

Submit Login
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password confirmation
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}

Login Should Succeed
    Main Page Should Be Open
