from django.shortcuts import render

def index(request):
    return render(request, 'frontend/index.html')


def default(request):

    """
    making logic
    """

    """
    with connections['default'].cursor() as cur:
        query = '''
            select *
            FROM table
            where sample = '{page}'
        '''.format(page=page)
        cur.execute(query)
        rows = cur.fetchall()
    """

    context = {}
    #context['sample_key'] = 'hello world'

    return render(request, 'frontend/default.html', context)