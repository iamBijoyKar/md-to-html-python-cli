import markdown as md
from .template import DEFAULT_STYLE,TAGSH
import uuid


def mdToHtml(content:list[str])->str:

    output = ""
    for line in content:
        output += md.markdown(line) + '\n'
    output += DEFAULT_STYLE + '\n'
    return output


def parseLine(line)->list[str,str]:
    fil_line = line.lstrip()
    count = 0
    idx = 0
    for i in range(len(fil_line)):
        if fil_line[i] == '#':
            count += 1
        else:
            idx = i
            break
    tag = TAGSH[count]
    content = ""
    i = idx
    for i in range(idx,len(fil_line)-1):
        if fil_line[i] == '$' and fil_line[i+1] == '[':
            idx = i
            break
        content += fil_line[i]
    if i == len(fil_line)-2 :
        content += fil_line[-1]
    ui = uuid.uuid1()
    css = fil_line[i+2:-3]
    default_css = """
   .uuid{
        css
    }
   """.replace('css',css)
    style = default_css.replace('uuid',str(ui))
    tag = tag.replace('$tag$',content)
    tag = tag.replace('$class$',str(ui))
    return tag,style


def parse(file)->str:
    html = ""
    style = ""
    lines = file.readlines()
    for line in lines:
        tag,css = parseLine(line)
        html += tag + '\n'
        style += css
    output = f"""
    {html}
    <style>
        {DEFAULT_STYLE}
        {style}
    </style>
    """
    return output