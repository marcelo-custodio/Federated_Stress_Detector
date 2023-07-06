import streamlit as st
import time
import random
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import requests
import json

# configurações iniciais
st.set_page_config(layout="wide")

# abas laterais
tabs = st.sidebar.radio('Real Time Stress', ('Apresentação', 'Medidações atuais', 'Dicas para Redução de Estresse'))

# aba apresentação
if tabs == 'Apresentação':
    # Título e apresentação
    st.markdown('<h1 style="text-align: center;">Real Time Stress</h1>', unsafe_allow_html=True)
    st.markdown('## Cuidando da sua saúde mental em tempo real')

    # intro
    st.markdown('A saúde mental é um aspecto fundamental para o bem-estar e qualidade de vida. O estresse é uma das principais causas de problemas de saúde mental, e é essencial identificar e gerenciar o estresse de forma adequada.')
    st.markdown('O Real Time Stress é um aplicativo desenvolvido para auxiliar no monitoramento do nível de estresse em tempo real, fornecendo uma ferramenta útil para acompanhar e tomar medidas para reduzir o estresse.')

    # benefícios
    st.markdown('### Benefícios do Real Time Stress')
    st.markdown('- Monitoramento contínuo do nível de estresse')
    st.markdown('- Identificação de momentos de alta tensão')
    st.markdown('- Orientações para redução do estresse')
    st.markdown('- Acompanhamento do progresso ao longo do tempo')

    # rodapé
    st.markdown('---')
    st.markdown('**Disclaimer:** Este aplicativo não substitui o acompanhamento médico ou profissional na área de saúde mental. Consulte sempre um profissional qualificado para obter orientações personalizadas.')

# aba do gráfico
elif tabs == 'Medidações atuais':
    # criar figura p gráfico
    fig = go.Figure()

    # dados do gráfico
    x_data = []
    y_data = []

    # adicionar trace inicial
    fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='lines', name='Nível de Estresse'))

    # função para att gráfico
    def update_graph(x, y):
        fig.data[0].x = x
        fig.data[0].y = y

        fig.update_layout(
            xaxis_title='Tempo',
            yaxis_title='Nível de Estresse',
            title='Gráfico em Tempo Real'
        )

        st.plotly_chart(fig, use_container_width=True)

    # Função para obter os dados do ESP
    def get_data_from_esp():
        # Fazer a solicitação GET para o ESP
        url = "http://192.168.2.18:5000/random_data"
        response = requests.get(url)

        if response.status_code == 200:
            data = json.loads(response.text)
            return data['data']
        else:
            return None

    # função principal
    def main():
        # configurar streamlit
        st.sidebar.markdown('## Real-Time Stress')
        st.sidebar.markdown('### Medidações Atuais')

        start_time = time.time()

        # obter dados iniciais do ESP
        stress_level = get_data_from_esp()
        if stress_level is not None:
            x_data.append(0)
            y_data.append(stress_level)
            update_graph(x_data, y_data)

        # loop para att gráfico
        while True:
            # obter dados ESP
            stress_level = get_data_from_esp()

            if stress_level is not None:
                # calcular tempo decorrido
                elapsed_time = time.time() - start_time

                # att grafico
                x_data.append(elapsed_time)
                y_data.append(stress_level)
                update_graph(x_data, y_data)

            # esperar um intervalo de tempo antes da proxima atualização
            time.sleep(1)

    # executar função princiapl
    if __name__ == '__main__':
        main()

# aba de dicas
else:
    st.markdown('<h1 style="text-align: center;">Dicas para Redução de Estresse</h1>', unsafe_allow_html=True)
    st.write('        ')
    st.write('        ')
    st.write('        ')
    st.write('        ')
    st.write('Aqui estão algumas dicas para ajudar a reduzir o estresse:')
    st.write('- Respire fundo e faça exercícios de relaxamento')
    st.write('- Pratique atividades físicas regulares')
    st.write('- Durma o suficiente e mantenha uma dieta saudável')
    st.write('- Faça pausas regulares durante o trabalho')
    st.write('- Encontre atividades prazerosas para relaxar, como ouvir música ou ler um livro')
    st.write('- Cultive relacionamentos saudáveis e compartilhe seus sentimentos com pessoas próximas')
    st.write('- Gerencie seu tempo e priorize suas tarefas')
    st.write('- Evite pensamentos negativos e pratique a positividade')
    st.write('- Busque ajuda profissional quando necessário')

    # adicional
    st.subheader('Dicas Avançadas')
    st.write('- Evite o consumo excessivo de cafeína e álcool')
    st.write('- Estabeleça limites saudáveis e aprenda a dizer "não" quando necessário')
    st.write('- Mantenha-se organizado e estabeleça metas realistas')
    st.write('- Aprenda técnicas de gerenciamento de estresse, como visualização e relaxamento muscular progressivo')
    st.write('- Desenvolva habilidades de comunicação e resolução de conflitos')
    st.write('- Reserve um tempo para hobbies e atividades criativas')
    st.write('- Mantenha-se conectado com a natureza e aproveite o ar livre')
    st.write('- Desconecte-se das telas e dedique tempo para desconectar e descansar')
