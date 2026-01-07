from ogb.nodeproppred import PygNodePropPredDataset

print("Downloading ogbn-arxiv dataset...")

dataset = PygNodePropPredDataset(
    name="ogbn-arxiv",
    root="dataset"
)

data = dataset[0]

print("Download finished.")
print("Number of nodes:", data.num_nodes)
print("Number of edges:", data.num_edges)
