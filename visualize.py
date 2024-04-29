import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
df = pd.read_csv('music_genre_graph_ready.csv')
# # Create a graph
G = nx.Graph()

# # Add edges and edge attributes
for _, row in df.iterrows():
    G.add_edge(row['Genre 1'], row['Genre 2'], weight=row['Cosine Similarity'])


# Draw the network
import plotly.graph_objects as go
import networkx as nx

# Generate positions for each node using a layout (e.g., spring layout)
pos = nx.spring_layout(G, weight='Cosine Similarity')

# Create edge traces
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])  # Use extend to add all three at once
    edge_y.extend([y0, y1, None])

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

# Create node traces
node_x = []
node_y = []
node_text = []  # Text for hoverinfo
for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    node_text.append(node)  # Add the node's name (rapper's name) for hoverinfo

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers',
    hoverinfo='text',
    text=node_text,  # Assign the hover text
    marker=dict(
        showscale=True,
        color=list(dict(G.degree).values()),
        size=10,
        colorbar=dict(
            thickness=15,
            title='Node Connections',
            xanchor='left',
            titleside='right'),
        line_width=2))

# Create the figure
fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    title='<br>Network graph made with Python',
                    titlefont_size=16,
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20, l=5, r=5, t=40),
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

# Show the figure
fig.show()