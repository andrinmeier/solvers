<div align="center">
  <h1>Solvers</h1>
  <img src="./solvers_logo.svg" width="200"/>
  <p>Solvers is a collection of puzzle solvers written in python using or-tools.</p>
</div>

> This project is still in an early alpha phase
> and you should expect breaking changes before the first stable release.

![Code Quality](https://github.com/andrinmeier/solvers/actions/workflows/quality_checks.yml/badge.svg)
[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
[![mypy](https://img.shields.io/badge/type%20checking-mypy-brightgreen)](http://mypy-lang.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=andrinmeier_solvers&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=andrinmeier_solvers)
[![Documentation Status](https://readthedocs.org/projects/solvers/badge/?version=latest)](https://solvers.readthedocs.io/en/latest/?badge=latest)
[![Discord](https://img.shields.io/discord/978401806990332014)](https://discord.com/channels/978401806990332014/978548776606240848)


# How to install

This project is also available on PyPI under the name [ortools-puzzle-solvers](https://pypi.org/project/ortools-puzzle-solvers/).

You can install the latest version by issuing the following command:

`pip install ortools-puzzle-solvers`

# How to use

Here's an example on how you can actually use the solvers:

```
from solvers.yakuso.yakuso_solver import YakusoSolver
solver = YakusoSolver()
solutions = solver.solve(param1, param2, param2, ...)
```

The actual parameters for each solver differ.
Take a look at the [written pytests](https://github.com/andrinmeier/solvers/tree/main/tests) for examples on how to use the solvers.

# What solvers can I use?

The following solvers have been tested and shown to work:

* [Doplo](https://www.janko.at/Raetsel/Doppelblock/index.htm)
* [Futoshiki](https://www.janko.at/Raetsel/Futoshiki/index.htm)
* [Killer Sudoku](https://www.janko.at/Raetsel/Sudoku/Killer/index.htm)
* [Sudoku](https://www.janko.at/Raetsel/Sudoku/index.htm)
* [Suguru](https://www.janko.at/Raetsel/Suguru/index.htm)
* [Yakuso](https://www.janko.at/Raetsel/Yakuso/index.htm)
* [Zehnergitter](https://www.janko.at/Raetsel/Zehnergitter/index.htm)

