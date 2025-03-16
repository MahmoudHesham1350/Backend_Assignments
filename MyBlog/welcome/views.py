from django.shortcuts import render

# Create your views here.

def welcome(request):
    if request.method == 'GET':
        return render(request, 'welcome/welcome.html')
    
def about(request):
    if request.method == 'GET':  
        return render(request, 'welcome/about.html')
    
def features(request):
    if request.method == 'GET':
        list_features = [
            'Feature 1: This is the first feature.',
            'Feature 2: This is the second feature.',
            'Feature 3: This is the third feature.',
            'Feature 4: This is the fourth feature.',
            'Feature 5: This is the fifth feature.',
            'Feature 6: This is the sixth feature.',
            'Feature 7: This is the seventh feature.',
            'Feature 8: This is the eighth feature.',
            'Feature 9: This is the ninth feature.',
            'Feature 10: This is the tenth feature.',
        ]
        return render(request, 'welcome/features.html', {'features': list_features})