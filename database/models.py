from collections import namedtuple

# define the structure of the password data
PasswordData = namedtuple('PasswordData', ['id', 'website', 'email', 'username', 'password_hash'])

# SQL query to create the password_data table in the SQLite database
CREATE_PASSWORD_DATA_TABLE = '''
CREATE TABLE IF NOT EXISTS pwd_manager (
    id INTEGER PRIMARY KEY, 
    website TEXT, 
    email TEXT, 
    username TEXT, 
    password_hash TEXT
)
'''

# SQL query to insert data into the database
INSERT_INTO_PASSWORD_DATA_TABLE = '''
INSERT INTO pwd_manager (website, email, username, password_hash)
VALUES (?, ?, ?, ?)
'''

# SQL query to retrieve data from the database
SELECT_PASSWORD = '''
SELECT id, website, email, username, password_hash FROM pwd_manager
'''

# SQL quercy to fetch psasword data for a given website
FETCH_PASSWORD_DATA_BY_WEBSITE = '''
SELECT * From pwd_manager WHERE website = ?
'''