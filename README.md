# IcoSet - Icon Setter for Windows Folders in Portable Drives

## What is Icoset?

IcoSet is a project made by me to make Icon setting easier on windows, especially when using portable drives. Just write the config once and voila you just need to execute the script once to get all your icons set correctly. If you use portable drives you can even modify the **"Autorun"** file to make the script execute automatically each time the drive is inserted.

## Why did I make this?

I really wanted custom icons to show up on all my windows systems, even when I carry them on my portable drive. So, I made this to solve my issue. I also did not want to install other software to solve this.

## Do I need to install this on my system to use it?

No, just place your **`config.json`** where ever you wish and just execute *`IcoSet.py`* with the proper path to the *`config.json`*

## How to use it?

First, you need `Python` installed or at least the embeddable package of `Python` on your system or drive and just execute the script like shown below

`python IcoSet.py -c "path/to/your/config.json"`

Where, you have to replace the path with your path

Also, you can do `python IcoSet.py -h` for help

There will be a release with the python embeddable package in  case if you don't have `Python` too

How to use the embeddable package version?

Well, there are two ways of doing it

***Way 1:***

* Open `python.exe` in the embeddable package
* Paste the below lines and replace with your path

```py
import os
os.system("python ./Code/IcoSet.py -c 'path/to/your/config.json'")
```

***Way 2:***

* Open a commandline in the root of the embeddable package and do `./python ./Code/IcoSet.py -c 'path/to/your/config.json'` and also replace the path with your path

## Things you should know

* **This program is completely self-contained and portable**
* Currently supports only one common path for folders
* Modifies a system file to achieve the result(This file **will** be modified even if you do this manually)
* This is *Open-Source* and you can modify it to your needs
* Uses a GPL 3.0 License
* An example config.json is also included which serves as a reference when writing your config.json

## Upcoming

Support for multiple common folder paths is coming soon
