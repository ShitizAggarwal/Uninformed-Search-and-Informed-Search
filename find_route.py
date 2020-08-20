import sys
from queue import PriorityQueue


def uninf_find(start_node, unode, graph_un):
    n_g = 0
    n_exp = 0
    frng_queue = PriorityQueue()
    frng_queue.put((0, start_node))
    visit_n = {}
    visit_n[start_node] = ("", 0)
    n_expl = []
    maxn = 0
    while not frng_queue.empty():
        if len(frng_queue.queue) > maxn:
            maxn = len(frng_queue.queue)
        _, mnode = frng_queue.get()
        n_exp += 1
        if mnode == unode:
            break
        if mnode in n_expl:
            continue
        n_expl.append(mnode)
        for nval in graph_un[mnode]:
            n_g += 1
            # n_expl.append(i)
            frng_queue.put((graph_un[mnode][nval] + visit_n[mnode][1], nval))
            if nval not in visit_n:
                visit_n[nval] = (mnode, graph_un[mnode][nval] + visit_n[mnode][1])

    travelled_path = []
    visit_dist = "infinity"

    if unode in visit_n:
        visit_dist = 0.0
        mnode = unode
        while mnode != start_node:
            visit_dist += graph_un[visit_n[mnode][0]][mnode]
            travelled_path.append(mnode)
            mnode = visit_n[mnode][0]
    return travelled_path, n_exp, n_g, visit_dist, maxn


def inf_find(start_node, unode, graph, heurval):
    generated = 0
    n_exp = 0
    frng_queue = PriorityQueue()
    frng_queue.put((0, start_node))
    visited = {}
    visited[start_node] = ("", 0)
    explored = []
    max_node = 0
    while not frng_queue.empty():
        if len(frng_queue.queue) > max_node:
            max_node = len(frng_queue.queue)
        _, mnode = frng_queue.get()
        n_exp += 1
        if mnode == unode:
            break
        if mnode in explored:
            continue
        explored.append(mnode)
        for val in graph[mnode]:
            generated += 1
            if val not in visited:
                visited[val] = (mnode, graph[mnode][val] + visited[mnode][1])
            frng_queue.put((graph[mnode][val] + visited[mnode][1] + heurval[val], val))
    travelled_path = []
    visit_dist = "infinity"
    if unode in visited:
        visit_dist = 0.0
        mnode = unode
        while mnode != start_node:
            visit_dist += graph[visited[mnode][0]][mnode]
            travelled_path.append(mnode)
            mnode = visited[mnode][0]
    return travelled_path, n_exp, generated, visit_dist, max_node


def file_par_heur(fi_name):
    heurval = {}
    heur_fl = open(fi_name, 'r')
    heur_line = heur_fl.readlines()
    heur_fl.close()
    for lin in heur_line[:-1]:
        par_data = lin.split()
        heurval[par_data[0]] = int(par_data[1])
    return heurval



def par_file(f_name):
    graph_und = {}
    inp_file = open(f_name, 'r')
    ln = inp_file.readlines()
    inp_file.close()
    for file_lines in ln[:-1]:
        graph_data = file_lines.split()

        if (graph_data[0] in graph_und):
            graph_und[graph_data[0]][graph_data[1]] = int(graph_data[2])
        else:
            graph_und[graph_data[0]] = {graph_data[1]: int(graph_data[2])}
        if (graph_data[1] in graph_und):
            graph_und[graph_data[1]][graph_data[0]] = int(graph_data[2])
        else:
            graph_und[graph_data[1]] = {graph_data[0]: int(graph_data[2])}
    return graph_und

if len(sys.argv) == 4:
    fi_name = sys.argv[1]
    src_node = sys.argv[2]
    dest_node = sys.argv[3]
    und_grph = par_file(fi_name)
    travelled_path, n_exp, n_g, visit_dist, maxn = uninf_find(src_node, dest_node, und_grph)
    print("nodes expanded: {}".format(n_exp))
    print("nodes generated: {}".format(n_g))
    print("max nodes in memory: {}".format(maxn))
    print("visit_dist: {}".format(visit_dist))
    print("route:")
    mnode = src_node
    for list_items in travelled_path[::-1]:
        print("{} to {}, {} km".format(mnode, list_items, und_grph[mnode][list_items]))
        mnode = list_items

elif len(sys.argv) == 5:
    fi_name = sys.argv[1]
    src_node = sys.argv[2]
    dest_node = sys.argv[3]
    fi_name_h = sys.argv[4]
    und_graph = par_file(fi_name)
    heurval = file_par_heur(fi_name_h)
    travelled_path, n_exp, n_g, visit_dist, maxn = inf_find(src_node, dest_node, und_graph, heurval)
    print("nodes expanded: {}".format(n_exp))
    print("nodes generated: {}".format(n_g))
    print("max nodes in memory: {}".format(maxn))
    print("visit_dist: {}".format(visit_dist))
    print("route:")
    mnode = src_node
    for list_items in travelled_path[::-1]:
        print("{} to {}, {} km".format(mnode, list_items, und_graph[mnode][list_items]))
        mnode = list_items
