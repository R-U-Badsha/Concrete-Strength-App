import streamlit as st
import pickle
import numpy as np

# মডেল লোড করা
model = pickle.load(open('concrete_model.pkl', 'rb'))

st.title("কংক্রিটের শক্তি নির্ণয়কারী এআই (Concrete Strength Predictor)")
st.write("নিচের বক্সে কংক্রিটের উপাদানগুলোর পরিমাণ (kg/m³) এবং বয়স দিন হিসেবে ইনপুট দিন:")

# ইনপুট নেওয়ার জন্য ফিল্ড বা বক্স তৈরি
cement = st.number_input("সিমেন্ট (Cement):", value=300.0)
blast_furnace_slag = st.number_input("ব্লাস্ট ফার্নেস স্ল্যাগ (Blast Furnace Slag):", value=0.0)
fly_ash = st.number_input("ফ্লাই অ্যাশ (Fly Ash):", value=0.0)
water = st.number_input("পানি (Water):", value=180.0)
superplasticizer = st.number_input("সুপারপ্লাস্টিকাইজার (Superplasticizer):", value=0.0)
coarse_aggregate = st.number_input("কোয়ার্স এগ্রিগেট (Coarse Aggregate):", value=1000.0)
fine_aggregate = st.number_input("ফাইন এগ্রিগেট / বালি (Fine Aggregate):", value=750.0)
age = st.number_input("বয়স (Age in days):", value=28.0)

# প্রেডিকশন বা ফলাফল বের করার বাটন
if st.button("শক্তি পরিমাপ করুন (Predict Strength)"):
    # ইনপুটগুলোকে অ্যারেতে রূপান্তর
    features = np.array([[cement, blast_furnace_slag, fly_ash, water, superplasticizer, coarse_aggregate, fine_aggregate, age]])
    
    # এআই মডেল দিয়ে প্রেডিকশন
    prediction = model.predict(features)
    strength = round(prediction[0], 2)
    
    st.success(f"কংক্রিটের আনুমানিক শক্তি (Compressive Strength): *{strength} MPa*")