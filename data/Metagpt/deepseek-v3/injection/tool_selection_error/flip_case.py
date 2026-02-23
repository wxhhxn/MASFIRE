def flip_case(s: str) -> str:
    """Flip lowercase characters to uppercase and vice versa.

    Non-alphabetic characters are unchanged.
    """
    return s.swapcase()


if __name__ == "__main__":
    # Simple demonstration
    print(flip_case("Hello, World!"))
