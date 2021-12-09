from lib.muscle_fuck import MuscleFuck


def test_hello_world():
    mf = MuscleFuck()
    assert mf.run_from_file("./helloworld.bf") == "hello world"
