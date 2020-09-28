#Change auditd parameters automatically

## Changing parameters in audit.rules
Buffer size and Rate limit parameters can be changed to a random value between the range specified. 

Time, value of parameter and output of 
``` 
auditctl -s
```
will be stored in a /auditRandom.txt.

Sample use:

```
./randomRules.sh --bufferMax=4 --bufferMin=1 --rateMax=10 --rateMin=5
```

## Changing parameters in auditd.conf
freq parameter can be changed to a random value between the range specified.

Time, value of parameter and output of 
``` 
auditctl -s
```
will be stored in a /auditRandom.txt.

Sample use:

```
./randomConfig.sh --freqMax=5 --freqMin=2
```

## Run these scripts periodically
Use corn job to run these scripts periodically. Setup corn job by following this [link](https://www.geeksforgeeks.org/how-to-setup-cron-jobs-in-ubuntu/).
