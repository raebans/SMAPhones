class Staff(model.Models):
    extension_number = models.IntegerField()
    staff_name = models.Charfield(max_length=20)

class Call(model.Models):
    call_type = models.boolean(
        ('I', 'Incoming'),
        ('O', 'Outgoung'),
        # transfer?
    )
    call_duration = models.DecimalField()
    call_date = models.DateTimeField()
    #something to link the call to the person
    #caller id?
