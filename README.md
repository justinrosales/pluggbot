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
- [x] add music/queue management commands
- [ ] `prefix` command - changes bot prefix command
- [x] add support for other platforms (~~Spotify~~/SoundCloud)
  - Spotify API does not provide access to raw audio streams due to licensing restrictions. Only allows metadata retrieval (e.g., track name, artist, album)
- [ ] deploy
