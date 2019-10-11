from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from OnlinelabApp.models import ScoreTable, DetailScore
import json


def hello(request):
    print("test success")
    return HttpResponse("Hello world14!")


@csrf_exempt
def login(request):
    print("test success")
    return HttpResponse(" token: super_admin")


@csrf_exempt
def userinfo(request):
    print("user info")
    return HttpResponse("super_admin")


@csrf_exempt
def message_count(request):
    print("messagecount")
    return HttpResponse(3)

@csrf_exempt
def save_error_logger(request):
    print("save_error_logger")
    return HttpResponse("success")


# 保存详细得分数据
def insert_detail_score(solution_name, score_list):
    for single_item in score_list:
        score = single_item['score']
        index = single_item['index']
        print(solution_name)

        detail_score = DetailScore(solution_name=solution_name, score=score, seq=index)
        detail_score.save()
    return True


# 计算总得分
def compute_total_score(score_list):
    return 80


@csrf_exempt
# 写入数据库
def post_score_table(request):
    if request.POST:
        data = json.loads(request.body.decode('utf-8'))
        score_list = data['score_list']
        company_name = data['company_name']

        solution_name = data['solution_name']
        judges = data['user_name']
        date = data['time']
        business_type = data['business_type']
        industry_type = data['industry_type']
        total_score = compute_total_score(score_list)

        score_table = ScoreTable(solution_name=solution_name, company_name=company_name, judges=judges, date=date,
                   business_type=business_type, industry_type=industry_type, total_score=total_score)
        score_table.save()
        # 插入详细得分信息
        insert_detail_score(score_table, score_list)

    return HttpResponse("success")


# 获取全部评分表格信息
# {}
def get_score_table(request):
    score_list = ScoreTable.objects.all()
    data_list = []
    for single_score in score_list:
        single_data = {'company_name': single_score.company_name, 'solution_name':  single_score.solution_name,
                         'business_type': single_score.business_type, 'industry_type': single_score.industry_type,
                         'user_name': single_score.judges, 'time': single_score.date, 'total_score': single_score.total_score}
        data_list.append(single_data)

    return HttpResponse(json.dumps(data_list))
