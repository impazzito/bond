import click
from bond.app import create_app

@click.group()
def cli():
    """Bond CLI for managing the FastAPI application."""
    pass

@cli.command()
@click.option("--host", default="127.0.0.1", help="Host to bind the server to")
@click.option("--port", default=8250, type=int, help="Port to bind the server to")
def run(host, port):
    """Start the FastAPI application server."""
    import uvicorn
    click.echo(f"Starting Bond server on {host}:{port}")
    uvicorn.run("bond.app:app", host=host, port=port, reload=True)

if __name__ == "__main__":
    cli()
