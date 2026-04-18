from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH= "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST= "unordered_list"
    ORDERED_LIST = "ordered_list" 

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    list_block = []
    for block in blocks:
        clean_block = block.strip()
        if clean_block == "":     
            continue
        
        lines = block.split("\n")
        stripped_lines = []
        for line in lines:
            stripped_line = line.strip()
            stripped_lines.append(stripped_line)
            
        content = "\n".join(stripped_lines).strip()
        
        if content != "":
            list_block.append(content)
        
    return list_block

def block_to_block_type(block)->BlockType:
    if block.startswith("# "):
        return BlockType.HEADING
    if block.startswith("## "):
        return BlockType.HEADING
    
    if block.startswith("### "):
        return BlockType.HEADING
    
    if block.startswith("#### "):
        return BlockType.HEADING
    
    if block.startswith("##### "):
        return BlockType.HEADING
    
    if block.startswith("###### "):
        return BlockType.HEADING
    
    if re.match(r"^```[\s\S]*?```$", block):
        return BlockType.CODE
    
    if block.startswith(">"):
        lines = block.split("\n")
        if all(line.startswith(">") for line in lines):
            return BlockType.QUOTE
    
    if block.startswith("-"):
        lines = block.split("\n")
        if all(line.startswith("- ") for line in lines):
            return BlockType.UNORDERED_LIST
    
    if block.startswith("1."):
        lines = block.split("\n")
        ordenada = True
        for i in range(len(lines)):
            start = f'{i+1}. '
            if not lines[i].startswith(start):
                ordenada = False
        
        if ordenada:
            return BlockType.ORDERED_LIST
            
    return BlockType.PARAGRAPH