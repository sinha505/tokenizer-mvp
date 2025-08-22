###############################################################################
############################ TEXT TO TOKEN GENERATION #########################
###############################################################################

# Load Libraies
import streamlit as st
import tiktoken
from token_colors import color_for_token

# Set Up
st.set_page_config(page_title="Tokenize • Byte by Byte", page_icon="🔤", layout="wide")
# st.title("🔤 Language Model Tokenizer")
st.markdown("### 🔤 **Language Model Tokenizer**")
st.caption("Pick a tokenizer, paste text, and see colored tokens, IDs, UTFs, and counts.")

# Elements
with st.sidebar:
    # st.header("⚙️ Settings")
    st.markdown("#### ⚙️ Settings")
    tokenizer_choice = st.selectbox(
        "Tokenizer",
        ["cl100k_base (GPT-4/3.5)", "gpt2 (r50k_base)", "p50k_base", "r50k_base"],
        index=0
    )
    show_ids = st.checkbox("Token IDs", value=True)
    show_bytes = st.checkbox("UTF-8 bytes", value=True)
    show_summary = st.checkbox("Summary", value=True)
    st.markdown("---")
    st.markdown("[Note]: Emojis and non-English scripts tokenize best with cl100k_base.")

enc_name_map = {
    "cl100k_base (GPT-4/3.5)": "cl100k_base",
    "gpt2 (r50k_base)": "gpt2",
    "p50k_base": "p50k_base",
    "r50k_base": "r50k_base",
}

default_text = "Hello!"
text = st.text_area("Enter Text", default_text, height=150)
enc = tiktoken.get_encoding(enc_name_map[tokenizer_choice])

# Encode to token ids
token_ids = enc.encode(text)

# Build display-safe segments with cumutative decode
segments = []
so_far = []
prev_render = ""
for tid in token_ids:
    so_far.append(tid)
    now_render = enc.decode(so_far)
    contrib = now_render[len(prev_render):]
    prev_render = now_render
    display = contrib if contrib else "?"   
    segments.append((display, tid))

# Colored Tokens 
st.markdown("##### 🎨 Tokens")
parts = []
for display, tid in segments:
    color = color_for_token(display)
    safe = display.replace(" ", "␠") if display.strip() == "" else display
    # wrap OFF (always inline)
    span = (
        f'<span style="display:inline; padding:2px 4px; margin:2px; border-radius:4px;'
        f' background:{color}22; outline:1px solid {color}55">{safe}</span>'
    )
    parts.append(span)

html = (
    "<div style='font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, "
    "Consolas, monospace; line-height:2.2'>" + "".join(parts) + "</div>"
)
st.markdown(html, unsafe_allow_html=True)

# Divider 
st.divider()

# Side Boxes
if show_ids:
    st.markdown("##### 🔢 Token IDs")
    st.code(str([tid for _, tid in segments]), language="text")

if show_bytes:
    st.markdown("##### 🧱 UTF-8 Bytes")
    st.code(str(list(text.encode("utf-8"))), language="text")

if show_summary:
    st.markdown("##### 📊 Summary")
    utf8_bytes = text.encode("utf-8")
    st.write({
        "Characters": len(text),
        "Tokens": len(token_ids),
        "UTF-8 Bytes": len(utf8_bytes),
        "Tokenizer": enc_name_map[tokenizer_choice],
    })




