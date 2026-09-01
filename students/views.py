from django.shortcuts import render

def student_list(request):
    # Just render the HTML file directly without talking to the database
    return render(request, 'students/list.html')