import XSSScanner

class URLInput:
    def __init__(self):
        self.xss_scanner = XSSScanner()
    
    def take_input(self):
        url = input("Enter the URL: ")
        parameter = input("Enter the parameter: ")
        self.xss_scanner.test_xss(url, parameter)
