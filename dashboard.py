import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide"
)

# 2. Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("data/main_data.csv")
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

df = load_data()

# 3. Sidebar - Filter Dashboard
st.sidebar.title("Filter Dashboard")

season_options = ["All"] + df['season'].unique().tolist()
weather_options = ["All"] + df['weathersit'].unique().tolist()

selected_season = st.sidebar.selectbox(
    "Select Season",
    options=season_options,
    index=0
)

selected_weather = st.sidebar.selectbox(
    "Select Weather",
    options=weather_options,
    index=0
)

# 4. Filter DataFrame
filtered_df = df.copy()

if selected_season != "All":
    filtered_df = filtered_df[filtered_df['season'] == selected_season]

if selected_weather != "All":
    filtered_df = filtered_df[filtered_df['weathersit'] == selected_weather]

# 5. Header Dashboard
st.title("🚲 Bike Sharing Dashboard")
st.markdown("Dashboard ini menyajikan hasil analisis Bike Sharing Dataset tahun **2011–2012**.")

# 6. Metrics KPI
col1, col2, col3 = st.columns(3)

total_rentals = filtered_df['cnt'].sum()
avg_rentals = filtered_df['cnt'].mean() if not filtered_df.empty else 0
max_rentals = filtered_df['cnt'].max() if not filtered_df.empty else 0

col1.metric("Total Rentals", f"{total_rentals:,.0f}")
col2.metric("Average Rentals", f"{avg_rentals:,.1f}")
col3.metric("Maximum Rentals", f"{max_rentals:,.0f}")

st.divider()

# 7. Menampilkan Visualisasi Utama (Secara Vertikal)
if not filtered_df.empty:
    
    # --- GRAFIK 1: Pengaruh Cuaca Terhadap Penyewaan ---
    st.subheader("1️⃣ Average Rentals by Weather Condition")
    weather_avg = filtered_df.groupby('weathersit')['cnt'].mean().reset_index()
    fig_weather = px.bar(
        weather_avg,
        x='weathersit',
        y='cnt',
        labels={'weathersit': 'Weather Condition', 'cnt': 'Average Rentals'},
        color='weathersit',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig_weather.update_layout(showlegend=False)
    st.plotly_chart(fig_weather, use_container_width=True)

    st.divider()

    # --- GRAFIK 2: Tren Penyewaan di Weekend vs Weekday ---
    st.subheader("2️⃣ Average Rentals: Weekend/Holiday vs Weekday")
    
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekday_avg = filtered_df.groupby(['weekday', 'workingday'])['cnt'].mean().reset_index()
    weekday_avg['weekday'] = pd.Categorical(weekday_avg['weekday'], categories=day_order, ordered=True)
    weekday_avg = weekday_avg.sort_values('weekday')

    fig_weekday = px.bar(
        weekday_avg,
        x='weekday',
        y='cnt',
        color='workingday',
        barmode='group',
        labels={
            'weekday': 'Day of Week', 
            'cnt': 'Average Rentals', 
            'workingday': 'Day Type'
        },
        color_discrete_map={
            'Working Day': '#1f77b4', 
            'Holiday/Weekend': '#ff7f0e'
        }
    )
    st.plotly_chart(fig_weekday, use_container_width=True)

    st.divider()

    # --- GRAFIK 3: Scatter Plot Harian (Bersih & Tidak Menumpuk) ---
    st.subheader("3️⃣ Temperature vs Bike Rentals Distribution (Daily Level)")
    st.caption("Agregasi harian untuk melihat hubungan suhu dan jumlah penyewaan secara lebih jelas.")
    
    # Diagregasi ke tingkat harian agar titik tidak menumpuk
    daily_scatter = filtered_df.groupby(['dteday', 'weathersit']).agg(
        avg_temp=('temp', 'mean'),
        total_cnt=('cnt', 'sum')
    ).reset_index()

    fig_scatter = px.scatter(
        daily_scatter,
        x='avg_temp',
        y='total_cnt',
        color='weathersit',
        labels={
            'avg_temp': 'Average Temperature (Normalized)', 
            'total_cnt': 'Total Daily Rentals',
            'weathersit': 'Weather Condition'
        },
        opacity=0.75,
        color_discrete_sequence=px.colors.qualitative.Set1
    )
    fig_scatter.update_traces(marker=dict(size=8))
    st.plotly_chart(fig_scatter, use_container_width=True)

else:
    st.warning("Data tidak ditemukan untuk kombinasi filter ini.")

# 8. Menampilkan Data Mentah
with st.expander("📄 Lihat Data Mentah (Filtered Data)"):
    st.dataframe(filtered_df)