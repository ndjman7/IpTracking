from django.db import models


class TrackingGroup(models.Model):
    name = models.CharField('팀 이름', max_length=100)
    description = models.TextField('설명', blank=True)
    entry_name = models.CharField(verbose_name='유입 경로 이름', max_length=100, unique=True)
    redirect_url = models.URLField(verbose_name='이동시킬 경로')

    class Meta:
        verbose_name = '팀'
        verbose_name_plural = '팀(들)'

    def __str__(self):
        return self.name


class HTTPRequestInfo(models.Model):
    group = models.OneToOneField(TrackingGroup, verbose_name='팀', on_delete=models.CASCADE, null=True)
    ip_address = models.CharField(max_length=100)
    user_agent = models.CharField(max_length=200)
    referer = models.CharField('유입 경로', max_length=300, blank=True)
    memo = models.TextField('메모', blank=True)
    created_at = models.DateTimeField('생성 시간', auto_now_add=True)
    updated_at = models.DateTimeField('최종 방문 시간', auto_now=True)

    class Meta:
        verbose_name = 'Request 정보'
        verbose_name_plural = 'Request 정보(들)'

    def __str__(self):
        return self.ip_address


class Redirection(models.Model):
    url = models.URLField()
    created_at = models.DateTimeField('생성 시간', auto_now_add=True)
    updated_at = models.DateTimeField('수정 시간', auto_now=True)

    class Meta:
        verbose_name = '리다이렉트 경로'
        verbose_name_plural = '리다이렉트 경로(들)'

    def __str__(self):
        return self.url
