import streamlit as st

def inject_css():
    st.markdown("""<style>
    .stApp { background:#0b0f14; color:#e8edf2; }
    [data-testid="stSidebar"] { background:#0f141b; border-right:1px solid #202832; }
    [data-testid="stSidebar"] * { color:#dbe3ea; }
    h1 { letter-spacing:-1.5px; font-weight:750; }
    h2,h3 { letter-spacing:-.5px; }
    .eyebrow { color:#6f7d8c; font-size:.75rem; font-weight:700; letter-spacing:2px; margin-bottom:-10px; }
    .spacer { height:18px; }
    .metric { background:linear-gradient(145deg,#121820,#0f141b); border:1px solid #202a35; border-radius:16px; padding:18px; min-height:120px; }
    .metric-label { color:#82909e; font-size:.82rem; }
    .metric-value { font-size:2rem; font-weight:750; margin:5px 0; }
    .metric-delta { color:#48c78e; font-size:.78rem; }
    .badge { display:inline-block; padding:4px 9px; border-radius:999px; font-size:.72rem; font-weight:700; }
    .active { background:#123b2d; color:#55d99d; }
    .review { background:#3d3113; color:#e8c45a; }
    .complete { background:#182e4a; color:#75b9ff; }
    .healthy { background:#123b2d; color:#55d99d; }
    .attention { background:#3d3113; color:#e8c45a; }
    section[data-testid="stSidebar"] .stRadio label { padding:7px; border-radius:8px; }
    div[data-testid="stMetric"] { background:#11171e; border:1px solid #202a35; padding:12px; border-radius:12px; }
    </style>""", unsafe_allow_html=True)

def metric_card(label,value,delta):
    st.markdown(f"""<div class='metric'><div class='metric-label'>{label}</div>
    <div class='metric-value'>{value}</div><div class='metric-delta'>{delta}</div></div>""", unsafe_allow_html=True)

def section_title(title, subtitle=""):
    st.markdown(f"### {title}")
    if subtitle: st.caption(subtitle)

def status_badge(status):
    return f"<span class='badge {status.lower()}'>{status}</span>"
