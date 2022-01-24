class Quality:
    def pd_quality(self):
        print("Quality is good")


class Potato(Quality):
    def price(self):
        print("Price is low")


potato1 =Potato()

potato1.pd_quality()
potato1.price()