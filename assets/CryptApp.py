from hashlib import sha256

def crypt_decrypt(entry_file, exit_file, key):
    keys = sha256(key.encode('utf-8')).digest()

    with open(entry_file, 'rb') as f_entree:
        with open(exit_file, 'wb') as f_sortie:
            i = 0
            while f_entree.peek():
                c = ord(f_entree.read(1))
                j = i % len(keys)
                b = bytes([c^keys[j]])
                f_sortie.write(b)
                i = i + 1
            return f_sortie
