import barcode


# バーコードを画像として出力するためのライブラリ
from barcode.writer import ImageWriter

# バイナリデータをメモリ上で扱うためのライブラリ
from io import BytesIO

# pip install pillow
# Python Imaging Library (PIL) は、画像処理機能を提供
from PIL import Image


def create_barcode(data, filename=None, barcode_format="ean13"):
    """
    指定されたデータを含むバーコードを画像として生成し、PIL.Image.Imageオブジェクトとして返す関数。

    この関数は `python-barcode` ライブラリを使用して、指定されたデータ（数字など）からバーコードを生成します。
    生成されたバーコードは、PIL.Image.Imageオブジェクトとしてメモリ上に生成され、返されます。
    オプションで、生成されたバーコードの画像ファイル名を指定することもできます。

    Args:
        data (str): バーコードにエンコードするデータ。数字のみ。
        filename (str, optional): 生成されたバーコードの画像ファイル名。指定されない場合はファイルに保存されません。
        barcode_format (str, optional): 生成するバーコードの形式。デフォルトは 'ean13'。

    Returns:
        PIL.Image.Image: 生成されたバーコードのイメージオブジェクト。
    """
    # 指定されたフォーマットのバーコードクラスを取得
    barcode_class = barcode.get_barcode_class(barcode_format)
    # バーコードオブジェクトの生成。ImageWriterを使用して画像として出力可能にする
    barcode_obj = barcode_class(data, writer=ImageWriter())

    if filename:
        # filenameが存在したら指定されたファイル名でバーコードを保存
        barcode_obj.save(filename)

    # メモリ上に画像データを格納するためのバッファ
    output_image = BytesIO()
    # バーコードの画像データをバッファに書き込む
    barcode_obj.write(output_image)
    # バッファの読み取り位置を最初に戻す
    output_image.seek(0)
    # PILライブラリを使用して画像オブジェクトを生成
    barcode_image = Image.open(output_image)

    # 生成したイメージオブジェクトを返す
    return barcode_image


##############################################################
# 関数のテスト
if __name__ == "__main__":

    # JANコード（EAN-13フォーマット）を生成するテストコード ※ファイルを作成しない、デフォルト ean13
    # test_data = "4901301336316"
    # barcode_image = create_barcode(test_data, "barcode_ean13_4901301336316", "ean13")
    # barcode_image.show()  # 画像を表示

    ### 以下からすべてpngファイルを作成します
    # JANコード（EAN-13フォーマット）を生成するテストコード
    test_data = "190175040485"  # チェックデジットがなければ、自動的に追加される
    barcode_image = create_barcode(test_data, "barcode_ean13", "ean13")
    barcode_image.show()  # 画像を表示

    # # JANコード（EAN-8フォーマット）を生成するテストコード
    # test_data = "49747157"
    # barcode_image = create_barcode(test_data, "barcode_ean8", "ean8")
    # barcode_image.show()  # 画像を表示

    # # NW-7（Codabarフォーマット）を生成するテストコード
    # test_data = "A123456B"  # Codabarバーコードのテストデータ。開始/終了文字にはA、B、C、Dが使用されます。
    # barcode_image = create_barcode(test_data, "barcode_codabar", "codabar")
    # barcode_image.show()  # 画像を表示

    # # CODE128 を生成するテストコード
    # test_data = (
    #     "Code128 !#$%&'()"  # 数字（0 ～ 9）,アルファベット大文字/小文字,記号,制御文字
    # )
    # barcode_image = create_barcode(test_data, "barcode_code128", "code128")
    # barcode_image.show()  # 画像を表示

    # # ISBN13 を生成するテストコード
    # test_data = "978-4061473515"
    # barcode_image = create_barcode(test_data, "barcode_isbn13", "isbn13")
    # barcode_image.show()  # 画像を表示

    # # ITF を生成するテストコード
    # test_data = "1234567890"  # 数字（0 ～ 9）のみ
    # barcode_image = create_barcode(test_data, "barcode_itf", "itf")
    # barcode_image.show()  # 画像を表示
