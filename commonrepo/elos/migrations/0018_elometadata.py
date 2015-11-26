# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0017_reusabilitytree'),
    ]

    operations = [
        migrations.CreateModel(
            name='ELOMetadata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('General_identifier', models.CharField(max_length=255, verbose_name='General-identifier', blank=True)),
                ('General_title', models.CharField(max_length=255, verbose_name='General-title', blank=True)),
                ('General_language', models.CharField(max_length=255, verbose_name='General-language', blank=True)),
                ('General_description', models.CharField(max_length=255, verbose_name='General-description', blank=True)),
                ('General_keyword', models.CharField(max_length=255, verbose_name='General-keyword', blank=True)),
                ('General_coverage', models.CharField(max_length=255, verbose_name='General-coverage', blank=True)),
                ('General_structure', models.CharField(max_length=255, verbose_name='General-structure', blank=True)),
                ('General_aggregationLevel', models.CharField(max_length=255, verbose_name='General-aggregationLevel', blank=True)),
                ('LifeCycle_version', models.CharField(max_length=255, verbose_name='LifeCycle-version', blank=True)),
                ('LifeCycle_status', models.CharField(max_length=255, verbose_name='LifeCycle-status', blank=True)),
                ('LifeCycle_contribute', models.CharField(max_length=255, verbose_name='LifeCycle-contribute', blank=True)),
                ('Meta_metadata_identifier', models.CharField(max_length=255, verbose_name='Meta-metadata-identifier', blank=True)),
                ('Meta_metadata_contribute', models.CharField(max_length=255, verbose_name='Meta-metadata-contribute', blank=True)),
                ('Meta_metadata_metadataSchema', models.CharField(max_length=255, verbose_name='Meta-metadata-metadataSchema', blank=True)),
                ('Meta_metadata_language', models.CharField(max_length=255, verbose_name='Meta-metadata-language', blank=True)),
                ('Technical_format', models.CharField(max_length=255, verbose_name='Technical-format', blank=True)),
                ('Technical_size', models.CharField(max_length=255, verbose_name='Technical-size', blank=True)),
                ('Technical_location', models.CharField(max_length=255, verbose_name='Technical-location', blank=True)),
                ('Technical_requirement', models.CharField(max_length=255, verbose_name='Technical-requirement', blank=True)),
                ('Technical_installationRemarks', models.CharField(max_length=255, verbose_name='Technical-installationRemarks', blank=True)),
                ('Technical_otherPlatformRequirements', models.CharField(max_length=255, verbose_name='Technical-otherPlatformRequirements', blank=True)),
                ('Technical_duration', models.CharField(max_length=255, verbose_name='Technical-duration', blank=True)),
                ('Educational_interactivityType', models.CharField(max_length=255, verbose_name='Educational-interactivityType', blank=True)),
                ('Educational_learningResourceType', models.CharField(max_length=255, verbose_name='Educational-learningResourceType', blank=True)),
                ('Educational_interactivityLevel', models.CharField(max_length=255, verbose_name='Educational-interactivityLevel', blank=True)),
                ('Educational_semanticDensity', models.CharField(max_length=255, verbose_name='Educational-semanticDensity', blank=True)),
                ('Educational_intendedEndUserRole', models.CharField(max_length=255, verbose_name='Educational-intendedEndUserRole', blank=True)),
                ('Educational_context', models.CharField(max_length=255, verbose_name='Educational-context', blank=True)),
                ('Educational_typicalAgeRange', models.CharField(max_length=255, verbose_name='Educational-typicalAgeRange', blank=True)),
                ('Educational_difficulty', models.CharField(max_length=255, verbose_name='Educational-difficulty', blank=True)),
                ('Educational_typicalLearningTime', models.CharField(max_length=255, verbose_name='Educational-typicalLearningTime', blank=True)),
                ('Educational_description', models.CharField(max_length=255, verbose_name='Educational-description', blank=True)),
                ('Educational_language', models.CharField(max_length=255, verbose_name='Educational-language', blank=True)),
                ('Rights_cost', models.CharField(max_length=255, verbose_name='Rights-cost', blank=True)),
                ('Rights_copyrightAndOtherRestrictions', models.CharField(max_length=255, verbose_name='Rights-copyrightAndOtherRestrictions', blank=True)),
                ('Rights_description', models.CharField(max_length=255, verbose_name='Rights-description', blank=True)),
                ('Relation_kind', models.CharField(max_length=255, verbose_name='Relation-kind', blank=True)),
                ('Relation_resource', models.CharField(max_length=255, verbose_name='Relation-resource', blank=True)),
                ('Annotation_entity', models.CharField(max_length=255, verbose_name='Annotation-entity', blank=True)),
                ('Annotation_date', models.CharField(max_length=255, verbose_name='Annotation-date', blank=True)),
                ('Annotation_description', models.CharField(max_length=255, verbose_name='Annotation-description', blank=True)),
                ('Classification_purpose', models.CharField(max_length=255, verbose_name='Classification-purpose', blank=True)),
                ('Classification_taxonPath', models.CharField(max_length=255, verbose_name='Classification-taxonPath', blank=True)),
                ('Classification_description', models.CharField(max_length=255, verbose_name='Classification-description', blank=True)),
                ('Classification_keyword', models.CharField(max_length=255, verbose_name='Classification-keyword', blank=True)),
            ],
        ),
    ]
