from django.db import models

# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=20)
    #lname = models.CharField(max_length=20)
    uname = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20, default=None, null=True, blank=True)
    address1 = models.CharField(max_length=20, default=None, null=True, blank=True)
    landmark = models.CharField(max_length=20, default=None, null=True, blank=True)
    city = models.CharField(max_length=20, default=None, null=True, blank=True)
    state = models.CharField(max_length=20, default=None, null=True, blank=True)
    pin = models.CharField(max_length=20, default=None, null=True, blank=True)
    bankName = models.CharField(default=None, null=True, max_length=50, blank=True)
    accountNumber = models.CharField(default=None, null=True, max_length=40, blank=True)

    def __str__(self):
        return str(self.id) + " " + self.name


class Seller(models.Model):
    name = models.CharField(max_length=20)
    uname = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(default=None, null=True, max_length=15, blank=True)
    address = models.CharField(default=None, null=True, max_length=50, blank=True)
    city = models.CharField(default=None, null=True, max_length=50, blank=True)
    bankName = models.CharField(default=None, null=True, max_length=28, blank=True)
    ifscCode = models.CharField(default=None, null=True, max_length=28, blank=True)
    accountNumber = models.CharField(default=None, null=True, max_length=28, blank=True)
    landmark = models.CharField(default=None, null=True, max_length=28, blank=True)
    state = models.CharField(default=None, null=True, max_length=28, blank=True)
    pin = models.CharField(default=None, null=True, max_length=28, blank=True)


    def __str__(self):
        return str(self.id) + " " + self.name


class FrozenFoods(models.Model):
    name = models.CharField(max_length=50)
    cat=models.CharField(default='FrozenFoods', max_length=20)
    desc = models.TextField()
    img1 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img2 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img3 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    basePrice = models.IntegerField()
    discount = models.IntegerField(default=0, null=True, blank=True)
    finalPrice = models.IntegerField()
    size = models.IntegerField(default=0, null=True, blank=True)
    quantity = models.IntegerField(default=0,null=True, blank=True)
    seller_details = models.ForeignKey(Seller, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id) + " " + self.name


class Bakery(models.Model):
    name = models.CharField(max_length=50)
    cat=models.CharField(default='Bakery', max_length=20)
    desc = models.TextField()
    img1 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img2 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img3 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    basePrice = models.IntegerField()
    discount = models.IntegerField(default=0, null=True, blank=True)
    finalPrice = models.IntegerField()
    size = models.IntegerField(default=0, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    seller_details = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + self.name


class Pulses(models.Model):
    name = models.CharField(max_length=50)
    cat=models.CharField(default='Pulses', max_length=20)
    desc = models.TextField()
    img1 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img2 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img3 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    basePrice = models.IntegerField()
    discount = models.IntegerField(default=0, null=True, blank=True)
    finalPrice = models.IntegerField()
    size = models.IntegerField(default=0, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    seller_details = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + self.name


class Spices(models.Model):
    name = models.CharField(max_length=50)
    cat=models.CharField(default='Spices', max_length=20)
    basePrice = models.IntegerField()
    discount = models.IntegerField(default=0, null=True, blank=True)
    finalPrice = models.IntegerField()
    desc = models.TextField()
    img1 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img2 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img3 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    size = models.IntegerField(default=0, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    seller_details=models.ForeignKey(Seller,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + self.name


class Vegetables(models.Model):
    name= models.CharField(max_length=50)
    cat=models.CharField(default='Vegetables', max_length=20)
    basePrice = models.IntegerField()
    discount = models.IntegerField(default=0, null=True, blank=True)
    finalPrice = models.IntegerField()
    desc = models.TextField()
    seller_details=models.ForeignKey(Seller, on_delete=models.CASCADE)
    img1=models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img2=models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img3=models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    size = models.IntegerField(default=0, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return str(self.id) + " " + self.name


class Snacks(models.Model):
    name = models.CharField(max_length=50)
    cat=models.CharField(default='Snacks', max_length=20)
    basePrice = models.IntegerField()
    discount = models.IntegerField(default=0, null=True, blank=True)
    finalPrice = models.IntegerField()
    desc = models.TextField()
    img1 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img2 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img3 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    size = models.IntegerField(default=0, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    seller_details = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + self.name


class Fruits(models.Model):
    name= models.CharField(max_length=50)
    cat=models.CharField(default='Fruits', max_length=20)
    basePrice = models.IntegerField()
    discount = models.IntegerField(default=0, null=True, blank=True)
    finalPrice = models.IntegerField()
    desc = models.TextField()
    seller_details=models.ForeignKey(Seller, on_delete=models.CASCADE)
    size = models.IntegerField(default=0, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    img1=models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img2=models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img3=models.ImageField(upload_to='images/', default=None, blank=True, null=True)

    def __str__(self):
        return str(self.id) + " " + self.name


class Beverages(models.Model):
    name = models.CharField(max_length=50)
    cat=models.CharField(default='Beverages', max_length=20)
    basePrice = models.IntegerField()
    discount = models.IntegerField(default=0, null=True, blank=True)
    finalPrice = models.IntegerField()
    desc = models.TextField()
    img1 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img2 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img3 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    seller_details = models.ForeignKey(Seller, on_delete=models.CASCADE)
    size = models.IntegerField(default=0, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return str(self.id) + " " + self.name


class KitchenCategory(models.Model):
    name=models.CharField(max_length=50, default=None, blank=True, null=True )

    def __str__(self):
        return str(self.id) + " " + self.name


class WishList(models.Model):
    user = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    frozenFoods = models.ForeignKey(FrozenFoods, on_delete=models.CASCADE)
    bakery = models.ForeignKey(Bakery, on_delete=models.CASCADE)
    spices = models.ForeignKey(Spices, on_delete=models.CASCADE)
    pulses = models.ForeignKey(Pulses, on_delete=models.CASCADE)
    vegetables = models.ForeignKey(Vegetables, on_delete=models.CASCADE)
    snacks = models.ForeignKey(Snacks, on_delete=models.CASCADE)
    fruits = models.ForeignKey(Fruits, on_delete=models.CASCADE)
    beverages = models.ForeignKey(Beverages, on_delete=models.CASCADE)
    cat = models.ForeignKey(KitchenCategory, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    frozenFoods = models.ForeignKey(FrozenFoods, on_delete=models.CASCADE)
    bakery = models.ForeignKey(Bakery, on_delete=models.CASCADE)
    spices = models.ForeignKey(Spices, on_delete=models.CASCADE)
    pulses = models.ForeignKey(Pulses, on_delete=models.CASCADE)
    vegetables = models.ForeignKey(Vegetables, on_delete=models.CASCADE)
    snacks = models.ForeignKey(Snacks, on_delete=models.CASCADE)
    fruits = models.ForeignKey(Fruits, on_delete=models.CASCADE)
    beverages = models.ForeignKey(Beverages, on_delete=models.CASCADE)
    cat = models.ForeignKey(KitchenCategory, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)
