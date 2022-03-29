import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

def test():
    st.title('Streamlit 株価チェックアプリ')
    """
    ## ★「yfinance」をインポート
    ### Yahoo! Financeから株価情報を取得するためのAPIです
    ```python
    !pip3 install yfinance -- jupyterで入力
    ```
    """
    st.title('Streamlit 株価チェックアプリ②')

    # """
    # ## ★ほかに必要なライブラリ等
    # ```python
    # import pandas as pd
    # import matplotlib.pyplot as plt
    # import yfinance as yf

    # %matplotlib inline
    # ```
    # """
    # """
    # ### !!ここでエラー発生
    # ```python
    # Duplicate key in file WindowsPath
    # ('C:/anaconda/lib/site-packages/matplotlib/mpl-data/matplotlibrc'), 
    # line 258 ('font.family:  IPAexGothic')
    # ```
    # ### 以下のサイトを参照しました
    # 【対策】
    # ①IPAが配布しているIPAexという日本語用フォントをダウンロード
    # ②ipaexg.ttf をmatplotlibのフォント用フォルダに置く
    # ③matplotlibの設定ファイル matplotlibrc でipaexg.ttf を読み込む設定をする

    # ```python
    # #4-05-1
    # # フォントを格納するフォルダを調べる

    # import matplotlib
    # matplotlib.matplotlib_fname()

    # 下の例では、使用OSは Windows10 で anaconda は D:\\sys\\anaconda3 にインストールされていて、 python仮想環境の名前は book3 である。

    # [matplotlib の設定ファイル]
    #     D:\sys\anaconda3\env\book3\Lib\site-packages\matplotlib\mpl-data\matplotlibrc
    # [ttf fontを置くパス]
    #     D:\sys\anaconda3\env\book3\Lib\site-packages\matplotlib\mpl-data\fonts\ttf
    # ```
    # """
