from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.template.defaultfilters import length
from .models import Poll
from .models import Question
from .models import Answer

# poll_list = [
#         {
# 		'id': 1,
# 		'title': 'การสอนวิชา Web Programming',
# 		'questions': [
# 			{
# 				'text': 'อาจารย์บัณฑิตสอนน่าเบื่อไหม',
# 				'choices': [
# 					{'text': 'น่าเบื่อมาก', 'value': 1},
# 					{'text': 'ค่อนข้างน่าเบื่อ', 'value': 2},
# 					{'text': 'เฉยๆ', 'value': 3},
# 					{'text': 'ค่อนข้างสนุก', 'value': 4},
# 					{'text': 'สนุกมากๆ', 'value': 5}
# 				]
# 			},
# 			{
# 				'text': 'นักศึกษาเรียนรู้เรื่องหรือไม่',
# 				'choices': [
# 					{'text': 'ไม่รู้เรื่องเลย', 'value': 1},
# 					{'text': 'รู้เรื่องนิดหน่อย', 'value': 2},
# 					{'text': 'เฉยๆ', 'value': 3},
# 					{'text': 'เรียนรู้เรื่อง', 'value': 4},
# 					{'text': 'เรียนเข้าใจมากๆ', 'value': 5}
# 				]
# 			},
# 			{
# 				'text': 'เครื่องคอมพิวเตอร์ใช้งานดีหรือไม่',
# 				'choices': [
# 					{'text': 'เครื่องช้ามาก', 'value': 1},
# 					{'text': 'เครื่องค่อนข้างช้า', 'value': 2},
# 					{'text': 'เฉยๆ', 'value': 3},
# 					{'text': 'เครื่องเร็ว', 'value': 4},
# 					{'text': 'เครื่องเร็วมากๆ', 'value': 5}
# 				]
# 			},
#
# 		]
# 	},
#         {
# 		'id': 2,
# 		'title': 'ความยากข้อสอบ mid-term',
# 		'questions': [
# 			{
# 				'text': 'ข้อ 1',
# 				'choices': [
# 					{'text': 'ง่ายมากๆ', 'value': 1},
# 					{'text': 'ค่อนข้างง่าย', 'value': 2},
# 					{'text': 'เฉยๆ', 'value': 3},
# 					{'text': 'ค่อนข้างยาก', 'value': 4},
# 					{'text': 'ยากมากๆ', 'value': 5}
# 				]
# 			},
# 			{
# 				'text': 'ข้อ 2',
# 				'choices': [
# 					{'text': 'ง่ายมากๆ', 'value': 1},
# 					{'text': 'ค่อนข้างง่าย', 'value': 2},
# 					{'text': 'เฉยๆ', 'value': 3},
# 					{'text': 'ค่อนข้างยาก', 'value': 4},
# 					{'text': 'ยากมากๆ', 'value': 5}
# 				]
# 			},
# 			{
# 				'text': 'ข้อ 3',
# 				'choices': [
# 					{'text': 'ง่ายมากๆ', 'value': 1},
# 					{'text': 'ค่อนข้างง่าย', 'value': 2},
# 					{'text': 'เฉยๆ', 'value': 3},
# 					{'text': 'ค่อนข้างยาก', 'value': 4},
# 					{'text': 'ยากมากๆ', 'value': 5}
# 				]
# 			},
# 			{
# 				'text': 'ข้อ 4',
# 				'choices': [
# 					{'text': 'ง่ายมากๆ', 'value': 1},
# 					{'text': 'ค่อนข้างง่าย', 'value': 2},
# 					{'text': 'เฉยๆ', 'value': 3},
# 					{'text': 'ค่อนข้างยาก', 'value': 4},
# 					{'text': 'ยากมากๆ', 'value': 5}
# 				]
# 			},
# 			{
# 				'text': 'ข้อ 5',
# 				'choices': [
# 					{'text': 'ง่ายมากๆ', 'value': 1},
# 					{'text': 'ค่อนข้างง่าย', 'value': 2},
# 					{'text': 'เฉยๆ', 'value': 3},
# 					{'text': 'ค่อนข้างยาก', 'value': 4},
# 					{'text': 'ยากมากๆ', 'value': 5}
# 				]
# 			},
# 			{
# 				'text': 'ข้อ 6',
# 				'choices': [
# 					{'text': 'ง่ายมากๆ', 'value': 1},
# 					{'text': 'ค่อนข้างง่าย', 'value': 2},
# 					{'text': 'เฉยๆ', 'value': 3},
# 					{'text': 'ค่อนข้างยาก', 'value': 4},
# 					{'text': 'ยากมากๆ', 'value': 5}
# 				]
# 			},
#
# 		]
# 	},
#
#         {
# 		'id': 4,
# 		'title': 'อาหารที่ชอบ',
# 		'questions': [
# 			{
# 				'text': 'พิซซ่า',
# 				'choices': [
# 					{'text': 'ไม่ชอบเลย', 'value': 1},
# 					{'text': 'ค่อนข้างไม่ชอบ', 'value': 2},
# 					{'text': 'เฉยๆ', 'value': 3},
# 					{'text': 'ค่อนข้างชอบ', 'value': 4},
# 					{'text': 'ชอบมากๆ', 'value': 5}
# 				]
# 			},
# 			{
# 				'text': 'ไก่ทอด',
# 				'choices': [
# 					{'text': 'ไม่ชอบเลย', 'value': 1},
# 					{'text': 'ค่อนข้างไม่ชอบ', 'value': 2},
# 					{'text': 'เฉยๆ', 'value': 3},
# 					{'text': 'ค่อนข้างชอบ', 'value': 4},
# 					{'text': 'ชอบมากๆ', 'value': 5}
# 				]
# 			},
# 			{
# 				'text': 'แฮมเบอร์เกอร์',
# 				'choices': [
# 					{'text': 'ไม่ชอบเลย', 'value': 1},
# 					{'text': 'ค่อนข้างไม่ชอบ', 'value': 2},
# 					{'text': 'เฉยๆ', 'value': 3},
# 					{'text': 'ค่อนข้างชอบ', 'value': 4},
# 					{'text': 'ชอบมากๆ', 'value': 5}
# 				]
# 			},
#
# 		]
# 	},
#     ]
def index(request):
	# lab week 1
    # context = {
    #     'page_title': 'welcome to ,y poll',
    #     'poll_list': poll_list
    # }
    # return render(request,'polls/index.html',context=context)

	poll_list = Poll.objects.all()

	for poll in poll_list:
		question_count = Question.objects.filter(poll_id=poll.id).count()
		poll.question_count = question_count
	context = {
		'page_title': 'My Polls',
		'poll_list': poll_list
	}
	return render(request, template_name = 'polls/index.html', context=context)
def detail(request,id1):
	# lab week 1
    # for i in range(len(poll_list)):
    #     j = poll_list[i]["id"]
    #     if(id1 == str(j)):
    #         context = {
    #             'poll_list': poll_list[i],
	#
    #         }
	poll = Poll.objects.get(pk=id1)
            # break
    # return render(request,'polls/detail.html',context=context)

	return render(request, 'polls/detail.html', {'poll': poll})


def create(request,id):
	poll = Poll.objects.get(pk=id)
	if request.POST.get('choice'):
		post = Answer()
		post.choice = request.POST.get('choice')
		post.save()

	return render(request, 'polls/create.html', {'poll': poll})

	# else:
	# 	return render(request, 'polls/create.html', context)