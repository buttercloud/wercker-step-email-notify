import smtplib
import sys

if len(sys.argv) < 8 :
  print 'There should be 8 arguments'
  sys.exit(1)

fromaddr = str(sys.argv[1])
toaddrs = str(sys.argv[2])
subject  = str(sys.argv[3])
body  = str(sys.argv[4])
username  = str(sys.argv[5])
password  = str(sys.argv[6])
host  = str(sys.argv[7])

msg = MIMEText(body)
msg["From"] = fromaddr
msg["To"] = toaddrs
msg["Subject"] = subject
server = smtplib.SMTP(host)
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg.as_string())
server.quit()
