# python 環境構築

## VENV で仮想環境初期設定

```
python -m venv venv
```

または、

```
python3 -m venv venv
```

<br>

# Win の場合

## VENV をアクティブにするために、PowerShell を有効かする（win の場合）

PowerShell を開いて、下記のコマンドを実行する

```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
```

## VENV をアクティブにする

プロジェクトのフォルダで下記を実行

```
.\venv\scripts\python.exe -m pip install --upgrade pip
.\venv\Scripts\activate
```

VENV の仮想環境に入れる

<br>
<br>

# Mac の場合
## venv を有効化

```
source ./venv/bin/activate
```


<br>
<br>




# ライブラリ
pip install uvicorn
pip install fastapi
<!-- pip install pillow -->
<!-- pip install Pillow==8.3.0 -->
<!-- pip install pybarcodes -->
pip install python-barcode
pip install pillow



## 移行元でライブラリ一覧を書き出す

```
pip freeze > requirements.txt
```

## 移行先でライブラリをインストールする

```
pip install -r requirements.txt
python3 -m pip install --upgrade pip
```


# API起動
開発環境を起動
ソースコードを更新したら、自動更新される
```
uvicorn app:app --reload
```



