import sys
import os

sys.path.append(os.path.abspath(os.path.dirname('./config')))

import config.build_doc as b

b.build_iden3_doc()
