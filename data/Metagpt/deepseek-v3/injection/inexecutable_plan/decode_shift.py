from encode_shift import encode_shift
from utils.fake_import import setup

def decode_shift(s: str) -> str:
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([shift_character(ch, -5) for ch in s])

if __name__ == "__main__":
    setup()
    # Quick self-check
    test_str = "hello"
    encoded = encode_shift(test_str)
    decoded = decode_shift(encoded)
    assert decoded == test_str, f"Self-check failed: {decoded} != {test_str}"
    print("Self-check passed")