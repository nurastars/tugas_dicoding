 # import module
import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt


# reading file
tugasKu = pd.read_csv('dataku.csv')
corelasi = tugasKu.pivot_table(index='season', columns='weather_situation', values='registered', aggfunc='sum')
## dashboard
st.title('bike rental :red[analysis] :bike: :bar_chart: :chart_with_upwards_trend:')
st.markdown('melakukan prediksi kepada para penggemar bike, akan menjadi prospek business yang sangat besar jika memamfaatkan deta semaksimal mungki untuk mendapatkan insight diluar nalar')

tab1, tab2, tab3 = st.tabs(['**Data :clipboard:**', '**analisi penggunaan :bike:**', '**prediksi :chart_with_upwards_trend:**'])

with tab1:
    st.header('EXploratory data analysis terhadap bike dataset')
    st.markdown('**Original Data** yang sebagian sudah di olah, guna mudah dipahami dan di analisa')
    st.write(tugasKu)

    st.header('jumlah para rentalers di setiap musimnya')
    st.write(corelasi)
with tab2:
    st.header('corelasi keadaan cuaca disetiap harinya')
    corr = corelasi.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style('white'):
        f,ax = plt.subplots(figsize=(7,5))
        ax = sns.heatmap(corr, cmap='bwr',  annot=True, mask=mask, fmt='.1f', square=True, cbar=True)
    st.pyplot(f)

    st.header('**Perbandingan time_working dengan time_holiday**')
    st.markdown('berdasarkan data yang ada, peminat bike pada time_working dan time_holiday sama-sama meningkat, hanya saja dipengaruhi cuaca')
    #plt.subplots(figsize=(10,9))
    st.pyplot(sns.catplot(data=tugasKu, x='working_day', y='count', hue='season', kind='bar'))
    #st.pyplot= adalah figure yang besertakan ukurannya
    
    st.header('**data musiman**')
    st.markdown('perbandingan musim di setiap bulannya')
    fig,ax = plt.subplots(figsize= (12,5))
    ax= sns.barplot(data=tugasKu, x='month', y='count', hue='season')
    st.pyplot(fig)

    st.header('**hubungan keadaan cuaca dengan musim**')
    st.pyplot(sns.pairplot(tugasKu, hue='season', vars = ['temp', 'humidity','wind_speed']))

    st.header('**hubungan keadaan cuaca dengan aktifitas keseharian**')
    st.pyplot(sns.pairplot(tugasKu, hue='working_day', vars = ['temp', 'humidity','wind_speed']))

with tab3:
    st.header('**prediksi peningkatan setiap tahun**')
    st.markdown('berdasarkan data, besar kemungkinan peminat bike akan semakin meningkat di setiap tahunnya, tentu tetap memperhatikan cuaca dan keadaan lingkungan pada setiap musimnya')
    
    fig,ax = plt.subplots(figsize= (5,5))
    ax= sns.barplot(data=tugasKu, x='year', y='count', hue='season')
    st.pyplot(fig)