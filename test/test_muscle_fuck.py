from lib.muscle_fuck import MuscleFuck


def test_hello_world():
    original_program = [0] * 3000
    mf = MuscleFuck(program=original_program)
    assert mf.run_from_file("test/helloworld.bf") == "hello world"
