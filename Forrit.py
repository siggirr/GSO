#GSO Forrit
txtfile = open("testfile.txt","w")
txtfile.write ("Echo world")
txtfile.close()
txtfile = open("testfile.txt","a")
txtfile.write("This is my second line")
txtfile.write("This is THE 3rd line")
txtfile.close()
