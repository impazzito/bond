import click


@click.group()
def cli():
    """Bond CLI for managing the FastAPI application."""


@cli.command()
@click.option("--host", default="0.0.0.0", help="Host to bind the server to")
@click.option("--port", default=8500, type=int, help="Port to bind the server to")
def run(host, port):
    """Start the FastAPI application server."""
    import uvicorn

    click.echo(f"Starting Bond server on {host}:{port}")
    uvicorn.run("bond.api:app", host=host, port=port, reload=True)


if __name__ == "__main__":
    cli()
