# bedanya kode ini kita bisa melihat proses cara kerja algoritmanya
import networkx as nx
import matplotlib.pyplot as plt

def basis_pengetahuan():
    G = nx.Graph()
    # Menambahkan node (lokasi)
    locations = ["cafet", "agape", "filia", "euodia", "didaktos", "biblos", "chara", "gnosis", "logos", "hagios", "makarios", "koinonia", "iama", "gor", "dispenser1", "dispenser2", "dispenser3", "dispenser4", "dispenser5", "dispenser6"]
    G.add_nodes_from(locations)

    # Menambahkan edge (jalan dengan jarak)
    edges = [
        ("cafet", "agape", 5),
        ("cafet", "filia", 15),
        ("agape", "dispenser1", 5),
        ("filia", "euodia", 10),
        ("euodia", "didaktos", 20),
        ("didaktos", "chara", 10),
        ("chara", "biblos", 10),
        ("didaktos", "dispenser3", 5),
        ("didaktos", "gnosis", 20),
        ("hagios", "gnosis", 10),
        ("logos", "hagios", 10),
        ("hagios", "didaktos", 30),
        ("hagios", "makarios", 10),
        ("logos", "koinonia", 50),
        ("logos", "iama", 15),
        ("logos", "euodia", 15),
        ("makarios", "iama", 10),
        ("koinonia", "iama", 40),
        ("koinonia", "gor", 70),
        ("logos", "gor", 20),
        ("gor", "dispenser6", 5),
        ("euodia", "dispenser2", 5),
        ("hagios", "dispenser4", 5),
        ("makarios", "dispenser5", 5)
    ]
    G.add_weighted_edges_from(edges)

    # Menambahkan status dispenser
    dispenser_status = {
        "dispenser1": "berfungsi",
        "dispenser2": "berfungsi",
        "dispenser3": "berfungsi",
        "dispenser4": "perbaikan",
        "dispenser5": "berfungsi",
        "dispenser6": "berfungsi"
    }

    nx.set_node_attributes(G, dispenser_status, "status")

    return G

def visualize_graph(G, path):
    # membuat layout grafik secara manual
    pos = {
        "cafet": (0, 2),
        "agape": (0, 0),
        "dispenser1": (0, -2),
        "filia": (0.951, 2.05),
        "euodia": (3.169, 2.00),
        "dispenser2": (2.453, 2.82),
        "didaktos": (3.057, 0.009),
        "chara": (2.5, -2),
        "biblos": (0.935, -2),
        "logos": (6.573, 1.98),
        "hagios": (5.629, -0.06),
        "gnosis": (5, -2),
        "makarios": (6.581, -1.90),
        "koinonia": (8.300, -0.40),
        "iama": (7.404, -0.5),
        "gor": (7.873, 2.80),
        "dispenser3": (3.615, 0.56),
        "dispenser4": (5.601, 1.01),
        "dispenser5": (5.870, -1.40),
        "dispenser6": (7.032, 3.03)
    }

    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=8, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    
    # Highlight path
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

    plt.show()

def temukan_dispenser_terdekat(G, start):
    dispensers = [node for node in G.nodes if "dispenser" in node and G.nodes[node]['status'] == "berfungsi"]
    shortest_distance = float('inf')
    nearest_dispenser = None
    shortest_path = []
    steps = []

    for dispenser in dispensers:
        try:
            length, path = nx.single_source_dijkstra(G, start, dispenser)
            steps.append(f"Langkah: Dari {start} ke {dispenser} dengan jarak {length}, jalur: {path}")
            if length < shortest_distance:
                shortest_distance = length
                nearest_dispenser = dispenser
                shortest_path = path
        except nx.NetworkXNoPath:
            continue
        print("\n".join(steps))

    return nearest_dispenser, shortest_distance, shortest_path


def main():
    titik_start = ["cafet", "agape", "filia", "euodia", "didaktos", "biblos", "chara", "logos", "hagios", "gnosis", "makarios", "koinonia", "iama", "gor"]
    print("Daftar titik lokasi: ")
    for i in titik_start:
        print(i)
        
    # Membuat graf
    G = basis_pengetahuan()

    # Lokasi awal pengguna
    lokasi_awal = input("mana titik lokasi yang paling dekat dari anda: ")

    # Menemukan dispenser terdekat
    nearest_dispenser, distance, path = temukan_dispenser_terdekat(G, lokasi_awal)

    # Menampilkan hasil
    if nearest_dispenser:
        print(f"Dispenser terdekat dari {lokasi_awal} adalah {nearest_dispenser} dengan jarak {distance} meter")
        print(f"Rute yang harus diambil: {' -> '.join(path)}")
    else:
        print("Tidak ada dispenser yang berfungsi ditemukan.")

    # Visualisasi graf
    visualize_graph(G, path if nearest_dispenser else [])

if __name__ == "__main__":
    main()
