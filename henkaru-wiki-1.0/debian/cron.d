*/5 * * * * root /opt/wiki/bin/trafreports.py 2>&1 >/dev/null
5 2 1 * * root /opt/wiki/bin/trafreports.py prev  && /opt/wiki/bin/sendreport.sh
