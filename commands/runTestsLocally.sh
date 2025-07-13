# Runs the CI/CD tests locally.
# This will invalidate any existing ReCodEx session you have (by deleting the context.yaml file),
# in case you want to login into ReCodEx later, you will have to delete this file first
# by running: rm ~/.local/share/recodex/context.yaml

if ! test -d ./venv; then
  echo "Initializing Python venv"
  python3.11 -m venv venv
  ./venv/bin/pip install -r requirements.txt
  ./venv/bin/pip install -e .
fi

source venv/bin/activate
rm ~/.local/share/recodex/context.yaml
python3 -m tests.testClasses

# remove the testing login token
rm ~/.local/share/recodex/context.yaml
