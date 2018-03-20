title: Curl Command
content:

## Response time
``
curl -s -w %{time_total}\\n -o /dev/null <http://domain.com>
```

Execute a few times
```
for i in {1..10}; do curl -s -w %{time_total}\\n -o /dev/null <http://domain.com>; done
```
