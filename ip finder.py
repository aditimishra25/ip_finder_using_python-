#importing socket module
import socket

#getting hostname by socket.gethostname() method
hostname=socket.gethostname()

#getting the ip by socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)

#printing the hostname and ip_address
print(f"Hostname:{hostname}")
print(f"IP Address:{ip_address}")
#A formatted string literal or f-string is a string literal that is prefixed with 'f' or 'F'.
# These strings may contain replacement fields, which are expressions delimited by curly braces {}.
# While other string literals always have a constant value, formatted strings are really expressions evaluated at run time.

