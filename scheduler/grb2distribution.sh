#!/bin/bash

source ~/.bash_profile

NIGHT=`date +"%Y%m%d" -d "now"`
# NIGHT=`date +"%Y%m%d" -d "now + 1 days"`
YEAR=${NIGHT:0:4}
MONTH=${NIGHT:4:2}
DAY=${NIGHT:6:2}

FINK_MM_CONFIG="path/config/file"
FINK_MM_LOG="path/to/store/log"


# same entries as in the .conf
ZTFXGRB_OUTPUT= # online_grb_data_prefix

HDFS_HOME="/opt/hadoop-2/bin/"

while true; do

     LEASETIME=$(( `date +'%s' -d '17:00 today'` - `date +'%s' -d 'now'` ))
     echo $LEASETIME

     $(hdfs dfs -test -d ${ZTFXGRB_OUTPUT}/online/year=${YEAR}/month=${MONTH}/day=${DAY})
     if [[ $? == 0 ]]; then
         echo "Launching distribution"

         # LEASETIME must be computed by taking the difference between now and max end 
         LEASETIME=$(( `date +'%s' -d '17:00 today'` - `date +'%s' -d 'now'` ))

         nohup fink_mm distribute --config ${FINK_MM_CONFIG} --night ${NIGHT} --exit_after ${LEASETIME} > ${FINK_MM_LOG}/grb_distribution_${YEAR}${MONTH}${DAY}.log
         break
     fi
     if [[ $LEASETIME -le 0 ]]
     then
        echo "exit scheduler, no data for this night."
        break
     fi
     DDATE=`date`
     echo "${DDATE}: no data yet. Sleeping..."
     sleep 5
done

