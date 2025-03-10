import random

class Robot:
    def __init__(self, nama, hp, kekuatan_serang, pertahanan, akurasi):
        self.nama = nama
        self.hp = hp
        self.kekuatan_serang = kekuatan_serang
        self.pertahanan = pertahanan
        self.akurasi = akurasi
        self.terkena_stun = False

    def serang_musuh(self, musuh):
        if self.terkena_stun:
            print(f"{self.nama} terkena stun dan tidak bisa menyerang!")
            self.terkena_stun = False  # Stun hanya berlaku satu ronde
            return

        if random.random() > self.akurasi:  # Serangan bisa meleset
            print(f"{self.nama} gagal menyerang!")
        else:
            damage = max(0, self.kekuatan_serang - musuh.pertahanan)
            if random.random() < 0.1:  # 10% kemungkinan serangan kritikal
                damage *= 2
                print("Serangan kritikal!")
            musuh.hp -= damage
            print(f"{self.nama} menyerang {musuh.nama} dan menyebabkan {damage} damage!")

            # 15% kemungkinan musuh terkena stun
            if random.random() < 0.15:
                musuh.terkena_stun = True
                print(f"{musuh.nama} terkena stun dan tidak bisa bergerak di ronde berikutnya!")

    def masih_hidup(self):
        return self.hp > 0

class Permainan:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.nomor_ronde = 1

    def mainkan(self):
        while self.robot1.masih_hidup() and self.robot2.masih_hidup():
            print(f"\nRonde-{self.nomor_ronde} ==================================================")
            print(f"{self.robot1.nama} [HP: {self.robot1.hp} | ATK: {self.robot1.kekuatan_serang}]")
            print(f"{self.robot2.nama} [HP: {self.robot2.hp} | ATK: {self.robot2.kekuatan_serang}]")
            
            aksi1 = self.dapatkan_aksi(self.robot1)
            aksi2 = self.dapatkan_aksi(self.robot2)
            
            if aksi1 == 3:
                print(f"{self.robot1.nama} menyerah!")
                print(f"{self.robot2.nama} menang!")
                return
            if aksi2 == 3:
                print(f"{self.robot2.nama} menyerah!")
                print(f"{self.robot1.nama} menang!")
                return
            
            if aksi1 == 1:
                self.robot1.serang_musuh(self.robot2)
            if aksi2 == 1:
                self.robot2.serang_musuh(self.robot1)
            
            self.nomor_ronde += 1
        
        self.tentukan_pemenang()

    def dapatkan_aksi(self, robot):
        while True:
            try:
                aksi = int(input(f"{robot.nama}, pilih aksi (1. Serang  2. Bertahan  3. Menyerah): "))
                if aksi in [1, 2, 3]:
                    return aksi
            except ValueError:
                pass
            print("Masukkan pilihan yang valid!")

    def tentukan_pemenang(self):
        if self.robot1.masih_hidup():
            print(f"{self.robot1.nama} menang!")
        else:
            print(f"{self.robot2.nama} menang!")

# Contoh penggunaan
robot1 = Robot("Atreus", 500, 50, 10, 0.85)
robot2 = Robot("Daedalus", 750, 40, 15, 0.75)
permainan = Permainan(robot1, robot2)
permainan.mainkan()
