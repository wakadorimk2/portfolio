import streamlit as st

def get_image_urls():
    image_urls = [
        'https://pbs.twimg.com/media/E-wmSP8UcBAYX9-?format=jpg&name=4096x4096',
        'https://pbs.twimg.com/media/FCi6IbpVgAUQUss?format=jpg&name=4096x4096',
        'https://pbs.twimg.com/media/FI6Nv84akAcB8gA?format=jpg&name=4096x4096',
        'https://pbs.twimg.com/media/FIL3KXZacAIBv48?format=jpg&name=4096x4096',
    ]
    return image_urls


def init_page():
    st.set_page_config(
        page_title='wakadoriのポートフォリオ',
        page_icon='🐔',
        layout='centered',
        initial_sidebar_state='expanded',
    )


def step_by_step():
    ss = st.session_state

    # 状態変数==================================
    if 'now' not in ss:     # 初期化
        ss.now = 0          # 初期化
    def countup():          # コールバック関数(1/3):次へ
        ss.now += 1
    def countdown():        # コールバック関数(2/3):戻る
        ss.now -= 1
    def reset():            # コールバック関数(3/3):リセット
        ss.now = 0

    # UIパーツ=================================
    def buttons(now):
        col = st.columns(3)
        if ss.now < 3:
            col[2].button('次へ進む', on_click=countup)
        if ss.now > 0:
            col[1].button('前へ戻る', on_click=countdown)
        if ss.now > 1:
            col[0].button('はじめから', on_click=reset)

    # アプリ本体=================================
    col = st.columns([2,1])
    col[0].write('wakadoriのポートフォリオ')
    if col[1].toggle('1枚ずつ', True):
        if   ss.now == 0:
            buttons(ss.now)
            st.image(get_image_urls()[ss.now])
        elif ss.now == 1:
            buttons(ss.now)
            st.image(get_image_urls()[ss.now])
        elif ss.now == 2:
            buttons(ss.now)
            st.image(get_image_urls()[ss.now])
        else:
            st.write('### 完了！')
            buttons(ss.now)
            st.success('全てのステップが完了しました')
    else:
        st.image(get_image_urls()[0])
        st.image(get_image_urls()[1])
        st.image(get_image_urls()[2])


def main():
    init_page()
    step_by_step()