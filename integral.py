import streamlit as st
import random
from PIL import Image 

st.title("積分ランダム演習(仮）")

button = st.button('積分を出題しますか？')
if button:
    n = str(random.randint(1,3))
    image = Image.open('q'+n+'.png')
    st.image(image, caption='問題',use_column_width=True)

    image2 = Image.open('a'+n+'.png')
    expander = st.expander('解答')
    expander.image(image2,use_column_width=True)

"""
## このページでは、ランダムで無限に積分の問題を演習することができます！
### ※試作品につき、問題が３問しか用意されておりませんが、順次、問題を追加する予定です。乞うご期待!
"""

