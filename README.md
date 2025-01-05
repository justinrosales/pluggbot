### External Software

- [ffmpeg](https://ffmpeg.org/download.html) - download download and add it to your system's `PATH` environment variable

### Other Depdendencies

- discord.py
- ffmpeg
- PyNaCl
- yt_dlp
- python-dotenv

Creating virtual environement **highly recommended**

You can use [Conda](https://anaconda.org/anaconda/conda) to set up the environment and install neccesseary dependencies

```
conda create --name pluggbot python=3.9
conda activate myenv
conda install discord.py
...
```

### Roadmap

- [x] play music via search or youtueb link
- [x] basic music commands
- [ ] `remove` command - removes last song from the queue
- [ ] `prefix` command - changes bot prefix command
- [ ] Integrate Spotify + SoundCloud (currently only supports YouTube)

### Current Bugs

- Certain songs do not work, bot times out. Only occurs when user searches the song instead of playing a song via song URL
