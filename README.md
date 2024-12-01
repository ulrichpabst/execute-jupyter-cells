# execute-jupyter-cells
A simple python script to execute individual cells of a Jupyter Notebook from the terminal.

## Installation

In your python environment, make sure to install `nbformat`.

```
pip install nbformat
```

Then, simply download the file `ex-jupyter.py` to your computer, and you are ready to go!

## Usage

In the terminal, simply run

```python
python ex-jupyter.py
```

using you desired python environment (e.g. activated via `conda activate <your-env>`).

This will yield

```
usage: ex-jupyter.py [-h] [--nb NB] [--all] [--cell CELL] [--until UNTIL] [--from FROM_CELL]

Run specific cells of a Jupyter notebook.

options:
  -h, --help        show this help message and exit
  --nb NB           Path to the Jupyter notebook.
  --all             Run all cells in the notebook.
  --cell CELL       Run a specific cell by its number.
  --until UNTIL     Run cells from the first until the given cell (inclusive).
  --from FROM_CELL  Run cells starting from the given cell number.
```
