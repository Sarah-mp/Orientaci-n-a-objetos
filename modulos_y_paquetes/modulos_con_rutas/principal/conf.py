# solo cuando los modulos estan en archivos diferentes
import sys
import os
from pathlib import Path


sys.path.append(os.path.join(os.path.dirname(__file__),'../todos'))

#ruta  = r''
#sys.path.append(ruta)
#ruta = os.path.join(os.path.dirname(__file__),'../todos')
#ruta = f"{Path(__file__).resolve().parent}/../todos/"