class TreeNode:
    def __init__(self, value=None, freq=0):
        self.value = value  
        self.freq = freq 
        self.left = None  
        self.right = None 

def calc_frequencies(image):
   
    frequency_dict = {}
    for row in image:
        for pixel in row:
            if pixel not in frequency_dict:
                frequency_dict[pixel] = 0
            frequency_dict[pixel] += 1
    return frequency_dict

def create_huffman_tree(frequencies):
   
    nodes = [TreeNode(value=pixel, freq=freq) for pixel, freq in frequencies.items()]
    
    while len(nodes) > 1:
        
        nodes = sorted(nodes, key=lambda node: node.freq)
        
        
        left = nodes.pop(0)
        right = nodes.pop(0)
        
        
        merged = TreeNode(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        
        nodes.append(merged)
    
   
    return nodes[0]

def build_huffman_codes(node, code='', codebook=None):
    if codebook is None:
        codebook = {}
    
    if node is not None:
        if node.value is not None:
            codebook[node.value] = code
        build_huffman_codes(node.left, code + '0', codebook)
        build_huffman_codes(node.right, code + '1', codebook)
    
    return codebook

def encode_image(image, huffman_codes):
    encoded_image = ''
    for row in image:
        for pixel in row:
            encoded_image += huffman_codes[pixel]
    return encoded_image

def compress_image_with_huffman(image):
    
    pixel_frequencies = calc_frequencies(image)
    
    
    huffman_tree_root = create_huffman_tree(pixel_frequencies)
    
    
    huffman_codes = build_huffman_codes(huffman_tree_root)
    
   
    compressed_image = encode_image(image, huffman_codes)
    
    return compressed_image, huffman_tree_root, huffman_codes