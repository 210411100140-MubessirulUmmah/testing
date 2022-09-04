#membuat node dengan python
class Node:                                 #kelas yang bernama node 
    #constructor
    def __init__(self, init_data):          #inisialisasi (self=nama node)
        self.data = init_data               #menuju item (datanya itu sendiri)
        self.next = None                    #pointer


#get_set (get sendiri digunakan untuk menambah data, set untuk setting(pointer harus kemana))
    def getData(self):                      #mengambil data        
        return self.data
    def getNext(self):                      #mengambil pointer next
        return self.next
    def setData(self, newdata):             #setting/di atur datanya
        self.data = newdata                 #masukkan datanyap
    def setNext(self, new_next):
        self.next = new_next                #setting node nya menuju new next(node yang mana)


#traversal(menggeser/menelusuri satu2)=>  untuk menghitung jumlah node pada link list

#membentuk kesatuan node
class Linkedlist:
    def __init__(self):                     #inisialisasi self head akan menuju ke none
        self.head = None
    def isEmpty(self):                      #cek isi list
        return self.head==None              #return terhadap self head
    def addNode(self,item):                 #fungsi untuk addnode (menambahkan node)
        temp=Node(item)                     #item=angka / nodenya
        temp.setNext(self.head)             #setting pointer menuju depan(head)
        self.head=temp                      #menggabungkan node yang ditambahkan dengan list yang ada


#search (mencari data dalam sebuah list ada(True)/tidak(False))
    def search(self,item):
        current = self.head                         #pada posisi paling depan current sama dengan head
        found = False                               #kondisi awal setting false atau tidak ditemukan
        while current != None and not found:        #geser satu satu tidak sama dengan false
            if current.getData() == item:           #jika current ged data sama dengan item (atau sama dengan node yang di cari)
                found = True
            else:
                current = current.getNext()         #kalo false maka currentnya geser
        return found


#display (menampilkan data pada linked list yang ada)        
    def display(self):
        current = self.head                         #pada posisi paling depan current sama dengan head
        while current != None:                      #perulangan while untuk mencari letak data hingga pada kondisi none
            print(current.getData())                #pointer current akan mengambil data tersebut yang telah ditemukan
            current = current.getNext()             #pointer current melakukan next / cek data selanjutnya


#insert previous (penambahan data sebelum node yang di tentukan)    
    def insert_previous(self, data, newdata):       #fungsi insert prev dengan parameter(namalist, posisi,data yang ditambah)
        current = self.head                         #pointer current di depan
        found = False                               #pemberian kondisi awal false pada variable found
        previous = None                             #pointer previous posisi none

        while current != None and not found:        #bentuk perulangan while dimana pointer current tidak sama dengan none dan found bernilai true
            if current.getData() == data:           #branching if, jika pointer current sama dengan data yang di tuju
                found = True                        #maka kondisinya bakal True / ditemukan
            else:                                   #jika tidak
                previous = current                  #pointer previous sama dengan pointer current
                current = current.getNext()         #lalu pointer current sama dengan current.getNext()
        
        if previous == None:                        #jika previous sama dengan none
            self.head = Node(newdata)               #self.head sama dengan node baru yang akan kita tambahkan
            self.head.setNext(current)              #self.head yang mengandung node baru tadi, akan set nodenya menuju pointer current
        elif current == None:                       #jika pointer currentnya sama dengan none, maka data node yang dicari itu tidak ditemukan
            print("node tidak ditemukan")
        else:                                       #jika tidak previous tidak sama dengan none, dan current juga tidak sama dengan none
            temp = Node(newdata)                    #maka kita akan membuat atau menambahkan node, melalui variable temp sama dengan node baru yang akan ditambahkan
            temp.setNext(current)                   #variable temp kita set menuju pointer current
            previous.setNext(temp)                  #lalu previousnya kita set menuju temp tadi

mylist = Linkedlist()
print("Data awal yakni :")
mylist.addNode(45)
mylist.addNode(22)
mylist.addNode(11)
mylist.addNode(55)
mylist.addNode(43)
mylist.addNode(10)
print(mylist.display())

print("insert previous")
angka = int(input("masukkan angka yang ingin ditambahkan : "))
node_ke = int(input("ingin memasukkan data sebelum node : "))
mylist.insert_previous(node_ke,angka)
print(mylist.display())