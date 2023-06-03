from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    test_cases = [
        ("message", 4, "ega_ssem"),
        ("message", 3, "sem_egas"),
        ("message", 10, "egassem"),
    ]

    for message, key, expected in test_cases:
        assert encrypt_message(message, key) == expected

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("hello", "hello")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1234, 4)
