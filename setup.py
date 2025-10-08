from setuptools import find_packages, setup

setup(
    name="chemeleon-dng",
    packages=find_packages(),
    install_requires=[
        "torch>=2.1.0",
        "pytorch-lightning>=2.1.0",
        "sacred",
        "ase",
        "torch-geometric",
        "torchmetrics",
        "ase",
        "tqdm",
        "wandb",
        "pydantic",
        "jupyterlab",
        "pymatgen",
        "fire",
    ],
)
