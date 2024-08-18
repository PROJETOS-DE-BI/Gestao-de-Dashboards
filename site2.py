import streamlit as st

# Título do site
st.title("Solicitação de Orçamento")

# Instruções
st.write("Preencha o formulário abaixo para solicitar um orçamento. Entraremos em contato em breve!")

# Formulário para inserção de e-mail e descriçãowith st.form(key='form_orcamento'):
    # Campo para inserir e-mail
    #email = st.text_input("Seu e-mail:")
    
    # Campo para descrever o serviço
    descricao = st.text_area("Descrição do serviço:")
    
    # Botão para enviar o formulário
    submit_button = st.form_submit_button(label='Enviar')

# Mensagem de confirmaçãoif submit_button:
    if email and descricao:
        st.write(f"Obrigado por sua solicitação, {email}! Recebemos sua descrição:")
        st.write(descricao)
    else:
        st.error("Por favor, preencha todos os campos.")
