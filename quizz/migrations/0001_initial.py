# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PopeCandidate'
        db.create_table(u'quizz_popecandidate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_man', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_catholic', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_married', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('stay_celibate', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'quizz', ['PopeCandidate'])


    def backwards(self, orm):
        # Deleting model 'PopeCandidate'
        db.delete_table(u'quizz_popecandidate')


    models = {
        u'quizz.popecandidate': {
            'Meta': {'object_name': 'PopeCandidate'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_catholic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_man': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_married': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'stay_celibate': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['quizz']