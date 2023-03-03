import click
from functions.funcs import compile,initConfig



@click.group()
def kar():
    pass

@click.command()
@click.argument('path',type=click.Path(exists=True))
@click.option('--outdir',default='output.html', type=click.Path(exists=False),help="Enter the path of the output file")
@click.option('-h','--host',default=False,type=bool,help='Want to host or not. --host=True')
def comp(path,outdir,host):
    compile(path,outdir,host)

@click.command()
@click.option('-b','--boil',default=False,help='Initialize a congif')
def init(boil):
    initConfig(boil)

    
kar.add_command(comp)
kar.add_command(init)

if __name__ == '__main__':
    kar()