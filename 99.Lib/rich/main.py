import os, json, time
from rich import print as rprint
from rich import print_json
from rich.pretty import pprint
from rich.console import Console
from rich.table import Column, Table
from rich.columns import Columns
from rich.progress import track, Progress
from rich.syntax import Syntax
from rich.tree import Tree
from rich.prompt import Prompt, Confirm


def print_example():
    print("hello world!")
    print("[italic red]Hello[/italic red] World!", locals())
    rprint("[italic red]Hello[/italic red], [bold magenta]World[/bold magenta]!", ":vampire:", locals())
    obj = {
        "a": 123,
        "b": "hello",
        "c": {
            "name": "Tom",
            "age": 20
        },
        "d": [1, 2, 3, 4, 5],
        'e': 'done'
    }
    rprint("====== pprint:")
    pprint(obj, expand_all=True)
    rprint("====== print_json str:")
    json_str = json.dumps(obj)
    print_json(json_str)

def table_example():
    table = Table(title="Table Example", show_header=True, header_style="bold yellow")
    table.add_column("Date", style="dim", width=12)
    table.add_column("Title")
    table.add_column("Production Budget", justify="right")
    table.add_column("Box Office", justify="right")
    table.add_row(
        "Dev 20, 2019", "Star Wars: The Rise of Skywalker", "$275,000,000", "$375,126,118"
    )
    table.add_row(
        "May 25, 2018",
        "[red]Solo[/red]: A Star Wars Story",
        "$275,000,000",
        "$393,151,347",
    )
    table.add_row(
        "Dec 15, 2017",
        "Star Wars Ep. VIII: The Last Jedi",
        "$262,000,000",
        "[bold]$1,332,539,889[/bold]",
    )
    
    rprint(table)

def column_example():
    #cols = ['col_1_asdfasdfwerwer', 'col_2', 'col_3', 'col_4',
    #        'col_5_oiueoribkhaksdhfkshkfsh', 'col_6', 'col_7_owihvbnkvjhfgalksfhkajh',
    #        'col_8', 'col_9', 'col_10', 'col_11_woeihkdhaksdjhfksjhfk', 'col_12']
    cols = os.listdir("C:\\")
    rprint(Columns(cols, title="Column Example"))

def syntax_example():
    my_code = '''
    def iter_first_last(values: Iterable[T]) -&gt; Iterable[Tuple[bool, bool, T]]:
        """Iterate and generate a tuple with a flag for first and last value."""
        iter_values = iter(values)
        try:
            previous_value = next(iter_values)
        except StopIteration:
            return
        first = True
        for value in iter_values:
            yield first, False, previous_value
            first = False
            previous_value = value
        yield first, True, previous_value
    '''
    syntax = Syntax(my_code, "python", theme="monokai", line_numbers=True)
    rprint(syntax)

def traceback_example():
    console = Console()
    try:
        rprint("hello")
        a = 123
        x = 1/ 0
    except Exception:
        console.print_exception(show_locals=True)
        

def emoji_example():
    rprint(":vampire:")
    rprint(":heart:")
    rprint(":star:")

def panel_example():
    from rich.console import Group
    from rich.panel import Panel

    Panel.fit("[bold yellow]Hi, I'm a Panel", border_style="red")
    panel_group = Group(
        Panel("Hello", style="on blue"),
        Panel("World", style="on red"),
    )
    rprint(Panel(panel_group, title="Panel Example"))


def tree_example():
    tree = Tree("Rich Tree")
    tree.add("foo")
    tree.add("bar")
    baz_tree = tree.add("baz")
    baz_tree.add("[red]Red").add("[green]Green").add("[blue]Blue")
    rprint(tree)

def progress_bar_example():
    # Basic usage:
    for step in track(range(1), description="Processing..."):
        print(step)
        time.sleep(0.5)

    # Advanced usage: multiple progress
    with Progress() as prog:
        task1 = prog.add_task("[red]Downloading...", total=1000)
        task2 = prog.add_task("[green]Processing...", total=1000)
        task3 = prog.add_task("[cyan]Cooking...", total=1000)

        cnt = 0
        while not prog.finished:
            prog.update(task1, advance=0.5)
            prog.update(task2, advance=0.3)
            prog.update(task3, advance=1.0)

            time.sleep(0.02)
            cnt += 1
            if cnt == 2:
                break

def prompt_example():
    name = Prompt.ask("Enter your name", choices=["Paul", "Jessica", "Duncan"], default="Tom")
    rprint(f"Your name is [yellow]{name}")

    is_rich_great = Confirm.ask("Do you like rich?", default="Y")
    rprint(f"[green]{is_rich_great}")


if __name__ == "__main__":
    console = Console()
    console.rule("[bold red]Be rich")
    print_example()
    table_example()
    column_example()
    syntax_example()
    emoji_example()
    panel_example()
    tree_example()
    progress_bar_example()

    traceback_example()
    prompt_example()
