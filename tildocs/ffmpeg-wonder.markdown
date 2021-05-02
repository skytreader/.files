# ffmpeg wonders

[Convert .webp to .jpg](https://unix.stackexchange.com/a/349116)

```
ffmpeg -i file.webp file.jpg
```

---

Compile a bunch of JPEGs to a slideshow movie:

```
ffmpeg -framerate 2 -pattern_type glob -i "DSC*.JPG" -c:v libx264 -vf "fps=25,format=yuv420p" out.mp4
```
