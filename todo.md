## Outline
- command line interface
- take master pswd, validate and show/save entries
- auto copy password to clipboard
- generate random password

## Implementation

## Configure
- MASTER PASSWORD is first inputted while configuring, and its hash is saved in a file
- DEVICE SECRET is generated randomly, also stored in a file
- MASTER PASSWORD + DEVICE SECRET is passing into hashing function to create a valid key, called MASTER KEY
Master Key
- Master Key is used to  encrypt/decrypt new entries
- Encrypted fields: email, username, password
- Plain fields: sitename, url

## Add new entries
- Ask for MASTER PASSWORD
- Validate MASTER PASSWORD by hashing and checking with existing hash
- Make hash(DEVICE SECRET + MASTER PASSWORD) = Master Key
- Input fields of the entry: site name, site url, email, username, password
- Encrypt email, username and password with MASTER KEY and save the fields into the database

## Get entry
- Input the field to search for: e.g. site name, site url, email, username
- Display all entriesthat match the search. Password hidden.
- If user chooses to get password (with -p flag), then:
    - ask for MASTER PASSWORD
    - Validate MASTER PASSWORD with hash and check existing hash
    - make has(DEVICE SECTRET + MASTER PASSWORD) = Master Key
    - Decrpyt the password and copy to the keyboard

https://www.youtube.com/watch?v=KQjf9get6PE 