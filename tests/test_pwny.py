from pwny import mkhash, num_pwned, main


def test_mkhash():
    assert mkhash("P@ssw0rd") == "21BD12DC183F740EE76F27B78EB39C8AD972A757"


def test_num_pwned():
    status, num = num_pwned("21BD12DC183F740EE76F27B78EB39C8AD972A757")
    assert status == 200
    assert num > 52500

def test_main(capsys):
    main("P@ssw0rd")
    out, err = capsys.readouterr()
    assert int(out) > 52000
