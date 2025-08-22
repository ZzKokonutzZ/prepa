import graph
import numpy as np
x=np.linspace(0,100,200)
y=np.random.normal(x)

print(graph.lr_graph(x,y))