import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')
"""
## ★ローカル環境で動作させる方法
```python
streamlit run main.py -- ターミナルで入力
```

"""
"""
## ★まず、ライブラリのインポート
```python
import streamlit as st (Webアプリケーションのフレームワーク)
import numpy as np     (数値計算を効率的に行う拡張モジュール)
import pandas as pd    (データ分析ライブラリ)
from PIL import Image  (Python Imaging Libraryの略)
(画像ファイルの読み込み・操作・保存を行う機能を提供するフリーライブラリ)
```

```python
※ちなみに...それぞれの意味
①モジュール：ある機能を提供してくれる .pyファイル。
②パッケージ：複数のモジュールをまとめた .pyファイル。
③ライブラリ：モジュールやパッケージのこと。定義は曖昧。
　　└ jQueryのライブラリのように、便利な機能がたくさん集まったファイルの意味。
```
"""

df = pd.DataFrame({
    '1列目': [1,2,3,4],
    '2列目': [10,20,30,40]
})

"""
## ★表を作成する方法3選
### テストデータ

```python
df = pd.DataFrame({
    '1列目': [1,2,3,4],
    '2列目': [10,20,30,40]
})
```
### ①write（※writeには引数が持てない）（動的なテーブル:並び替えができる）
```python
st.write(df)
```

"""
# 上のデータを表で作成する（※writeには引数が持てない）（動的なテーブル：並び替えができる）
st.write(df)

"""
### ②dataframe ※推奨（※dataframeには引数が持てる）（動的なテーブル:並び替えができる） 
#### 「dataframe」は引数を持てる、最大値に色を付けたり、サイズを変更したりできる
#### また、並び替えもできる動的なテーブルとなる
```python
st.dataframe(df.style.highlight_max(), width=200, height=200)
```
"""
# 上のデータを表で作成する（※dataframeには引数が持てる）（動的なテーブル：並び替えができる）
st.dataframe(df.style.highlight_max(), width=200, height=200)

"""
### ③table（※tableはただ表を表示するだけ）（静的なテーブル：並び替えができない）
```python
st.table(df.style.highlight_max())
```
"""

# 上のデータを表で作成する（※tableはただ表を表示するだけ）（静的なテーブル：並び替えができない）
st.table(df.style.highlight_max())

"""
## ★折れ線グラフ
### テストデータ
```python
(20行、3列のデータを生成する)
gra = pd.DataFrame(
    np.random.rand(20, 3), 
    columns=['a','b','c']
)
```
"""
gra = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a','b','c']
)
gra


"""
### 折れ線グラフで表示(line_chart)
```python
st.line_chart(gra) ※graは変数
```
"""
st.line_chart(gra)

"""
### 折れ線グラフで表示(中を塗りつぶしver)(area_chart)
```python
st.area_chart(gra) ※graは変数
```
"""
st.area_chart(gra)

"""
## ★棒グラフで表示(bar_chart)
```python
st.bar_chart(gra) ※graは変数
```
"""
st.bar_chart(gra)

"""
## ★マップで表示(map_chart)

### テストデータ

```python
新宿の緯度、経度の周辺マップを作成
小さい値で変化するよう、それぞれの値を50で割る
map = pd.DataFrame(
    np.random.rand(100, 2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
)
```
### 
```python
st.map_chart(map) ※mapは変数
```
"""
map = pd.DataFrame(
    np.random.rand(100, 2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
)
st.map(map)

"""
## ★画像を表示(Image.open)⇒(st.image)
```python
img = Image.open('mikan.png')
st.image(img, caption='Mikan', use_column_width=True)
・caption:下に出すタイトル
・use_column_width:画面サイズによって横幅を調整する
```
"""
img = Image.open('mikan.png')
st.image(img, caption='Mikan', use_column_width=True)

"""
## ★チェックボックス(checkbox)
### もしチェックがついていたら画像を表示する
```python
if st.checkbox('Show Image'):
    img = Image.open('mikan.png')
    st.image(img, caption='Mikan', use_column_width=True)
```
"""
if st.checkbox('Show Image'):
    img = Image.open('mikan.png')
    st.image(img, caption='Mikan', use_column_width=True)

"""
## ★セレクトボックス(selectbox)
### リストの中から選択したものを表示する
```python
option = st.selectbox(
    'あなたが好きな数字を教えてください、',
    list(range(1,11))   -- [1,2,3,4,5,6,7,8,9,10]
)
```
"""
option = st.selectbox(
    'あなたが好きな数字を教えてください、',
    list(range(1,11))
)
'あなたの好きな数字は、', option , 'です。'

"""
## ★テキストボックス(text_input)
### テキストボックスに入力したものを表示する
```python
text = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味：', text , 'です。'
```
"""
text = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味：', text , 'です。'

"""
## ★スライダー(slider)
```python
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition , 'です。'
```
"""
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition , 'です。'

"""
## ★サイドスライダー(sidebar)
```python
sidetext = st.sidebar.text_input('あなたの趣味を教えてください。(サイド)')
'あなたの趣味：', sidetext , 'です。'
sidecondition = st.sidebar.slider('あなたの今の調子は？(サイド)', 0, 100, 50)
'サイドバー側のコンディション：', sidecondition , 'です。'
```
### エラー発生
```python
DuplicateWidgetID: There are multiple identical st.text_input widgets with the same generated key.
(原因)st.sidebar.text_input('ここの中身が前に書いた文と一緒だから')
※キー(引数)が同じだとエラーになるようだ
(対策)キーに「あなたの今の調子は？(サイド)←」を付けた
```
"""
sidetext = st.sidebar.text_input('あなたの趣味を教えてください。(サイド)')
'あなたの趣味：', sidetext , 'です。'
sidecondition = st.sidebar.slider('あなたの今の調子は？(サイド)', 0, 100, 50)
'サイドバー側のコンディション：', sidecondition , 'です。'

"""
## ★複数列表示(st.columns(n))
```python
left_culumn, right_culumn= st.columns(2)
button = left_culumn.button('右カラムに文字を表示')
if button:
    right_culumn.write('ここは右カラム')
```
"""

left_culumn, right_culumn= st.columns(2)
button = left_culumn.button('右カラムに文字を表示')
if button:
    right_culumn.write('ここは右カラム')

"""
## ★エキスパンダ：折りたたまれて非表示な領域(st.expander)
```python
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')
```
"""

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')

"""
## ★プログレスバーの表示
```python
st.write('プログレスバーの表示')
sbutton = st.button('Start!!')
if sbutton:

    latest_iteration = st.empty() -- テキスト初期化
    bar = st.progress(0)          -- バーの状態を初期化

    for i in range(100):
        latest_iteration.text(f'Iteration:{i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)           -- 0.1s待ってから次のループへ
    'Done!!'
```
"""

st.write('プログレスバーの表示')
sbutton = st.button('Start!!')
if sbutton:

    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        latest_iteration.text(f'Iteration:{i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)
    st.write('Done')

