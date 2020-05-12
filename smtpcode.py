import smtplib 

sender="sender@gmail.com"
receiver="receiver@gmail.com" 
password="password"
smtpserver=smtplib.SMTP("smtp.gmail.com",587) 
smtpserver.ehlo()
smtpserver.starttls
smtpserver.ehlo
smtpserver.login(sender,password)
msg="\subject:demo"
smtpserver.sendmail(sender,receiver,msg)
print("sent")
smtpserver.close()
#do not forget to turn on less secure apps for working if this 
