# Unscrambles tools.enc back into tools/ (needs RCC_KEY). Run this first in every research session.
import io, os, sys, tarfile, base64, gzip
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
HERE = os.path.dirname(os.path.abspath(__file__))
k = bytes.fromhex(os.environ['RCC_KEY'].strip()); raw = base64.b64decode(open(os.path.join(HERE, 'tools.enc')).read().strip()[5:])
d = Cipher(algorithms.AES(k), modes.CBC(raw[:16])).decryptor(); data = d.update(raw[16:]) + d.finalize()
u = padding.PKCS7(128).unpadder(); data = gzip.decompress(u.update(data) + u.finalize())
tarfile.open(fileobj=io.BytesIO(base64.b64decode(data)), mode='r:gz').extractall(HERE, filter='data')
print('tools/ unpacked')
