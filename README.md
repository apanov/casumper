# casumper
Cassandra 0.6 commitlog extractor. Casumper can be used to dump pairs of table:key from cassandra 0.6 CommitLog-*.log.

Usages: 
1. Print pairs table:key of row mutations
```
cat CommitLog-1532176199996.log | python -u casumper.py
```

2. Find frequently keys by table
```
cat CommitLog-1532176199996.log | python -u casumper.py | sort | uniq -c | sort -n
```

3. Find frequently keys by table for multiple commit logs
```
find CommitLog-*.log | xargs cat | python -u casumper.py >> /tmp/commitlog-pairs.log
less /tmp/commitlog-pairs.log | sort | uniq -c | sort -n
```

