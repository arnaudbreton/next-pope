from django.db import models

# Create your models here.
class PopeCandidate(models.Model):
    MAX_SCORE = 4
    is_man = models.BooleanField()
    is_catholic = models.BooleanField()
    is_married = models.BooleanField()
    stay_celibate = models.BooleanField()

    def get_score(self):
        return int(self.is_man + self.is_catholic + (not self.is_married) + (not self.stay_celibate))