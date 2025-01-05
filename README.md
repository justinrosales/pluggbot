### External Software

- [ffmpeg](https://ffmpeg.org/download.html) - download and add it to your system's `PATH` environment variable

### Other Depdendencies

- discord.py
- ffmpeg
- PyNaCl
- yt_dlp
- python-dotenv

Creating virtual environement **highly recommended**

You can use [Conda](https://anaconda.org/anaconda/conda) to set up the environment and install necessary dependencies

```
conda create --name pluggbot python=3.9
conda activate myenv
conda install discord.py
...
```

### Roadmap

- [x] play music via search or youtube link
- [x] basic music commands (help, play, stop, pause, resume)
- [ ] queue management commands (~~queue~~, ~~skip~~, ~~clear~~, remove)
- [ ] `prefix` command - changes bot prefix command
- [ ] Integrate Spotify + SoundCloud (currently only supports YouTube)

### Current Bugs

- Music stops in the middle of the song
