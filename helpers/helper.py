from src.textnode import TextType, TextNode
import re
import os
import shutil

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        parts = node.text.split(delimiter)
        
        if len(parts) % 2 == 0:
            raise ValueError(f"Markdown inválido: no se encontró el delimitador de cierre '{delimiter}'")
                
        for i in range(len(parts)):
            if parts[i] == "":
                continue
            
            if i % 2 == 0:
                new_nodes.append(TextNode(parts[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(parts[i], text_type))
             
    return new_nodes

def extract_markdown_images(text):
   re_image_link = r"!\[(.*?)\]\((.*?)\)"
   matches = re.findall(re_image_link, text)
   return matches
   
def extract_markdown_links(text):
   re_markodown_link= r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
   matches = re.findall(re_markodown_link, text)
   return matches
            
def split_nodes_image(old_nodes):
    lista_nueva = []

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            lista_nueva.append(node)
            continue

        texto_restante = node.text
        imagenes = extract_markdown_images(texto_restante)

        if not imagenes:
            lista_nueva.append(node)
            continue

        for (alt_text, url) in imagenes:
            formato_markdown = f"![{alt_text}]({url})"
            
            partes = texto_restante.split(formato_markdown, 1)
            
            if len(partes) != 2:
                raise ValueError("Markdown inválido: imagen no cerrada o mal formada")

            if partes[0] != "":
                lista_nueva.append(TextNode(partes[0], TextType.TEXT))

            lista_nueva.append(TextNode(alt_text, TextType.IMAGE, url))

            texto_restante = partes[1]

        if texto_restante != "":
            lista_nueva.append(TextNode(texto_restante, TextType.TEXT))

    return lista_nueva
    


def split_nodes_link(old_nodes):
    lista_nueva = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            lista_nueva.append(node)
            continue

        texto_restante = node.text
        links = extract_markdown_links(texto_restante)

        if not links:
            lista_nueva.append(node)
            continue

        for anchor_text, url in links:
            formato_markdown = f"[{anchor_text}]({url})"
            partes = texto_restante.split(formato_markdown, 1)

            if len(partes) != 2:
                raise ValueError("Markdown inválido: enlace no cerrado o mal formado")

            if partes[0] != "":
                lista_nueva.append(TextNode(partes[0], TextType.TEXT))

            lista_nueva.append(TextNode(anchor_text, TextType.LINK, url))
            texto_restante = partes[1]

        if texto_restante != "":
            lista_nueva.append(TextNode(texto_restante, TextType.TEXT))

    return lista_nueva

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    
    nodes = split_nodes_image(nodes)
    
    nodes = split_nodes_link(nodes)

    return nodes

def copy_files(origin,destination):
    
    source_path = os.path.abspath(origin)
    destination_path = os.path.abspath(destination)
    if not os.path.exists(source_path):
        raise ValueError("La ruta de origen no existe.")
   
    if not os.path.exists(destination_path):
        raise ValueError("La ruta de destino no existe.")

    contenido = os.listdir(origin)    
    
    for content in contenido:
        src_path = os.path.join(source_path, content)
        dst_path = os.path.join(destination_path, content)
        
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
        else:
            os.mkdir(dst_path)
            copy_files(src_path, dst_path)