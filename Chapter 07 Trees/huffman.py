import math

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


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
        # Keep huffman_nodes sorted.
        i = len(huffman_nodes) - 1
        while i > 0 and huffman_nodes[i] > huffman_nodes[i - 1]:
            huffman_nodes[i], huffman_nodes[i - 1] = huffman_nodes[i - 1], huffman_nodes[i]
            i -= 1

    return huffman_nodes[0]


def build_huffman_codes(node, current_code='', huffman_codes={}):
    if node.char is not None:  # It's leaf node.
        huffman_codes[node.char] = current_code
        return

    build_huffman_codes(node.left, current_code + '0', huffman_codes)
    build_huffman_codes(node.right, current_code + '1', huffman_codes)
    
    return huffman_codes


char_freq = {'A': 0.1, 'B': 0.05, 'C': 0.3, 'D': 0.2, 'E': 0.15, 'F': 0.15, 'G': 0.03, 'H': 0.02}
# char_freq = {'A': 1/2, 'B': 1/4, 'C': 1/8, 'D': 1/16, 'E': 1/32, 'F': 1/64, 'G': 1/128, 'H': 1/128}

root = build_huffman_tree(char_freq)
huffman_codes = build_huffman_codes(root)
print(huffman_codes)

avg_code_len = 0
shannon_entropy  = 0
for k, v in huffman_codes.items():
    avg_code_len += len(v) * char_freq[k]
    shannon_entropy += char_freq[k] * -math.log2(char_freq[k])
print(avg_code_len)
print(shannon_entropy)
