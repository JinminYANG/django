from django.contrib.auth.models import User
from django.db import models
import datetime
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class DBfCompany(models.Model):
    company_seq = models.IntegerField(primary_key=True)  # external Company PK
    company_name = models.CharField(max_length=50, blank=True, null=True)
    view_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return '{0}({1})'.format(self.company_name, self.company_seq)

    def __unicode__(self):
        return '{0}({1})'.format(self.company_name, self.company_seq)


class UpdateFromDB(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  # 동기화 시도 시간
    company = models.DateTimeField(null=True, blank=True)  # 동기화 데이터 마지막 시간
    user = models.DateTimeField(null=True, blank=True)  # 동기화 데이터 마지막 시간


class Company(models.Model):
    # mapping
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # 인증 모델과 연결

    # company_seq = models.ForeignKey(DBfCompany, on_delete=models.PROTECT)  # DBfCompany PK
    '''
    지금 이거때문에 계속 에러나는데 왜냐하면 기존에 내가 만들어놓은 테이블이 있었는데 그 안에 필드를 새로 추가하는 경우
    기존에 테이블은 새로 추가하는 필드에 대한 데이터가 없기 때문에 default 값이나 이런거를 통해 처리를 해야하는데 
    sequence의 default를 뭘로 해야할지 모르겠다..
    '''

    # 추가 정보
    name = models.CharField(max_length=200, default='noname_company')

    # 관리 정보
    is_active = models.BooleanField(default=False)  # 계정 활성화 여부
    created_at = models.DateTimeField(auto_now_add=True)  # 계정 생성일
    updated_at = models.DateTimeField(auto_now=True)  # 계정 수정일

    is_updating = models.BooleanField(default=False)  # 업데이트 중
    statistics_updated_at = models.DateTimeField()  # 통계 정보 수정일
    member_updated_at = models.DateTimeField()  # 회원 정보 수정일
    coupon_updated_at = models.DateTimeField()  # 구독권 정보 수정일

    def __str__(self):
        return '{0}({1})'.format(self.name, self.user)

    def __unicode__(self):
        return '{0}({1})'.format(self.name, self.user)


class Statistics(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    statistics_month = models.DateTimeField()  # 통계 목표 기간 (월단위)

    # stat from tb
    sum_member_count = models.IntegerField(blank=True, null=True)
    avg_read_book_count = models.IntegerField(blank=True, null=True)
    min_read_book_count = models.IntegerField(blank=True, null=True)
    max_read_book_count = models.IntegerField(blank=True, null=True)
    sum_read_book_count = models.IntegerField(blank=True, null=True)
    avg_read_book_time = models.IntegerField(blank=True, null=True)
    min_read_book_time = models.IntegerField(blank=True, null=True)
    max_read_book_time = models.IntegerField(blank=True, null=True)
    sum_read_book_time = models.IntegerField(blank=True, null=True)
    min_read_book_percent = models.IntegerField(blank=True, null=True)
    max_read_book_percent = models.IntegerField(blank=True, null=True)
    sum_read_book_percent = models.IntegerField(blank=True, null=True)
    avg_read_book_percent = models.IntegerField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    reg_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{0}[{1}]'.format(self.company, self.statistics_month.strftime('%Y-%m'))

    def __unicode__(self):
        return '{0}[{1}]'.format(self.company, self.statistics_month.strftime('%Y-%m'))


class Member(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    member_id = models.CharField(max_length=200, default='noname_id', null=True)
    coupon_id = models.CharField(max_length=200, default='coupon_id', null=True)
    mem_seq = models.IntegerField(null=True)

    last_login = models.DateTimeField(null=True, blank=True)
    total_read_books = models.IntegerField(null=True)

    def __str__(self):
        return '{0}({1})'.format(self.member_id, self.company)

    def __unicode__(self):
        return '{0}({1})'.format(self.member_id, self.company)


class StatisticsMember(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    statistics_month = models.DateTimeField()  # 통계 목표 기간 (월단위)

    read_book_count = models.IntegerField(blank=True, null=True)

    avg_read_book_time = models.IntegerField(blank=True, null=True)
    sum_read_book_time = models.IntegerField(blank=True, null=True)

    min_read_book_percent = models.IntegerField(blank=True, null=True)
    max_read_book_percent = models.IntegerField(blank=True, null=True)
    sum_read_book_percent = models.IntegerField(blank=True, null=True)
    avg_read_book_percent = models.IntegerField(blank=True, null=True)

    update_date = models.DateTimeField(blank=True, null=True)
    reg_date = models.DateTimeField(blank=True, null=True)


class StatisticsBestBook(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    statistics_month = models.DateTimeField()  # 통계 목표 기간 (월단위)
    book_seq = models.IntegerField()
    book_name = models.CharField(max_length=100, blank=True, null=True)

    read_book_count = models.IntegerField(blank=True, null=True)

    avg_read_book_time = models.IntegerField(blank=True, null=True)
    min_read_book_time = models.IntegerField(blank=True, null=True)
    max_read_book_time = models.IntegerField(blank=True, null=True)
    sum_read_book_time = models.IntegerField(blank=True, null=True)

    avg_read_book_percent = models.IntegerField(blank=True, null=True)
    min_read_book_percent = models.IntegerField(blank=True, null=True)
    max_read_book_percent = models.IntegerField(blank=True, null=True)
    sum_read_book_percent = models.IntegerField(blank=True, null=True)

    update_date = models.DateTimeField(blank=True, null=True)
    reg_date = models.DateTimeField(blank=True, null=True)


class StatisticsBestCategory(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    statistics_month = models.DateTimeField()  # 통계 목표 기간 (월단위)
    category_seq = models.IntegerField()
    category_depth = models.IntegerField(blank=True, null=True)
    category_name = models.CharField(max_length=100, blank=True, null=True)

    read_book_count = models.IntegerField(blank=True, null=True)

    read_book_percent = models.IntegerField(blank=True, null=True)
    read_book_percent_detail = models.FloatField(blank=True, null=True)

    avg_read_book_time = models.IntegerField(blank=True, null=True)
    min_read_book_time = models.IntegerField(blank=True, null=True)
    max_read_book_time = models.IntegerField(blank=True, null=True)
    sum_read_book_time = models.IntegerField(blank=True, null=True)

    avg_read_book_percent = models.IntegerField(blank=True, null=True)
    min_read_book_percent = models.IntegerField(blank=True, null=True)
    max_read_book_percent = models.IntegerField(blank=True, null=True)
    sum_read_book_percent = models.IntegerField(blank=True, null=True)

    update_date = models.DateTimeField(blank=True, null=True)
    reg_date = models.DateTimeField(blank=True, null=True)


class CouponMaster(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    coupon_master_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return '{0}({1})'.format(self.title, self.company)

    def __unicode__(self):
        return '{0}({1})'.format(self.title, self.company)


class CouponPublish(models.Model):
    coupon_id = models.CharField(max_length=200, default='coupon_id')
    coupon_master = models.ForeignKey(CouponMaster, on_delete=models.CASCADE)
    member_id = models.CharField(max_length=200, blank=True, null=True)

    coupon_use_yn = models.CharField(max_length=1, blank=True, null=True)

    reg_date = models.DateTimeField(blank=True, null=True)
    use_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{0}({1})'.format(self.coupon_id, self.coupon_master.title)

    def __unicode__(self):
        return '{0}({1})'.format(self.coupon_id, self.coupon_master.title)
