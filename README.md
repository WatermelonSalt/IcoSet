# IcoSet - Icon Setter for Windows Folders in Portable Drives

## What is Icoset?

IcoSet is a project made by me to make Icon setting easier on windows, especially when using portable drives. Just write the config once and voila you just need to execute the script once to get all your icons set correctly. If you use portable drives you can even modify the **"Autorun"** file to make the script execute automatically each time the drive is inserted.

## Why did I make this?

I really wanted custom icons to show up on all my windows systems, even when I carry them on my portable drive. So, I made this to solve my issue. I also did not want to install other software to solve this.

## Do I need to install this on my system to use it?

No, just place your **`config.json`** where ever you wish and just execute *`IcoSet.py`* with the proper path to the *`config.json`*

## How to use it?

`pip install colorama` to install the only dependency

You need `Python` installed on your system or drive and just execute the script like shown below

`python IcoSet.py -c "path/to/your/config.json"`

Where, you have to replace the path with your path

Also, you can do `python IcoSet.py -h` for help

## Things you should know

* **This program is completely self-contained and portable**
* Currently supports multiple common paths for folders
* Modifies a system file to achieve the result(This file **will** be modified even if you do this manually)
* This is *Open-Source* and you can modify it to your needs
* Uses a GPL 3.0 License
* An example config.json is also included which serves as a reference when writing your config.json

## Upcoming

Please suggest something

**Previous upcoming feature *"Multiple common folder support!"* added!**
