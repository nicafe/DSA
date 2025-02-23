class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq
    
    def __le__(self, other):
        return self.freq <= other.freq


def build_huffman_tree(char_freq):
    huffman_nodes = []
    for k, v in char_freq.items():
        huffman_nodes.append(HuffmanNode(k, v))
    
    huffman_nodes.sort(reverse=True)

    while len(huffman_nodes) > 1:
        left = huffman_nodes.pop()
        right = huffman_nodes.pop()
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        huffman_nodes.append(merged)
        for i in range(len(huffman_nodes) - 1, 0, -1):
            if huffman_nodes[i] <= huffman_nodes[i - 1]:
                break
            huffman_nodes[i], huffman_nodes[i - 1] = huffman_nodes[i - 1], huffman_nodes[i]

    return huffman_nodes[0]


def build_huffman_codes(node, current_code, huffman_codes):
    if node.char is not None:
        huffman_codes[node.char] = current_code
        return

    build_huffman_codes(node.left, current_code + "0", huffman_codes)
    build_huffman_codes(node.right, current_code + "1", huffman_codes)


char_freq = {'A': 0.1, 'B': 0.05, 'C': 0.3, 'D': 0.2, 'E': 0.15, 'F': 0.15, 'G': 0.03, 'H': 0.02}

root = build_huffman_tree(char_freq)
huffman_codes = {}
build_huffman_codes(root, '', huffman_codes)
print(huffman_codes)


