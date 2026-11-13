# make.fun cutest-picture-01 entry (Python 3.13, standard library only).
# The picture is the entry.png beside this file: a chubby baby penguin in
# an oversized yellow beanie, holding a tiny glowing star. The program
# copies it to the output directory.
# Deterministic: the same bytes go out on every run.
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

SRC = HERE / "entry.png"
DST = OUT / "entry.png"
MAX_BYTES = 1_048_576  # the gate's file cap: refuse to ship anything over it

if SRC.stat().st_size > MAX_BYTES:
    raise SystemExit(f"entry.png is {SRC.stat().st_size} bytes, over the 1 MiB cap")

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SRC, DST)
# Fail loudly on a short write instead of handing the judge a corrupt file.
if DST.stat().st_size != SRC.stat().st_size:
    raise SystemExit("entry.png copy came out short")
