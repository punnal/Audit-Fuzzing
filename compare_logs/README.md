# Compare auditd logs and syzkaller logs

Use simpleCompare.py to compare logs.

```
python3 simpleCompare.py auditlog syzkallerlog output
```

**Note:**  auditlog is the log file obtained after parsing auditd logs and syzkallerlog is the log file obtained after parsing syzkaller logs. Click [here](https://github.com/punnal/Audit-Fuzzing/tree/master/parse_logs) to see how to parse log files.
