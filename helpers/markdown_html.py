from helpers.block_functions import BlockType, markdown_to_blocks, block_to_block_type
from src.htmlnode import ParentNode, LeafNode
from src.textnode import text_node_to_html_node 
from helpers.helper import text_to_textnodes


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_nodes.append(html_node)
    return html_nodes

def create_paragraph_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    return ParentNode("p", text_to_children(paragraph))

def create_quote_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
        
    content = " ".join(new_lines)
    return ParentNode("blockquote", text_to_children(content))

def create_ul_node(block):
    lines = block.split("\n")
    items = []
    for line in lines:
        clean_line = line[2:].strip()
        items.append(ParentNode("li", text_to_children(clean_line)))
    return ParentNode("ul", items)

def create_ol_node(block):
    lines = block.split("\n")
    items = []
    for line in lines:
        clean_line = line[2:].strip()
        items.append(ParentNode("li", text_to_children(clean_line)))
    return ParentNode("ol", items)

def create_code_node(block):
    content = block.strip("`")
    if content.startswith("\n"):
        content = content[1:]
    code_leaf = LeafNode("code", content)
    return ParentNode("pre", [code_leaf])

def create_heading_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
        
    content = block[level + 1:].strip()
    return ParentNode(f'h{level}', text_to_children(content))


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    
    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == BlockType.QUOTE:
            node = create_quote_node(block)
        elif block_type == BlockType.UNORDERED_LIST:
            node = create_ul_node(block)
        elif block_type == BlockType.ORDERED_LIST:
            node = create_ol_node(block)
        elif block_type == BlockType.CODE:
            node = create_code_node(block)
        elif block_type == BlockType.HEADING:
            node = create_heading_node(block)
        else:
            node = create_paragraph_node(block)
            
        block_nodes.append(node)
        
    return ParentNode("div", block_nodes)