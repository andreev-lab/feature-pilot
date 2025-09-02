import glob
import os
from pathlib import Path


def get_reload_dirs() -> list[str]:
  """
  By default uvicorn watches only the files of the app, in our case (feature-pilot/apps/api/src).
  This means that updating lib code won't trigger app rebuilt.
  To fix it, we provide all the paths to server libs, to uvicorn to listen to.
  :return:
  """
  script_dir = Path(__file__).parent.resolve()
  root_dir = script_dir.parent.parent.parent
  libs_dir = root_dir / "libs"

  server_libs_pattern = str(libs_dir / "**" / "server")
  server_libs = glob.glob(server_libs_pattern, recursive=True)

  cwd = Path.cwd().resolve()

  relative_server_libs = [os.path.relpath(path, cwd) for path in server_libs]

  return [".", *relative_server_libs]
