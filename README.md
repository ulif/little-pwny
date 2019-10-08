# pwny
Check whether a password has been compromised

Query the [have-i-been-pwned database](https://haveibeenpwned.com) for breaches
that contain a given password. Returns the number of breaches found in the
database:

    $ pwny p@ssw0rd
    51763

    $ pwny aiPh1eehec8AhY2y
    0

At no time the raw password is transferred to https://haveibeenpwned.com.
Instead we use the generoulsy offered API to deploy
[k-anonymity](https://en.wikipedia.org/wiki/K-anonymity). I.e. we send the
first five chars of the SHA1 hash of any given password. This way you can check
new passwords withpout revealing them to the server (or any listening party).
