# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Transaction'
        db.create_table(u'users_transaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('offer_from', self.gf('django.db.models.fields.related.ForeignKey')(related_name='offer_from', to=orm['users.CustomUser'])),
            ('offer_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='offer_to', to=orm['users.CustomUser'])),
            ('offer_about', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crops.Crop'])),
            ('quoted_price', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('status', self.gf('django.db.models.fields.CharField')(default='Waiting', max_length=50)),
        ))
        db.send_create_signal(u'users', ['Transaction'])

        # Adding model 'TransactionMetaInfo'
        db.create_table(u'users_transactionmetainfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('transaction', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['users.Transaction'], unique=True)),
            ('offer_from_feedback', self.gf('django.db.models.fields.IntegerField')()),
            ('offer_to_feedback', self.gf('django.db.models.fields.IntegerField')()),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'users', ['TransactionMetaInfo'])


    def backwards(self, orm):
        # Deleting model 'Transaction'
        db.delete_table(u'users_transaction')

        # Deleting model 'TransactionMetaInfo'
        db.delete_table(u'users_transactionmetainfo')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'crops.crop': {
            'Meta': {'object_name': 'Crop'},
            'expiry': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.CustomUser']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '3'}),
            'type_crop': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'users.customuser': {
            'Meta': {'object_name': 'CustomUser'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'payment_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'primary_occupation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'reputation': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'users.transaction': {
            'Meta': {'object_name': 'Transaction'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'offer_about': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crops.Crop']"}),
            'offer_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'offer_from'", 'to': u"orm['users.CustomUser']"}),
            'offer_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'offer_to'", 'to': u"orm['users.CustomUser']"}),
            'quoted_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Waiting'", 'max_length': '50'})
        },
        u'users.transactionmetainfo': {
            'Meta': {'object_name': 'TransactionMetaInfo'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'offer_from_feedback': ('django.db.models.fields.IntegerField', [], {}),
            'offer_to_feedback': ('django.db.models.fields.IntegerField', [], {}),
            'transaction': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['users.Transaction']", 'unique': 'True'})
        }
    }

    complete_apps = ['users']