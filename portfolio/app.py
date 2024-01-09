import tomllib
import streamlit as st


def init_page():
    st.set_page_config(
        page_title='wakadori\'s works',
        page_icon='🐔',
        layout='wide',
        initial_sidebar_state='auto',
    )
    with open("portfolio/works.toml", "rb") as f:
        works = tomllib.load(f)
    st.session_state.works = works["works"]["illustrations"]


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
        col = st.columns(2)
        col[1].button('次へ進む', on_click=countup)
        col[0].button('前に戻る', on_click=countdown)

    # アプリ本体=================================
    st.title('wakadori\'s works')
    if   ss.now == 0:
        left_pane, center_pane, right_pane = st.columns(3)
        height = len(ss.works) // 3
        with left_pane:
            for work in ss.works[:height]:
                st.image(work["image_urls"][0])
        with center_pane:
            for work in ss.works[height:2*height]:
                st.image(work["image_urls"][0])
        with right_pane:
            for work in ss.works[2*height:]:
                st.image(work["image_urls"][0])
    else:
        pass


def main():
    init_page()
    step_by_step()