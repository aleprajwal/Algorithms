from DSA.Authentication import Authentication

def testAuthentication():
    username, password = ["admin", "admin123"]
    authentication = Authentication(username, password)
    assert authentication.authentication() == True