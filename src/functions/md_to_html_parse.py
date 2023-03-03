import markdown as md




def mdToHtml(content:list[str])->str:

    output = ""
    for line in content:
        output += md.markdown(line) + '\n'
    return output
