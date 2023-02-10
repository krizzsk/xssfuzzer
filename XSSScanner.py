import gc
from selenium import webdriver
from payload_obfuscator import PayloadObfuscator

class XSSScanner:
    def __init__(self):
        self.payload_obfuscator = PayloadObfuscator()
        self.driver = webdriver.Chrome()
    
    def test_xss(self, url, parameter):
        payloads = []
        with open("xss_payloads.txt", "r") as f:
            for line in f:
                payload = line.strip()
                payloads.append(payload)
        
        for payload in payloads:
            obfuscated_payloads = self.payload_obfuscator.obfuscate(payload)
            for obfuscated_payload in obfuscated_payloads:
                test_url = url.replace(parameter, obfuscated_payload)
                self.driver.get(test_url)
                try:
                    alert = self.driver.switch_to.alert
                    print("XSS vulnerability found with payload: ", obfuscated_payload)
                    alert.dismiss()
                except:
                    pass
                gc.collect()
        self.driver.quit()
