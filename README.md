# Documentation microservices
Microservices
1. Create python virtual environment `python3 -m venv ~/.venv` or `virtualenv ~/.venv`
2. Run `nano ~/.bashrc` and add following line at the end `source ~/.venv/bin/activate`
3. Create empty files:
    a. `touch requirements.txt`
    b. `touch Dockerfile`
    c. `touch Makefile`
    d. `mkdir mylib`
    e. `touch mylib/__init__.py`
    f. `touch mylib/logic.py`
    g. `touch main.py`
4. Build the Makefile
5. Build the requirements.txt file as follows (without version numbers)
    wikipedia
    pytest
    pytest-cov
    pylint
    black
    fire
6. Run `make install`
7. Run `pip freeze|less`
8. Copy version numbers into requirements.txt
9. Run `make install` again
10. git status git add * git commit -m "pinning installed versions" git push git status
11. Add format code in Make file `black *.py mylib/*.py`
12 Run `make format`
13. In main import wiki and print wiki
14. Run `python main.py`