import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
from preprocessor import Preprocessor
import time
df = pd.read_csv('cleaned_5250.csv')
st.sidebar.title('A DETAILED STUDY ON :red[NASA] :blue[EXOPLANETS]')
st.sidebar.image('NASA_logo.png')
strt = st.sidebar.radio('Menu',['Introduction',
                         'Overall Analysis',
                         'Each Planet Analysis'
                         # 'Comparing Any two planets',
                         # 'Explore The Habitable Planets'
                         ])

st.sidebar.caption('This is just a demo version , I will update this app on a regular basis, as soon as i get new ideas,'
                   'Thank you for visiting')
nasa = Preprocessor(df)

if strt == 'Introduction':
    st.snow()
    st.title(':red[N]:blue[A]:red[S]:blue[A] EXOPLANETS')
    st.title('')
    st.title('')
    col1, col2 = st.columns(2)
    with col1:
        st.image('NASA_logo.png')
    with col2:
        st.subheader('About NASA')
        st.caption(
            '''NASA, or the National Aeronautics and Space Administration, is a US government agency responsible for leading the country's civilian space program, as well as aeronautics and aerospace research. Established in 1958, NASA has been at the forefront of space exploration, launching manned and unmanned missions to explore the Moon, Mars, and beyond. NASA has also developed numerous technologies that have been adapted for use in everyday life, such as water filters, artificial limbs, and cordless power tools. The agency is headquartered in Washington D.C. and employs over 17,000 people across the United States.''')

    st.subheader('About This Project')
    cola, colb = st.columns(2)
    with cola:
        st.caption(
            '''The project will involve analyzing data from NASA's Kepler and TESS missions, which have discovered thousands of exoplanets orbiting stars outside our solar system. The goal of the project is to use statistical analysis and machine learning techniques to better understand the properties of these exoplanets, such as their size, mass, and orbital characteristics. The project will involve cleaning and processing large datasets, performing exploratory data analysis to identify patterns and trends, and building predictive models to make predictions about the properties of newly discovered exoplanets. The results of the analysis may help to shed light on the formation and evolution of planetary systems and contribute to the search for potentially habitable worlds beyond our own.''')
    with colb:
        st.image('Jupiter-PNG-HD-Quality.png')
    with cola:
        st.title('Types of Exoplanets')
        st.subheader('1. Neptune Like')
        st.image('Neptune_cutout.png')
    with colb:
        st.caption('''Neptune-like planets, also known as ice giants, are a type of planet that shares similar characteristics with Neptune, the eighth planet in our solar system. These planets are usually located beyond the frost line of their star system, which is the distance from the star beyond which water and other volatile compounds can condense into solid ice.

Neptune-like planets are typically composed of a rocky core surrounded by a thick layer of hydrogen and helium gas, and an outer layer of water, methane, and ammonia ices. They are smaller and less massive than gas giants like Jupiter and Saturn, but larger and more massive than terrestrial planets like Earth.

The atmosphere of a Neptune-like planet is characterized by strong winds, turbulent weather patterns, and intense storms. These planets have strong magnetic fields, which trap charged particles from the solar wind and create auroras similar to those on Earth.

One notable example of a Neptune-like planet is Kepler-438b, which is located approximately 640 light-years from Earth.''')
    with colb:
        st.image('super_earth.png')
    with cola:
        st.subheader('2. Super Earth')
        st.caption('''Super Earths are a class of exoplanets that are more massive than Earth but less massive than gas giants like Jupiter. They typically have a rocky or icy core and a thick atmosphere composed of hydrogen and helium gas, but may also have oceans or ice layers depending on their distance from their host star.

Super Earths are of interest to astronomers because they are the most common type of exoplanet discovered so far. They are thought to form through a process similar to that of the terrestrial planets in our solar system, but with a higher density of materials available for accretion.''')

    with colb:
        st.subheader('3. Terrestrial')
        st.caption('''Terrestrial planets are a class of planets that are similar in size, mass, and composition to Earth. They are primarily composed of rocks or metals and have a solid surface, unlike gas giants like Jupiter and Saturn. In our solar system, the terrestrial planets include Mercury, Venus, Earth, and Mars.

Terrestrial planets are thought to have formed closer to their host star than the gas giants, where the temperature was high enough to vaporize volatile compounds like water and methane. As a result, they have lower atmospheric content and are denser than gas giants.''')
    with cola:
        st.image('terrestrial.png')
    with cola:
        st.subheader('4. Gas Giant')
        st.caption('''Gas giants are a class of planets that are similar in size, mass, and composition to Jupiter and Saturn in our solar system. They are called gas giants because they are primarily composed of hydrogen and helium gas, with small amounts of other volatile compounds like methane, ammonia, and water.

Gas giants are much larger and more massive than terrestrial planets like Earth, with thick atmospheres that extend far out from their solid cores. They do not have a well-defined surface, and their atmospheres are characterized by bands of different colors and patterns caused by swirling winds and storms.''')
    with colb:
        st.image('Jupiter-PNG-HD-Quality.png')
if strt == 'Each Planet Analysis':
    plnt_typ = st.sidebar.selectbox('SELECT PLANET TYPE',df['planet_type'].unique().tolist())
    planet = st.sidebar.selectbox('SELECT ONE PLANET',nasa.planets_list(plnt_typ))
    st.title(f'About :green[{planet}]')
    planet_info = df[df['name'] == planet]
    col1,col2 = st.columns(2)
    if planet_info['planet_type'].values[0] == 'Gas Giant':
        with col1:
            st.image('Jupiter-PNG-HD-Quality.png')
    elif planet_info['planet_type'].values[0] == 'Super Earth':
        with col1:
            st.image('super_earth.png')
    elif planet_info['planet_type'].values[0] == 'Neptune-like':
        with col1:
            st.image('Neptune_cutout.png')
    elif planet_info['planet_type'].values[0] == 'Terrestrial':
        with col1:
            st.image('terrestrial.png')
    else:
        with col1:
            st.image('black.png')

    with col2:
        cola,colb = st.columns(2)
        with cola:
            st.markdown(f'**:red[Planet Name]**: {planet}')
        with colb:
            st.markdown(f'**:red[Distance (in ly)]**: {planet_info["distance"].values[0]}')
        with cola:
               st.markdown(f'**:red[Stellar Magnitude]**:{planet_info["stellar_magnitude"].values[0]}')
        with colb:
            st.markdown(f'**:red[Planet Type]**: {planet_info["planet_type"].values[0]}')
        with cola:
            st.markdown(f'**:red[Discovery Year]**: {planet_info["discovery_year"].values[0]}')
        with colb:
            st.markdown(f'**:red[Mass Multiplier]**: {planet_info["mass_multiplier"].values[0]}')
        with cola:
            st.markdown(f'**:red[Mass wrt]**: {planet_info["mass_wrt"].values[0]}')
        with colb:
            st.markdown(f'**:red[Radius Multiplier]**: {planet_info["radius_multiplier"].values[0]}')
        with cola:
            st.markdown(f'**:red[Radius wrt]**: {planet_info["radius_wrt"].values[0]}')
        with colb:
            st.markdown(f'**:red[Orbital Radius(in AU)]**: {planet_info["orbital_radius"].values[0]}')
        with cola:
            st.markdown(f'**:red[Orbital Period (in years)]**: {planet_info["orbital_period"].values[0]}')
        with colb:
            st.markdown(f'**:red[Eccentricity]**: {planet_info["eccentricity"].values[0]}')
        with cola:
            st.markdown(f'**:red[Detection Method]**: {planet_info["detection_method"].values[0]}')

    st.subheader(f'How :green[long] will it take to reach :red[{planet}] from :blue[earth]')
    transport = st.selectbox('CHOSE ONE MEDIUM TO REACH THIS PLANET',['Speed of Light','Voyager','Jet','Bullet-Train','Car','Space Swimming'])
    cola,colb = st.columns(2)
    stndrd_distance = planet_info['distance']
    if transport == 'Speed of Light':
        with cola:
            st.metric('Your Speed','300,000 km / s')
        with colb:
            st.metric('Time in years',stndrd_distance)
    if transport == 'Voyager':
        with cola:
            st.metric('Your Speed','17.8 km/s')
        with colb:
            st.metric('Time in Million Years',round(stndrd_distance*16854/1000000,2))
    if transport == 'Jet':
        with cola:
            st.metric('Your Speed','2 km/s')
        with colb:
            st.metric('Time in Million Years',round(stndrd_distance*0.15,2))
    if transport == 'Bullet-Train':
        with cola:
            st.metric('Your Speed','0.16 km/s')
        with colb:
            st.metric('Time in Billion Years',round(stndrd_distance*0.001875,2))
    if transport == 'Car':
        with cola:
            st.metric('Your Speed','0.135 km/s')
        with colb:
            st.metric('Time in Billion Years',round(stndrd_distance*0.0022,2))
    if transport == 'Space Swimming':
        with cola:
            st.metric('Your Speed','0.0024 km/s')
        with colb:
            st.metric('Time in Billion Years',round(stndrd_distance*0.13368983957,2))



if strt == 'Overall Analysis':
    st.title(':red[Overall] :blue[Analysis]')
    st.subheader('Scatterplot between planet mass & planet radius')
    plnt_cmp = st.selectbox('Planets Comparable',['Jupiter','Earth'])
    temp_df = df[(df['mass_wrt']==plnt_cmp) & (df['radius_wrt'] == plnt_cmp)]
    st.write(f'Planets whose mass and size are comparable to {plnt_cmp}')
    cola,colb = st.columns(2)
    with cola:
        fig = px.scatter(temp_df,x='mass_multiplier',y='radius_multiplier',size='radius_multiplier',color='planet_type',title='scatter-plot radius vs mass')
        st.plotly_chart(fig)
    with colb:
        td = nasa.plnt_type_count()
        fig = px.pie(td,values='Count',names='Planet type',title='Planet type pie-chart')
        st.plotly_chart(fig)

    with cola:
        st.subheader(':red[Mass] wrt to :green[Earth] but :blue[radius] wrt to :brown[Jupiter]')
        temp_df2 = df[(df['mass_wrt']=='Earth') & (df['radius_wrt']=='Jupiter')]
        fig2 = px.scatter(temp_df2,x='mass_multiplier',y='radius_multiplier',size='radius_multiplier',color='planet_type')
        st.plotly_chart(fig2)
    with colb:
        st.subheader('Planet Discovery methods')
        td = nasa.detection_method_cnt()
        fig = px.pie(td,values='Count',names='Detection Method',title='Detection Method pie-chart')
        st.plotly_chart(fig)
    with colb:
        st.subheader(':red[Mass] wrt to :brown[Jupiter] but :blue[radius] wrt to :green[Earth]')
        temp_df3 = df[(df['mass_wrt']=='Jupiter') & (df['radius_wrt']=='Earth')]
        fig3 = px.scatter(temp_df3,x='mass_multiplier',y='radius_multiplier',size='radius_multiplier',color='planet_type')
        st.plotly_chart(fig3)
        st.info(' further observations and studies are needed to fully understand these objects.',icon="ℹ️")
    with cola:
        st.warning('what about those planets whose size are comparable to earth but mass comparable to jupiter',
                   icon="⚠️")
        st.caption('Here\'s Analysis for them')
        st.subheader('Some possible :red[Explainations..]')
        st.caption('''
        There are a few possible explanations for why some exoplanets can have a size similar to Earth but a mass greater than Jupiter:

Composition: Exoplanets that are primarily composed of dense materials like iron and rock can have a smaller size but greater mass compared to Jupiter, which is mostly composed of gas. A planet with a rocky or metallic core surrounded by a thick layer of gas can have a similar size to Earth but a much greater mass.

Atmosphere: An exoplanet with a thick and dense atmosphere can add significant mass to the planet without increasing its size. This can be seen in gas giants like Jupiter, which have relatively small rocky cores but massive gaseous atmospheres.

Density: The density of an exoplanet can affect its mass relative to its size. A planet with a higher density will have a greater mass for a given size compared to a planet with a lower density.

Gravitational compression: Exoplanets with a very high mass can experience gravitational compression, which can cause the planet to become more dense and compact. This can result in a smaller size but a greater mass compared to a less massive planet.

Overall, there can be many factors that contribute to an exoplanet having a size similar to Earth but a mass greater than Jupiter.
        ''')
    st.subheader('Let\'s see how many :green[planets] are :blue[discovered] every year')
    td = nasa.plnts_each_year()
    fig = px.bar(td,x='Discovery year',y='Count',color='Detection method')
    st.plotly_chart(fig)

    cola,colb = st.columns(2)
    with cola:
        st.subheader('Let\'s Study :orange[Stellar magnitude] of each planet type')
        fig,ax = plt.subplots()
        sns.kdeplot(data=df, x='stellar_magnitude', hue='planet_type',ax=ax)
        ax.grid(True)
        fig.set_size_inches(6,4)
        # sns.set_theme()
        st.pyplot(fig)
    with colb:
        st.subheader('Relation between :orange[stellar magnitude] and :blue[distance]')
        fig = px.scatter(df,y='stellar_magnitude',x='distance',color='planet_type')
        st.plotly_chart(fig)
        st.info('As distance is increasing, stellar magnitude is :green[logarithmically increasing]',icon="ℹ️")

    st.subheader('A :red[HeatMap] for planet type & detection method')
    fig,ax = plt.subplots()
    fig.set_size_inches(10,5)
    sns.heatmap(pd.pivot_table(df,values='discovery_year',index='detection_method',columns='planet_type',aggfunc='count',fill_value=0),ax=ax)
    plt.xlabel('Planet type')
    plt.ylabel('Detection method')
    sns.set_theme()
    st.pyplot(fig)
    st.info('As we can conclude from this heatmap is that it is directly telling us that :red[transit method] is most commonly used to discover planets in the outer space', icon="ℹ️")


