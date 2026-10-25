import click

from demo_clean.stats import mean


@click.command()
@click.argument("values", nargs=-1, type=float, required=True)
def main(values: tuple[float, ...]) -> None:
    """Print the mean of VALUES."""
    click.echo(mean(list(values)))


if __name__ == "__main__":
    main()
