import hashlib
import sys
import urllib.request
import pkg_resources
from argparse import ArgumentParser


__version__ = pkg_resources.get_distribution('little-pwny').version


def print_version():
    """Output current version and other infos.
    """
    print("little-pwny %s" % __version__)
    print("Copyrright (C) 2019 ulif")


def handle_options(args):
    """Handle commandline arguments.
    """
    parser = ArgumentParser(
        description=(
            "Check, how often a passphrase appears on haveibeenpwned.com"))
    parser.add_argument('passphrase', metavar='PASSPHRASE', nargs=1)
    parser.add_argument(
        '--version', action='store_true',
        help='output version information and exit.',
        )
    args = parser.parse_args(args)
    return args


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
    resp = urllib.request.urlopen(
        "https://api.pwnedpasswords.com/range/%s" % hash_val[:5])
    entries = resp.read().decode('utf-8').split('\r\n')
    result = dict([x.split(':') for x in entries]).get(hash_val[5:], 0)
    return resp.status, int(result)


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    args = handle_options(argv)
    if args.version:
        print_version()
        sys.exit(0)
    print(num_pwned(mkhash(args.passphrase[0]))[1])
