import streamlit as st
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load model and tokenizer from folder
@st.cache_resource
def load_model():
    model = T5ForConditionalGeneration.from_pretrained("hashtag_model")
    tokenizer = T5Tokenizer.from_pretrained("hashtag_model")
    return model, tokenizer

model, tokenizer = load_model()

st.title("💍 Wedding Hashtag Generator (AI-Powered)")
st.markdown("Get creative, unique wedding hashtags instantly using AI 🤖")

bride = st.text_input("👰 Bride's Name")
groom = st.text_input("🤵 Groom's Name")
vibe = st.selectbox("🎉 Wedding Vibe", ["Romantic", "Royal", "Fun", "Desi", "Elegant"])
year = st.text_input("📅 Wedding Year", "2025")

if st.button("Generate Hashtags"):
    prompt = f"""
    Generate 5 unique wedding hashtags using bride and groom names.
    Output only hashtags. No extra text.

    Examples: #DeepVeerKiShaadi #VirushkaForever #RanAlia2025 #ShaadiWithSidKiara

    Bride: {bride}
    Groom: {groom}
    Vibe: {vibe}
    Year: {year}

    Hashtags:
    """
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    output = model.generate(input_ids, max_length=96, temperature=0.9, do_sample=True)

    result = tokenizer.decode(output[0], skip_special_tokens=True)
    hashtags = [tag for tag in result.split() if tag.startswith("#")]

    st.success("✨ Your Hashtags:")
    for tag in hashtags[:5]:
        st.write(tag)
