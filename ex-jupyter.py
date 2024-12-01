import os
import sys
import argparse
import nbformat


def execute_code(code, global_context):
    """
    Execute a code string in a given global context.

    Parameters
    ----------
    code : str
        The code to execute.
    global_context : dict
        The global namespace to use while executing the code.
    """
    exec(code, global_context)

def execute_cells(notebook_path, cell_indices=None):
    """
    Execute code cells from a Jupyter notebook.

    Parameters
    ----------
    notebook_path : str
        The path to the Jupyter notebook file.
    cell_indices : list of int, optional
        Indices of the cells to execute. If None is given, all code cells are executed.

    Notes
    -----
    The code is executed in the global namespace of this module. The kernel used is the
    current IPython kernel.
    """
    with open(notebook_path, "r") as file:
        notebook = nbformat.read(file, as_version=4)
        
    global_context = {"__name__": "__main__"}
    
    for i, cell in enumerate(notebook.cells):
        if cell.cell_type == "code" and (cell_indices is None or i in cell_indices):
            try:                   execute_code(cell.source, global_context)
            except Exception as e: print(f"Error executing cell {i}:\n{e}")

def main():
    """
    Command line interface to run specific cells of a Jupyter notebook.

    Parameters
    ----------
    --nb : str
        Path to the Jupyter notebook.
    --all : None
        Run all cells in the notebook.
    --cell : int
        Run a specific cell by its number.
    --until : int
        Run cells from the first until the given cell (inclusive).
    --from : int
        Run cells starting from the given cell number.

    Notes
    -----
    The code is executed in the global namespace of this module. The kernel used is the
    current IPython kernel.
    """
    parser = argparse.ArgumentParser(description="Run specific cells of a Jupyter notebook.")
    parser.add_argument("--nb", type=str, help="Path to the Jupyter notebook.")
    parser.add_argument("--all", action="store_true", help="Run all cells in the notebook.")
    parser.add_argument("--cell", type=int, help="Run a specific cell by its number.")
    parser.add_argument("--until", type=int, help="Run cells from the first until the given cell (inclusive).")
    parser.add_argument("--from", dest="from_cell", type=int, help="Run cells starting from the given cell number.")
    args = parser.parse_args()
    
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    notebook_path = args.nb
    if not os.path.exists(notebook_path):
        print("Error: Notebook file does not exist.")
        return

    try:
        if args.all:                 execute_cells(notebook_path)
        elif args.cell is not None:  execute_cells(notebook_path, cell_indices=[args.cell - 1])
        elif args.until is not None: execute_cells(notebook_path, cell_indices=list(range(args.until)))
        elif args.from_cell is not None:
            with open(notebook_path, "r") as file:
                notebook = nbformat.read(file, as_version=4)
                total_cells = len(notebook.cells)
            execute_cells(notebook_path, cell_indices=list(range(args.from_cell - 1, total_cells)))
        else: print("Error: Please specify one of the options --all, --cell, --until, or --from.")
    finally: pass

if __name__ == "__main__": main()
