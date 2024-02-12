import json
from pathlib import Path
from typing import Annotated

import typer


def main(
    notebook_filepath: Annotated[
        Path, typer.Argument(exists=True, dir_okay=False)
    ] = None,
) -> None:
    """
    Sorts execution counts in a Jupyter Notebook.

    Parameters
    ----------
    notebook_filepath:
        The notebook filepath
    """
    with open(notebook_filepath) as f_in:
        doc = json.load(f_in)

    count = 1
    for cell in doc['cells']:
        if 'execution_count' not in cell:
            continue
        cell['execution_count'] = count
        for o in cell.get('outputs', []):
            if 'execution_count' in o:
                o['execution_count'] = count
        count = count + 1

    with open(notebook_filepath, 'w') as f_out:
        json.dump(doc, f_out, indent=1)


if __name__ == '__main__':
    typer.run(main)
