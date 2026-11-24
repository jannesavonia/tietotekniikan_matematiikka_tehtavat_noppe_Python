import html
import json
import os
from pathlib import Path
from urllib.parse import urlencode

from IPython.display import HTML, display
from jupyter_server.serverapp import list_running_servers


python_file = (
    Path.cwd()
    / "src"
    / "my_code.py"
).resolve()

csharp_file = (
    Path.cwd()
    / "src"
    / "my_code.cs"
).resolve()


if python_file.is_file():
    solution_file = python_file

elif csharp_file.is_file():
    solution_file = csharp_file

else:
    raise FileNotFoundError(
        "Ratkaisupohjaa src/my_code.py tai "
        "src/my_code.cs ei löytynyt."
    )


def get_jupyter_base_url() -> str:
    # Nopessa/JupyterHubissa tämä sisältää käyttäjäkohtaisen palvelupolun.
    base_url = os.environ.get(
        "JUPYTERHUB_SERVICE_PREFIX"
    )

    # Paikallisessa JupyterLabissa luetaan base_url
    # käynnissä olevan palvelimen runtime-tiedoista.
    if not base_url:
        running_servers = list(
            list_running_servers()
        )

        if running_servers:
            base_url = running_servers[0].get(
                "base_url",
                "/",
            )
        else:
            base_url = "/"

    if not base_url.startswith("/"):
        base_url = "/" + base_url

    if not base_url.endswith("/"):
        base_url += "/"

    return base_url


base_url = get_jupyter_base_url()


query_parameters = {
    "folder": str(
        solution_file.parent.parent
    ),
}


if True:
    query_parameters["payload"] = json.dumps([
        [
            "openFile",
            (
                "vscode-remote://"
                + solution_file.as_posix()
            ),
        ]
    ])


vscode_url = (
    base_url
    + 'vscode'
    + "/?"
    + urlencode(query_parameters)
)


button = (
    '<a href="'
    + html.escape(
        vscode_url,
        quote=True,
    )
    + '" '
    + 'target="_blank" '
    + 'rel="noopener noreferrer" '
    + 'style="'
    + 'display:inline-block;'
    + 'padding:9px 15px;'
    + 'background:#0078d4;'
    + 'color:white;'
    + 'text-decoration:none;'
    + 'border-radius:4px;'
    + 'font-weight:600;'
    + '">'
    + 'Avaa ratkaisu VS Codessa'
    + "</a>"
)


display(
    HTML(button)
)
