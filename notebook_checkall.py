from pathlib import Path
import subprocess
import sys

results_file = Path("results.txt")
results_file.unlink(missing_ok=True)

print("Testing...")
result = subprocess.run(
    [sys.executable, "testall.py"],
    stdin=subprocess.DEVNULL,
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
    check=False,
)
print("...Completed")

if not results_file.is_file():
    raise RuntimeError(
        "testall.py ei luonut results.txt-tiedostoa "
        f"(paluukoodi {result.returncode})."
    )

print(32 * "-")
print(results_file.read_text(encoding="utf-8"), end="")
print(32 * "-")
