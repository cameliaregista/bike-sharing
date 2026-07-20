import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =====================================================
# Page Configuration
# =====================================================

st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide"
)

sns.set_style("whitegrid")

# =====================================================
# Load Data
# =====================================================

day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

# =====================================================
# Mapping Label
# =====================================================

season_labels = {
    1: "Spring",
    2: "Summer",
    3: "Fall",
    4: "Winter"
}

weather_labels = {
    1: "Clear",
    2: "Mist",
    3: "Light Snow/Rain",
    4: "Heavy Rain"
}

workingday_labels = {
    0: "Holiday/Weekend",
    1: "Working Day"
}

day_df["season"] = day_df["season"].map(season_labels)
day_df["weathersit"] = day_df["weathersit"].map(weather_labels)

hour_df["workingday"] = hour_df["workingday"].map(workingday_labels)

# =====================================================
# Sidebar
# =====================================================

st.sidebar.header("Filter Dashboard")

selected_season = st.sidebar.multiselect(
    "Select Season",
    options=day_df["season"].unique(),
    default=day_df["season"].unique()
)

filtered_day = day_df[
    day_df["season"].isin(selected_season)
]

# =====================================================
# Dashboard Title
# =====================================================

st.title("🚲 Bike Sharing Dashboard")

st.markdown("""
Dashboard ini menyajikan hasil analisis Bike Sharing Dataset tahun **2011–2012**.
""")

# =====================================================
# KPI
# =====================================================

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Rentals",
    f"{filtered_day['cnt'].sum():,.0f}"
)

col2.metric(
    "Average Rentals",
    f"{filtered_day['cnt'].mean():.0f}"
)

col3.metric(
    "Maximum Rentals",
    f"{filtered_day['cnt'].max():,.0f}"
)

st.markdown("---")

# =====================================================
# Business Question 1
# =====================================================

st.subheader("1️⃣ Average Bike Rentals by Weather Condition")

weather_avg = (
    filtered_day.groupby("weathersit")["cnt"]
    .mean()
    .reset_index()
)

fig, ax = plt.subplots(figsize=(8,5))

sns.barplot(
    data=weather_avg,
    x="weathersit",
    y="cnt",
    palette="Blues_d",
    ax=ax
)

ax.set_xlabel("Weather Condition")
ax.set_ylabel("Average Rentals")
ax.set_title("Average Bike Rentals by Weather")

st.pyplot(fig)

st.info(
"""
**Insight**

- Cuaca cerah menghasilkan rata-rata penyewaan tertinggi.
- Semakin buruk kondisi cuaca, rata-rata penyewaan semakin menurun.
"""
)

# =====================================================
# Business Question 2
# =====================================================

st.subheader("2️⃣ Hourly Rental Pattern")

hour_pattern = (
    hour_df
    .groupby(["workingday","hr"])["cnt"]
    .mean()
    .reset_index()
)

fig2, ax2 = plt.subplots(figsize=(10,5))

sns.lineplot(
    data=hour_pattern,
    x="hr",
    y="cnt",
    hue="workingday",
    linewidth=3,
    ax=ax2
)

ax2.set_xlabel("Hour")
ax2.set_ylabel("Average Rentals")
ax2.set_title("Hourly Bike Rental Pattern")

st.pyplot(fig2)

st.info(
"""
**Insight**

- Hari kerja menunjukkan dua jam sibuk pada pagi dan sore hari.
- Hari libur memiliki pola yang lebih merata dengan puncak pada siang hari.
"""
)

# =====================================================
# Recommendation
# =====================================================

st.markdown("---")

st.header("💡 Recommendation")

st.success("""
- Menambah jumlah sepeda pada jam sibuk (07.00–09.00 dan 16.00–18.00).
- Mengoptimalkan redistribusi sepeda berdasarkan pola permintaan.
- Memberikan promo pada kondisi cuaca buruk untuk meningkatkan penggunaan layanan.
""")

# =====================================================
# Footer
# =====================================================

st.caption("Bike Sharing Dashboard | Data Analysis Project")