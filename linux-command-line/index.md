# Title: GNU/Linux command line examples
<!-- Date: 2017-10-01 22:00:00 -->
<!-- dateModified: 2017-11-01 22:00:00 -->
---

## grep
Search for every file who has the word `unsubscribe` and for each file search the word subject
```
$ grep -i "unsubscribe" * -l | while read file ; do grep -i "subject" "$file" --color ; done
```

## Search and replace a word
Search `foo` and replace for `bar` in the file `filename.txt`
```
$ sed -i -e 's/foo/bar/g' filename.txt
```

## Permissions to files and directories
Change all directories permissions to rwx-rx-rx
```
find . -type d -exec chmod 755 {} \;
```

Change all files permissions to rw-r-r
```
find . -type f -exec chmod 644 {} \;
```

## Fork bomb
```
:(){ :|:& };:
```

- http://askubuntu.com/a/159496