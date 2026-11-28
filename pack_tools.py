# Scrambles the tools/ folder into tools.enc so the research data isn't public. Needs RCC_KEY.
import io, os, sys, tarfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'tools'))
import seal, base64
buf = io.BytesIO()
with tarfile.open(fileobj=buf, mode='w:gz') as t: t.add(os.path.join(HERE, 'tools'), arcname='tools', filter=lambda i: None if '__pycache__' in i.name else i)
open(os.path.join(HERE, 'tools.enc'), 'w').write(seal.seal(base64.b64encode(buf.getvalue()).decode()))
print('tools.enc written')
