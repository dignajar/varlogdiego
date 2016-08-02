title: Crontab
description: Little examples of crontab
tags: Linux, Crontab, Jobs, schedule
position: 1
date: 2016-03-10 18:20:00
content:

## Crontab format

```
*    *    *    *    *  command to be executed
┬    ┬    ┬    ┬    ┬
│    │    │    │    │
│    │    │    │    │
│    │    │    │    └───── day of week (0 - 6) (0 is Sunday, or use names)
│    │    │    └────────── month (1 - 12)
│    │    └─────────────── day of month (1 - 31)
│    └──────────────────── hour (0 - 23)
└───────────────────────── min (0 - 59)
```

