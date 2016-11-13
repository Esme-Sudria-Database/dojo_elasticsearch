#!/usr/bin/env bash

readonly SCRIPT_DIR=$(dirname "$(readlink -m "$0")");

function main
{
  check_command_exists python "You have to setup python (https://docs.python.org/3/using/index.html)"
  check_command_exists pip "You have to setup pip (https://pip.pypa.io/en/stable/installing/)"
  check_command_exists pip "You have to setup virtualenv -> pip install virtualenv"

  set -o errexit
  set -o pipefail
  # set -o nounset
  set -o errtrace

  if [ ! -d "${SCRIPT_DIR}/venv" ]
  then
    virtualenv "${SCRIPT_DIR}/venv"
  fi

  source "${SCRIPT_DIR}/venv/bin/activate"

  pip install -r "${SCRIPT_DIR}/requirements.txt"
}

function error_exit
{
  echo "$1" 1>&2
  exit 1
}

# function to check a command is available
function check_command_exists
{
  command=$1
  message=$2
  command -v ${command} >/dev/null 2>&1 || { echo >&2 $2; exit 1; }
}

check_command_exists plantuml

main "$@"
