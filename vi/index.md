# Title: VI / VIM (vi improved)
<!-- Date: 2017-10-01 22:00:00 -->
<!-- dateModified: 2017-11-01 22:00:00 -->
---

## About vi
vi is a screen-oriented text editor originally created for the Unix operating system.

The name "vi" is derived from the shortest unambiguous abbreviation for the ex command visual, which switches the ex line editor to visual mode.

## Fix arrow keys and backspace
```
$ vi ~/.vimrc
```

Add this lines
```
set nocompatible
set backspace=2
```

## Search and replace
```
:%s/word-to-find-here/replace-word-here/g
```

## Shortcuts
```
# Go to the last line
G
```