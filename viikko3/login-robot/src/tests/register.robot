*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  k  kalle123
    Output Should Contain  Username must be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  k4ll3  kalle123
    Output Should Contain  Username must contain only letters from alphabet
    Input Credentials  ka!!e  kalle123
    Output Should Contain  Username must contain only letters from alphabet

Register With Valid Username And Too Short Password
    Input Credentials  kalle  k4lle
    Output Should Contain  Password must be at least 8 characters long    

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kallekalle
    Output Should Contain  Password must contain atleast one number or special character

*** Keywords ***
Input New Command
    Input  new
