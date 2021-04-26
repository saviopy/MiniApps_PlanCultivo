import streamlit as st
from math import floor
st.title('Planejamento de Ciclo de cultivo de peixes 🐟') 
st.write('')
st.write('')
st.write('Uma forma prática e fácil de calcular a quantidade de peixes a se colocar no viveiro.')
st.header('Selecione o que deseja calcular:')
engorda= st.checkbox('Número de peixes para a fase de engorda')
alevinagem = st.checkbox('Número de peixes no tanque de alevinagem')
densidade = st.checkbox('Densidade de estocagem na alevinagem')
tanque = st.checkbox('Definição do tanque de alevinagem (em hectares)')

st.header('Para fazer esses cálculos preencha todas as informações abaixo.')
st.write('')
st.write('') 
biomassa_final = st.number_input('Qual a biomassa final da engorda (kg/ha)?',value = 0.01)
biomassafinal_verifica = st.empty()
peso_final_e = st.number_input('Qual o peso final da engorda (kg)?', value = 0.01)
pesofinale_verifica = st.empty()
mortalidade = st.number_input('Qual é taxa de mortalidade (%)?',value = 0.01, help ='Não use o símbolo de porcentagem!')
mortalidade_verifica = st.empty()
peso_final_a = st.number_input('Qual o peso final da alevinagem? (kg)',value = 0.01)
pesofinala_verifica = st.empty()
if st.button('MOSTRAR RESULTADOS'):
    resultados = []
    parametros = [] 
    variaveis = []
    nomes = []   
    if peso_final_e == 0.01:
        pesofinale_verifica.error('Valor definido como 0.01, insira um valor válido.')
    if biomassa_final == 0.01:
        biomassafinal_verifica.error('Valor definido como 0.01, insira um valor válido.')
    if mortalidade == 0.01:
        mortalidade_verifica.error('Valor definido como 0.01, insira um valor válido.')
    if peso_final_a == 0.01:
        pesofinala_verifica.error('Valor definido como 0.01, insira um valor válido.')

    for i in range(1):
        if engorda == True:
            n_peixes = biomassa_final / peso_final_e
            fn_peixes = floor(n_peixes)
            resultados.append(fn_peixes)
            parametros.append('Quantidade de peixes final')
            variaveis.append(biomassa_final)
            n1 = 'Biomassa final da engorda'
            nomes.append(n1)
            st.success('Para a engorda serão necessários **{} peixes**.'.format(floor(n_peixes)))
        if alevinagem == True:
            n_peixes = biomassa_final / peso_final_e
            t_alevinagem = n_peixes * (mortalidade / 100) + n_peixes
            ft_alevinagem = floor(t_alevinagem)
            resultados.append(ft_alevinagem)
            parametros.append('Quantidade de peixes inicial')
            variaveis.append(str(peso_final_e))
            n2 = 'Peso final da engorda'
            nomes.append(n2)
            st.success('Para a alevinagem precisará de **{} peixes.**'.format(floor(t_alevinagem)))
        if densidade == True:
            d_alevinagem = biomassa_final / 3
            fd_alevinagem = (round(d_alevinagem,1))
            resultados.append(str(fd_alevinagem))
            variaveis.append(mortalidade)
            n3 = 'Mortalidade (%)'
            nomes.append(n3)
            parametros.append('Biomassa final da alevinagem(kg/ha)')
            st.success ('A densidade da alevinagem será de **{:.1f} kg/ha.**'.format(d_alevinagem))
        if tanque == True:
            n_peixes = biomassa_final / peso_final_e
            t_alevinagem = n_peixes * (mortalidade / 100) + n_peixes
            d_alevinagem = biomassa_final / 3
            tanque_alev = t_alevinagem - (t_alevinagem * (mortalidade / 100))
            b_estocada = tanque_alev * peso_final_a
            tamanho_tanque = (b_estocada / d_alevinagem)
            ftamanho_tanque = (round(tamanho_tanque,2))
            resultados.append(str(ftamanho_tanque))
            variaveis.append(str(peso_final_a))
            n4 = 'Peso final da alevinagem (kg)'
            nomes.append(n4)
            parametros.append('Área de viveiro (ha)')
            st.success('O tanque de alevinagem será de **{:.2f} hectares**.'.format(tamanho_tanque))

        import pandas as pd
        import base64
        st.write('')
        st.write('')
        st.header('**Tabela de resultados**')
        tabela = {
            'Dados': nomes,
            'Valores': variaveis,
            'Parâmetro': parametros,
            'Valor': resultados,
        }

        df = pd.DataFrame(tabela)

        st.table(df)

        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f' <a href="data:file/csv;base64,{b64}" download="Planejamento_Cultivo.csv">Download da tabela</a>'
        st.markdown(href, unsafe_allow_html=True)
        st.markdown("Se o download não iniciar, clique com o botão direito sobre **Download da tabela** e escolha a opção **'Salvar link como'**")

        #st.markdown(get_table_download_link(data), unsafe_allow_html=True)
st.write('')
st.write('')
st.markdown('Para mais informações sobre Índices Zootécnicos [clique aqui.] (https://www.infoteca.cnptia.embrapa.br/infoteca/bitstream/doc/1023958/1/2015cpamtituassucalculopovoamentoviveiros.pdf)')