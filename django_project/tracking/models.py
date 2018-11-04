from django.db import models


class HTTPRequestInfo(models.Model):
    ip_address = models.CharField(max_length=100)
    user_agent = models.CharField(max_length=200)
    referer = models.CharField('유입 경로', max_length=300, blank=True)
    visits = models.IntegerField('방문 횟수', default=1)
    created_at = models.DateTimeField('생성 시간', auto_now_add=True)
    updated_at = models.DateTimeField('최종 방문 시간', auto_now=True)

    class Meta:
        verbose_name = 'Request 정보'
        verbose_name_plural = 'Request 정보(들)'

    def __str__(self):
        return self.ip_address

    def increase_visits(self):
        self.visits += 1
        self.save()


class Redirection(models.Model):
    url = models.URLField()
    created_at = models.DateTimeField('생성 시간', auto_now_add=True)
    updated_at = models.DateTimeField('수정 시간', auto_now=True)

    class Meta:
        verbose_name = '리다이렉트 경로'
        verbose_name_plural = '리다이렉트 경로(들)'

    def __str__(self):
        return self.url
