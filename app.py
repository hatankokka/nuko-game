from __future__ import annotations

import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


APP_DIR = Path(__file__).parent
ASSET_DIR = APP_DIR / "assets"


def as_data_uri(path: Path, mime_type: str) -> str:
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"


st.set_page_config(
    page_title="ずっこけぬこゲーム",
    page_icon="n",
    layout="wide",
    initial_sidebar_state="collapsed",
)

template = (APP_DIR / "game_template.html").read_text(encoding="utf-8")
html = (
    template.replace("__NUKO_IMAGE__", as_data_uri(ASSET_DIR / "nuko.png", "image/png"))
    .replace("__BGM_AUDIO__", as_data_uri(ASSET_DIR / "bgm.mp3", "audio/mpeg"))
    .replace("__MATTER_JS__", (ASSET_DIR / "matter.min.js").read_text(encoding="utf-8"))
)

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 0.9rem;
        padding-bottom: 0.8rem;
        max-width: 980px;
    }
    header, footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

components.html(html, height=1040, scrolling=False)
