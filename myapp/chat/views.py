from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Conversation, Message
# Create your views here.


def index(request):
    conversation_list = Conversation.objects.all()
    output = ', '.join([c.conv_name for c in conversation_list])
    return render(request, 'conversations/index.html', {'conversation_list': conversation_list})


def detail(request, conversation_id):
    conversation = get_object_or_404(Conversation, pk=conversation_id)
    return render(request, 'conversations/detail.html', {'conversation': conversation})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#

def send(request, conversation_id):
    conversation = get_object_or_404(Conversation, pk=conversation_id)
    message_text = request.POST['sent_text']
    conversation.message_set.create(text=message_text)
    conversation.save()

    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('chat:detail', args=(conversation.id,)))



def new_conversation(request):
    new_conv_name = request.POST['conv_name']
    new_conv = Conversation(conv_name=new_conv_name)
    new_conv.save()

    return HttpResponseRedirect(reverse('chat:index'))
