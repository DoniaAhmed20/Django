# Create your views here.
# def index(request):
#     return HttpResponse("Book Store")

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

# Create your views here.
def index(request):
   
    # return HttpResponse("Book Store")
    return render(request, 'main/base_layout.html')



task_list = [
    {
        'index': 0,
        'id': 1,
        'name': ' A TIME TO KILL ',
        'priority': 1,
        'description': "This one is from 3:3 in the Ecclesiastes, again part of the Old Testament",
    },
    {
        'index': 1,
        'id': 2,
        'name': ' THE HOUSE OF MIRTH ',
        'priority': 4,
        'description': "The heart of the wise is in the house of mourning; but the heart of fools is in the house of mirth",
    },
    {
        'index': 2,
        'id': 3,
        'name': 'THE SUN ALSO RISES',
        'priority': 2,
        'description': "The sun also ariseth, and the sun goeth down, and hasteth to his place where he arose",
    },
    {
        'index': 3,
        'id': 4,
        'name': 'BRAVE NEW WORLD',
        'priority': 2,
        'description': "This is possibly the most famous book to take its title from a Shakespeare play – in this case, The Tempest",
    },
]


def _get_task(task_id):
    for task in task_list:
        if 'id' in task and task['id'] == task_id:
            return task
    return None
    
def book_store_list(request):
    my_context = {'taks_list': task_list}
    return render(request, 'book_store/book_store_list.html', context=my_context)

def book_store_detail(request, *args, **kwrgs):
    task_id = kwrgs.get('task_id')
    task_object = _get_task(task_id)
    my_context = {
        'task_id': task_object.get('id'),
        'task_name': task_object.get('name'),
        'task_priority': task_object.get('priority'),
        'task_description': task_object.get('description')
    }

    return render(request, 'book_store/book_store_details.html', context=my_context)


def book_store_delete(request, **kwargs):
    task_id = kwargs.get('task_id')
    task_object = _get_task(task_id)
    if task_list:
        task_list.remove(task_object)
    return redirect('book_store:book_store-list')   

def book_store_update(request, **kwargs):
    task_id = kwargs.get('task_id')
    task_object = _get_task(task_id)
    for task in task_list:
        if task == task_object:
            task['name'] = f"Update {task_object['name']}"
            
    return redirect('book_store:book_store-list') 
