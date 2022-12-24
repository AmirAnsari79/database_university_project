import sqlite3


def get_db_connection():
    connect = sqlite3.connect('database.db', check_same_thread=False)
    connect.row_factory = sqlite3.Row
    return connect


class Model:
    connect = get_db_connection()
    cur = connect.cursor()

    # def __init__(self):
    #     pass
    #     # self.connect = get_db_connection()
    #     # self.cur = self.connect

    @classmethod
    def create_customer(cls):
        try:
            cls.cur.execute("""
                create table customer 
            (
            CID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            full_name CHAR(30) NOT NULL ,
            phone_number CHAR(11) NOT NULL UNIQUE 
            );
            
            """)
            cls.cur.close()
        except:
            print(f'customer model is already exists')

    @classmethod
    def create_invoice(cls):
        try:
            cls.cur.execute("""
                 create table invoice 
            (
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            _date Datetime NOT NULL ,
            amount Decimal(9) NOT NULL,
            addr TEXT NOT NULL,
            CID INTEGER NOT NULL,
            POID INTEGER NOT NULL ,
            service_type TEXT NOT NULL ,
            FOREIGN KEY (CID) 
                REFERENCES customer (CID)
                ON DELETE CASCADE 
                ON UPDATE CASCADE,
            FOREIGN KEY (POID)
                REFERENCES operator(POID)
                ON DELETE CASCADE 
                ON UPDATE CASCADE
                
            );
            """)
        except:
            print('invoice model is already exists')

    @classmethod
    def create_offering(cls):
        try:
            cls.cur.execute("""
                create table offering
                (
                CID INTEGER,
                POID INTEGER,
                SHID INTEGER,
                PRIMARY KEY (CID,POID,SHID),
                FOREIGN KEY (SHID)
                    REFERENCES service(SHIPMENT_ID)
                        ON DELETE CASCADE 
                        ON UPDATE CASCADE ,
                FOREIGN KEY (POID)
                    REFERENCES operator (POID)
                        ON DELETE CASCADE 
                        ON UPDATE CASCADE ,
                FOREIGN KEY (CID)
                    REFERENCES customer(CID)
                        ON DELETE CASCADE 
                        ON UPDATE CASCADE 
                );
            
            """)
        except:
            print('offering model is already exists')

    @classmethod
    def create_employee(cls):
        try:
            cls.cur.execute("""
            create table employee
            (
            PID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            full_name CHAR(20) NOT NULL,
            phone_number CHAR(11) NOT NULL UNIQUE,
            salary DECIMAL(9) NOT NULL
            );
            """)
        except:
            print(f'employee model is already exists')

    @classmethod
    def create_carrier(cls):
        try:
            cls.cur.execute("""
                create table carrier
                (
                PCID INTEGER ,
                license_number INTEGER NOT NULL UNIQUE,
                PRIMARY KEY (PCID),
                FOREIGN KEY (PCID)
                    REFERENCES employee (PID) 
                    ON DELETE CASCADE 
                    ON UPDATE NO ACTION
                );
            """)
        except:
            print('carrier model is already exists')

    @classmethod
    def create_operator(cls):
        try:
            cls.cur.execute("""
                create table operator
                (
                POID INTEGER,
                hour_work SMALLINT NOT NULL ,
                pass CHAR(14) NOT NULL, 
                PRIMARY KEY (POID),
                FOREIGN KEY (POID)
                 REFERENCES employee (PID)             
                 ON DELETE CASCADE 
                 ON UPDATE NO ACTION 
                 
                );
                
            """)
        except:
            print('operator model is already exists')

    @classmethod
    def create_packagingManager(cls):
        try:
            cls.cur.execute("""
            create table package_manager
            (
                PAID INTEGER ,
                package_in_day SMALLINT,
                PRIMARY KEY (PAID),
                FOREIGN KEY (PAID) 
                    REFERENCES employee(PID)
                    ON DELETE CASCADE 
                    ON UPDATE NO ACTION 
                        );
            """)
        except:
            print('packagingManager is already exists ')

    @classmethod
    def create_manager(cls):
        try:
            cls.cur.execute("""
            create table manager
            (
                PMID INTEGER,
                location TEXT NOT NULL ,
                hist_manage CHAR(20),
                branch_id INTEGER NOT NULL UNIQUE, 
                PRIMARY KEY (PMID),
                FOREIGN KEY (PMID)
                REFERENCES employee (PID)
                ON DELETE CASCADE 
                ON UPDATE NO ACTION 
    
            );
            
            """)
        except:
            print('manager model is already exists')

    @classmethod
    def create_service(cls):
        try:
            cls.cur.execute("""
                create table service
                (
                SHIPMENT_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
                service_type TEXT NOT NULL ,
                POID INTEGER NOT NULL ,
                FOREIGN KEY (POID)
                    REFERENCES operator(POID)
                    ON DELETE NO ACTION 
                    ON UPDATE CASCADE ,
                FOREIGN KEY (service_type)
                    REFERENCES service_type(pistaz)
                    ON DELETE NO ACTION 
                    ON UPDATE CASCADE 
                     
                
                );
            """)
        except:
            print('service model is already exists ')

    @classmethod
    def create_service_type(cls):
        try:
            cls.cur.execute("""
                create table service_type
                (
                pishtaz CHAR(1) NOT NULL UNIQUE ,
                two_q   CHAR(1) NOT NULL UNIQUE ,
                havai CHAR(1) NOT NULL UNIQUE ,
                mamoli CHAR(1) NOT NULL UNIQUE 
                
                
                );
            
            """)
        except:
            print('service type model is already exists')
