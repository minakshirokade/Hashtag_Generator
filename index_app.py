import streamlit as st
import os
import base64

# ===== SET BACKGROUND =====
def set_bg_from_local(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
        st.markdown(f"""
            <style>
                .stApp {{
                    background-image: url("data:image/jpeg;base64,{encoded}");
                    background-size: cover;
                    background-position: center;
                    background-attachment: fixed;
                }}
            </style>
        """, unsafe_allow_html=True)

set_bg_from_local("C:/Users/ASUS/Documents/Projects/Hastag Generator/background2_img.jpeg")

# ===== HEADER =====
st.markdown("""
    <h1 style='text-align: center; color: #FFD700; font-family:Georgia; font-size: 70px;'>
        👑 The Royals
    </h1>
    <h4 style='text-align: center; color: #FAFAD2; font-family:Georgia; font-size: 24px;'>
        “From Regal to Reels — Hashtags for Every Kind of Love.”
    </h4>
    <hr style='border-top: 3px solid gold;'>
""", unsafe_allow_html=True)

# ===== STYLING =====
st.markdown("""
    <style>
        label, .stSelectbox label {
            font-size: 50px !important;
            color: #FFD700 !important;
            font-family: 'Times New Roman', serif !important;
            font-weight: bold;
        }

        .stTextInput > div > input, .stSelectbox > div {
            background-color: #fdf6d8;
            color: #3a2e00;
            font-size: 20px;
            font-weight: bold;
            border: 2px solid #FFD700;
            font-family: 'Times New Roman', serif !important;
        }

        div.stButton > button {
            background: linear-gradient(to right, #ffd700, #ffcc00);
            color: black;
            font-size: 28px;
            border-radius: 12px;
            border: none;
            padding: 10px 25px;
            transition: 0.3s ease-in-out;
            font-family: 'Times New Roman', serif !important;
        }

        div.stButton > button:hover {
            transform: scale(1.05);
            background-color: #fff066;
        }
    </style>
""", unsafe_allow_html=True)

# ===== INPUT FIELDS =====
bride = st.text_input("👰 Bride's Name")
groom = st.text_input("🤵 Groom's Name")
vibe = st.selectbox("🎉 Wedding Vibe", ["Romantic", "Royal", "Fun", "Desi", "Elegant"])
year = st.text_input("📅 Wedding Year", "2025")

# ===== HASHTAG LOGIC =====
def generate_fullname_hashtags(bride, groom, year, vibe):
    b = bride.strip().capitalize()
    g = groom.strip().capitalize()
    
    romantic = [
        f"#{g}Hearts{b}", f"#{g}And{b}Forever", f"#{g}Weds{b}InLove", f"#TogetherWith{b}And{g}", f"#{g}{b}Romance{year}", f"#Purely{b}n{g}", f"#MadeForEachOther{g}{b}", f"#Forever{g}And{b}", f"#TieTheKnotWith{b}{g}", f"#RomanticSagaOf{b}{g}"
    ]
    royal = [
        f"#{g}RoyaltyWith{b}", f"#TheMajestic{b}{g}Affair", f"#RegalShaadiOf{g}And{b}", f"#RoyaltyMeetsLove{g}{b}", f"#RajwadaVows{g}{b}", f"#CrownAndHearts{b}And{g}", f"#SovereignShaadi{b}{g}", f"#PalaceVibesWith{g}{b}", f"#DynastyOf{g}{b}", f"#ThroneForTwo{g}{b}"
    ]
    fun = [
        f"#{g}KiShaadiFunKeSaath", f"#BaraatiGoneCrazy{year}", f"#DanceFloorOnFire{g}{b}", f"#ShaadiFullOn{b}{g}", f"#MadFunWith{g}And{b}", f"#PatakhaVibes{b}And{g}", f"#JollyShaadi{g}{b}", f"#NoSleepTillShaadi{g}{b}", f"#CrazyInLove{b}{g}", f"#BandBaaja{g}With{b}"
    ]
    desi = [
        f"#DesiShaadiWith{b}{g}", f"#GharKiShaadi{g}{b}", f"#DholTasha{b}{g}", f"#NaachGaana{g}{b}", f"#RasamWith{b}And{g}", f"#DesiLoveSaga{b}{g}", f"#HaldiShaadi{b}{g}", f"#PunjabiTadka{g}{b}", f"#RangBarseShaadi{b}{g}", f"#FullDesiMela{g}{b}"
    ]
    elegant = [
        f"#ClassyShaadiOf{g}And{b}", f"#TimelessLove{g}{b}", f"#TheElegantAffair{b}{g}", f"#VowsWithGrace{b}And{g}", f"#SimpleYetRoyal{g}{b}", f"#EleganceRedefined{g}{b}", f"#PoisedAndPerfect{b}{g}", f"#Eleganza{g}{b}", f"#VintageVows{g}{b}", f"#TheChicWedding{b}{g}"
    ]
    
    hashtag_pool = {
        "Romantic": romantic,
        "Royal": royal,
        "Fun": fun,
        "Desi": desi,
        "Elegant": elegant
    }

    return hashtag_pool.get(vibe, romantic)[:10]

def generate_merged_hashtags(bride, groom):
    b = bride.strip().capitalize()
    g = groom.strip().capitalize()
    return [
        f"#{b[:3]}{g[-3:]}KiShaadi",
        f"#{g[:2]}{b[-2:]}Forever",
        f"#{b[:2]}And{g[:2]}LoveStory",
        f"#M{g}{b}TieTheKnot",
        f"#Team{b[:3]}{g[:2]}",
        f"#Foreveril{b[:2]}",
        f"#Happily{b[:2]}{g[:1]}",
        f"#ShaadiGoals{b[:2]}{g[:2]}",
        f"#DreamWeddingOf{b[:2]}{g[:2]}",
        f"#{b[:1]}{g[:3]}Wed"
    ]

# ===== GENERATE BUTTON =====
if st.button("💍 Generate My Wedding Hashtags"):
    if bride and groom:
        full_hashtags = generate_fullname_hashtags(bride, groom, year, vibe)
        merged_hashtags = generate_merged_hashtags(bride, groom)

        st.markdown("<hr>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
                <div style='background-color:#FFB347; padding: 20px; border-radius: 10px; font-family: "Times New Roman", serif;'>
                    <h3 style='text-align: center; color: black; font-size: 26px;'>✨ Trending Wedding Hashtags</h3>
                    <div style='background-color: black; padding: 15px; border-radius: 10px;'>
            """, unsafe_allow_html=True)
            for tag in full_hashtags:
                st.markdown(f"<p style='color:#00FFCC; font-size:20px; font-family: \"Times New Roman\", serif;'>✅ {tag}</p>", unsafe_allow_html=True)
            st.markdown("</div></div>", unsafe_allow_html=True)

        with col2:
            st.markdown("""
                <div style='background-color:#FFB347; padding: 20px; border-radius: 10px; font-family: "Times New Roman", serif;'>
                    <h3 style='text-align: center; color: black; font-size: 26px;'>🔀 Name Fusion Hashtags</h3>
                    <div style='background-color: black; padding: 15px; border-radius: 10px;'>
            """, unsafe_allow_html=True)
            for tag in merged_hashtags:
                st.markdown(f"<p style='color:#98FF98; font-size:20px; font-family: \"Times New Roman\", serif;'>✅ {tag}</p>", unsafe_allow_html=True)
            st.markdown("</div></div>", unsafe_allow_html=True)

# ===== FOOTER =====
st.markdown("""
    <hr style='border-top: 2px dashed #FFD700; margin-top: 50px;'>
    <div style='text-align:center; background-color:black; padding: 18px; border-radius: 10px; font-family: "Times New Roman", serif;'>
        <p style='color: #FFD700; font-size:22px;'>🎨 A canvas of words for your timeless romance 🎨</p>
        <p style='color: #FAFAD2; font-size:20px;'><strong>Powered by <span style="color:#FFD700;">The Royals 💍</span> | Crafted with 💛 and code</strong></p>
    </div>
""", unsafe_allow_html=True)
