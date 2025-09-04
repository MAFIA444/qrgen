import streamlit as st
import qrcode

st.title("QR Code Generator")

url = st.text_input("Enter the URL")
app_name = st.text_input("Enter File Name:")

if st.button("Generate QR Code"):
    if url and app_name:
        qr = qrcode.make(url)
        qr.save(f"{app_name}.png")

        st.success("✅ QR Code generated successfully!")
        st.image(f"{app_name}.png")
    else:
        st.error("⚠️ Please enter both a URL and a file name.")
