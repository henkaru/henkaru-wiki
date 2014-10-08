#!/bin/bash
# Converts url from dokuwiki to pdf report the previous month
# and sends it via mail

PDFDIR='/opt/wiki/pdf'
[ -e "/opt/maillist" ] && ADDRLIST=`cat "$PDFDIR"/maillist` || ADDRLIST="admin"
[ ! -d "$PDFDIR" ] && mkdir -p "$PDFDIR"
DATE=`date -d 'month ago' +%m-%Y | sed 's/0//'`
filename="stats_${DATE}"
URL='http://wiki.a/doku.php?id=reports:'$filename

# Coverting url to PDF file
wkhtmltopdf "$URL" ${PDFDIR}/${filename}.pdf

# Sending mail with url of report and attached pdf
[ ! -s "${PDFDIR}/${filename}.pdf" ] && exit 1 || \
echo "Сообщение создано автоматически, отвечать на него не нужно.
    Статистику по входящему трафику можно посмотреть по ссылке
    $URL
    или в приложенном файле." | mutt -s "Интернет трафик за $DATE" -a ${PDFDIR}/${filename}.pdf -- $ADDRLIST

exit 0
