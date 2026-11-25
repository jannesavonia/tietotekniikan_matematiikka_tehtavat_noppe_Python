from pathlib import Path
import shutil
from IPython.display import display, Javascript


def start_course():
    """Copy course data to ~/my-work/<course> once, then open 00*.ipynb."""

    base_dir = Path(__file__).resolve().parent
    course_name = base_dir.name
    source_dir = base_dir / "data"
    my_work = Path.home() / "my-work"
    target_dir = my_work / course_name

    if not course_name.strip():
        raise RuntimeError("Kurssin nimeä ei voitu päätellä käynnistyshakemistosta.")

    # If a start notebook already exists, never copy anything.
    start_notebooks = sorted(target_dir.glob("00*.ipynb")) if target_dir.is_dir() else []

    if not start_notebooks:
        if target_dir.exists():
            raise FileExistsError(
                f"Kohdehakemisto on jo olemassa, mutta sieltä ei löydy 00*.ipynb-notebookia:\n"
                f"{target_dir}\n\n"
                "Turvallisuussyistä olemassa olevaan hakemistoon ei kopioida eikä sen sisältöä muuteta."
            )

        if not source_dir.exists():
            raise FileNotFoundError(
                f"Kurssin data-hakemistoa ei löydy:\n{source_dir}"
            )
        if not source_dir.is_dir():
            raise NotADirectoryError(
                f"Polku 'data' löytyy, mutta se ei ole hakemisto:\n{source_dir}"
            )

        source_starts = sorted(source_dir.glob("00*.ipynb"))
        if not source_starts:
            raise FileNotFoundError(
                f"Data-hakemistosta ei löydy käynnistysnotebookia 00*.ipynb:\n{source_dir}"
            )

        try:
            my_work.mkdir(parents=True, exist_ok=True)
            shutil.copytree(source_dir, target_dir)
        except PermissionError as exc:
            raise PermissionError(
                f"Ei kirjoitusoikeutta kohteeseen:\n{target_dir}"
            ) from exc
        except OSError as exc:
            # Avoid leaving a partial course directory after an unsuccessful first copy.
            if target_dir.exists():
                try:
                    shutil.rmtree(target_dir)
                except OSError:
                    pass
            raise RuntimeError(
                f"Kurssitiedostojen kopiointi epäonnistui:\n{source_dir}\n->\n{target_dir}\n\n{exc}"
            ) from exc

        start_notebooks = sorted(target_dir.glob("00*.ipynb"))

    if not start_notebooks:
        raise FileNotFoundError(
            f"Käynnistysnotebookia 00*.ipynb ei löydy kohdehakemistosta:\n{target_dir}"
        )

    notebook = start_notebooks[0]

    try:
        relative_path = notebook.relative_to(my_work)
    except ValueError as exc:
        raise RuntimeError(
            f"Notebook ei sijaitse ~/my-work-hakemiston alla:\n{notebook}"
        ) from exc

    url = "/lab/tree/" + relative_path.as_posix()
    display(Javascript(f"window.location.href = {url!r};"))
