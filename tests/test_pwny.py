import os
import pytest
from pwny import mkhash, num_pwned, main


def faux_urlopen(url):
    # A replacement for `urllib.request.urlopen`
    path = os.path.join(
        os.path.dirname(__file__),
        "21BD12DC183F740EE76F27B78EB39C8AD972A757.hash")
    f = open(path, "rb")
    f.status = 200
    return f


@pytest.fixture(scope="function")
def offline(request, monkeypatch):
    # Replace network functions we use in tests with fake ones.
    monkeypatch.setattr(
        "urllib.request.urlopen", faux_urlopen)


def test_mkhash():
    # the hashes we build are regular sha1 hashes
    assert mkhash("P@ssw0rd") == "21BD12DC183F740EE76F27B78EB39C8AD972A757"


def test_num_pwned(offline):
    # we get expectable numbers as results
    status, num = num_pwned("21BD12DC183F740EE76F27B78EB39C8AD972A757")
    assert status == 200
    assert num == 52579


def test_main(capsys, offline):
    # we can run the main function w/o trouble
    main("P@ssw0rd")
    out, err = capsys.readouterr()
    assert out == "52579\n"


def test_main_none(capsys, offline, monkeypatch):
    # sys.argv is used if no arg was passed in
    monkeypatch.setattr("sys.argv", ["<scriptname>", "P@ssw0rd"])
    main()
    out, err = capsys.readouterr()
    assert out == "52579\n"
