try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen


def internet_on():
    try:
        urlopen('http://216.58.192.142', timeout=1)
        return True
    except : 
        return False



