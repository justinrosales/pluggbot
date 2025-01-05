### External Software

- [ffmpeg](https://ffmpeg.org/download.html) - download download and add it to your system's `PATH` environment variable

### Other Depdendencies

- discord.py
- ffmpeg
- PyNaCl
- yt_dlp
- python-dotenv

Creating virtual environement **highly recommended!**

For example, use [Conda](https://anaconda.org/anaconda/conda) to set up the environment and install neccesseary dependencies

```
conda create --name pluggbot python=3.9
conda activate myenv
conda install discord.py
...
```

### Commands to add later

- remove - removes last song from the queue
- prefix - changes bot prefix command

### Current Bugs

- Certain songs dont work, bot times out. Only occurs when user searches the song instead of playing a song via song URL
