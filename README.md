# BatteryGUI

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](https://github.com/shuhuang/batterygui/blob/master/LICENSE)

This is a GUI for the visualisation of the battery database based on PyQt5.

## Installation

To use the BatteryGUI, firstly create a virtual environment: 
```
python -m venv batterygui
```

Activate the virtual environment and install the required packages: 
```
pip install -r requirements.txt
```

Run: 
```
python appMain.py
```

**Create the executable(.exe) file and installer**

We suggest using fbs (fmans build system) to build a stand-alone executable for this GUI application. More details in this [website](https://build-system.fman.io/pyqt-exe-creation/).

## Example Usage
**Table View**
<p>
    <img src="QtApp/images/battery/table.png">
</p>

**Figure View**

<p>
    <img src="QtApp/images/battery/figures.gif">
</p>

## Citation
```
@article{huang2020database,
  title={A database of battery materials auto-generated using ChemDataExtractor},
  author={Huang, Shu and Cole, Jacqueline M},
  journal={Scientific Data},
  volume={7},
  number={1},
  pages={1--13},
  year={2020},
  publisher={Nature Publishing Group}
}
```
[![DOI](https://zenodo.org/badge/DOI/10.1038/s41597-020-00602-2.svg)](https://doi.org/10.1038/s41597-020-00602-2)

