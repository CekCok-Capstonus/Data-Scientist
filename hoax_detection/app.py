import streamlit as st
import joblib

st.set_page_config(
    page_title="AI Hoax Detector",
    page_icon="📰",
    layout="centered"
)

model = joblib.load("model_svm.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

/* ── Background ── */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0a0f1e 0%, #0d1b2a 40%, #0f2027 100%);
    min-height: 100vh;
}

[data-testid="stHeader"] {
    background: transparent;
}

/* ── Hide default streamlit elements ── */
/* Biarkan bawaan Streamlit tetap tampil untuk keperluan deploy */

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #334155; border-radius: 10px; }

/* ── Hero Section ── */
.hero-wrapper {
    text-align: center;
    padding: 48px 0 32px 0;
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(99, 102, 241, 0.15);
    border: 1px solid rgba(99, 102, 241, 0.35);
    color: #a5b4fc;
    font-size: 13px;
    font-weight: 500;
    letter-spacing: 0.05em;
    padding: 6px 16px;
    border-radius: 999px;
    margin-bottom: 24px;
}

.hero-title {
    font-size: 56px;
    font-weight: 800;
    line-height: 1.1;
    background: linear-gradient(135deg, #ffffff 0%, #c7d2fe 50%, #818cf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 16px;
    letter-spacing: -1px;
}

.hero-subtitle {
    font-size: 17px;
    color: #94a3b8;
    font-weight: 400;
    max-width: 480px;
    margin: 0 auto;
    line-height: 1.6;
}

/* ── Stats Row ── */
.stats-row {
    display: flex;
    justify-content: center;
    gap: 24px;
    margin: 32px 0;
    flex-wrap: wrap;
}

.stat-chip {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 12px;
    padding: 12px 20px;
    text-align: center;
    min-width: 110px;
}

.stat-chip .stat-value {
    font-size: 22px;
    font-weight: 700;
    color: #e2e8f0;
}

.stat-chip .stat-label {
    font-size: 11px;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-top: 2px;
}

/* ── Main Card ── */
.card {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 24px;
    padding: 36px;
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    box-shadow:
        0 0 0 1px rgba(255,255,255,0.03),
        0 20px 60px rgba(0,0,0,0.5),
        inset 0 1px 0 rgba(255,255,255,0.06);
    margin-bottom: 20px;
}

.card-label {
    font-size: 13px;
    font-weight: 600;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 10px;
}

/* ── Textarea override ── */
textarea {
    background: rgba(15, 23, 42, 0.8) !important;
    border: 1px solid rgba(99, 102, 241, 0.25) !important;
    border-radius: 14px !important;
    color: #e2e8f0 !important;
    font-size: 15px !important;
    font-family: 'Inter', sans-serif !important;
    line-height: 1.7 !important;
    padding: 16px !important;
    transition: border-color 0.2s ease !important;
    resize: vertical !important;
}

textarea:focus {
    border-color: rgba(99, 102, 241, 0.6) !important;
    box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.12) !important;
    outline: none !important;
}

textarea::placeholder {
    color: #475569 !important;
}

/* ── Button ── */
.stButton > button {
    width: 100%;
    height: 54px;
    border-radius: 14px;
    background: linear-gradient(135deg, #4f46e5, #6366f1);
    color: white;
    font-size: 15px;
    font-weight: 600;
    border: none;
    letter-spacing: 0.02em;
    transition: all 0.2s ease;
    box-shadow: 0 4px 20px rgba(99, 102, 241, 0.35);
    margin-top: 4px;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #4338ca, #4f46e5);
    box-shadow: 0 6px 28px rgba(99, 102, 241, 0.5);
    transform: translateY(-1px);
}

.stButton > button:active {
    transform: translateY(0px);
}

/* ── Result Cards ── */
.result-hoax {
    background: linear-gradient(135deg, rgba(127,29,29,0.6), rgba(153,27,27,0.4));
    border: 1px solid rgba(239, 68, 68, 0.4);
    border-radius: 20px;
    padding: 32px 28px;
    text-align: center;
    box-shadow: 0 8px 32px rgba(239, 68, 68, 0.2), inset 0 1px 0 rgba(255,255,255,0.05);
    animation: fadeInUp 0.4s ease;
}

.result-fakta {
    background: linear-gradient(135deg, rgba(20,83,45,0.6), rgba(21,128,61,0.4));
    border: 1px solid rgba(34, 197, 94, 0.4);
    border-radius: 20px;
    padding: 32px 28px;
    text-align: center;
    box-shadow: 0 8px 32px rgba(34, 197, 94, 0.2), inset 0 1px 0 rgba(255,255,255,0.05);
    animation: fadeInUp 0.4s ease;
}

.result-icon {
    font-size: 48px;
    margin-bottom: 12px;
    display: block;
}

.result-label {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    opacity: 0.7;
    margin-bottom: 6px;
}

.result-title {
    font-size: 32px;
    font-weight: 800;
    color: white;
    letter-spacing: -0.5px;
}

.result-desc {
    font-size: 14px;
    color: rgba(255,255,255,0.6);
    margin-top: 10px;
    line-height: 1.5;
}

/* ── Divider ── */
.custom-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.08), transparent);
    margin: 28px 0;
}

/* ── Footer ── */
.footer {
    text-align: center;
    padding: 24px 0 40px 0;
}

.footer-text {
    font-size: 13px;
    color: #334155;
}

.footer-pills {
    display: flex;
    justify-content: center;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 12px;
}

.footer-pill {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.07);
    color: #475569;
    font-size: 11px;
    font-weight: 500;
    padding: 4px 12px;
    border-radius: 999px;
    letter-spacing: 0.04em;
}

/* ── Warning override ── */
[data-testid="stAlert"] {
    background: rgba(234, 179, 8, 0.1) !important;
    border: 1px solid rgba(234, 179, 8, 0.3) !important;
    border-radius: 12px !important;
    color: #fde68a !important;
}

/* ── Animations ── */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(16px); }
    to   { opacity: 1; transform: translateY(0); }
}

.hero-wrapper { animation: fadeInUp 0.5s ease; }
.card         { animation: fadeInUp 0.5s ease 0.1s both; }
</style>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-wrapper">
    <div class="hero-badge">🤖 &nbsp;Powered by SVM + TF-IDF</div>
    <div class="hero-title">AI Hoax Detector</div>
    <div class="hero-subtitle">
        Deteksi berita hoax secara instan menggunakan<br>
        Machine Learning dan Natural Language Processing
    </div>
</div>
""", unsafe_allow_html=True)

# ── Stats ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stats-row">
    <div class="stat-chip">
        <div class="stat-value">SVM</div>
        <div class="stat-label">Model</div>
    </div>
    <div class="stat-chip">
        <div class="stat-value">TF-IDF</div>
        <div class="stat-label">Vectorizer</div>
    </div>
    <div class="stat-chip">
        <div class="stat-value">NLP</div>
        <div class="stat-label">Teknologi</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Input Card ────────────────────────────────────────────────────────────────
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="card-label">📝 &nbsp;Teks Berita</div>', unsafe_allow_html=True)

text = st.text_area(
    label="teks_berita",
    label_visibility="collapsed",
    height=200,
    placeholder="Tempel atau ketik teks berita yang ingin Anda verifikasi di sini...",
)

st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

predict_btn = st.button("🔍 &nbsp; Analisis Sekarang", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# ── Prediction ────────────────────────────────────────────────────────────────
if predict_btn:
    if text.strip() == "":
        st.warning("⚠️  Masukkan teks berita terlebih dahulu sebelum menganalisis.")
    else:
        with st.spinner("Menganalisis teks..."):
            text_tfidf = tfidf.transform([text])
            pred = model.predict(text_tfidf)

        if pred[0] == 1:
            st.markdown("""
            <div class="result-hoax">
                <span class="result-icon">🚨</span>
                <div class="result-label">Hasil Analisis</div>
                <div class="result-title">Terdeteksi Hoax</div>
                <div class="result-desc">
                    Berita ini kemungkinan besar mengandung informasi yang tidak akurat.<br>
                    Harap verifikasi dari sumber terpercaya sebelum menyebarkan.
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="result-fakta">
                <span class="result-icon">✅</span>
                <div class="result-label">Hasil Analisis</div>
                <div class="result-title">Berita Fakta</div>
                <div class="result-desc">
                    Berita ini terindikasi sebagai informasi yang valid.<br>
                    Tetap bijak dalam mengonsumsi dan menyebarkan informasi.
                </div>
            </div>
            """, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <div class="footer-pills">
        <span class="footer-pill">Streamlit</span>
        <span class="footer-pill">Scikit-learn</span>
        <span class="footer-pill">TF-IDF</span>
        <span class="footer-pill">SVM</span>
        <span class="footer-pill">Python</span>
    </div>
</div>
""", unsafe_allow_html=True)
