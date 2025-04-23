import time
from rich.progress import (
    track, Progress,
    TextColumn, BarColumn, TaskProgressColumn,
    SpinnerColumn, TimeElapsedColumn,
)

def run_job(job):
    #print("run job: ", job)
    time.sleep(0.5)

def main():
    with Progress() as progress:
        task = progress.add_task("twiddling thumbs", total=10)
        for job in range(10):
            progress.console.print(f"Working on job #{job}")
            run_job(job)
            progress.advance(task)


def table_col():
    from time import sleep

    from rich.table import Column
    from rich.progress import Progress, BarColumn, TextColumn

    text_column = TextColumn("{task.description}", table_column=Column(ratio=1))
    bar_column = BarColumn(bar_width=None, table_column=Column(ratio=2))
    progress = Progress(text_column, bar_column, expand=True)

    with progress:
        for n in progress.track(range(10)):
            progress.print(n)
            sleep(0.1)


def indeterminate_progress():
    # Advanced usage: multiple progress
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        TimeElapsedColumn()) as prog:
        task0 = prog.add_task("[red]Waiting for approve...", start=False, total=10)
        task1 = prog.add_task("[red]Downloading...", total=100)
        time.sleep(3)
        prog.start_task(task0)

        cnt = 0
        while not prog.finished:
            prog.update(task0, advance=1)
            prog.update(task1, advance=5)
            time.sleep(1)
            cnt += 1

if __name__ == "__main__":
    #main()
    #table_col()
    indeterminate_progress()
