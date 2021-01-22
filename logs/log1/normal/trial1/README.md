# Logs description

## Syzkaller Logs
**syzkallerLogsRaw:** Logs obtained from syzkaller 

**syzkallerLogs:** Parsed syzkallerLogsRaw to extract systemcalls only

## Auditd Logs
**auditLogsRaw:** Logs obtained from syzkaller

**auditdLogs:** Parsed auditLogsRaw to extract systemcalls only

## System Logs
**systemLogs.txt:** Logs obtained from running ```dmesg```, ```service auditd status``` and ```auditctl -s``` commands every 2 minutes.

## Comparison Report
**systemLogs.txt:** Reports obtained by comparing syzkallerLogs and auditdLogs. The Report shows the name and number of lost systemcalls. It also shows the line number where a system call was expected in auditd logs.
