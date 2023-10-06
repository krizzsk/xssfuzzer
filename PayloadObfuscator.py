import urllib.parse

class PayloadObfuscator:
    def obfuscate(self, payload):
        double_encoded = urllib.parse.quote(urllib.parse.quote(payload))
        html_encoded = payload.encode("ascii", "xmlcharrefreplace").decode("ascii")
        leading_zeros = "0" * 100 + payload
        unicode_escaped = payload.encode("unicode-escape").decode("utf-8")
        hex_escaped = payload.encode("utf-8").hex()

        return [double_encoded, html_encoded, leading_zeros, unicode_escaped, hex_escaped]
