*** Settings ***
Documentation       Template robot main suite.

Library             ExtendedSelenium.py


*** Tasks ***
Minimal task
    Open Configured Available Browser
    Go To    www.yahoo.com
    Log    Done.
