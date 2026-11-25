from pathlib import Path
import shutil
import json

from IPython.display import display, HTML, Javascript


def start_course():
    """
    Kopioi kurssin data hakemistoon ~/my-work/<course> tarvittaessa
    ja näyttää START-painikkeen, jolla 00*.ipynb avataan
    uuteen selaimen välilehteen.

    JupyterLabin /notebooks/<id>/ -prefix päätellään automaattisesti
    nykyisen sivun URL:sta.
    """

    # ------------------------------------------------------------
    # Hakemistot
    # ------------------------------------------------------------

    base_dir = Path(__file__).resolve().parent
    course_name = base_dir.name

    source_dir = base_dir / "data"
    my_work = Path.home() / "my-work"
    target_dir = my_work / course_name

    if not course_name.strip():
        raise RuntimeError(
            "Kurssin nimeä ei voitu päätellä käynnistyshakemistosta."
        )

    # ------------------------------------------------------------
    # Tarkastetaan, onko kurssi jo kopioitu
    # ------------------------------------------------------------

    start_notebooks = (
        sorted(target_dir.glob("00*.ipynb"))
        if target_dir.is_dir()
        else []
    )

    # ------------------------------------------------------------
    # Jos 00*.ipynb puuttuu, kurssi täytyy mahdollisesti kopioida
    # ------------------------------------------------------------

    if not start_notebooks:

        # Kohdehakemisto on olemassa, mutta siellä ei ole
        # 00*.ipynb-tiedostoa. Emme muuta hakemistoa.
        if target_dir.exists():
            raise FileExistsError(
                "Kohdehakemisto on jo olemassa, mutta sieltä ei löydy "
                "00*.ipynb-notebookia:\n"
                f"{target_dir}\n\n"
                "Turvallisuussyistä olemassa olevaan hakemistoon ei "
                "kopioida eikä sen sisältöä muuteta."
            )

        # Tarkastetaan data-hakemisto.
        if not source_dir.exists():
            raise FileNotFoundError(
                "Kurssin data-hakemistoa ei löydy:\n"
                f"{source_dir}"
            )

        if not source_dir.is_dir():
            raise NotADirectoryError(
                "Polku 'data' löytyy, mutta se ei ole hakemisto:\n"
                f"{source_dir}"
            )

        # Tarkastetaan jo ennen kopiointia, että lähteessä on
        # käynnistysnotebook.
        source_starts = sorted(source_dir.glob("00*.ipynb"))

        if not source_starts:
            raise FileNotFoundError(
                "Data-hakemistosta ei löydy käynnistysnotebookia "
                "00*.ipynb:\n"
                f"{source_dir}"
            )

        # --------------------------------------------------------
        # Kopiointi
        # --------------------------------------------------------

        try:
            my_work.mkdir(parents=True, exist_ok=True)

            print(
                f"Kopioidaan kurssitiedostot:\n"
                f"{source_dir}\n"
                f"->\n"
                f"{target_dir}"
            )

            shutil.copytree(source_dir, target_dir)

        except PermissionError as exc:
            raise PermissionError(
                "Ei kirjoitusoikeutta kohteeseen:\n"
                f"{target_dir}"
            ) from exc

        except OSError as exc:

            # Jos ensimmäinen kopiointi epäonnistui,
            # poistetaan mahdollisesti syntynyt vajaa hakemisto.
            if target_dir.exists():
                try:
                    shutil.rmtree(target_dir)
                except OSError:
                    pass

            raise RuntimeError(
                "Kurssitiedostojen kopiointi epäonnistui:\n"
                f"{source_dir}\n"
                "->\n"
                f"{target_dir}\n\n"
                f"{exc}"
            ) from exc

        # Tarkastetaan kopioinnin lopputulos.
        start_notebooks = sorted(
            target_dir.glob("00*.ipynb")
        )

        print("Kurssitiedostot kopioitu.")

    else:
        print(
            "Kurssihakemisto on jo olemassa. "
            "Tiedostoja ei kopioida."
        )

    # ------------------------------------------------------------
    # Tarkastetaan käynnistysnotebook
    # ------------------------------------------------------------

    if not start_notebooks:
        raise FileNotFoundError(
            "Käynnistysnotebookia 00*.ipynb ei löydy "
            "kohdehakemistosta:\n"
            f"{target_dir}"
        )

    notebook = start_notebooks[0]

    # ------------------------------------------------------------
    # Muodostetaan notebookin polku JupyterLabin juuresta
    #
    # Levypolku:
    #
    #   ~/my-work/KURSSI/00_start_here.ipynb
    #
    # JupyterLab-polku:
    #
    #   my-work/KURSSI/00_start_here.ipynb
    # ------------------------------------------------------------

    try:
        relative_path = notebook.relative_to(Path.home())

    except ValueError as exc:
        raise RuntimeError(
            "Notebook ei sijaitse käyttäjän kotihakemiston alla:\n"
            f"{notebook}"
        ) from exc

    notebook_path = relative_path.as_posix()

    print(f"Käynnistysnotebook: {notebook.name}")

    # ------------------------------------------------------------
    # START-painike
    #
    # Nykyisestä selaimen URL:sta etsitään JupyterLabin base path.
    #
    # Esimerkiksi:
    #
    # /notebooks/fd189213ab9343e9be7f319abf4afd3/lab/tree/...
    #
    # ->
    #
    # /notebooks/fd189213ab9343e9be7f319abf4afd3
    #
    # Lopulliseksi osoitteeksi tulee:
    #
    # /notebooks/<id>/lab/tree/my-work/KURSSI/00_start_here.ipynb
    # ------------------------------------------------------------

    button_id = "course-start-button"

    display(
        HTML(
            f"""
            <div style="margin-top: 16px; margin-bottom: 16px;">
                <button
                    id="{button_id}"
                    type="button"
                    style="
                        min-width: 180px;
                        padding: 14px 28px;
                        background-color: #198754;
                        color: white;
                        font-size: 18px;
                        font-weight: 600;
                        text-align: center;
                        border: none;
                        border-radius: 6px;
                        cursor: pointer;
                    "
                >
                    START
                </button>
            </div>
            """
        )
    )

    # JavaScript erikseen, koska JupyterLab ei välttämättä suorita
    # HTML-outputin sisällä olevaa <script>-elementtiä.
    js = f"""
    (() => {{
        const button = document.getElementById({json.dumps(button_id)});

        if (!button) {{
            console.error("START-painiketta ei löydy.");
            return;
        }}

        button.addEventListener("click", () => {{

            const currentPath = window.location.pathname;

            /*
             * Etsitään nykyisestä URL:sta /lab/-kohdan alku.
             *
             * Esimerkiksi:
             *
             * /notebooks/ABC123/lab/tree/START.ipynb
             *
             * basePath:
             *
             * /notebooks/ABC123
             */

            const labIndex = currentPath.indexOf("/lab/");

            if (labIndex === -1) {{
                alert(
                    "JupyterLabin peruspolkua ei voitu päätellä " +
                    "nykyisestä osoitteesta.\\n\\n" +
                    "Nykyinen polku:\\n" +
                    currentPath
                );
                return;
            }}

            const basePath = currentPath.substring(0, labIndex);

            const target =
                basePath +
                "/lab/tree/" +
                {json.dumps(notebook_path)};

            console.log("Opening notebook:", target);

            window.open(
                target,
                "_blank"
            );
        }});
    }})();
    """

    display(Javascript(js))


start_course()
