# pip install streamlit streamlit-lottie pillow requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import requests

st.set_page_config(page_title='ValerApp', 
                   page_icon='🛥️', 
                   layout='wide') #layout='centered'

def css_load(css_file):
    with open(css_file) as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)

css_load('styles/main.css')


def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie = load_lottie('https://assets6.lottiefiles.com/packages/lf20_ggwq3ysg.json')


with st.container():
    st.header('Hola, somos ValerApp')
    st.title('Creamos soluciones para acelerar tu negocio')
    st.write('Consequat culpa reprehenderit deserunt cupidatat nisi culpa. Do elit ipsum ad sit commodo non in excepteur labore aliquip enim excepteur ea. Excepteur sint dolor Lorem incididunt pariatur aute enim cupidatat ea magna non occaecat. Excepteur voluptate deserunt aute ex reprehenderit voluptate Lorem dolore non commodo. Consectetur exercitation mollit ipsum deserunt. Sit elit sit ea fugiat reprehenderit occaecat excepteur sit.')
    st.write('[Saber mas > ](https://valerapp.com/)')

with st.container():
    st.write('---')
    t_col, a_col = st.columns(2)
    
    with t_col:
        st.header('Sobre nosotros')
        st.write(
            '''
        Nostrud adipisicing quis ipsum aliquip fugiat veniam. Nulla proident culpa duis eiusmod fugiat consequat culpa et do cillum mollit. Nulla laborum culpa quis amet consectetur commodo eiusmod nostrud voluptate.

        Quis consectetur aliquip aute amet consectetur aute irure. Quis Lorem pariatur magna do ex et non eu ut duis eu id. Anim eu est sunt ea aliquip enim exercitation amet dolor minim eiusmod. Ad anim reprehenderit aute nulla id ad labore.

        Aliquip magna nisi ut irure anim occaecat culpa occaecat duis mollit. Amet reprehenderit commodo voluptate deserunt irure ex elit eu fugiat. Sit amet cupidatat nostrud fugiat deserunt ad elit qui minim. Lorem id consectetur voluptate laboris dolore ea esse nulla qui deserunt ea sint reprehenderit. Est nostrud ex nostrud nostrud excepteur aliqua consequat est in sit. Qui eiusmod occaecat nulla duis adipisicing exercitation eu ex. Nostrud magna occaecat amet velit in aliquip voluptate aute est.
        '''
        )
        st.write('[Mas sobre nosotros > ](https://valerapp.com/about/)')
    
    with a_col:
        st_lottie(lottie, height=400)
    
with st.container():
    st.write('---')
    st.header('Servicios')
    st.write('##')
    i_col, t_col = st.columns((1,2))

    with i_col:
        image = Image.open('images/image.jpg')
        st.image(image, use_column_width=True)
    
    with t_col:
        st.subheader('Diseno de aplicaciones')
        st.write(
            '''
            Fugiat excepteur exercitation nulla fugiat anim cillum in proident nostrud nulla elit mollit incididunt occaecat. Lorem eu fugiat Lorem aliqua pariatur culpa in commodo non incididunt qui est. Id dolore commodo non et ullamco duis quis quis laborum mollit.
            '''
                 )
        st.write('[Ver servicios](https://vaperapp/services/)')

