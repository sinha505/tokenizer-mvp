#############################
Language Model Tokenizer
#############################
Pick a tokenizer, paste text, and see colored tokens, IDs, UTFs, and counts.
A simple Streamlit app that shows how your text is split into tokens using OpenAI-style tokenizers.

Its similar to:   https://platform.openai.com/tokenizer

#############################
Features
#############################
- Choose tokenizer: cl100k_base (GPT‑4/3.5), gpt2, p50k_base, r50k_base
- Colored tokens per token
- Show Token IDs and UTF‑8 bytes
- Emoji + multilingual capability

#############################
Run
#############################
python -m venv .venv 
.venv\Scripts\activate (Windows)
pip install -r requirements.txt
streamlit run app.py

#############################
Project Files
#############################

tokenizer-mvp/
├─ app.py
├─ token_colors.py
├─ requirements.txt
├─ README.txt
├─ LICENSE
└─ .gitignore

#############################
License
#############################
MIT License


