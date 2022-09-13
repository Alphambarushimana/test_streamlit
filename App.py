import streamlit as st
st.title('oh baby baby, how was i.... ')

sentences1=st.text_input('Instert sentence 1:')
sentences2=st.text_input(' Insert sentence 2: 2')


if st.button('Submit'):
  st.write('Sentences1 is: ', sentences1)
  st.write(' Sentences2 is:', sentences2)

