 
# Import modules for CGI handling 
import cgi,os,sys,cgitb,subprocess;
 
# Create instance of FieldStorage 
form = cgi.FieldStorage() 
 
# Get data from fields
interface = form.getvalue('interface');
 
# Avoid script injection escaping the user input
interface = cgi.escape(interface)
 
result=subprocess.Popen("/var/www/deneme/cgi-bin/getPacketInfo.py "+interface, stdout=subprocess.PIPE, shell=True).communicate()[0];
pre_res=result.split(",");
rx_bytes=pre_res[0];
tx_bytes=pre_res[1];
 
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<body>"
print "<h3>Secilen Interface: " + interface  + "</h3>"
print "<h3>Alinan Byte: " + rx_bytes  + "</h3>"
print "<h3>Gonderilen Byte: " + tx_bytes  + "</h3>"
print "</body>"
print "</html>"