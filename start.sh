#!/bin/bash

#获得当前路径
currentdir=`dirname $0`
# JAVA_OPTS="-Xdebug -Xrunjdwp:transport=dt_socket,address=9025,server=y,suspend=n"

runjar="pagetest.py"

#JAVA_OPTS="-XX:PermSize=64m -XX:MaxPermSize=64m -Xmx256m -Xms128m -Xmn128m -Xss128k -XX:ParallelGCThreads=4 -XX:+UseConcMarkSweepGC -XX:+CMSParallelRemarkEnabled -XX:+UseParNewGC -XX:+Use    CMSCompactAtFullCollection -XX:+ScavengeBeforeFullGC -Xloggc:/stat-analysis-client/gc.log -XX:+PrintGC -XX:+PrintGCDetails -XX:+PrintGCTimeStamps"
# EXEC_COMMAND="java -jar $JAVA_OPTS ${currentdir}/${runjar}"
EXEC_COMMAND="python ${runjar}"
#pidfile='/tmp/crawler-node.pid'

#currentdir=`cd "$currentdir" > /dev/null ; pwd`

#判断是否已经启动,kill已经启动的client
#for pid in `ps -ef | grep stat-analysis-client。jar | grep -v grep | awk '{print $2}'`
#  do kill -9 $pid
#done
usage() {
   echo "$0 start|stop|restart"
   exit 1
}

[ $# -ne 1 ] && usage


start() {
	echo "start "
	if [ -f ${currentdir}/${runjar} ]
	then
	    echo "start $runjar"
	    echo "current dir -> $currentdir"
	    nohup $EXEC_COMMAND > $currentdir/out.log 2>&1 &
	    echo "end of start  $runjar"
	else
	  echo "$runjar does not exists!"
	fi
}

stop() {
	pid=`ps -ef | grep ${runjar} | grep -v grep | awk '{print $2}'`
        if [ -n $pid ]
	then
	    echo "stopping..."
            kill -9 $pid
            echo "done"
	else
	    echo 'client had already stopped'
	fi
}

restart(){
    stop
    start
}

case $1 in
    start)
    start
    ;;
    stop)
    stop
    ;;
    restart)
    restart
    ;;
    *)
    usage
    ;;
esac
