Title: VI / VIM (vi improved)

Content:

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
:%s/Word-to-find-here/Replace-word-here/g
```
