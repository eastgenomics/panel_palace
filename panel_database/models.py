from django.db import models

# Create your models here.


class Test(models.Model):
    test_id = models.CharField(max_length=100)
    name = models.TextField(max_length=200)
    method = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    gemini_name = models.CharField(max_length=200)

    class Meta:
        db_table = "test"


class TestPanel(models.Model):
    test = models.ForeignKey(Test, on_delete=models.DO_NOTHING)
    panel = models.ForeignKey("Panel", on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "test_panel"


class TestGene(models.Model):
    test = models.ForeignKey(Test, on_delete=models.DO_NOTHING)
    gene = models.ForeignKey("Gene", on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "test_gene"


class Panel(models.Model):
    panelapp_id = models.IntegerField()
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    signedoff = models.CharField(max_length=100)
    is_superpanel = models.BooleanField()

    class Meta:
        db_table = "panel"


class Superpanel(models.Model):
    superpanel = models.ForeignKey(
        "Panel", on_delete=models.DO_NOTHING, related_name="superpanel"
    )
    panel = models.ForeignKey(
        "Panel", on_delete=models.DO_NOTHING, related_name="panel"
    )

    class Meta:
        db_table = "superpanel"


class PanelStr(models.Model):
    panel = models.ForeignKey(Panel, on_delete=models.DO_NOTHING)
    str = models.ForeignKey("Str", on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "panel_str"


class Str(models.Model):
    gene = models.ForeignKey("Gene", on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    repeated_sequence = models.CharField(max_length=100)
    nb_repeats = models.IntegerField()
    nb_pathogenic_repeats = models.IntegerField()

    class Meta:
        db_table = "str"


class RegionStr(models.Model):
    str = models.ForeignKey("Str", on_delete=models.DO_NOTHING)
    region = models.ForeignKey("Region", on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "region_str"


class PanelCnv(models.Model):
    panel = models.ForeignKey(Panel, on_delete=models.DO_NOTHING)
    cnv = models.ForeignKey("Cnv", on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "panel_cnv"


class Cnv(models.Model):
    choices = (
        ("cnv_gain", "cnv_gain"),
        ("cnv_loss", "cnv_loss")
    )
    name = models.CharField(max_length=100)
    variant_type = models.CharField(max_length=100, choices=choices)

    class Meta:
        db_table = "cnv"


class RegionCnv(models.Model):
    cnv = models.ForeignKey("Cnv", on_delete=models.DO_NOTHING)
    region = models.ForeignKey("Region", on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "region_cnv"


class PanelGene(models.Model):
    panel = models.ForeignKey(Panel, on_delete=models.DO_NOTHING)
    gene = models.ForeignKey("Gene", on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "panel_gene"


class Gene(models.Model): 
    symbol = models.CharField(max_length=100)
    clinical_transcript = models.ForeignKey(
        "Transcript", on_delete=models.DO_NOTHING, null=True,
        related_name="clinical_transcript"
    )

    class Meta:
        db_table = "gene"


class Transcript(models.Model):
    refseq = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    gene = models.ForeignKey(Gene, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "transcript"


class Exon(models.Model):
    number = models.IntegerField()
    transcript = models.ForeignKey(Transcript, on_delete=models.DO_NOTHING)
    region = models.ForeignKey("Region", on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "exon"


class Region(models.Model):
    choices = [(f"{i}", f"{i}") for i in range(1, 23)]
    choices.append(("X", "X"))
    choices.append(("Y", "Y"))
    choices = tuple(choices)

    chrom = models.CharField(max_length=100, choices=choices)
    start = models.IntegerField()
    end = models.IntegerField()
    reference = models.ForeignKey("Reference", on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "region"


class Reference(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "reference"
