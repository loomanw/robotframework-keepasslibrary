# Copyright 2020-     Robot Framework Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import logging
import os
import re
import subprocess
import sys
from pathlib import Path
from .translation import compare_translation, get_library_translation
import click

ROOT_FOLDER = Path(__file__).resolve().parent.parent
is_terminal = sys.stdout.isatty()
CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}
# ANSI_ESCAPE = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])", flags=re.IGNORECASE)
logger = logging.getLogger(__name__)


def _log(message: str, silent_mode: bool = False):
    if silent_mode:
        return
    if os.name == "nt":
        message = re.sub(r"[^\x00-\x7f]", r" ", message)
    try:
        logger.info(message.strip("\n"))
        if is_terminal:
            print(message.strip("\n"), flush=True)  # noqa: T201
    except Exception as error:
        logger.info(f"Could not log line, suppress error {error}")


def _write_marker(silent_mode: bool = False):
    _log(f'\n{"=" * 70}', silent_mode)


def _python_info():
    _write_marker()
    python_version = (
        f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    )
    _log(f"Used Python is: {sys.executable}\nVersion: {python_version}")
    _write_marker()
    _log("pip freeze output:\n\n")
    process = subprocess.run(  # noqa: PLW1510
        [sys.executable, "-m", "pip", "freeze"],
        stderr=subprocess.STDOUT,
        stdout=subprocess.PIPE,
        timeout=60,
    )
    _log(process.stdout.decode("UTF-8"))
    _write_marker()


def get_rf_version():
    process = subprocess.run(
        [sys.executable, "-m", "robot", "--version"], capture_output=True, check=False
    )
    return process.stdout.decode("utf-8").split(" ")[2]


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    _write_marker()
    version_file = ROOT_FOLDER / "version.py"
    version_text = version_file.read_text()
    match = re.search(r"\"\d+\.\d+.\d+\"", version_text)
    keepass_lib_version = match.group(0) if match else "unknown"
    _log(f"Installed KeePassLibrary version is: {keepass_lib_version}")
    _log(f'Robot Framework version: "{get_rf_version()}"')
    _write_marker()


@click.group(
    invoke_without_command=True, context_settings=CONTEXT_SETTINGS, no_args_is_help=True
)
@click.option(
    "--version",
    is_flag=True,
    help="Prints versions and exits",
    callback=print_version,
    expose_value=False,
    is_eager=True,
)
@click.option(
    "--silent", is_flag=True, help="Does not log anything, not even in the log file."
)
@click.pass_context
def cli(ctx, silent):
    """Robot Framework KeePassLibrary command line tool.

    \b
    Possible commands are:
    translation

    \b
    1) pip install robotframework-browser
    2) rfbrowser translation

    translation will generate default translation json file from library keywords.

    See each command argument help for more details what (optional) arguments that command supports.
    """
    ctx.ensure_object(dict)
    ctx.obj["SILENT"] = silent


@cli.command()
@click.argument(
    "filename",
    type=click.Path(exists=False, dir_okay=False, path_type=Path),
    required=True,
)
@click.option(
    "--compare",
    help="Compares the translation file sha256 sum to library documentation.",
    default=False,
    is_flag=True,
    show_default=True,
)
def translation(
    filename: Path,
    compare: bool = False,
):
    """Default translation file for KeePasslibrary keywords.

    This will help users to create their own translation as Python plugins. Command
    will populate json file with english language. To create proper translation
    file, users needs to translate the keyword name and doc arguments values in
    json file.

    The filename argument will tell where the default json file is saved.

    If the --compare flag is set, then command does not generate template
    translation file. Then it compares sha256 sums from the filenane
    to ones read from the library documenentation. It will print out a list
    of keywords which documentation sha256 does not match. This will ease
    translation projects to identify keywords which documentation needs updating.
    """
    translation = get_library_translation()
    if compare:
        if table := compare_translation(filename, translation):
            _log(
                "Found differences between translation and library, see below for details."
            )
            for line in table:
                _log(line)
        else:
            _log("Translation is valid, no updated needed.")
    else:
        with filename.open("w") as file:
            json.dump(translation, file, indent=4)
        _log(f"Translation file created in {filename.absolute()}")


if __name__ == "__main__":
    cli()
