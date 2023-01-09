import requests
import random
import string
import base64
import urllib.parse

def double_url_encode(payload):
  # Double-URL-encode the payload
  return urllib.parse.quote(urllib.parse.quote(payload))

def html_encode(payload):
  # HTML-encode the payload
  return payload.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&#x27;')

def add_leading_zeros(payload):
  # Add leading zeros to the payload
  return '0' * random.randint(1, 10) + payload

def xml_encode(payload):
  # XML-encode the payload
  return payload.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&apos;')

def unicode_escape(payload):
  # Unicode-escape the payload
  return ''.join(f'\\u{ord(c):04x}' for c in payload)

def hex_escape(payload):
  # Hex-escape the payload
  return ''.join(f'\\x{ord(c):02x}' for c in payload)

# Get the URL and parameter name from the user
url = input("Enter the URL: ")
param = input("Enter the parameter name: ")

# Set the maximum number of iterations
max_iterations = 1000

# Set the minimum length of the payload
min_length = 5

# Set the maximum length of the payload
max_length = 50

for i in range(max_iterations):
  # Generate a random payload
  payload = ''.join(random.choices(string.ascii_letters + string.digits + '<>/\\', k=random.randint(min_length, max_length)))

  # Choose a random obfuscation method
  obfuscation_method = random.choice([double_url_encode, html_encode, add_leading_zeros, xml_encode, unicode_escape, hex_escape])

  # Obfuscate the payload using the chosen method
  payload = obfuscation_method(payload)

  # Construct the full URL with the payload injected into the parameter
  test_url = url + "?" + param + "=" + payload

  # Make a request to the URL
  r = requests.get(test_url)

  # Check the response for signs of XSS
  if "XSS" in r.text:
    print("XSS found at " + test_url)
  else:
    print("No XSS found at " + test_url)
