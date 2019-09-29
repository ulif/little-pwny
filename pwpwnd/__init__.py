import hashlib
import http.client
import sys


def mkhash(password):
    """Create SHA1 hash from `password`.

    HIBP API requests SHA1 hashed password.
    """
    return hashlib.sha1(
            password.encode('utf-8')).hexdigest().upper()


def num_pwned(hash_val):
    """Lookup haveibeenpwned.com for `hash_val`.

    Returns the number of entries found starting with the first 5 chars of
    `hash_val`.
    """
    conn = http.client.HTTPSConnection("api.pwnedpasswords.com")
    conn.request("GET", "/range/%s" % hash_val[:5])
    resp = conn.getresponse()
    entries = resp.read().decode('utf-8').split('\r\n')
    result = dict([x.split(':') for x in entries]).get(hash_val[5:], 0)
    return resp.status, int(result)


def main(argv=None):
    if argv is None:
        argv = sys.argv[1]
    return num_pwned(mkhash(argv))[1]
