import urllib.parse
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
# https://app.screenshotapi.net/
# @param {String} $token - String containing your API Key
# @param {String} $url - Encoded URI string container the URI you're targeting
# @param {Integer} $width - Integer indicating the width of your target render
# @param {Integer} $height - Integer indicating the height of your target render
# @param {String} $output - String specifying the output format, "image" or "json"
token = "G7EQTZW-W01MX0J-JMK0BBD-8MPH9YR"
target = "https://google.com"
url = urllib.parse.quote_plus(target)
width = 1920
height = 1080
output = "image"

# Construct the query params and URL
query = "https://shot.screenshotapi.net/screenshot"
query += "?token=%s&url=%s&width=%d&height=%d&output=%s" % (token, url, width, height, output)

# Call the API
try:
    urllib.request.urlretrieve(query, "./Screenshots/screenshot.png")
except Exception as ex:
    print('Exception:', ex)

