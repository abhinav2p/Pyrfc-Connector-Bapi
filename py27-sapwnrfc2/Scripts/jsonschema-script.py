#!c:\users\pac\desktop\pyrfc\py27-sapwnrfc2\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'jsonschema==3.0.0a3','console_scripts','jsonschema'
__requires__ = 'jsonschema==3.0.0a3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('jsonschema==3.0.0a3', 'console_scripts', 'jsonschema')()
    )
