# Accessible Virtual Keyboard
*November 15th, 2018*

## Dedicated to Benjamin Knapp
Approximately 7 years ago, Benjamin Knapp experienced cardiac arrest. Today, he has difficulty moving and speaking, but can
communicate with others by squeezing his fingers and opening his mouth. These small muscle movements can be used to create an
efficient communication device that will be able to help Ben type his thoughts on a virtual keyboard, and even speak words and sentences with the aid of a text-to-speech program. This project's purpose is to develop a predictive virtual keyboard that can be controlled with two binary inputs. This keyboard can be installed on a Raspberry Pi and connected to two [MyoWare Muscle Sensors](https://www.sparkfun.com/products/13723) to allow people with disabilities to communicate concisely and effectively.

## Getting Started
The following items are needed for this project:
* **1x** [Raspberry Pi 3 Model B+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/)
* **2x** [MyoWare Muscle Sensors](https://www.sparkfun.com/products/13723)
* **1x** Display for Raspberry Pi 3 Model B+
* **1x** Speaker for Raspberry Pi 3 Model B+

For a complete list of parts, see the [parts-list.md](/docs/parts-list.md) file.

### Prerequisites
After obtaining the previous items, install a Linux or Unix operating system (preferrably [Raspbian](https://www.raspberrypi.org/downloads/raspbian/)).

## Installation
1. Install and update packages
```bash
apt-get update --fix-missing -y
apt-get dist-upgrade -y
apt-get autoremove -y
apt-get autoclean -y
```
2. Install Python 3.6 (if not already installed)
```bash
apt-get install python3 -y
```
3. Install Python packages
```bash
pip install tensorflow; pip3 install tensorflow
pip install numpy; pip3 install numpy
pip install autocomplete; pip3 install autocomplete
pip install kivy; pip3 install kivy
pip install gTTS; pip3 install gTTS
```
4. Clone/download the repository
* Clone repository: `git clone https://github.com/computer-geek64/accessible-virtual-keyboard/`
* Download repository: `wget https://github.com/computer-geek64/accessible-virtual-keyboard/archive/master.zip; unzip master.zip`
5. Execute `Main.py`

### Deployment
* Before executing the program, ensure that the line `#!/usr/bin/python3` is at the top of `Main.py`. If it is not, make sure to
add it there before running `./Main.py`. The other alternative is to use the `python3` command as so: `python3 Main.py`.
* Always ensure that the line endings are compatible with the operating system that you are using.
* If a warning message surfaces regarding `pip`, execute the following command: `python -m pip install --upgrade pip; python3 -m pip install --upgrade pip`

## Execution
* After `Main.py` is executed (either by running `./Main.py` or `python3 Main.py`), a GUI (Graphical User Interface) should appear.

### Functionality
Explain each function of the accessible virtual keyboard.

## Built With
* Software:
  * [Python](https://www.python.org/) - *Primary project language*
    * [TensorFlow](https://www.tensorflow.org/) - *Machine learning back-end development*
    * [NumPy](http://www.numpy.org/) - *Scientific computation package*
    * [Autocomplete](https://pypi.org/project/autocomplete/) - *Basic autocomplete functionality*
    * [Kivy](https://kivy.org/) - *GUI (Graphical User Interface) front-end development*
    * [gTTS](https://pypi.org/project/gTTS/) - *Google Text-to-Speech*
  * IDE: [JetBrains](https://www.jetbrains.com/pycharm/) - *High-end integrated development environment for Python*
  * Shell: [GNU Bash](https://www.gnu.org/software/bash/) - *Open-source Bourne Again Shell*
* Hardware:
  * [Raspberry Pi](https://www.raspberrypi.org/) - *Inexpensive and efficient single-board computer*
  * [MyoWare Muscle Sensors](https://www.sparkfun.com/products/13723) - *Arduino-based electromyography (EMG) sensor for muscle control*

## Contributing
Please read the [CONTRIBUTING.md](/docs/CONTRIBUTING.md) file for details on our code of conduct and pull request policy.

## Versioning
This project uses [git](https://git-scm.com/) version control.

## Sources
See the [sources.md](/docs/sources.md) file for information gathered to help create this project.

## Developers
* **Ashish D'Souza** - *Sole developer* - [computer-geek64](https://github.com/computer-geek64/)

See also the list of [contributors](/docs/CONTRIBUTORS.md) who participated in this project.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
* **Benjamin Knapp**
  * This is dedicated to you. I hope this project will help you find your own voice again.
* **Christopher Knapp**
  * Project founder
  * Thank you for such an amazing opportunity to help others
