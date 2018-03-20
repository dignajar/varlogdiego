Title: Bash scripts and stuff

Content:

## While / For

While
```
#!/bin/bash

COUNT=1
while [ $COUNT -lt 10 ]; do
	echo $COUNT
	COUNT=$(($COUNT + 1))
done
```

For
```
#!/bin/bash

AMOUNT=10
for i in $(seq 1 $AMOUNT); do
	echo $i
done
```

One line command
```
ps aux | grep php | awk '{print $2}' | xargs -L1 echo
```

## Check environment variable is defined
```
#!/bin/bash

MYVARIABLE="${MYVARIABLE:-hello world}"
```

## Exit code
```
#!/bin/bash

echo "Hello world" | grep "food"
let EXIT_CODE=$?

if [ $EXIT_CODE -ne 0 ]
then
	echo "Food word not found"
fi
```

```
#!/bin/bash

let EXIT_CODE=1
while [  $EXIT_CODE -eq 1 ]; do
	echo "Hello world" | grep "world"
	let EXIT_CODE=$?
done
```

## Foreach line on file
```
#!/bin/bash

while read LINE; do
	echo $LINE
done < filename.txt
```
