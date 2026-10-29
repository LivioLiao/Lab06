from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        # TODO
        connection = get_connection()
        if connection is None:
            return None
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT codice, tipo, marca, anno_acquisto, valore, disponibile FROM strumento")
            rows = cursor.fetchall()
            strumenti = []
            for row in rows:
                strumenti.append(Strumento(
                    codice = row['codice'],
                    tipo = row['tipo'],
                    marca = row['marca'],
                    anno_acquisto = row['anno_acquisto'],
                    valore = row['valore'],
                    disponibile = bool(row['disponibile'])
                ))
            return strumenti
        except Exception as e:
            print(f"Errore get_strumenti: {e}")
            return None
        finally:
            cursor.close()
            connection.close()


    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        # TODO
        connection = get_connection()
        if connection is None:
            return None

        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute(
                "SELECT codice, tipo, marca, anno_acquisto, valore, disponibile "
                "FROM strumento WHERE tipo = %s", (tipo,)
            )
            rows = cursor.fetchall()
            strumenti = []
            for row in rows:
                strumenti.append(Strumento(
                    codice=row['codice'],
                    tipo=row['tipo'],
                    marca=row['marca'],
                    anno_acquisto=row['anno_acquisto'],
                    valore=row['valore'],
                    disponibile=bool(row['disponibile'])
                ))
            return strumenti
        except Exception as e:
            print(f"Errore cerca_strumenti_per_tipo: {e}")
            return None
        finally:
            cursor.close()
            connection.close()
