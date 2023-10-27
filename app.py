import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

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

    # Draw the graph
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=12, font_weight='bold')
    plt.axis('off')
    st.pyplot()

# Call the function to generate and display the SWOT analysis mind map
generate_swot_mind_map()

if __name__ == '__main__':
    st.title('SWOT-анализ открытого коммерческого хостинга с открытым искусственным интеллектом для университетов/студентов/преподавателей')
    generate_swot_mind_map()
