import mysql.connector

class Bank:
    def __init__(self, host='localhost', user='root', password='', database='5220411250'):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                account_number INT PRIMARY KEY,
                account_holder VARCHAR(255),
                balance DECIMAL(10, 2)
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id INT AUTO_INCREMENT PRIMARY KEY,
                account_number INT,
                amount DECIMAL(10, 2),
                transaction_type VARCHAR(10),
                FOREIGN KEY (account_number) REFERENCES accounts(account_number)
            )
        ''')
        self.conn.commit()

    def create_account(self, account_number, account_holder, initial_balance=0.0):
        self.cursor.execute('''
            INSERT INTO accounts (account_number, account_holder, balance)
            VALUES (%s, %s, %s)
        ''', (account_number, account_holder, initial_balance))
        self.conn.commit()
        print("Akun berhasil dibuat.")

    def deposit(self, account_number, amount):
        self.cursor.execute('''
            UPDATE accounts
            SET balance = balance + %s
            WHERE account_number = %s
        ''', (amount, account_number))
        self.conn.commit()
        print("Setoran berhasil.")

    def withdraw(self, account_number, amount):
        self.cursor.execute('''
            UPDATE accounts
            SET balance = balance - %s
            WHERE account_number = %s AND balance >= %s
        ''', (amount, account_number, amount))
        if self.cursor.rowcount == 0:
            print("Akun tidak ditemukan atau saldo tidak mencukupi!")
        else:
            print("Penarikan berhasil.")
            self.conn.commit()

    def get_balance(self, account_number):
        self.cursor.execute('''
            SELECT balance FROM accounts
            WHERE account_number = %s
        ''', (account_number,))
        result = self.cursor.fetchone()
        if result is not None:
            return result[0]
        else:
            return None

    def delete_account(self, account_number):
        self.cursor.execute('''
            DELETE FROM accounts
            WHERE account_number = %s
        ''', (account_number,))
        if self.cursor.rowcount == 0:
            print("Akun tidak ditemukan!")
        else:
            print("Akun berhasil dihapus.")
            self.conn.commit()

    def display_all_accounts(self):
        self.cursor.execute('''
            SELECT * FROM accounts
        ''')
        accounts = self.cursor.fetchall()
        if accounts:
            for account in accounts:
                print("Nomor Akun: {}, Pemilik: {}, Saldo: {}".format(account[0], account[1], account[2]))
        else:
            print("Tidak ada akun.")
    
    def record_transaction(self, account_number, amount, transaction_type):
        self.cursor.execute('''
            INSERT INTO transactions (account_number, amount, transaction_type)
            VALUES (%s, %s, %s)
        ''', (account_number, amount, transaction_type))
        self.conn.commit()
        print("Catatan transaksi berhasil ditambahkan.")


def get_user_input(prompt):
    return input(prompt).strip()


bank = Bank()

while True:
    print("\nMenu:")
    print("1. Buat Akun")
    print("2. Setoran")
    print("3. Penarikan")
    print("4. Hapus Akun")
    print("5. Lihat Semua Akun")
    print("6. Catatan Transaksi")
    print("0. Keluar")

    choice = get_user_input("Pilih menu (0-6): ")

    if choice == '0':
        print("Keluar dari program.")
        break
    elif choice == '1':
        account_number = int(get_user_input("Masukkan nomor akun: "))
        account_holder = get_user_input("Masukkan nama pemilik akun: ")
        initial_balance = float(get_user_input("Masukkan saldo awal: "))
        bank.create_account(account_number, account_holder, initial_balance)
    elif choice == '2':
        account_number = int(get_user_input("Masukkan nomor akun untuk setoran: "))
        amount = float(get_user_input("Masukkan jumlah uang: "))
        bank.deposit(account_number, amount)
        bank.record_transaction(account_number, amount, 'Deposit')
    elif choice == '3':
        account_number = int(get_user_input("Masukkan nomor akun untuk penarikan: "))
        amount = float(get_user_input("Masukkan jumlah uang: "))
        bank.withdraw(account_number, amount)
        bank.record_transaction(account_number, amount, 'Withdrawal')
    elif choice == '4':
        account_number = int(get_user_input("Masukkan nomor akun untuk dihapus: "))
        bank.delete_account(account_number)
    elif choice == '5':
        bank.display_all_accounts()
    elif choice == '6':
        account_number = int(get_user_input("Masukkan nomor akun untuk melihat catatan transaksi: "))
        bank.cursor.execute('''
            SELECT * FROM transactions
            WHERE account_number = %s
        ''', (account_number,))
        transactions = bank.cursor.fetchall()
        if transactions:
            for transaction in transactions:
                print("ID Transaksi: {}, Jumlah: {}, Tipe Transaksi: {}".format(transaction[0], transaction[2], transaction[3]))
        else:
            print("Tidak ada catatan transaksi untuk akun ini.")
    else:
        print("Pilihan tidak valid. Silakan pilih antara 0 dan 6.")
