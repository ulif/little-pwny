# pwny
Check whether a password has been compromised

Query the `have-i-been-pwned` database for breaches that contain a given
password. Returns the number of breaches found in the database:

    $ pwny p@ssw0rd
    51763

    $ pwny aiPh1eehec8AhY2y
    0

