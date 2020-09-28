#!/bin/bash

FREQMAX=32767
FREQMIN=0

usage='usage: \n
        [-h] \n
        [--freqMax[=]<value>] \n
        [--freqMin[=]<value>] \n'

while getopts ":h-:" opt; do
  case ${opt} in
    - )
        case "${OPTARG}" in
          freqMax=* )
            val=${OPTARG#*=}
            opt=${OPTARG%=$val}
            FREQMAX=$val
            echo "Parsing option: '--${opt}', value: '${val}'" >&2
            ;;
          freqMin=* )
            val=${OPTARG#*=}
            opt=${OPTARG%=$val}
            FREQMIN=$val
            echo "Parsing option: '--${opt}', value: '${val}'" >&2
            ;;
          *)
            echo -e $usage 1 >&2
            exit 1

        esac

      ;;
    t )
      echo -e $OPTARG
      exit 1
      ;;
    h )
      echo -e $usage
      exit 1
      ;;
    \? )
      echo -e $usage
      exit 1
      ;;
    : )
      echo -e $usage
      exit 1
      ;;
  esac
done


echo "-----------------" >> /auditConfRandom.txt ;
echo "" >> /auditConfRandom.txt ;
OUTPUT=$(($FREQMIN + $(( $RANDOM % $(($FREQMAX - $FREQMIN + 1)) )) ));
echo $OUTPUT
date "+%H:%M:%S %d/%m/%y">> /auditConfRandom.txt ;
sed -i "s/freq = [0-9]*/freq = $OUTPUT/1" /etc/audit/auditd.conf
service auditd restart
echo "Randomised" >> /auditConfRandom.txt ;
date "+%H:%M:%S %d/%m/%y">> /auditConfRandom.txt ;
echo "freqSize" >> /auditConfRandom.txt ;
echo $OUTPUT >> /auditConfRandom.txt;
auditctl -s >> /auditConfRandom.txt;
echo "" >> /auditConfRandom.txt;
