from setuptools import setup, find_packages

setup(
    name="bond",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "fastapi>=0.104.0",
        "uvicorn>=0.23.2",
        "click>=8.1.7",
        "websockets>=11.0.3",
    ],
    entry_points="""
        [console_scripts]
        bond=bond.__main__:cli
    """,
)
