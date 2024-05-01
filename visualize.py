import pandas as pd
import networkx as nx
import plotly.graph_objects as go
import community as community_louvain

# Load data from CSV
df = pd.read_csv('rappers_famous_graph_ready1.csv')
G = nx.Graph()

# Add edges from the DataFrame
for _, row in df.iterrows():
    G.add_edge(row['Artist 1'], row['Artist 2'])

# Detect communities using the Louvain method
partition = community_louvain.best_partition(G)

# Create a dictionary to assign community numbers to nodes (for coloring)
community_index = {node: comm for node, comm in partition.items()}

# Calculate initial positions using the spring layout
pos = nx.spring_layout(G, seed=42)

# Adjusting positions by community to enhance separation
# Create a center point for each community and move nodes towards their community's center
community_centers = {}
scale = 2  # Scale factor for adjusting distances within communities
for node, comm in partition.items():
    if comm not in community_centers:
        community_centers[comm] = pos[node]
    else:
        # Calculate the new center as a mean of the current position and the node's position
        community_centers[comm] = [((community_centers[comm][0] + pos[node][0]) / 2), 
                                   ((community_centers[comm][1] + pos[node][1]) / 2)]

for node, comm in partition.items():
    # Move node position towards the community center
    pos[node][0] += (community_centers[comm][0] - pos[node][0]) / scale
    pos[node][1] += (community_centers[comm][1] - pos[node][1]) / scale

# Continue with creating Plotly traces and the figure...
# Prepare edge traces for visualization
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])  # 'None' ensures that the lines do not connect across edges
    edge_y.extend([y0, y1, None])

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')
# Prepare node traces, assigning colors based on community membership
node_x = []
node_y = []
node_text = []
node_color = []

for node in G.nodes():
    node_x.append(pos[node][0])
    node_y.append(pos[node][1])
    node_text.append(node)
    node_color.append(community_index[node])

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        colorscale='Viridis',
        size=9,
        color=node_color,
        colorbar=dict(
            thickness=15,
            title="Community",
            xanchor='left',
            titleside='right'
        )
    ),
    text=node_text)
# Setup the overall figure layout
fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    showlegend=False,
                    hovermode='closest',
                    title='Network of Rappers Grouped by Community',
                    titlefont_size=16,
                    margin=dict(b=0, l=0, r=0, t=40),
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
                ))

# Display the figure
fig.show()
