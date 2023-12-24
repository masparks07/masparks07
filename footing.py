#footing material cacluator
width = float(input('How many feet wide is your footing?'))
length = float(input('How many feet long is your footing?'))
blockprice = float(input('How much is each block?'))
steelprice = float(input('How much is a stick of steel?'))
concreteprice = float(input('how much is yard of concrete?'))
chairprice = float(input('price of chairs?'))
blockcourse = float(input('how many courses of block?'))
#
#
#
area = width * length
yards4 = area / 72 #yards for 4 inches deep
yards = yards4 * 3 #yards for 12 inches deep
rebar1 = length / 18 #needed for 1 run
rebar = rebar1 * 3 #needed for 3 runs
chairs = length / 5
inches = length * 12 #converts feet to inches
blocks = inches / 16
blocktotal = blockcourse * blocks
#
#
#
concretepricetotal = concreteprice * yards
steelpricetotal = steelprice * rebar
chairpricetotal = chairprice * chairs
blocktotalprice = blockprice * blocks
grandtotal = steelpricetotal + chairpricetotal + blocktotalprice + concretepricetotal
#
#
#
print("the sq feet of footing is:", area)
print("yards of concrete for 12 inches deep is:", yards)
print("20 foot sticks rebar needed for 3 runs is:", rebar)
print("chairs and pins needed is:", chairs)
print("blocks needed:", blocktotal)
#
#
print("concrete total price is:", concretepricetotal)
print("steel total price is:", steelpricetotal)
print("block total price is:", blocktotalprice)
print("chair total price is:", chairpricetotal)
#
print("total material price is:", grandtotal)



      
                           


        
