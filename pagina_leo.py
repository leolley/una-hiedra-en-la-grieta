# Primero importamos las librerías necesarias
import streamlit as st # pagina web
import pandas as pd # bases de datos
import folium # mapa
import streamlit.components.v1 as components 
from streamlit_folium import st_folium
from streamlit_option_menu import option_menu
from docx import Document

# 🔹 FUNCIÓN (también arriba, fuera de cualquier if)
def cargar_poemas(docx_file):
    doc = Document(docx_file)

    poemas = []
    poema_actual = {}
    modo = "poema"

    for para in doc.paragraphs:

        texto_plano = para.text.strip()

        if not texto_plano:
            continue

        # 🔹 Detectar estructura
        if texto_plano.startswith("TÍTULO:"):
            if poema_actual:
                poemas.append(poema_actual)
                poema_actual = {}

            poema_actual["titulo"] = texto_plano.replace("TÍTULO:", "").strip()
            modo = "poema"

        elif texto_plano.startswith("AUTOR:"):
            poema_actual["autor"] = texto_plano.replace("AUTOR:", "").strip()

        elif texto_plano.startswith("INFO:"):
            modo = "info"
            poema_actual["info"] = ""

        else:
            # 🔹 Aquí conservamos formato
            linea_html = ""

            for run in para.runs:
                texto = run.text

                if run.italic:
                    texto = f"<i>{texto}</i>"
                if run.underline:
                    texto = f"<u>{texto}</u>"
                if run.bold:
                    texto = f"<b>{texto}</b>"

                linea_html += texto

            if modo == "poema":
                poema_actual.setdefault("texto", "")
                poema_actual["texto"] += linea_html + "<br>"

            elif modo == "info":
                poema_actual["info"] += linea_html + "<br>"

    if poema_actual:
        poemas.append(poema_actual)

    return poemas

st.set_page_config(
    page_title="La hiedra en la grieta",
    page_icon="🍃",
    layout="wide"
)

st.markdown("""
    <style>
    div[data-baseweb="select"] > div {
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
    /* Texto dentro del selectbox */
    section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
        font-size: 18px !important;
        font-weight: bold !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- PORTADA TIPO BLOG (ANTES DEL MENÚ) ---
# 1. Obtenemos el link de Pinterest (clic derecho en la imagen > copiar dirección de imagen)
url_portada = "https://i.pinimg.com/1200x/f5/bf/ae/f5bfaeecc82f09bb56fdf5e8319ffc42.jpg" 

st.markdown(f"""
    <div style="width: 100%; max-height: 250px; overflow: hidden; margin: 0; padding: 0;">
        <img src="{url_portada}" style="
            width: 100%; 
            height: 400px; 
            object-fit: cover; 
            object-position: center 68%; 
            display: block;">
    </div>
    """, unsafe_allow_html=True)

# 2. Ajuste de márgenes para que la imagen toque los bordes (Opcional)
st.markdown("""
    <style>
    .block-container {
        padding-top: 0rem !important; /* Elimina el espacio blanco superior */
    }
    </style>
    """, unsafe_allow_html=True)
# ------------------------------------------

## ----------ESTO ES PARA LA BARRA DE MENÚ
# Insertamos un poco de espacio arriba con HTML antes del menú
st.markdown('<div style="margin-top: 0px;"></div>', unsafe_allow_html=True)

st.markdown("""
    <style>
    /* Elimina el espacio extra que Streamlit pone arriba por defecto */
    .block-container {
        padding-top: 2rem !important; 
        padding-bottom: 0rem !important;
    }
    
    /* Hace que el menú horizontal se vea más centrado */
    .nav-link {
        padding: 10px 15px !important;
    }
    </style>
    """, unsafe_allow_html=True)

selected = option_menu(
    menu_title=None, 
    options=["Sobre mí", "Después de leer", "Intelectuales en el mundo", "Versos sueltos"], 
    icons=['person-heart', 'pencil-square', 'globe-americas', 'journal-richtext'], 
    menu_icon="cast", 
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {
            "padding": "15px 0px", # Más aire para que no se corte
            "background-color": "#FCFBF7", # Tu crema de fondo
            "border-radius": "0px"
        },
        "icon": {
            "color": "#9a62a5", 
            "font-size": "18px"
        }, 
        "nav-link": {
            # --- AQUÍ CAMBIAMOS LA LETRA ---
            "font-family": "Georgia, serif", # La misma de tus títulos, es muy suave
            "font-size": "17px",
            "font-weight": "400", # 400 es 'normal', hace que se vea delgada y fina
            "text-align": "center", 
            "margin": "0px 15px", 
            "color": "#1A1A1A", # Color del texto negro suave
            "--hover-color": "#F3EAF4"
        },
        "nav-link-selected": {
            "background-color": "#4B0082", # Tu morado profundo
            "color": "white",
            "font-weight": "500", # Un poquito más de grosor solo cuando está seleccionada
            "border-radius": "8px" # Bordes redondeados para el botón seleccionado
        },
    }
)

# Un separador sutil para que el contenido no se pegue al menú
st.markdown('<hr style="margin-top: 0px; margin-bottom: 20px; border: 0.5px solid #eee;">', unsafe_allow_html=True)
## -------------AQUÍ TERMINA LA BARRA DE MENÚ

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

if selected == "Sobre mí":
    #col1, col2, col3 = st.columns([1,2,1])

    #with col2:
        #st.image("fotos/logo.png", width=1600)

    título = """
    ¡Hola! Soy Natalí C. Cardoza Rojas
    """
    st.markdown(f"<div style='text-align: center; font-size: 40px; color: #9a62a5; font-weight: bold'>{título}</div>", unsafe_allow_html=True)
    
    st.write("")
    
    col1, col2 = st.columns([1,2]) #Esto es la extensión de columnas

    with col1:
        st.image("foto_guapa.jpeg", width=350) #Esta es la extensión de mi foto

        st.markdown("""
        <p style="text-align:center; font-size:14px; color:#777; margin-top:-10px;">
        <i>Flor de Almendro</i> de Van Gogh y un cactus feliz
        </p>
        """, unsafe_allow_html=True)
        
    with col2:
        texto_1 = """
        <p>
        Filósofa en formación, predocente e investigadora en mis tiempos no libres.
        Trabajo en la intersección entre la epistemología, los feminismos y los estudios decoloniales, con su respectivo análisis crítico de nuestra cotidianidad.
        </p>
        <p>
        Me interesa cuestionar las formas en que se construye el conocimiento, las relaciones de poder que lo atraviesan 
        y las maneras en que estas se reproducen en nuestra vida diaria. Por eso, aquí encontrarás reflexiones sobre
        feminismos, epistemologías contemporáneas, lógica y argumentación, siempre conectadas con la política peruana y la cultura pop.
        </p>
        <p>
        Además de ser teórica y activista, soy mugiwara de corazón, <i>amateur</i> en botánica y amante de la música en sus múltiples formas.
        Este espacio nace como una forma de salir de la academia sin abandonar el pensamiento riguroso. 
        Porque sí, <b>la filosofía no es para unos pocos</b>: nos permite incomodarnos, entendernos más y transformar lo que vivimos.
        </p>
        <p>
        Te recomiendo empezar por el vídeo <i>La hiedra en la grieta</i>, que da sentido a este espacio.
        </p>
        """
        st.markdown(f"<div style='text-align: justify; font-size: 22px'>{texto_1}</div>", unsafe_allow_html=True)
 
    st.write("")

    col3, col4 = st.columns([2,1.6]) #Si quiero agrandar el vídeo de la hiedra, solo incremento el 1.5.

    with col3:
        texto_2 = """
        <p>
        ¿Por qué una hiedra en la grieta? Durante mucho tiempo 
        <a href="https://www.bbc.com/mundo/ciencia_tecnologia/2010/05/100524_hiedra_contaminacion_lp">
        se creyó que la hiedra era una amenaza
        </a> 
        para los muros; 
        <a href="https://www.sciencedaily.com/releases/2010/05/100516124817.htm" target="_blank">
        en la actualidad
        </a>
        , se demostró que, en construcciones intactas, 
        puede protegerlas de cambios extremos de temperatura, ayudar a filtrar contaminantes 
        y reducir el deterioro. Solo en superficies ya dañadas sus raíces pueden aprovechar 
        grietas existentes y agravar el daño.
        </p>
        <p>
        La hiedra me interesa como metáfora de lo que emerge en las fisuras del orden 
        establecido: algo que insiste, crece y transforma desde dentro de lo aparentemente 
        sólido. Escribo desde la ruptura, desde lo que incomoda y no encaja, 
        como muchas intelectuales y activistas críticas han abierto caminos para habitar y reformular 
        las grietas.
        </p>
        """
        st.markdown(f"<div style='text-align: justify; font-size: 22px'>{texto_2}</div>", unsafe_allow_html=True)
    
    with col4:
        st.video("https://youtu.be/sAVNZkBlg38")

    # 👇 ESTE VA FUERA DE LAS COLUMNAS (ancho completo)
    
    st.write("")

    texto_final = """
        <p>
        Si algo de lo que lees te hace pensar o querer cuestionar, puedes escribirme al correo:
        <a href="mailto:ncardozar@gmail.com">ncardozar@gmail.com</a>.
        </p>
        <p>
        Y si tienes interés en programar, conocer más del universo de Python o de las 
        humanidades digitales, comunícate con 
        <a href="mailto:luisa.gomez@pucp.edu.pe">luisa.gomez@pucp.edu.pe</a>.
        Sin su paciencia y sabiduría, los contenidos de este humilde blog no hubieran sido posible expresarse aquí. 
        </p>
        """
    st.markdown(f"<div style='text-align: justify; font-size: 22px'>{texto_final}</div>", unsafe_allow_html=True)

# AQUÍ EMPIEZA LA SECCIÓN DE LECTURA

# GLOSARIO EN PAUSA
# Sigue el formato "palabra": "definición",
    glosario_filosofico = {
        "neoliberalismo": "Sistema que busca reducir la intervención del Estado en la economía. Con capitalismo neoliberal, nos referimos a la versión contemporánea del capitalismo que adopta las políticas neoliberales de libre mercado. Se caracteriza por la desregulación económica, la privatización de empresas y servicios públicos, la apertura comercial y la reducción del papel del Estado en la economía.",
        "segunda ola": "Movimiento feminista de los años 60-80 centrado en  la agenda feminista más allá del sufragio, abarcando desigualdades sociales y de facto, derechos reproductivos, la familia, el lugar de la mujer en el trabajo y la sexualidad.",
        "patriarcado": "Sistema social y político basado en la primacía de los hombres. En él, la autoridad y los recursos están concentrados en manos masculinas, lo que impone un orden de dominación sobre las mujeres y define «lo propio» de cada género. Como señala Cinzia Arruzza, el término se usa para enfatizar que la opresión de género es un fenómeno constante y estructural (arraigada en las instituciones y relaciones sociales), no un hecho aislado de actitudes personales. ",
        "capitalismo": "Sistema económico basado en la propiedad privada y el mercado. Su dinámica fundamental es la inversión de capital para obtener beneficios, lo que permite relaciones centradas en la producción, el intercambio y el trabajo asalariado.",
        "emancipación": "Proceso histórico por el cual las mujeres han obtenido y buscado asegurar la igualdad legal, política, laboral, social y familiar que antes se les negaba. En este sentido, la emancipación femenina es la liberación de las diversas formas de opresión patriarcal que tradicionalmente las subordinaban.",
        "división sexual del trabajo": "Reparto o especialización de las tareas sociales según el género. En la mayoría de las sociedades patriarcales a los hombres se le atribuyen las tareas productivas (trabajo remunerado, espacio público) y a las mujeres las tareas reproductivas(cuidados, crianza, trabajo doméstico). ",
        "igualdad salarial": "Principio según el cual personas que realizan trabajos de igual valor o productividad deben recibir la misma remuneración, sin importar su género u otras condiciones. En la práctica, busca corregir las brechas salariales de género asegurando que una mujer reciba igual salario que un hombre por el mismo trabajo.",
        "representación simbólica": "Presencia visible de mujeres en roles o espacios públicos que tiene más carácter emblemático que real. Por ejemplo, la designación de mujeres en cargos honoríficos o imágenes oficiales puede cumplir una función de “símbolo” de igualdad, aunque no transforme sustancialmente el poder político o las condiciones materiales de las mujeres.",
        "feministas marxistas": "Corriente feminista que considera que la raíz de la opresión de las mujeres está en el sistema capitalista. Desde esta perspectiva, el patriarcado se entiende como una superestructura alimentada por las relaciones económicas de producción. Las feministas marxistas, como Silvia Federici, examinan la opresión de las mujeres como algo inherente al capitalismo, heredando el análisis materialista de Marx. Para ellas, la emancipación pasa por transformar las relaciones económicas y sociales de forma anticapitalista.",
        "feministas socialistas": "Corriente teórica y política que crítica tanto al capitalismo como al patriarcado. Coincide con el feminismo marxista en que la liberación de las mujeres requiere un cambio económico profundo, y con el feminismo radical en que hay que cuestionar las estructuras patriarcales, sin quedarle “solo” a lo político o cultural. Las feministas socialistas abogan por reestructurar la sociedad (por ejemplo, eliminando la propiedad privada sobre la familia y colectivizando las tareas domésticas) para acabar con las causas materiales y culturales de la desigualdad de género.",
        "feministas radicales": "Corriente surgida en los años 60-70 que enfatiza la transformación profunda de la sociedad para abolir el patriarcado. Analizan la dominación masculina como un fenómeno estructural y sistémico, no solo como desigualdad en leyes, y consideran que el patriarcado (a saber, el conjunto de normas e instituciones que dan poder a los hombres) es la forma primaria de opresión de las mujeres.",
        "opresión de género": "Conjunto de desigualdades estructurales, discriminación y violencia que sufren las personas por su género (en especial las mujeres y las disidencias sexuales) dentro de un sistema patriarcal. Implica la subordinación sistemática de las mujeres en ámbitos legales, económicos, simbólicos y cotidianos, generando una posición desventajosa mantenida por la cultura y las instituciones sociales.",
        "patriarcado moderno": "Concepto que describe las formas contemporáneas del patriarcado en el capitalismo avanzado. En esta versión, la familia nuclear heterosexual funciona como eje de reproducción de la fuerza de trabajo, asignando a las mujeres las tareas de cuidado y reproduciendo privilegios masculinos tanto en el hogar como en el mercado laboral. Es decir, el patriarcado moderno se instituye junto al capitalismo mediante la división entre producción (asociada a lo masculino) y reproducción (asociada a lo femenino).",
        "contrato social": "Teoría política clásica (Rousseau, Hobbes, Locke) que explica el origen del Estado por un pacto voluntario entre individuos. Según esta idea, las personas acuerdan renunciar su libertad natural para constituir un poder común que garantice derechos y deberes. En concreto, el contrato social propone que todos los miembros de la sociedad aceptan reglas y autoridades a cambio de protección y orden.",
        "contrato sexual": "Término acuñado por Carole Pateman para denunciar que el contrato social liberal esconde un pacto patriarcal implícito que subyugó a las mujeres desde el principio. Según esta teoría, los contratos civiles (como el matrimonio) están diseñados para asegurar el derecho sexual y reproductivo de los hombres, manteniendo a las mujeres subordinadas e inhibiendo su autonomía.",
        "colonialismo": "Sistema de dominación político y económico en el que un Estado extranjero se impone sobre un territorio ajeno. El colonialismo implica controlar y explotar directamente los recursos y poblaciones de la colonia. Históricamente, se caracteriza por la colonización física o administración colonial (imperios europeos en América, África, etc.) y por imponer estructuras culturales ajenas a las sociedades dominadas.",
        "matriz heteronormativa": "Conjunto de normas y prácticas sociales que asumen la heterosexualidad y la familia nuclear heterosexual como modelo natural o normal. En una matriz heteronormativa se presupone que la orientación sexual y la identidad de género deben alinearse (sexo-biológico masculino = identidad masculina, relaciones heterosexuales, roles tradicionales, etc.). Esto invisibiliza y margina otras identidades sexuales y de género, relegándolas como <b>anormales</b> en la cultura dominante.",
        "igualdad": "Principio por el cual todas las personas son equiparadas en derechos y obligaciones, sin privilegios o discriminaciones arbitrarias. En la cuestión del género, la igualdad exige que mujeres y hombres disfruten de las mismas oportunidades, derechos y libertades.",
        "sistema económico": "Conjunto de instituciones, normas, mecanismos y relaciones que organizan la actividad económica de una sociedad. Define cómo se producen, distribuyen e intercambian bienes y servicios, quién posee los medios de producción y qué papel tiene el Estado. Ejemplos de sistemas económicos son el capitalismo de mercado, el socialismo planificado o las economías mixtas.",
        "obligación biológica": "Idea (acepción crítica) de que a las mujeres les corresponde por naturaleza una tarea reproductiva obligatoria, como la maternidad y el cuidado. En el feminismo se rechaza esta <b>obligación biológica</b>: se argumenta que los roles reproductivos no son meramente inescapables por biología, sino que están influidos por factores sociales y deben ser una elección.",
        "determinismo biológico": "Doctrina según la cual el comportamiento humano y las diferencias sociales (incluyendo la desigualdad de género) están fijados por la biología heredada; es decir, las normas y jerarquías sociales reflejan diferencias innatas entre individuos. El determinismo biológico afirma que rasgos y roles sociales dependen de los genes, idea que las ciencias contemporáneas rechazan, pues reconocen la compleja interacción entre biología y ambiente.",
        "esencialismo de mujer": "Creencia de que existe una esencia innata y universal que define a todas las mujeres (por ejemplo, una supuesta naturaleza maternal o pasiva). Este enfoque asume que el género femenino es una categoría fija y natural. En contraste, las teorías de género lo critican: argumentan que las características atribuidas a las «mujeres» cambian históricamente y culturalmente, por lo que no hay una esencia femenina única.",
        "género": "Categoría sociocultural que clasifica a las personas según rasgos asociados tradicionalmente a la masculinidad o la feminidad. No coincide necesariamente con el sexo biológico.",
        "desigualdades de género": "Fenómeno social, jurídico y cultural de discriminación estructural que pone un género (usualmente el masculino) en posición de privilegio sobre otro. Se basa en roles sociales tradicionales de varones y mujeres.",
        "constructo social": "Entidad o idea creada culturalmente que no existe por sí sola en la naturaleza, sino por acuerdo convencional. Se sostiene porque la sociedad acepta reglas o normas que le dan existencia.",
        "innatas": "Cualidades o comportamientos presentes desde el nacimiento, sin necesidad de aprendizaje, ligados a la dotación biológica heredada.",
        "relaciones de poder": "Dinámicas sociales en las que individuos o grupos ejercen control, autoridad o influencia sobre otros, determinando desigualdades y jerarquías en la sociedad.",
        "pater familias": "Término del derecho romano que designa al jefe o cabeza de familia (asociado al varón). En contextos patriarcales, simboliza la autoridad paterna tradicional.",
        "masculinidad hegemónica": "Forma de masculinidad dominante que legitima el patriarcado. Según Connell, es la configuración culturalmente idealizada de la masculinidad que sostiene la posición social superior de los hombres y la subordinación de las mujeres. ",
        "masculinidades no hegemónicas": "Todas las formas de ser varón que no corresponden al patrón hegemónico. Incluyen masculinidades subordinadas (con rasgos asociados a lo femenino), cómplices (que se benefician de la hegemonía sin liderarla) y otras identidades alternativas.",
        "virilidad": "Conjunto de cualidades asociadas a la hombría o masculinidad madura, como fuerza, vigor y vigorosidad.",
        "personaje disruptivo": "Individuo que rompe con normas establecidas y subvierte los símbolos o reglas dominantes, provocando cambios en la estructura social o simbólica.",
        "ruptura simbólica": "Acto de cuestionar o quebrar significados culturales preestablecidos (como estereotipos de género) mediante la alteración de símbolos y representaciones dominantes.",
        "estructuras sociales": "Ordenamiento de normas, instituciones y relaciones que organizan una sociedad. Incluye familia, clases, leyes, costumbres, etc."
}

## EL GLOSARIO QUEDA EN STANDBY, A VER SI LUISA ME AYUDA U.U

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

    # 👇 Texto descriptivo corto
    st.markdown("""
    <div style="text-align: justify; font-size:16px;">
    <p>
    <b>Leer es entrar en diálogo con otras voces. No solo busco comprender, sino pensar con 
    y desde otras filósofas, pensadoras y teóricas. Estos escritos reflejan ese proceso.
    Recomiendo empezar en orden del buscador, pero eres libre de elegir qué tema te interesa leer :)
    </b></p>
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
        Hablar del feminismo de la segunda ola sin hablar del capitalismo es, sencillamente, 
        imposible. Ambos procesos históricos crecieron en paralelo y, aunque muchas veces se 
        los presenta como fuerzas opuestas, la relación entre ellos es más compleja e incómoda 
        de lo que solemos admitir. No podemos negar que la segunda ola avanzó en proyectos 
        que favorecen en al menos tres dimensiones de la justicia: el reconocimiento 
        (visibilizar la subordinación de las mujeres), la redistribución (exigir igualdad 
        económica y laboral) y la representación (ampliar la participación política de las 
        mujeres); no obstante, también debemos reconocer que parte de sus demandas resultaron 
        ser beneficiosas para las transformaciones del capitalismo.
        De ahí que la filósofa política Nancy Fraser nos plantee la siguiente pregunta en su 
        artículo titulado <i>El feminismo, el capitalismo y la astucia de la historia</i> (2020): 
        “¿Fue mera coincidencia que la segunda ola feminista y el neoliberalismo prosperasen 
        unidos? ¿O había una perversa y soterrada afinidad electiva entre ellos?” (p. 148). 
        Planteado de otro modo: <b>¿por qué no reconocer que algunas de las demandas de la 
        segunda ola feminista terminaron convergiendo con las transformaciones del capitalismo 
        neoliberal?</b> El objetivo de este escrito no busca desacreditar los logros del feminismo,
        sino detenernos a pensar en sus límites históricos. 
        </p>
        <p>
        El existencialismo de la filósofa francesa, Simone de Beauvoir, nos permitió apartarnos
        de una mirada esencialista sobre la “naturaleza femenina”. En <i>El segundo sexo</i> (1999), 
        al sostener que <i>no se nace mujer, sino que se llega a serlo</i>, De Beauvoir rechazó 
        las nociones del <i>eterno femenino</i> y la existencia de una naturaleza <i>per se</i>; 
        en su lugar, afirmó que la mujer se realiza en su actuar, en sus experiencias mismas 
        que la sitúan en contextos políticos, históricos, culturales y económicos concretos. 
        Esta ruptura fue decisiva. Aun así, la filósofa francesa reconocía su posición 
        privilegiada para desarrollar estos temas de la forma más neutral, por lo que valdría 
        la pena preguntarnos: ¿de qué mujeres hablamos cuando nos referimos a “la mujer”? 
        ¿Estamos abarcando a todas las mujeres concretas, de distintas clases, color, 
        orientación sexual, entre otras categorías?            
        </p>
        <p>            
        Recordemos, en este punto, la expansión del feminismo en Estados Unidos en la década 
        de 1960, al mando de figuras como Betty Friedan, miembro de la Organización Nacional 
        para las Mujeres (NOW). Se trató de un movimiento que, pese a su impulso transformador, 
        también excluyó, dentro de su feminismo, a muchas mujeres lesbianas, quienes fueron 
        consideradas una 
        <a href="https://www.thoughtco.com/lavender-menace-feminism-definition-3528970" target="_blank">
        "amenaza lavanda" dentro del movimiento,
        </a> 
        y las experiencias de mujeres racializadas o de otras clases sociales quedaron 
        frecuentemente fuera de la agenda. El sujeto político "mujer", entonces, no incluía 
        a estas otras pese a que, en sus discursos, pretendían luchar y alzar la voz por todas.
        </p>
                    
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
        Así, mientras que el feminismo exigía emancipación, el capitalismo reorganizaba el 
        trabajo y promovía el modelo de doble ingreso familiar. Aquí aparece la tensión central,
        pues la incorporación masiva de mujeres al mercado laboral, consolidada por la segunda 
        ola en la década de 1960, no eliminó la división sexual del trabajo 
        —uno de los objetivos principales del feminismo—; caso contrario, <b>la duplicó</b>. 
        ¿Cuál es, entonces, el resultado que aún persiste hoy en día? El trabajo doméstico y 
        de cuidados sigue recayendo de manera desproporcionada sobre aquellas mujeres cuyas 
        condiciones de clase o color influyen más en su trayectoria, 
        <a href="https://videoteca.cultura.pe/video/categoria/documentales/una-casa-no-se-limpia-con-libros" target="_blank">
        como ser mujer andina y quechua hablante en nuestro contexto peruano.
        </a> 
        Son estas mujeres quienes experimentan de forma más aguda las desigualdades asociadas al 
        trabajo doméstico, donde las condiciones laborales son frecuentemente más precarias, 
        peor remuneradas y socialmente menos valoradas.
        </p>
        <p>
        Para Fraser, el problema no fue haber luchado por reconocimiento o redistribución, 
        <b>sino haber separado dimensiones que, en realidad, están entrelazadas.</b> Es decir, la 
        justicia de género no puede reducirse ni a igualdad salarial ni a representación 
        simbólica; requiere pensar las estructuras económicas, culturales y políticas como un 
        todo. Por ejemplo, cuando se habla del trabajo doméstico, durante mucho tiempo se lo 
        consideró una tarea “natural” de las mujeres y, por ello, ni siquiera se pensaba que 
        debía ser remunerado o redistribuido. Aquí vemos cómo el problema no es solo económico 
        (la falta de salario), sino también cultural: la idea de que cuidar es simplemente 
        parte del rol femenino, sin ser discutido en la agenda política. Es en este punto 
        donde recordamos, entonces, que la justicia no solo consiste en distribuir bienes, 
        sino también en reconocer las distintas situaciones y exigir que todas participen en 
        la agenda política.
        </p>
        <p>
        Las feministas marxistas y socialistas profundizaron esta crítica. Por un lado, 
        Cinzia Arruzza (2016) cuestionó la idea de que el capitalismo sea “neutral” respecto 
        a la opresión de género. La filósofa feminista exploró las teorías en torno a las 
        relaciones entre desigualdad de género y capitalismo, para demostrar que este último 
        necesita del patriarcado para formar un único sistema que separe a hombres y mujeres 
        en función de la lógica capitalista. Por su parte, Silvia Federici (2015) evidenció 
        cómo el patriarcado moderno se consolidó junto con el capitalismo, especialmente a 
        través de la asignación del trabajo reproductivo a las mujeres. Esta ancla de la 
        reproducción permite al capitalismo asignarles una tarea que no es la misma para los 
        varones; es decir, además de participar en la producción económica, las mujeres han 
        sido históricamente responsables de reproducir la fuerza de trabajo —tener hijos, 
        cuidar el hogar y sostenerlo— sin que estas tareas sean reconocidas o remuneradas. 
        Por ende, la división radical proletaria, impuesta con la llegada del capitalismo, 
        define lo que debe ser y hacer la mujer. En palabras de Carole Pateman (1995), el 
        contrato social pudo desarrollarse ocultando este otro contrato sexual que relegó a 
        las mujeres a la esfera privada.
        </p>
        <p>
        Desde esta perspectiva, la opresión de género no es un residuo premoderno que el 
        capitalismo podría superar fácilmente —sin mencionar, en este apartado, el colonialismo 
        y la matriz heteronormativa que profundizan las jerarquías de género—. Siguiendo todo 
        el panorama anterior, cuestionemos, entonces, nuestro horizonte actual. ¿Qué tipo de 
        igualdad buscamos las feministas hoy? ¿Uno contestatario y radical frente al capitalismo
        neoliberal? ¿O uno que exija políticas y busque una integración plena en las lógicas 
        del mercado? Estas preguntas nos obligan a excluir propuestas para quedarnos con la 
        que consideramos que será la solución al problema; sin embargo, 
        <b>¿no existe el riesgo de que este discurso de igualdad, que buscan los feminismos, 
        termine adaptándose a las prioridades del propio sistema económico?</b>
        En la medida en que exijamos ser incluidas en la fuerza de trabajo y ocupar espacios 
        tradicionalmente masculinos —como vía para alcanzar independencia económica frente a 
        los varones—, esta idea de “igualdad” puede terminar significando solo la posibilidad 
        de integrar a las mujeres al mismo mundo laboral que permanece intacto, sin cuestionar 
        las lógicas competitivas que estructuran el mercado laboral. De ser así, 
        <b>¿el sistema capitalista no consigue su objetivo de replicar sus prácticas y seguir 
        reproduciendo jerarquías similares, donde algunas mujeres logran ascender mientras 
        otras continúan ocupando posiciones más precarias?</b>         
        </p>
        <p>
        Algunas propuestas, como la de Shulamith Firestone (1976), imaginaron una revolución 
        con nuevas tecnologías que permitan liberar a las mujeres de la función reproductiva,
        de modo que, si se prescinde de la obligación biológica, las mujeres no se encontrarán 
        más en una posición subordinada. Desde la postura de Firestone, la reproducción ya no 
        sería el destino de las mujeres. Otras corrientes, en diálogo con las socialistas y 
        radicales, apuestan por reorganizar radicalmente el trabajo y la vida social, pues se 
        trata de un cambio estructural, tanto de la economía, la política y lo social. Sin embargo,
        quizá el desafío no consista en elegir una única estrategia, sino en mantener un 
        diálogo crítico de perspectivas diversas entre mujeres blancas y mujeres 
        afrodescendientes, mujeres urbanas y mujeres indígenas, mujeres heterosexuales y 
        mujeres trans. Reconocer estas diferencias y particularidades, sea de clase, color, 
        orientación sexual, ubicación geopolítica, no debilita la lucha, sino que la vuelve 
        más honesta al visibilizar estas otras vidas y experiencias silenciadas.  
        </p>
        <p>
        La historia del feminismo de la segunda ola no es una historia de fracaso, sino de 
        tensiones productivas y debates internos. Hemos dado un gran avance al cuestionar el 
        determinismo biológico y el supuesto esencialismo de mujer. Es preciso, ahora, 
        cuestionar cuál es esa igualdad que buscamos dentro de las estructuras actuales y 
        en el contexto neoliberal. 
        <b>O si es que en realidad necesitamos seguir pensando en una.</b> 
        Mostrar estas contradicciones no debilita al feminismo. Al contrario, lo fortalece, 
        pues una teoría feminista que no examina sus propias alianzas y límites corre el riesgo
        de reproducir aquello que pretendía cuestionar.
        </p> 
        <hr style="margin-top:40px;">

        <p style="font-size:20px; font-weight:bold; color:#9a62a5;">
        Bibliografía
        </p>

        <p style="margin-bottom:12px; font-size:16px;">
        Arruzza, C. (2016). “Reflexiones degeneradas: patriarcado y capitalismo”, en <i>Marxismo crítico</i>.
        </p>

        <p style="margin-bottom:12px; font-size:16px;">
        De Beauvoir, S. (1999) [1949]. <i>El segundo sexo</i>. Buenos Aires: Sudamericana.
        </p>

        <p style="margin-bottom:12px; font-size:16px;">
        Federici, S. (2015). <i>Calibán y la bruja: mujeres, cuerpo y acumulación originaria</i>. Buenos Aires: Tinta Limón Ediciones.
        </p>

        <p style="margin-bottom:12px; font-size:16px;">
        Firestone, S. (1976). <i>La dialéctica del sexo: en defensa de la revolución feminista</i>. Barcelona: Kairós.
        </p>

        <p style="margin-bottom:12px; font-size:16px;">
        Fraser, N. (2020). “El feminismo, el capitalismo y la astucia de la historia”, en <i>Los talleres ocultos del capital: un mapa para la izquierda</i>. Madrid: Traficantes de Sueños, pp. 137–157.
        </p>

        <p style="margin-bottom:12px; font-size:16px;">
        Pateman, C. (1995) [1988]. <i>El contrato sexual</i>. Barcelona: Anthropos.
        </p>
        
        <hr style="margin-top:40px; margin-bottom:10px;">

        <p style="font-size:14px; color:#777; text-align:justify;">
        He adaptado este escrito que elaboré para un curso de la MEG en diciembre del 2025. 
        Busco plantear más preguntas que afirmaciones.
        </p>

        <p style="font-size:14px; color:#777; text-align:justify; margin-top:10px;">
        Si te surgen dudas o quieres dialogar sobre algún punto, puedes escribirme.
        Se agradece respetar la autoría y no acudir al copyright.
        </p>       
               
        </div>
        """, unsafe_allow_html=True) #Aquí termina mi reseña 1

#EN ORDEN POR AQUÍ, SOLO FALTA VER EL GLOSARIO.

#Con los disclaimers, coloco <p style="font-size:14px; color:#777; margin-top:40px;">

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
        <div style="width:60%; margin-left:auto;">

        <div style="font-size:16px; margin-bottom:25px;">
        <p style="font-style:italic;">
        Las profundas transformaciones ocurridas en las relaciones de género en el mundo, producen cambios ferozmente complejos en las condiciones de la práctica a la que deben adherir tanto hombres como mujeres.
        <b>Nadie es un espectador inocente en este escenario de cambio. </b> Estamos todos comprometidos en construir un mundo de relaciones de género.
        </p>
        <p style="text-align:right; margin-top:5px;">
        — Raewyn Connell
        </p>
        </div>

        <div style="font-size:16px; margin-bottom:25px;">
        <p style="font-style:italic;">
        El verdadero enfoque del cambio revolucionario no está nunca meramente en las situaciones opresivas de las que buscamos escapar, sino 
        <b>en ese pedazo del opresor que llevamos plantado profundamente en cada uno de nosotros.</b>
        </p>
        <p style="text-align:right; margin-top:5px;">
        — Audre Lorde
        </p>
        </div>

        <div style="font-size:16px;">
        <p style="font-style:italic;">
        Hasta ahora, los filósofos solo han interpretado el mundo de diversas maneras; 
        <b>de lo que se trata es de transformarlo.</b>
        </p>
        <p style="text-align:right; margin-top:5px;">
        — Karl Marx
        </p>
        </div>

        </div>
        """, unsafe_allow_html=True)
        
        #Para colocar en cursiva, coloco dentro de la frase <i>...</i>
        #Para colocar en negrita, dentro de la frase <b>...</b>
        #Aquí fueron las citas. Continuo con la reseña

#Aquí inicia un markdown (estructura de texto con su estilo, alias Luisa)
        st.markdown("""
        <div style="text-align: justify; font-size:18px;"> 
        <p>
        El género como categoría de análisis es una herramienta necesaria para comprender las dinámicas en nuestras interacciones humanas. 
        Además, nos invita a cuestionar los roles impuestos por la sociedad y, junto ello, la construcción histórica, racial y patriarcal de los mismos. 
        En este apartado, demostraré estos dos puntos, el de análisis y cuestionamiento, con el cortometraje español <i>El orden de las cosas</i> (2010), dirigido por los hermanos Esteban Alenda. 
        Este producto audiovisual nos permite dar cuenta, en un aproximado de 20 minutos, que la violencia, muchas veces, no se muestra de forma evidente. 
        Es en el silencio, en los gestos cotidianos y la complicidad de terceros donde también se manifiesta la violencia para seguir manteniendo el orden, sin necesitar gritos ni escenas dramáticas. 
        </p>           
        </div>
        """, unsafe_allow_html=True) #Para colocar en cursiva, coloco dentro de la frase <i>...</i>
#Aquí termina el markdown (la estructura del texto con su estilo)

        col9, col10, col11 = st.columns([1,2,1])
        with col10: 
            st.markdown("""
            Recomiendo ver el cortometraje antes de proceder con la lectura:
            """)
            st.video("https://www.youtube.com/watch?v=hfGsrMBsX1Q", width=800)   
            
        
        st.markdown("""
        <div style="text-align: justify; font-size:18px;">
        <p>
        Esta historia, protagonizada por la familia de Marcos y Julia (cónyuges) y Marquitos 
        (su hijo), se desarrolla casi por completo en un baño. Cargado de símbolos y metáforas, 
        este corto nos muestra que, con el paso del tiempo, el hijo crece, el esposo envejece 
        y el mobiliario dentro del hogar cambia; sin embargo, Julia permanece dentro de una 
        bañera, con la puerta siempre abierta y con la misma apariencia. Ella no pronuncia una 
        sola palabra. Todo lo que sabemos sobre su vida ocurre a través de los diálogos entre 
        Marcos, su hijo y otros familiares que entran y salen del espacio doméstico. Marcos, 
        sobre todo, es quien le habla, le pregunta y le exige respuestas, pero cabe enfatizar 
        que no es un diálogo entre dos personas: todo el temor, la desesperanza y la tristeza 
        de Julia se transmite por medio de sus expresiones faciales y corporales.
        Ella en ninguna escena emite su voz. Pero, pese a esa falta de palabras, aun así, podemos aseverar de
        que ella sufre violencia, por los moretones de su cuerpo, en sus gestos de miedo y en las palabras ambiguas de su esposo. 
        <i>“Tú sabes que te quiero mucho”</i> o <i>“Te cuidaré siempre”</i>, le asegura Marcos, 
        aunque la relación entre ellos está fuertemente marcada por el control y la intimidación. 
        </p>       
        <p> 
        Se trata de una subordinación sostenida por las desigualdades de género. En ella, 
        las mujeres son excluidas del espacio público —históricamente masculinizado— y 
        confinadas al ámbito doméstico, siendo receptoras pasivas, administradoras del hogar 
        y dependientes económicamente. Así, estos roles exigen a las mujeres cumplir con 
        estas condiciones devenidas del constructo social (y, en ese sentido, no innatas) 
        para seguir reproduciendo los estereotipos femeninos.
        Esta idea nos lo recuerda Carole Pateman (2000), ya que sugiere que la violencia no 
        es simplemente un problema individual y privado entre dos personas. 
        Al contrario, forma parte de un sistema de relaciones de poder que se reproduce dentro
        de la familia y fuera en la sociedad. De esta manera, si las mujeres no son consideradas
        ciudadanas con derechos plenos, ¿cómo el Estado pretende garantizar su bienestar? Para que su invisibilización sea permanente en la 
        ciudadanía, instituciones y políticas, es necesario que se ubiquen en el ámbito privado 
        siendo cuidadoras y dependientes, mientras que el Estado refuerza la división sexual.
        </p> 
        <p> 
        En esta lógica patriarcal, la familia aparece como un espacio donde las jerarquías de 
        género se “naturalizan”. Los hombres ocupan el lugar de autoridad y control, como el 
        pater familias, mientras que a las mujeres se les asigna el rol de cuidadoras y 
        administradoras del hogar. El personaje de Julia encarna precisamente esta posición y 
        su identidad se reduce a <i>ser madre de</i> Marquitos, <i>esposa de</i> Marcos y ama de casa, 
        rasgos identitarios que evidencian dependencia y vulnerabilidad. 
        Sin embargo, el cortometraje también permite observar pequeños gestos de resistencia. 
        En determinados momentos del corto, observamos que Julia ejerce su agencia —aunque de 
        forma limitada— dentro de contextos de dominación. Quizá la evidencia más notoria para 
        mostrar esta limitación es el lugar donde permanece y no sale, es vigilada por los demás
        y la puerta se mantiene siempre abierta. Aún así, en este espacio de la bañera, muestra 
        actos de rebeldía como, por ejemplo, no cumplir con los mandatos del hogar que sus 
        cuñados le exigen u ocultar el cinturón de Marcos, un objeto que funciona como símbolo 
        de la violencia y con el que parte el cortometraje: 
        <i>"Cariño, ¿has visto mi cinturón?"</i>.
        Pese a que no se muestra violencia física de forma explícita, sabemos que ella es 
        víctima de agresiones física, psicológica y emocional. Además de los moretones en el 
        cuerpo y el rostro de Julia, Marcos la manipula con promesas contradictorias: 
        <i>“Cariño, te cuidaré siempre”</i> o <i>“Tú sabes que te quiero mucho y que te cuidaré
        siempre. Si me duele más a mí.”</i>. Del mismo modo, es él quien habla por ella 
        creyendo manifestar lo que ella desea: <i>“Ella quiere quedarse aquí conmigo”</i>. 
        Y si no fuera poco lo anterior, le transmite el mensaje como si Julia fuera la 
        responsable: <i>“No sé por qué te niegas a aceptar el orden de las cosas, Julia. 
        No lo entiendo”</i>. Entre contradicciones se disfrazan de palabras de afecto y, 
        como es de esperarse, las promesas no se cumplen al estar regido por una relación 
        vertical y violenta contra Julia.  
        </p>
        <p>
        Otro punto a señalar es que la historia sugiere que estas prácticas se transmiten 
        de generación en generación. Los hermanos de Marcos lo presionan para que ejerza 
        la "mano dura" que interiorizaron ellos de su padre: <i>“¿Es que acaso no aprendiste 
        de papá? ¿Qué pasa, que tienes una mujer desobediente y un niño malcriado? 
        A ver si el verdadero problema eres tú, que no te haces respetar”</i> y <i>“Mano dura 
        es lo que siempre te ha hecho falta”</i>. Vemos así que la violencia aparece no 
        solo como una acción individual, sino como una expectativa social vinculada a ciertos 
        modelos de masculinidad. La socióloga Raewyn Connell (1997) ha explicado este fenómeno a través del concepto 
        de "masculinidad hegemónica": una forma dominante de ser hombre que se legitima 
        mediante la autoridad, la fuerza y el control sobre hombres “más débiles” y 
        mujeres, demostrando constantemente su aceptación y legitimación dentro del 
        patriarcado. <b>El género, más allá de sustentarse en una base biológica, es una 
        forma de ordenamiento de prácticas sociales.</b> En el cortometraje, Marcos parece 
        sentirse constantemente evaluado por ese ideal masculino, especialmente frente a 
        sus hermanos. Por ello, no es casual que se muestren incluso con una apariencia 
        distinta a él; es decir, son más altos que él y andan con “las corbatas bien puestas”, 
        de modo que la virilidad y respetabilidad se gana dominando a los más marginados, 
        incluyendo a las mujeres.
        </p>
        <p>
        Lo más resaltante aquí es que esta práctica no se reproduce únicamente entre los 
        hombres. En una de las escenas, las cuñadas de Julia también la critican por no 
        cumplir adecuadamente con su rol doméstico. En lugar de cuestionar la violencia, 
        son las propias mujeres quienes también la reinterpretan como un problema de 
        desobediencia o falta de amor: <i>“Si (Julia) te quisiera de verdad, no te haría 
        sufrir tanto”</i>. Aquí, la contradicción es posible al creer que la sumisión y 
        obediencia muestra el amor hacia el esposo; el poder violentarla permite que él 
        siga legitimando su poder en el sistema dominado por la masculinidad hegemónica. 
        <b>De este modo, la violencia tergiversa haciendo creer que el que sufre es él y 
        no ella, pese a que los golpes y la manipulación lo recibe Julia.</b> 
        La responsable es ella por romper con el orden patriarcal y esto lo podemos 
        comprobar con los comentarios comunes de la sociedad, como <i>“ella se buscó el golpe”</i> 
        o <i>“ella no tiene por qué negarse a tener relaciones con su marido”</i>.
        </p>
        <p>
        El sistema de poder patriarcal se sostiene a través de estas prácticas y creencias 
        compartidas por quienes viven dentro de él, de modo que, si salimos de él, 
        <i>“puede ser peor”</i> como le dice una de las cuñadas a Julia. Sin embargo, 
        también es necesario enfatizar que, a lo largo de la historia, vemos a Marquitos 
        como un personaje disruptivo. Él crece dentro de este ambiente familiar marcado por 
        la violencia. Su padre intenta enseñarle el mismo modelo de masculinidad que aprendió 
        de generaciones anteriores: ser fuerte, imponer autoridad y mantener el control; 
        aun así, su hijo rechaza este mandato. Desde el momento en que descubre los moretones 
        de su madre se produce una ruptura simbólica. El juguete de avión que llevaba en la 
        mano cae al suelo y se rompe, como símbolo del quiebre de su infancia y, al mismo 
        tiempo, <b>la posibilidad de que ese ciclo de violencia no continúe necesariamente en 
        la siguiente generación</b>. Así lo mostró al crecer y tener la mayoría de edad para 
        salir de casa y no perpetuar la violencia aprendida en familia. 
        </p>
        <p>
        El título del cortometraje, <i>“El orden de las cosas”</i>, parece aludir precisamente a esa 
        normalización de la violencia. Cuando Marcos le dice a Julia que <i>"así son las cosas"</i> 
        o su cuñada le aconseja porque puede ser peor para ella, se está apelando a la idea de que 
        estas jerarquías son naturales o inevitables. No obstante, es el mismo cortometraje el que 
        nos invita a cuestionar esa afirmación. De ahí que el título de este escrito se remita al 
        (des)orden de las cosas. Lo que se presenta como un orden natural es, en realidad, el 
        resultado de relaciones históricas de poder. 
        La violencia que ocurre dentro del hogar no es simplemente un asunto privado; 
        <b>forma parte de estructuras sociales más amplias.</b> Tal como se muestra al final 
        del cortometraje, Julia sale del mar y la última escena proyecta varias tinas vacías, 
        sugiriendo que muchas otras mujeres, cuyas experiencias de violencia permanecen ocultas
        dentro de los espacios privados, salen a la luz cuando ya es tarde. Por eso, se 
        proclama el lema "lo personal es político". Si bien las experiencias ocurren en el 
        ámbito íntimo, en las relaciones de pareja, la vida familiar y el trabajo doméstico, 
        también están atravesadas por relaciones de poder que tienen consecuencias sociales y 
        políticas en el espacio público.
        </p>
        <p>
        El énfasis se encuentra también en que tanto la familia como la sociedad lo enseñan 
        como <i>un deber</i>: los infantes deben diferenciar lo que le corresponde a un hombre 
        (usar ropa o implementos azules, jugar con carros, practicar el fútbol y practicar 
        deportes de contacto), totalmente distinto a lo que sería para la mujer (utilizar 
        el rosa, jugar con muñecas, practicar el ballet y tener “buenos” modales). Por ello, 
        la figura del cinturón aparece también como mecanismo para que Marcos le enseñe a su 
        hijo lo que le corresponde, como hombre, en función de la tradición familiar: aplicar 
        la dureza, tal como le enseñó su abuelo a su padre, y este a él y a sus hermanos. 
        </p>
        <p>
        Esto nos permite comprender por qué la violencia incluso es tolerable socialmente. 
        En nuestro contexto peruano, por ejemplo, según los datos del 
        <a href="https://www.gob.pe/institucion/inei/noticias/1205421-28-6-de-las-mujeres-de-18-y-mas-anos-de-edad-vive-bajo-la-dependencia-economica-de-la-pareja-o-expareja" target="_blank">
        INEI (2025)
        </a>
        , una parte significativa de la población declara tolerar ciertas formas de violencia contra las 
        mujeres: el 80,8% de los hombres mayores de 18 años toleran la violencia contra la 
        mujer, mientras que en el caso de las mujeres es el 70,9%. Algunas ideas compartidas 
        se sintetizan en 
        </p>
        <p>
        <p style="margin-left:40px;">
        (a) Si ella decide emborracharse y es abusada, es su culpa.
        </p>
        <p style="margin-left:40px;">
        (b) Si es infiel, debe ser castigada.
        </p>
        <p style="margin-left:40px;">
        (c) Si no da señales de resistencia, no puede decir que fue violada.
        </p>
        <p>
        Estas creencias no aparecen de la nada: se construyen a lo largo de la vida a través 
        de la familia, la cultura y las normas sociales. En muchos contextos patriarcales, 
        la violencia se mantiene allí sobre estructuras sociales que la normalizan y cuyos 
        agentes (los hombres) aprenden a ejercerla como legítima y en contra de las mujeres, 
        personas trans, masculinidades no hegemónicas. Como lo desarrollaría Rita Segato en 
        <i>Contra-pedagogías de la crueldad</i> (2018), si vemos un escenario de violencia 
        machista, este no es un acto individual o que se ubique solamente en vínculos 
        domésticos, pues proviene de un escenario cultural que organiza a sus individuos 
        tanto en la sociedad, el Estado, la Iglesia y el mercado: “Es imposible hoy abordar 
        el problema de la violencia de género y la letalidad en aumento de las mujeres como 
        si fuera un tema separado de la situación de intemperie de la vida, con la suspensión 
        de las normativas que dan previsibilidad y amparo a las gentes dentro de una gramática 
        compartida” (p. 14).
        </p>
        <p>
        En suma, no solo es resignarnos a escuchar a Marcos decir que <i>“No puedes elegir. 
        Las cosas son así y ya está. Así ha sido siempre”</i>. Si queremos transformar 
        realmente estas relaciones, no basta preguntarnos por qué Julia no se fue. 
        Más que conformarnos con culparla por escogerlo a él o quedarse, valdría cuestionarnos 
        <b>cuáles son las condiciones sociales, culturales y económicas que hacen posible que ese 
        "orden de las cosas" continúe existiendo de manera histórica y sistemática. </b>
        En la medida que se trate de una herencia patriarcal, deberíamos centrarnos en responder: 
        <b>¿qué mundo hace posible que quedarse parezca la única opción?</b>
        </p>
        <hr style="margin-top:40px;">
        <p style="font-size:20px; font-weight:bold; color:#9a62a5;">
        Bibliografía
        </p>
        <p style="margin-bottom:12px; font-size:16px;">
        AlendaBros (2013). <i>EL ORDEN DE LAS COSAS - Corto contra la violencia de género</i> [Vídeo]. YouTube. 
        <a href="https://www.youtube.com/watch?v=hfGsrMBsX1Q" target="_blank">
        https://www.youtube.com/watch?v=hfGsrMBsX1Q
        </a>
        </p>
        <p style="margin-bottom:12px; font-size:16px;">
        Connell, R. W. (1997). La organización social de la masculinidad. En T. Valdés & J. Olavarría (Eds.), 
        <i>Masculinidad/es: Poder y crisis</i> (pp. 31–48). Ediciones de las Mujeres.
        </p>
        <p style="margin-bottom:12px; font-size:16px;">
        Instituto Nacional de Estadística e Informática. (2025, 8 de julio). 28,6 % de las mujeres de 18 y más años de edad vive bajo la dependencia económica de la pareja o expareja. 
        <a href="https://www.gob.pe/institucion/inei/noticias/1205421-28-6-de-las-mujeres-de-18-y-mas-anos-de-edad-vive-bajo-la-dependencia-economica-de-la-pareja-o-expareja" target="_blank">
        Ver fuente
        </a>
        </p>
        <p style="margin-bottom:12px; font-size:16px;">
        Pateman, C. (2000). El estado de bienestar patriarcal. En <i>Contextos</i> (N.º 5, pp. 1–20). Lima: PUCP/DEG.
        </p>
        <p style="margin-bottom:12px; font-size:16px;">
        Segato, R. (2018). <i>Contra-pedagogías de la crueldad</i>. Ciudad Autónoma de Buenos Aires: Prometeo Libros.
        </p>
        <hr style="margin-top:40px; margin-bottom:10px;">

        <p style="font-size:14px; color:#777; text-align:justify;">
        Al momento de releer este escrito que elaboré para un curso de la MEG (julio 2025), 
        no pude evitar pensar en la ausencia de otros contextos no desarrollados aquí. En este escrito, 
        me enfoqué en una forma específica de violencia —urbana, heterosexual y familiar— que, si bien es 
        ampliamente documentada y es posible acceder a ella, no agota la diversidad de experiencias tales 
        como de comunidades indígenas, relaciones no-heterosexuales o economías no plenamente urbanizadas. 
        En estos contextos, tanto la división de lo público y lo privado, como los roles de género, podrían 
        adquirir formas distintas que serán analizadas en otras hiedras. 
        </p>

        <p style="font-size:14px; color:#777; text-align:justify; margin-top:10px;">
        Aun así, si te surge algún cuestionamiento o quieres dialogar sobre algún aspecto de este tema en particular, 
        escríbeme. 
        Se agradece respetar la autoría y no acudir al copyright.
        </p>     
        </div>
        """, unsafe_allow_html=True)  

#Aquí cierro mi reseña 2 con el markdown  

# EMPIEZA LA SECCIÓN DE INTELECTUALES EN EL MUNDO
    
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
    <div style="text-align: justify; font-size:16px;">
    <p>
    <b>Este mapa nace de una constatación simple: la historia de la filosofía (y del pensamiento crítico) ha sido construida desde una perspectiva parcial, marcada por la exclusión sistemática de otras voces y experiencias. 
    Aquí se reúnen filósofas, teóricas y pensadoras cuyas ideas han cuestionado esa ausencia, analizando el poder, el conocimiento, el cuerpo y la justicia desde perspectivas que incomodan y transforman. 
    Aunque muchas de estas autoras han reflexionado sobre el género y las desigualdades, el mapa no se limita a ello: busca visibilizar la participación de las mujeres en la producción de conocimiento en sentido amplio. 
    Actualmente, incluye más de 70 mujeres de diversas tradiciones y contextos, y se encuentra en constante crecimiento. En la medida en que nuevas lecturas, investigaciones y hallazgos amplíen este recorrido, el mapa seguirá incorporando más voces
    (¡también acepto sugerencias!).</b>
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
                <div style="
                    width:220px; 
                    text-align:center;
                    font-family:sans-serif;
                ">
                    <b style="font-size:16px;">{fila['Filósofa / Pensadora']}</b><br><br>

                    <img src="{fila['Foto de la filósofa (Buscador)']}" 
                    width="160" style="border-radius:8px;"><br><br>

                    <div style="text-align:left; font-size:13px; line-height:1.4;">
                        <b>Nacionalidad:</b> {fila['Nacionalidad']}<br>
                        <b>Lugar:</b> {fila['Lugar de nacimiento']}<br>
                        <b>Áreas:</b> {fila['Áreas de investigación']}<br>
                        {url}
                    </div>
                </div>
                """
            # Agregamos un marcador en las coordenadas del país
            folium.Marker(
                location=[lat, lon],                   # Coordenadas del marcador
                popup=folium.Popup(contenido, max_width=300),  # Popup con información en HTML
                tooltip=fila['Filósofa / Pensadora'],  # CLAVE PARA SINCRONIZAR
                icon=folium.Icon(color='darkred', icon='user')    # Ícono azul con forma de usuario
            ).add_to(m)

    # --- MAPA ---
    mapa = st_folium(m, use_container_width=True, height=500)

    # --- CAPTURA CLICK ---
    seleccion_mapa = None

    if mapa and mapa.get("last_object_clicked_tooltip"):
        seleccion_mapa = mapa["last_object_clicked_tooltip"]

    # --- SESSION STATE ---
    if "autor_seleccionado" not in st.session_state:
        st.session_state["autor_seleccionado"] = None

    if seleccion_mapa:
        st.session_state["autor_seleccionado"] = seleccion_mapa

    # --- TÍTULO BUSCADOR ---
    st.markdown("""
    <h2 style="
        font-size:30px;
        color:#9a62a5;
        font-weight:900;
        text-align:center;
        margin-bottom:20px;
    ">
    Buscador de autora o pensadora
    </h2>
    """, unsafe_allow_html=True)

    # --- SELECTBOX CONECTADO ---
    lista_nombres = datos_filo["Filósofa / Pensadora"].sort_values().unique()

    if st.session_state["autor_seleccionado"] in lista_nombres:
        index_default = list(lista_nombres).index(st.session_state["autor_seleccionado"])
    else:
        index_default = 0

    nombre = st.selectbox(
        "¡Indaga por aquí!",
        lista_nombres,
        index=index_default,
        key="autor_seleccionado" # 🔗 sincroniza si el usuario cambia manualmente
    )

    # --- RESULTADO ---
    resultado = datos_filo[datos_filo["Filósofa / Pensadora"] == nombre]

    if not resultado.empty:
        fila = resultado.iloc[0]

        # --- NOMBRE ---
        st.markdown(f"""
        <h2 style="
            font-size:28px;
            color:#9a62a5;
            font-weight:900;
            text-align:center;
            margin-bottom:5px;
        ">
        {fila["Filósofa / Pensadora"]}
        </h2>
        """, unsafe_allow_html=True)

    # --- BLOQUE 1: IDENTIDAD + FOTO ---
    col1, col2 = st.columns([1,2])

    with col1:
        st.image(fila["Foto de la filósofa (Buscador)"], width=180)

    with col2:
        st.markdown(f"""
        <div style="font-size:15px; line-height:1.6; text-align:justify;">
        <b>Nacionalidad:</b> {fila["Nacionalidad"]}<br>
        <b>Lugar de nacimiento:</b> {fila["Lugar de nacimiento"]}<br>
        <b>Áreas:</b> {fila["Áreas de investigación"]}
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # --- BLOQUE 2: DESCRIPCIÓN ---
    descripcion = fila["Descripción (Buscador)"]

    partes = descripcion.split("\n", 1)

    if len(partes) == 2:
        titulo, cuerpo = partes
    else:
        titulo, cuerpo = descripcion, ""

    st.markdown(f"""
    <div style="
        background-color:#f5f5f5;
        padding:12px 14px;
        border-radius:8px;
        line-height:1.4;
    ">
        <div style="
            font-weight:bold;
            margin-bottom:4px;
        ">
            {titulo}
        </div>
        <div style="
            font-size:0.95rem;
            text-align: justify;
        ">
            {cuerpo}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")

    # --- BLOQUE 3: OBRAS + IMAGEN ---
    col3, col4 = st.columns([2,1])
    
    import re

    with col3:
        st.markdown("""
        <h3 style="color:#9a62a5;">Obras principales</h3>
        """, unsafe_allow_html=True)

        obras = fila["Obras"]

        lista_obras = re.findall(r'.+?\(\d{4}\)', obras)
        lista_obras = [obra.strip().lstrip(", ") for obra in lista_obras]
        lista_obras = list(dict.fromkeys(lista_obras))

        for obra in lista_obras:
            st.markdown(f"- {obra}")

            
    with col4:
        st.image(fila["Foto de la obra"], width=140)

    st.write("")

    # --- BLOQUE 4: VIDEOS ---
    if pd.notna(fila["Video explicativo sobre la autora"]) and str(fila["Video explicativo sobre la autora"]).strip() != "":
        col_video = st.columns([1,2,1])[1]
        with col_video:
            st.video(fila["Video explicativo sobre la autora"])

    if pd.notna(fila["Entrevista o conferencia"]) and str(fila["Entrevista o conferencia"]).strip() != "":
        col_video = st.columns ([1,2,1])[1]
        with col_video:
            st.video(fila["Entrevista o conferencia"])

    st.write("")

# SECCIÓN DE POEMAS

elif selected == "Versos sueltos":

    st.markdown("""
    <h1 style="
        font-size:60px;
        color:#9a62a5;
        font-weight:900;
        text-align:center;
        margin-bottom:20px;
    ">
    El eco en la poesía
    </h1>
    """, unsafe_allow_html=True)


    st.markdown("""
    <div style="text-align: justify; font-size:16px;">
    <p><b>La memoria es frágil, así que opto por guardar aquí aquellos poemas que me motivan 
    a seguir construyendo las ideas que defiendo y aspiro. Todos ellos tienen un núcleo en común: 
    desde actos de resistencia, hasta el derecho inalienable a no ser "iguales”.</b></p>
    </div>
    """, unsafe_allow_html=True)

    # 🔹 AQUÍ he llamado al docx tal como se mantiene
    poemas = cargar_poemas("poemas.docx")


    # 🔹 AQUÍ los muestro
    for p in poemas:
        if "titulo" not in p:
            continue
        with st.expander(f" {p['titulo']} ({p.get('autor','')})"):

            st.markdown(f"""
            <div style="
                font-size:18px;
                line-height:1.8;
                margin-left:120px;
                border-left:2px solid #9a62a5;
                padding-left:20px;
            ">
            {p['texto']}
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style="
                background-color:#f5f5f5;
                padding:15px;
                border-radius:10px;
                margin-top:20px;
                font-size:14px;
            ">
            🍃 {p.get('info','')}
            </div>
            """, unsafe_allow_html=True)


# AQUÍ TERMINA LA SECCIÓN DE VERSOS SUELTOS

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