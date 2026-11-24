import html
import json
import os
from pathlib import Path
from urllib.parse import urlencode

from IPython.display import HTML, display

python_file = (Path.cwd() / "src" / "my_code.py").resolve()
csharp_file = (Path.cwd() / "src" / "my_code.cs").resolve()

if python_file.is_file():
    solution_file = python_file
elif csharp_file.is_file():
    solution_file = csharp_file
else:
    raise FileNotFoundError(
        "Ratkaisupohjaa src/my_code.py tai src/my_code.cs ei löytynyt."
    )

base_url = os.environ.get("JUPYTERHUB_SERVICE_PREFIX", "/")
if not base_url.startswith("/"):
    base_url = "/" + base_url
if not base_url.endswith("/"):
    base_url += "/"

query_parameters = {
    "folder": str(solution_file.parent.parent),
}

if True:
    query_parameters["payload"] = json.dumps([
        ["openFile", "vscode-remote://" + solution_file.as_posix()]
    ])

vscode_url = (
    base_url + 'vscode' + "/?" + urlencode(query_parameters)
)
button = (
    '<a href="' + html.escape(vscode_url, quote=True) + '" '
    'target="_blank" rel="noopener noreferrer" '
    'style="display:inline-block;padding:9px 15px;'
    'background:#0078d4;color:white;text-decoration:none;'
    'border-radius:4px;font-weight:600;">'
    + 'Avaa ratkaisu VS Codessa' + '</a>'
)
display(HTML(button))
