#! /bin/bash
DATE=$(date +%d-%m-%Y)
File=$DATE-$HOSTNAME

uptime
echo "Running checks on $HOSTNAME for $DATE"
touch $File
osts ()
{
    ost | grep -v "===" | sed -e ' s^NOT UP^NOTUP^g' | awk '{printf("%-8s %-8s %-10                                                                                     s %-12s %-10s\n",$1,$2,$3,$4,$NF)}'
}
fpa ()
{
    ast | egrep -i "$1|AppName|------"
}
echo "1# check file system efficiency" >> $File
echo "-----------------------" >> $File
df -kh >> $File
echo "-----------------------" >> $File

echo "2# uptime for $HOSTNAME" >> $File
uptime >> $File
echo "-----------------------" >> $File
echo "3# check Ocelots stats for $HOSTNAME" >> $File
osts >> $File
echo "-----------------------" >> $File
echo "4# show down tasks in probe $HOSTNAME" >> $File
ast | grep -v ApU >> $File
echo "-----------------------" >> $File
echo "5# RUN topit command for  $HOSTNAME " >> $File
topit >> $File
echo "-----------------------" >> $File
echo "6# RUN suds log analyzer for $HOSTNAME " >> $File
sudsLogAnalyzer >> $File
echo "-----------------------" >> $File
echo "Dump port | grep -i "unknown" for $HOSTNAME" >> $File
/inet/spIprobe/basic/atca-x86-linux/etc/Dump port | grep -i "unknown" >> $File
echo "-----------------------" >> $File
echo "Dump port | grep -i "unassign" for $HOSTNAME" >> $File
/inet/spIprobe/basic/atca-x86-linux/etc/Dump port | grep -i "unassign" >> $File
echo "-----------------------" >> $File
echo "show all tasks in all $HOSTNAME probe" >> $File
fpa >> $File
echo "-----------------------" >> $File

echo "##################end of Checks"


