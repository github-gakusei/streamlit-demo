import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz as pgv

# SWOT analysis data
swot_data = {
    'Strengths (Сильные стороны)': ['Бесплатное использование', 'Легкость использования', 'Гибкость', 'Обучение и поддержка'],
    'Weaknesses (Слабые стороны)': ['Ограниченные ресурсы', 'Техническая сложность'],
    'Opportunities (Возможности)': ['Распространение знаний', 'Интеграция с AI'],
    'Threats (Угрозы)': ['Конкуренция', 'Безопасность данных']
}

def generate_swot_mind_map():
    # Create an empty graph
    G = nx.Graph()

    # Add nodes to the graph
    for category in swot_data:
        G.add_node(category)
        for item in swot_data[category]:
            G.add_node(item)
            G.add_edge(category, item)

    # Create a layout using pygraphviz
    pos = nx.nx_agraph.graphviz_layout(G, prog='dot', root='Strengths (Сильные стороны)')

    # Draw the graph
    plt.figure(figsize=(10, 8))
    nx.draw_networkx(G, pos, with_labels=False, node_color='lightblue', node_size=2000, font_size=12, font_weight='bold')
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', font_color='black')
    plt.axis('off')
    st.pyplot()

# Set a white background color for the Streamlit app
st.markdown('<style>body{background-color: #ffffff;}</style>', unsafe_allow_html=True)

# Display the title
st.title('SWOT-анализ открытого коммерческого хостинга с открытым искусственным интеллектом для университетов/студентов/преподавателей')

# Call the function to generate and display the SWOT analysis mind map
generate_swot_mind_map()
