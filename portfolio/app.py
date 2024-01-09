import tomllib
import streamlit as st


def init_page():
    st.set_page_config(
        page_title='ワカドリ\'s works',
        page_icon='🐔',
        layout='wide',
        initial_sidebar_state='auto',
    )
    with open("portfolio/works.toml", "rb") as f:
        works = tomllib.load(f)
    st.session_state.author = works["author"]
    st.session_state.works = works["works"]["illustrations"]


def app():
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
    name = ss.author["name"]
    st.title(f"{name}\'s works")
    description = ss.author["description"]
    email = ss.author["email"]
    x_url = ss.author["x_url"]
    pixiv_url = ss.author["pixiv_url"]
    github_url = ss.author["github_url"]
    st.sidebar.title(f'{name}\'s profile')
    st.sidebar.markdown(f'📝 {description}')
    st.sidebar.markdown(f'📧 {email}')
    st.sidebar.markdown(f'🌐 {x_url}')
    st.sidebar.markdown(f'🎨 {pixiv_url}')
    st.sidebar.markdown(f'🐙 {github_url}')

    if   ss.now == 0:
        left_pane, center_pane, right_pane = st.columns(3)
        height = len(ss.works) // 3
        with left_pane:
            for work in ss.works[:height]:
                with st.container():
                    name = work["name"]
                    category = work["category"]
                    likes = work["x_likes"]
                    reposts = work["x_reposts"]
                    caption = f"{name} / {category} / ❤{likes} / 🔂{reposts}"
                    st.image(work["image_urls"][0], caption=caption)
        with center_pane:
            for work in ss.works[height:2*height]:
                with st.container():
                    name = work["name"]
                    category = work["category"]
                    likes = work["x_likes"]
                    reposts = work["x_reposts"]
                    caption = f"{name} / {category} / ❤{likes} / 🔂{reposts}"
                    st.image(work["image_urls"][0], caption=caption)
        with right_pane:
            for work in ss.works[2*height:]:
                with st.container():
                    name = work["name"]
                    category = work["category"]
                    likes = work["x_likes"]
                    reposts = work["x_reposts"]
                    caption = f"{name} / {category} / ❤{likes} / 🔂{reposts}"
                    st.image(work["image_urls"][0], caption=caption)
    else:
        pass


def main():
    init_page()
    app()