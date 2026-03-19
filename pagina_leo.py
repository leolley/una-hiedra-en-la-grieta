# Primero importamos las librerías necesarias
import streamlit as st # pagina web
import pandas as pd # bases de datos
import folium # mapa
import streamlit.components.v1 as components 
from streamlit_folium import st_folium
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="La hiedra en la grieta",
    page_icon="🍃",
    layout="wide"
)

st.markdown("""
    <style>
    /* Texto dentro del selectbox */
    section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
        font-size: 18px !important;
        font-weight: bold !important;
    }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu("Explora por aquí :)",["Entre líneas", "Después de leer", "Intelectuales en el mundo", "Versos sueltos"], 
        icons=['house', 'pencil', 'map', 'book'], menu_icon="cast", default_index=1)


st.markdown("""
<style>
.block-container {
    padding-top: 1rem;
}

img {
    margin-bottom: 5px !important;
}
</style>
""", unsafe_allow_html=True)

if selected == "Entre líneas":
    #col1, col2, col3 = st.columns([1,2,1])

    #with col2:
        #st.image("fotos/logo.png", width=1600)

    título = """
    Sobre mí
    """
    st.markdown(f"<div style='text-align: center; font-size: 60px; color: #a256d6; font-weight: bold'>{título}</div>", unsafe_allow_html=True)
    
    st.write("")
    

    col1, col2 = st.columns([1,2]) #Esto es la extensión de columnas

    with col1:
        st.image("foto_guapa.jpeg", width=350) #Esta es la extensión de mi foto
    with col2:
        texto_1 = """
        Soy filósofa en formación, predocente e investigadora en mis tiempos no-libres. Somos del mismo nicho si sientes amor por los animales. Me gustan las artes marciales y me considero amateur en botánica. Fan de One Piece y la música, tanto en sus distintos géneros, bailes e instrumentos. 
        Feminista decolonial, teórica y activista. Salgo de la academia para no seguir a la masa con ideas en torno a "la filosofía es para unos pocos" (¡qué pereza defender el engaño de un genio maligno!).
        En estos apartados encontrarás desde cuestionamientos de y a los feminismos, aproximaciones a las epistemologías contemporáneas, debates en torno a la razón y la lógica, y toda la sabiduría que me comparten los estudios de género. Todo ello conectado, por supuesto, con nuestros problemas cotidianos, la política peruana y cultura pop.
        Porque sí, Rick, no todo se trata de abstraer conceptos y llegar al mundo de las Ideas en esta efímera vida.
        ¡Espero lo disfrutes! Aconsejo empezar por el vídeo "la hiedra en la grieta", que es motivo de este blog, y cuyo nombre es la inspiración para crear este diario virtual y difundir mis conocimientos.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 22px'>{texto_1}</div>", unsafe_allow_html=True)
 
    st.write("")

    col3, col4 = st.columns([2,1.5]) #Si quiero agrandar el vídeo de la hiedra, solo incremento el 1.5.

    with col3:
        texto_2 = """
        Explicación de por qué 'la hiedra en la grieta'.
        Si tienes interés en conocer el mundo del python, desde las humanidades, comunícate con luisa.gomez@pucp.edu.pe
        """
        st.markdown(f"<div style='text-align: justify; font-size: 22px'>{texto_2}</div>", unsafe_allow_html=True)
    
    with col4:
        st.video("https://youtu.be/sAVNZkBlg38")

elif selected == "Después de leer":
    st.markdown("""
    <h1 style="
        font-size:65px;
        color:#9a62a5;
        font-weight:900;
        text-align:center;
        margin-bottom:20px;
    ">
    Después de leer
    </h1>
    """, unsafe_allow_html=True)

    Reseña = st.selectbox(
    "Selecciona el título: ", ["Feminismo y neoliberalismo: la incómoda historia de la segunda ola",
    "El (des)orden de las cosas: ¿cómo romper con la herencia patriarcal?"                           
    ]) #Aquí voy enlistado los títulos de mis reseñas (que la paciencia de luisa me perdone)

#Aquí comienza mi reseña 1
    if Reseña == "Feminismo y neoliberalismo: la incómoda historia de la segunda ola":
        st.markdown("""
        <h2 style="
            font-size:25px;
            color:#9a62a5;
            font-weight:900;
            text-align:center;
            margin-bottom:18px;
        ">
        Feminismo y neoliberalismo: la incómoda historia de la segunda ola
        </h2>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style="text-align: justify; font-size:18px;">
        <p>
        Hablar del feminismo de la segunda ola sin hablar del capitalismo es, sencillamente, imposible. 
        Ambos procesos históricos crecieron en paralelo y, aunque muchas veces se los presenta como fuerzas opuestas, la relación entre ellos es más compleja e incómoda de lo que solemos admitir. 
        No podemos negar que la segunda ola avanzó en proyectos que favorecen en al menos tres dimensiones de la justicia: el reconocimiento (visibilizar la subordinación de las mujeres), la redistribución (exigir igualdad económica y laboral) y la representación (ampliar la participación política de las mujeres); 
        no obstante, también debemos reconocer que parte de sus demandas resultaron ser beneficiosas para las transformaciones del capitalismo.
        </p>
                    
        <p>
        De ahí que la filósofa política Nancy Fraser nos plantee la siguiente pregunta en su artículo titulado <i>El feminismo, el capitalismo y la astucia de la historia</i> (2020): “¿Fue mera coincidencia que la segunda ola feminista y el neoliberalismo prosperasen unidos? ¿O había una perversa y soterrada afinidad electiva entre ellos?” (p. 148). 
        Planteado de otro modo: <b>¿por qué no reconocer que algunas de las demandas de la segunda ola feminista terminaron convergiendo con las transformaciones del capitalismo neoliberal?</b> El objetivo de este escrito no busca desacreditar los logros del feminismo, sino detenernos a pensar en sus límites históricos. </p>
        
                    
        </div>
        """, unsafe_allow_html=True) #Para colocar en cursiva, coloco dentro de la frase <i>...</i>
        #Para colocar en negrita, dentro de la frase <b>...</b>
        col7,col8 = st.columns (2)
       #Estructurar la visualización de las imágenes como columnas
        with col7: 
            st.image("https://www.biografiasyvidas.com/biografia/f/fotos/fiedan_1971.jpg", width=500)
        with col8: 
            st.image("https://pymstatic.com/5625/conversions/segunda-ola-feminismo-default.jpg")
        
        st.markdown("""
        <div style="text-align: justify; font-size:18px;">
        <p>
        Así, mientras que el feminismo exigía emancipación, el capitalismo reorganizaba el trabajo y promovía el modelo de doble ingreso familiar. 
        Aquí aparece la tensión central, pues la incorporación masiva de mujeres al mercado laboral, consolidada por la segunda ola en la década de 1960, no eliminó la división sexual del trabajo —uno de los objetivos principales del feminismo—; 
        caso contrario, la duplicó. ¿Cuál es, entonces, el resultado que aún persiste hoy en día? El trabajo doméstico y de cuidados sigue recayendo de manera desproporcionada sobre aquellas mujeres cuyas condiciones de clase o color influyen más en su trayectoria, como ser mujer andina y quechua hablante en nuestro contexto peruano. 
        Son estas mujeres quienes experimentan de forma más aguda las desigualdades asociadas al trabajo doméstico, donde las condiciones laborales son frecuentemente más precarias, peor remuneradas y socialmente menos valoradas.
        </p>
         
               
        </div>
        """, unsafe_allow_html=True) #Aquí termina mi reseña 1

#Aquí comienza mi reseña 2
    elif Reseña == "El (des)orden de las cosas: ¿cómo romper con la herencia patriarcal?":
        st.markdown("""
        <h2 style="
            font-size:25px;
            color:#9a62a5;
            font-weight:900;
            text-align:center;
            margin-bottom:18px;
        ">
        El (des)orden de las cosas: ¿cómo romper con la herencia patriarcal?
        </h2>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style="text-align: justify; width:60%; margin-left:auto; font-size:18px;"> 
        <p>
        <i>Las profundas transformaciones ocurridas en las relaciones de género en el mundo, producen cambios ferozmente complejos en las condiciones de la práctica a la que deben adherir tanto hombres como mujeres. <b>Nadie es un espectador inocente en este escenario de cambio. Estamos todos comprometidos en construir un mundo de relaciones de género.</b></i>
        </p> <p style="text-indent: 560px;">   Raewyn Connell
        </p>

        <p>
        <i>El verdadero enfoque del cambio revolucionario no está nunca meramente en las situaciones opresivas de las que buscamos escapar, sino <b>en ese pedazo del opresor que llevamos plantado profundamente en cada uno de nosotros.</b></i>
        <br></p> <p style="text-indent: 570px;">   Audre Lorde
        </p> 

        <p>
        <i>Hasta ahora, los filósofos solo han interpretado el mundo de diversas maneras; <b>de lo que se trata es de transformarlo.</b></i>
        <br></p> <p style="text-indent: 580px;">   Karl Marx
        </p>  
                                   
        </div>
        """, unsafe_allow_html=True) #Para colocar en cursiva, coloco dentro de la frase <i>...</i>
        #Para colocar en negrita, dentro de la frase <b>...</b>
        #Aquí fueron las citas. Continuo con la reseña
#Aquí inicia un markdown (estructura de texto con su estilo, alias Luisa)
        st.markdown("""
        <div style="text-align: justify; font-size:18px;"> 
        <p>
        El género como categoría de análisis es una herramienta necesaria para comprender las dinámicas en nuestras interacciones humanas. 
        Además, nos invita a cuestionar los roles impuestos por la sociedad y, con ello, la construcción histórica, racial y patriarcal de los mismos. 
        En este apartado, demostraré estos dos puntos, el de análisis y cuestionamiento, con el cortometraje español <i>El orden de las cosas</i> (2010), dirigido por los hermanos Esteban Alenda. 
        Este producto audiovisual nos permite dar cuenta, en un aproximado de 20 minutos, que la violencia, muchas veces, no se muestra de forma evidente. 
        Es en el silencio, en los gestos cotidianos y la complicidad de terceros donde también se manifiesta la violencia para seguir manteniendo el orden, sin necesitar gritos ni escenas dramáticas. 
        [recomiendo ver el cortometraje antes de proceder con la lectura]
        </p>           
        </div>
        """, unsafe_allow_html=True) #Para colocar en cursiva, coloco dentro de la frase <i>...</i>
#Aquí termina el markdown (la estructura del texto con su estilo)

        col9, col10, col11 = st.columns([1,2,1])
        with col10: 
            st.video("https://www.youtube.com/watch?v=hfGsrMBsX1Q", width=800)   
            
        
        st.markdown("""
        <div style="text-align: justify; font-size:18px;">
        <p>
        Esta historia, protagonizada por la familia de Marcos y Julia (cónyuges) y Marquitos (su hijo), se desarrolla casi por completo en un baño. Cargado de símbolos y metáforas, este corto nos muestra que, con el paso del tiempo, el hijo crece, el esposo envejece y el mobiliario dentro del hogar cambia; sin embargo, Julia permanece dentro de una bañera, con la puerta siempre abierta y con la misma apariencia. Ella no pronuncia una sola palabra. Todo lo que sabemos sobre su vida ocurre a través de los diálogos entre Marcos, su hijo y otros familiares que entran y salen del espacio doméstico. Marcos, sobre todo, es quien le habla, le pregunta y le exige respuestas, pero cabe enfatizar que no es un diálogo entre dos personas: todo el temor, la desesperanza y la tristeza de Julia se transmite por medio de sus expresiones faciales y corporales.</p>
         
               
        </div>
        """, unsafe_allow_html=True)  
#Aquí cierro mi reseña 2 con el markdown      
elif selected == "Intelectuales en el mundo":
    st.markdown("""
    <h1 style="
        font-size:60px;
        color:#9a62a5;
        font-weight:900;
        text-align:center;
        margin-bottom:20px;
    ">
    Intelectuales en el mundo
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: justify; font-size:18px;">
    <p>
    Este mapa nace de una constatación simple: la historia de la filosofía y del pensamiento crítico ha sido contada, en gran medida, sin sus protagonistas femeninas. 
    Aquí se reúnen filósofas, teóricas y pensadoras cuyas ideas han cuestionado esa ausencia, analizando el poder, el conocimiento, el cuerpo y la justicia desde perspectivas que incomodan y transforman. 
    Aunque muchas de estas autoras han reflexionado sobre el género y las desigualdades, el mapa no se limita a ello: busca visibilizar la participación de las mujeres en la producción de conocimiento en sentido amplio. 
    Actualmente, incluye más de 70 autoras de diversas tradiciones y contextos, y se encuentra en constante crecimiento. En la medida en que nuevas lecturas, investigaciones y hallazgos amplíen este recorrido, el mapa seguirá incorporando más voces.
    </p>
    </div>
    """, unsafe_allow_html=True)

    datos_filo = pd.read_excel("hiedra-filosofas-mapa-listo.xlsx")
    
    # Creamos el mapa base con una vista global inicial
    # location define el centro del mapa (latitud 20, longitud 0)
    # zoom_start define el nivel de zoom inicial (2 = vista muy amplia)
    m = folium.Map(location=[20, 0], zoom_start=2)

    datos_mapa = datos_filo.groupby("Filósofa / Pensadora")

    # Iteramos sobre cada grupo (país) y su correspondiente sub-DataFrame
    for nacion, geo in datos_mapa:
        # Tomamos la latitud y la longitud 
        lat = geo["Latitud"].iloc[0]
        lon = geo["Longitud"].iloc[0]

        # Comprobamos que las coordenadas no sean nulas
        if pd.notna(lat) and pd.notna(lon):

            contenido = ""

            # Recorremos cada fila del grupo
            for _, fila in geo.iterrows():

                url = ""

                # Verificamos si existe URL
                url_value = fila["URL (página web personal o red social)"]

                if pd.notna(url_value) and str(url_value).strip() != "":
                    url = f'<a href="{url_value}" target="_blank">Página web</a><br>'

                contenido += f"""
                <div style="width:200px; text-align:center;">
                <b>{fila['Filósofa / Pensadora']}</b><br><br>
                <img src="{fila['Foto de la filósofa (Buscador)']}" 
                width="180"><br><br>
                {fila['Nacionalidad']}<br>
                {fila['Lugar de nacimiento']}<br>
                {fila['Áreas de investigación']}<br>
                {url}
                </div><br>
                """
            # Agregamos un marcador en las coordenadas del país
            folium.Marker(
                location=[lat, lon],                   # Coordenadas del marcador
                popup=folium.Popup(contenido, max_width=300),  # Popup con información en HTML
                icon=folium.Icon(color='blue', icon='user')    # Ícono azul con forma de usuario
            ).add_to(m)

    # Finalmente, mostramos el mapa interactivo con todos los marcadores agregados
    st_folium(m, use_container_width=True, height=500)

    st.markdown("""
    <h2 style="
        font-size:30px;
        color:#9a62a5;
        font-weight:900;
        text-align:center;
        margin-bottom:20px;
    ">
    Buscador de filósofas
    </h2>
    """, unsafe_allow_html=True)
    
    nombre = st.selectbox(
    "Selecciona una filósofa",
    datos_filo["Filósofa / Pensadora"].sort_values().unique()
    )
    resultado = datos_filo[datos_filo["Filósofa / Pensadora"] == nombre]

    if not resultado.empty:
        fila = resultado.iloc[0]

        descripcion = fila["Descripción (Buscador)"]
        pos = descripcion.find(")")

        if pos != -1:
            parte_negrita = descripcion[:pos+1]
            resto = descripcion[pos+1:]
        else:
            parte_negrita = descripcion
            resto = ""

        st.markdown(f"""
        <div style="text-align: justify; font-size:18px;">
        <b>{parte_negrita}</b>{resto}
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        col5, col6 = st.columns(2)
        with col5:
            st.markdown("""
            <h2 style="
                font-size:20px;
                color:#9a62a5;
                font-weight:900;
                text-align:center;
                margin-bottom:20px;
            ">
            Obras
            </h2>
            """, unsafe_allow_html=True)
            
            obras = fila["Obras"]

            lista_obras = [obra.strip() for obra in obras.split(",")]

            texto = "\n".join([f"- {obra}" for obra in lista_obras])

            st.markdown(texto)

        with col6:
            st.image(fila["Foto de la obra"], width=200)

        if pd.notna(fila["Video explicativo sobre la autora"]) and str(fila["Video explicativo sobre la autora"]).strip() != "":
            st.markdown("### 🎥 Video")
            st.video(fila["Video explicativo sobre la autora"])

        if pd.notna(fila["Entrevista o conferencia"]) and str(fila["Entrevista o conferencia"]).strip() != "":
            st.markdown("### 🎥 Video")
            st.video(fila["Entrevista o conferencia"])

elif selected == "Versos sueltos":
    st.markdown("""
    <h1 style="
        font-size:60px;
        color:#9a62a5;
        font-weight:900;
        text-align:center;
        margin-bottom:20px;
    ">
    Poemas
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h2 style="
        font-size:30px;
        color:#9a62a5;
        font-weight:900;
        text-align:center;
        margin-bottom:20px;
    ">
    Título del poema
    </h2>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: center; font-size:18px;">
    <p>
    vnjfnvkjfnvjkfnvjknv <br>            
    nvkjnfkvjnkj
    </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<hr style="margin-top:20px; margin-bottom:10px;">

<div style="
    text-align:center;
    font-size:18px;
    color:#555;
">
    <p> Si quieres compartir ideas: </p> 📩 ncardozar@gmail.com 
</div>
""", unsafe_allow_html=True)
# br : saltos de línea