Title: PostgresSQL

Content:

## Client

Ubuntu installation
```
$ apt-get install postgresql-client
```

Connect to database
```
$ psql -h {HOSTNAME} {DATABASE} {USERNAME}
```

Exit connection
```
\q
```

## Troubleshooting

### ERROR: function uuid_generate_v4() does not exist

Connect to database and execute.
```
CREATE EXTENSION "uuid-ossp";
```

