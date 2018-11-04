import bitgen
import bitnet
import threading
import bitmail


class MyThread(threading.Thread):
    def run(self):
        print("{} started!".format(self.getName()))

        while True:
            private_key = bitgen.BitGen.generate_private_key()
            # print(private_key)
            wif = bitgen.BitGen.private2wif(private_key)
            # print(wif)
            address = bitgen.BitGen.private2address(private_key)
            # print(address)
            balance = bitnet.BitNet.get_balance(address)
            # print(balance)

            if balance.isdigit() == False:
                print(balance)
                continue

            if balance != "0":
                f = open("success.txt", "a")
                message = private_key+"\n"+wif+"\n"+address+"\n"+balance+"\n"
                f.write(message)
                f.close()
                bitmail.BitMail.send_email(message)


if __name__ == '__main__':
    bitmail.BitMail.send_email("I am runing")
    for x in range(20):
        mythread = MyThread(name="Thread-{}".format(x + 1))
        mythread.start()
