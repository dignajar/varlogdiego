# Title: Screenshot over SSH / Command line
<!-- Position: 1 -->
<!-- Date: 2016-03-10 18:20:00 -->
---
This is not a feature of the SSH, it's just a app for the command line and has the feature to specifying parameters such as the display port of the X11.

You need the app `scrot`, and the DISPLAY port of your X11 session.

```
$ DISPLAY=:0 scrot screenshot.png
```
