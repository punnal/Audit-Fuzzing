#!/bin/bash

BUFFERMAX=32767
BUFFERMIN=0

RATEMAX=32767
RATEMIN=0

usage='usage: \n
        [-h] \n
        [--bufferMax[=]<value>] \n
        [--bufferMin[=]<value>] \n
        [--rateMax[=]<value>] \n
        [--rateMin[=]<value>] \n'

while getopts ":h-:" opt; do
  case ${opt} in
    - )
        case "${OPTARG}" in
          bufferMax=* )
            val=${OPTARG#*=}
            opt=${OPTARG%=$val}
            BUFFERMAX=$val
            echo "Parsing option: '--${opt}', value: '${val}'" >&2
            ;;
          bufferMin=* )
            val=${OPTARG#*=}
            opt=${OPTARG%=$val}
            BUFFERMIN=$val
            echo "Parsing option: '--${opt}', value: '${val}'" >&2
            ;;
          rateMax=* )
            val=${OPTARG#*=}
            opt=${OPTARG%=$val}
            RATEMAX=$val
            echo "Parsing option: '--${opt}', value: '${val}'" >&2
            ;;
          rateMin=* )
            val=${OPTARG#*=}
            opt=${OPTARG%=$val}
            RATEMIN=$val
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

echo "----------------" >> /auditRandom.txt ;

OUTPUT=$(($BUFFERMIN + $(( $RANDOM % $(($BUFFERMAX - $BUFFERMIN + 1)) )) ));
echo "1) " $OUTPUT
auditctl -b $OUTPUT >> /auditRandom.txt;
echo "" >> /auditRandom.txt ;
date "+%H:%M:%S %d/%m/%y">> /auditRandom.txt ;
echo "BufferSize" >> /auditRandom.txt ;
echo $OUTPUT >> /auditRandom.txt;
echo "" >> /auditRandom.txt;

OUTPUT=$(($RATEMIN + $(( $RANDOM % $(($RATEMAX - $RATEMIN + 1)) )) ));
echo "2) " $OUTPUT
auditctl -r $OUTPUT >> /auditRandom.txt;
echo "" >> /auditRandom.txt ;
date "+%H:%M:%S %d/%m/%y">> /auditRandom.txt ;
echo "Message Per Seconds" >> /auditRandom.txt ;
echo $OUTPUT>> /auditRandom.txt;
echo "" >> /auditRandom.txt;
