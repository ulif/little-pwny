import os
import pytest
from pwny import handle_options, mkhash, num_pwned, main


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
    assert mkhash(
            "P@ssw0rd") == "21BD12DC183F740EE76F27B78EB39C8AD972A757"
    assert mkhash(
            "aiPh1eehec8AhY2y") == "373DFCD311EB075C6B66B167F7FA188E5D4639A4"
    assert mkhash("") == "DA39A3EE5E6B4B0D3255BFEF95601890AFD80709"


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


def test_handle_options_passphrse():
    # we can tell a passphrase to check
    args = handle_options(['some-passphrase'])
    args.passphrase == 'some-passphrase'


def test_handle_options_no_phrase(capsys):
    # we tell, that a passphrase is required
    with pytest.raises(SystemExit) as exc_info:
        handle_options([])
    out, err = capsys.readouterr()
    assert exc_info.value.code == 2
    assert "the following arguments are required" in err
