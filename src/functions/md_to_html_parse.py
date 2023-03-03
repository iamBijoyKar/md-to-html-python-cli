import markdown as md
from .template import DEFAULT_STYLE



def mdToHtml(content:list[str])->str:

    output = ""
    for line in content:
        output += md.markdown(line) + '\n'
    output += DEFAULT_STYLE + '\n'
    return output
