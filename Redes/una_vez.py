from random import randint

ascii_chars = ''.join(map(chr, range(32, 127)))


def ascii_to_7bit_bin(message: str) -> tuple[str]:
    return tuple(map(lambda c: bin(ord(c))[2:].zfill(7), message))


def generate_random_str(length: int) -> str:
    return ''.join(
        [ascii_chars[randint(0,
                             len(ascii_chars) - 1)] for _ in range(length)])


def apply_xor(original: tuple[str], key: tuple[str]) -> tuple[str]:
    return tuple(
        map(lambda x, y: bin(int(x, 2) ^ int(y, 2))[2:].zfill(7), original,
            key))


def run():
    message = input("Escribe el mensaje a cifrar: ")

    # binarios
    original_binary = ascii_to_7bit_bin(message)
    random_binary = ascii_to_7bit_bin(generate_random_str(len(message)))

    print(f'Mensaje original en binario:\t{original_binary}')
    print(f'Clave en binario:\t\t{random_binary}')

    # cifrado con XOR
    encrypted_binary = apply_xor(original_binary, random_binary)

    print(f'Mensaje cifrado en binario:\t{encrypted_binary}')


if __name__ == "__main__":
    run()