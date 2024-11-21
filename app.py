# ---APIサーバに必要なモジュール---
import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from typing import Dict, Union, List
from pydantic import BaseModel
from firebase.init import db, bucket, upload_svg_to_storage

# ライブラリ-------------------------------
from wsgiref.simple_server import make_server
import json
import time
from datetime import datetime, date, timedelta
import os
import sys
import glob
import shutil
import zipfile
from pathlib import Path
import importlib  # モジュールのリロードに使います



parent = Path(__file__).resolve().parent  # ファイルのディレクトリを取得

app = FastAPI()





# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------
print(__name__)
if __name__ == "__main__":
    # uvicorn.run(app, host="127.0.0.1", port=9100)
    uvicorn.run(app, host="127.0.0.1", port=8000)

