title: elasticsearch
content:

## Cluster information
```
curl localhost:9200/_cluster/health?pretty
```

## Indices list
```
curl localhost:9200/_cat/indices
```

## Remove indices
! Check this command !
```
curl -XDELETE http://localhost:9200/*2017.10*
```