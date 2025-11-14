# pytest_restapi
Basic pytest demo for RestAPI testing

Install python3, create a virtual environment for python, install required software packages and run the test suite
```bash
cd <repo_folder>
sudo apt install python3 python3-venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest --html=test-results/report.html --junitxml=test-results/report.xml -vvv
```