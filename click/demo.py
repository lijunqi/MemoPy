import click #(1)

@click.command() #(2)
@click.option("-i", "--id", required=True, help="input an id")
@click.option("-n", "--num", type=int, default=123, show_default=True, help="input a num")
def main(num):
    click.echo(f"{num =}")

if __name__ == '__main__':
    main()

"""
-n: 表示我们在命令行指定参数名的时候使用它即可, 注意是一个短'-'
--num: 是第一个参数的完整名称,我们在程序中接收值的时候使用它. 注意是二个短'-'.
help: 在命令行输入 "python3 demo.py --help" 的时候, 它可以提示我们这个程序有哪些命令可以用.

=======================================================
Output:
=======================================================
> python demo.py --help

Usage: demo.py [OPTIONS]

Options:
  -i, --id TEXT      input an id  [required]
  -n, --num INTEGER  input a num  [default: 123]
  --help             Show this message and exit.
=======================================================

=======================================================
Error: No required id
=======================================================
> python demo.py -n 1234

Usage: demo.py [OPTIONS]
Try 'demo.py --help' for help.

Error: Missing option '-i' / '--id'.
=======================================================

"""
