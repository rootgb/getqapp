from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from quickfeedback.models import Event, Question, Response

def index(request):
	return render_to_response('index.html', context_instance = RequestContext(request))

def register(request):
    
    context = RequestContext(request)

    registered = False

   
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

   
        if user_form.is_valid() and profile_form.is_valid():
            
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            registered = True

        
        else:
            print user_form.errors, profile_form.errors

    
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

   
    return render_to_response(
            'register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)
			

def user_login(request):
  
    context = RequestContext(request)

   
    if request.method == 'POST':
       
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        
        if user:
           
            if user.is_active:
                
                login(request, user)
                return HttpResponseRedirect('/')
            else:
               
                return HttpResponse("Your account is disabled.")
        else:
            
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    
    else:
        
        return render_to_response('login.html', {}, context)

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    return HttpResponseRedirect('/')
	
@login_required
def createq(request):
	if request.method == 'POST':
		c = {}
		c.update(csrf(request))
		form = createqform(request.POST)
		if form.is_valid():
			ques = Question(q_1 = form.cleaned_data['q1'] , q_2 = form.cleaned_data['q2'] , q_3 = form.cleaned_data['q3'])
			ques.save()
			
			ev = Event(code = form.cleaned_data['slug'], name = form.cleaned_data['name'])
			ev.save()
			
			
			
			return render_to_response('thanks.html')
			
	else:
		form = createqform()
		return render_to_response('createq.html', {'form':form}, context_instance= RequestContext(request))

def qform(request,qid):
    if request.method == 'POST':
        if 'a_1' in request.POST or 'a_2' in request.POST or 'a_3' in request.POST:
            a_1=''
            a_2=''
            a_3=''
            try:
                if 'a_1' in request.POST:
                    a_1= request.POST['a_1']
                if 'a_2' in request.POST:
                    a_2= request.POST['a_2']
                if 'a_3' in request.POST:
                    a_3= request.POST['a_3']
                event = get_object_or_404(Event, code=qid)
                questions = event.question_set.get()
                res= Response(event = event, a_1=a_1,a_2=a_2,a_3=a_3)
                res.save()
                c={}
                return render_to_response('thanks.html',c)
            except Exception, e:
                event = get_object_or_404(Event, code=qid)
                questions = event.question_set.get()
                c= RequestContext(request, {'error':"Incorrect submission, Please fill question 1 & 2. Thanks",'q_1': questions.q_1, 'q_2': questions.q_2, 'q_3': questions.q_3, 'event_name': questions.event.name, 'event_code': questions.event.code })
                return render_to_response('qform.html',c)
            else:
                pass
            finally:
                pass
        else:
            event = get_object_or_404(Event, code=qid)
            questions = event.question_set.get()
            c= RequestContext(request, {'error':"Please fill question 1 & 2. Thanks :) ",'q_1': questions.q_1, 'q_2': questions.q_2, 'q_3': questions.q_3, 'event_name': questions.event.name, 'event_code': questions.event.code })
            return render_to_response('qform.html',c)

    else:
        event = get_object_or_404(Event, code=qid)
        questions = event.question_set.get()
        c= RequestContext(request, {'q_1': questions.q_1, 'q_2': questions.q_2, 'q_3': questions.q_3, 'event_name': questions.event.name, 'event_code': questions.event.code })
        return render_to_response('qform.html',c)


