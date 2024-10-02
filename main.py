import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st


mean_df = pd.read_csv('dataset/mean_season_hour.csv')
casual_registered_df = pd.read_csv('dataset/casual_registered.csv')
pm_df = pd.read_csv('dataset/pm_hour.csv')
am_df = pd.read_csv('dataset/am_hour.csv')

st.title('Bicycle Rental Dashboard :sparkles:')


st.subheader('Average bicycle renter each season')

col1, col2, col3, col4 = st.columns(4)

with col1:
    spring_average = mean_df[mean_df['season'] == 'Spring']['cnt'].values[0]
    st.metric("spring Average", value=round(spring_average, 2))

with col2:
    winter_average = mean_df[mean_df['season'] == 'Winter']['cnt'].values[0]
    st.metric("Winter Average", value=round(winter_average, 2))

with col3:
    summer_average = mean_df[mean_df['season'] == 'Summer']['cnt'].values[0]
    st.metric("summer Average", value=round(summer_average, 2))

with col4:
    fall_average = mean_df[mean_df['season'] == 'Fall']['cnt'].values[0]
    st.metric("Fall Average", value=round(fall_average, 2))

colors = ["#D3D3D3","#D3D3D3", "#D3D3D3", "#72BCD4"]
fig, ax = plt.subplots(figsize=(12, 7))

sns.barplot(
    x='season',
    y='cnt',
    data=mean_df,
    palette=colors,
    hue='season',
    legend=False
)

st.pyplot(fig)

st.subheader('Most popular customer type in each season')
sns.barplot(
    x='season',
    y='count',
    data=casual_registered_df,
    hue='cust_type'
)

plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)
st.pyplot(fig)

st.subheader('Most popular customer type between 12 PM - 11 PM')
fig, ax = plt.subplots(figsize=(12, 7))
sns.barplot(
    x='hr',
    y='count',
    data=pm_df,
    hue='cust_type',
    ax=ax
)

ax.grid(True, alpha=0.3)
st.pyplot(fig=fig)

st.subheader('Most popular customer type between 12 AM - 11 AM')
fig, ax = plt.subplots(figsize=(12, 7))
sns.barplot(
    x='hr',
    y='count',
    data=am_df,
    hue='cust_type',
    ax=ax
)

ax.grid(True, alpha=0.3)
st.pyplot(fig=fig)