title: GNU/Linux command line examples
position: 1
date: 2016-03-10 18:20:00
content:

## Grep

grep -i "unsubscribe" * -l | while read file ; do grep -i "subject" "$file" --color ; done

