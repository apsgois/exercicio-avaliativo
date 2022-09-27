import pymongo


class Database:
    def __init__(self, database, collection, dataset=None):
        connectionString = "mongodb+srv://root:root@cluster0.0e9b5ex.mongodb.net/test"
        self.clusterConnection = pymongo.MongoClient(
            connectionString,
            # CASO OCORRA O ERRO [SSL_INVALID_CERTIFICATE]
            tlsAllowInvalidCertificates=True
        )
        self.db = self.clusterConnection[database]
        self.collection = self.db[collection]
        if dataset:
            self.dataset = dataset

