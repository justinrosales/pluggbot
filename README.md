### External Software

- [ffmpeg](https://ffmpeg.org/download.html) - download and add it to your system's `PATH` environment variable

### Other Depdendencies

- discord.py
- ffmpeg
- PyNaCl
- yt_dlp
- python-dotenv

I recommend setting up a virtual environtment (e.g. [Conda](https://anaconda.org/anaconda/conda)) to manage dependencies

```
conda create --name myenv python=3.9
conda activate myenv
conda install discord.py
...
```

### Roadmap

- [x] play music via search or youtube link
- [x] basic music/queue management commands
- [ ] `prefix` command - changes bot prefix command
- [ ] Integrate Spotify + SoundCloud (currently only supports YouTube)
- [ ] DEPLOY!
