def encrypt(text, n):

    s = [text]

    def encrypt_once(text):
        e_str = ""
        o_str = ""

        for i in range(0, len(text)):
            if i % 2 != 0:
                e_str += text[i]
            else:
                o_str += text[i]

        return e_str + o_str

    for i in range(1, n + 1):
        s.append(encrypt_once(s[i - 1]))

    return s[n]


def decrypt(text, n):
    s = [text]

    def decrypt_once(text):
        decry_one = ""
        decry_two = ""

        mid = int(len(text) / 2)

        decry_one += text[0:mid]
        decry_two += text[mid:]

        s = ""

        for i in range(0, mid):
            s += decry_two[i] + decry_one[i]

        if len(text) % 2 != 0:
            s += decry_two[mid]

        return s

    for i in range(1, n + 1):
        s.append(decrypt_once(s[i - 1]))

    return s[n]