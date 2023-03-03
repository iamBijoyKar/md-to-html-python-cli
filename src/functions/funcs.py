import json
import webbrowser
import markdown as md
import colorama as col
import os
from .md_to_html_parse import mdToHtml
from .template import TAGSH,CONFIG_BOILER,CONFIG_FILE_NAME,BKAR_BOILER


def identConfig():
    try:
        with open(CONFIG_FILE_NAME,'r') as conf:
            conf_settings = json.load(conf)
            return conf_settings["rootDir"],conf_settings["outDir"]
    except FileNotFoundError:
        print(col.Fore.RED + 'config file was missing in ./ root directory' + col.Style.RESET_ALL)
        initConfig(False)
        exit()


def mdStyleSplitter(file)->list[str,str]:
    md_list = []
    style_list = []
    lines = file.readlines()
    for line in lines:
        temp_md,temp_style = '',''
        idx = -1
        for i in range(len(line)-1):
            if line[i] != '$' and line[i+1] != '[':
                temp_md += line[i]
            else:
                idx = i
                break
        temp_style = line[idx:-1]
        md_list.append(temp_md)
        if idx == -1:
            style_list.append("")
        else:
            style_list.append(temp_style)
    return md_list,style_list




def compile(path:str,outdir:str,h:bool)->None:
    input_file = open(path,'r')
    md_list,style_list = mdStyleSplitter(input_file)
    output = mdToHtml(md_list)
    output_file = open(outdir,'w+')
    output_file.write(output)
    input_file.close()
    output_file.close()


def initConfig(boil:bool):
    with open(CONFIG_FILE_NAME,'w+') as conf:
        json.dump(CONFIG_BOILER,conf,ensure_ascii=False, indent=4)
    if(boil):
        with open('index.html','w+') as boil_html:
            boil_html.write(BKAR_BOILER)
