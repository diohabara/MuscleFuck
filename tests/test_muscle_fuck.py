from src.muscle_fuck import MuscleFuck


def test_hello_world() -> None:
    mf = MuscleFuck()
    test_directory = "data/"
    test_expected_pairs = [
        ("helloworld.bf", "Hello, World!"),
        ("hoge.bf", "hoge"),
    ]
    for test_file, expected in test_expected_pairs:
        mf.reset()
        output = mf.run_from_file(test_directory + test_file)
        assert "".join(output) == expected
