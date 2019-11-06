from django.shortcuts import render
from django.http import HttpResponse # create a response to a URL request 



# Create your views here.

def homePageView(request):
    ''' This function will respond to an HTTP request and return an HttpRequest object.'''

  

    s = '''
<html>
<head> 
    <title>Hello,world!</title>
</head>
<body>
<h1>Hello,world! </h1>
Welcome to our first Django web application! 
<p> 

</body>
</html>
    '''
    return HttpResponse(s)