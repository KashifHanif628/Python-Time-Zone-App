import streamlit as st
from datetime import datetime  # 🕰️ Built-in Python module for handling date & time
from zoneinfo import ZoneInfo  # 🌍 Provides time zones from around the world

# ✨ Available Time Zones List ✨
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

st.title("⏳✨ 𝕋𝕚𝕞𝕖 ℤ𝕠𝕟𝕖 𝔸𝕡𝕡 ✨⏳")  # Stylish Symbolic Title

# 🌟 Multi-Select Dropdown for Time Zones 🌟
selected_timezone = st.multiselect(
    "🌍 **𝓢𝓮𝓵𝓮𝓬𝓽 𝓣𝓲𝓶𝓮𝔃𝓸𝓷𝓮𝓼** 🕰️", TIME_ZONES, default=["UTC", "Asia/Karachi"]
)

# 🕰️ Display current time for selected time zones
st.subheader("📌 **𝓢𝓮𝓵𝓮𝓬𝓽𝓮𝓭 𝓣𝓲𝓶𝓮𝔃𝓸𝓷𝓮𝓼** 🌟")
for tz in selected_timezone:  # tz is short for timezone  
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d ⏰ %I:%M:%S %p")  
    st.write(f"🌍 **{tz}** → 🕒 {current_time}")

# 🔄 Time Conversion Section 🔄
st.subheader("🔄 **𝓣𝓲𝓶𝓮 𝓒𝓸𝓷𝓿𝓮𝓻𝓼𝓲𝓸𝓷** 🌍")

# ⏳ Time Input Field ⏳
current_time = st.time_input("⏳ **𝓔𝓷𝓽𝓮𝓻 𝓣𝓲𝓶𝓮**", value=datetime.now().time())

# 🌍 Select Source Timezone 🌍
from_tz = st.selectbox("🌎 **𝓕𝓻𝓸𝓶 𝓣𝓲𝓶𝓮𝔃𝓸𝓷𝓮** 🏁", TIME_ZONES, index=0)

# 🎯 Select Target Timezone 🎯
to_tz = st.selectbox("🚀 **𝓣𝓸 𝓣𝓲𝓶𝓮𝔃𝓸𝓷𝓮** 🎯", TIME_ZONES, index=1)

# 🔘 Convert Button 🔘
if st.button("🔄 **𝓒𝓸𝓷𝓿𝓮𝓻𝓽 𝓣𝓲𝓶𝓮** ⏳"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d ⏰ %I:%M:%S %p")
    st.success(f"✅ **Converted Time in {to_tz}** → 🕒 {converted_time}")
