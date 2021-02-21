# Approach

It's a graph search problem. 

Any optimal graph search algorithm, that considers edge weights or costs (such as A*  or Dijkstra's) would work in this case. 
I've choosen Dijkstra's here, due to lack of a good heuristic. The graph given is small so the optimisation that A* could bring ist not really significant  

## Pre - requisites 
- Python 3
- Pip 

Install the requirements if needed 
```
pip install -r requirements.txt

```

# Run the code 
In the root of the repo search.py by passing in the start and end location as arguments
For example to go from DUB to SYD run
```
 python search.py DUB SYD
```
#Run the tests 
in the root of the repo run 
```
 pytest .
```
