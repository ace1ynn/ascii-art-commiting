import typer
import os
import shutil
import stat

app = typer.Typer()



@app.command()
def init():
    if not os.path.isdir('./.git'):
        raise Exception('Not a git repo')
    home = os.environ.get('XDG_CACHE_HOME')
    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)
    if not os.path.isdir(f'{home}/todo'):
        os.makedirs(f'{home}/todo')
    if not os.path.isdir(f'{home}/current'):
        os.makedirs(f'{home}/current')
    if not os.path.isdir(f'{home}/done'):
        os.makedirs(f'{home}/done')
    shutil.copyfile(f'{dir_path}/cat1.txt' ,f'{home}/todo/cat1.txt')
    shutil.copyfile(f'{dir_path}/cat2.txt',f'{home}/todo/cat2.txt')
    typer.echo("setting up app")

@app.command()
def addtorepo():
    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)
    shutil.copyfile(f'{dir_path}/runsticker.py', './.git/hooks/post-commit')
    st = os.stat('./.git/hooks/post-commit')
    os.chmod('./.git/hooks/post-commit', st.st_mode | stat.S_IEXEC)
    typer.echo("adding sticker to repo")


@app.command()
def addsticker(filepath):
    filename = filepath.split('/')[-1]
    home = os.environ.get('XDG_CACHE_HOME')
    shutil.copyfile(f'{filepath}' ,f'{home}/todo/{filename}')
    typer.echo("added sticker")